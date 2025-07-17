import json
import logging
import asyncio
import aiofiles
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Any, Optional, List
import config

# Variables globales pour les verrous et instances
file_lock = None
endpoint_health_manager = None

def set_file_lock(lock: asyncio.Lock):
    """Définit le verrou de fichier global"""
    global file_lock
    file_lock = lock

def set_endpoint_health_manager_global(manager):
    """Définit le gestionnaire de santé des endpoints global"""
    global endpoint_health_manager
    endpoint_health_manager = manager

def setup_logging():
    """Configure le système de logging"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(config.LOG_FILE),
            logging.StreamHandler()
        ]
    )
    
    # Logger séparé pour les erreurs critiques
    error_logger = logging.getLogger('error_logger')
    error_logger.setLevel(logging.ERROR)
    error_handler = logging.FileHandler(config.ERROR_LOG_PATH)
    error_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    error_logger.addHandler(error_handler)
    
    return logging.getLogger(__name__), error_logger

async def safe_json_read(file_path: Path, default: Any = None) -> Any:
    """Lit un fichier JSON de manière sécurisée avec verrou"""
    if file_lock:
        async with file_lock:
            try:
                if file_path.exists():
                    async with aiofiles.open(file_path, 'r', encoding='utf-8') as f:
                        content = await f.read()
                        return json.loads(content) if content.strip() else default
                return default
            except Exception as e:
                logging.error(f"Erreur lecture JSON {file_path}: {e}")
                return default
    else:
        # Fallback sans verrou
        try:
            if file_path.exists():
                with open(file_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return default
        except Exception as e:
            logging.error(f"Erreur lecture JSON {file_path}: {e}")
            return default

async def safe_json_write(file_path: Path, data: Any):
    """Écrit dans un fichier JSON de manière sécurisée avec verrou"""
    if file_lock:
        async with file_lock:
            try:
                file_path.parent.mkdir(parents=True, exist_ok=True)
                async with aiofiles.open(file_path, 'w', encoding='utf-8') as f:
                    await f.write(json.dumps(data, indent=2, ensure_ascii=False))
            except Exception as e:
                logging.error(f"Erreur écriture JSON {file_path}: {e}")
    else:
        # Fallback sans verrou
        try:
            file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logging.error(f"Erreur écriture JSON {file_path}: {e}")

def format_file_size(size_bytes: int) -> str:
    """Formate la taille d'un fichier en format lisible"""
    if size_bytes == 0:
        return "0 B"
    size_names = ["B", "KB", "MB", "GB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    return f"{size_bytes:.1f} {size_names[i]}"

def is_file_size_valid(file_size: int, max_size: int = config.MAX_FILE_SIZE) -> bool:
    """Vérifie si la taille du fichier est valide"""
    return file_size <= max_size

def get_user_quota_key(user_id: int, quota_type: str) -> str:
    """Génère une clé pour les quotas utilisateur"""
    today = datetime.now().strftime("%Y-%m-%d")
    return f"{user_id}_{quota_type}_{today}"

def get_hourly_quota_key(user_id: int, quota_type: str) -> str:
    """Génère une clé pour les quotas horaires utilisateur"""
    current_hour = datetime.now().strftime("%Y-%m-%d_%H")
    return f"{user_id}_{quota_type}_{current_hour}"

async def check_user_quota(user_id: int, quota_type: str) -> bool:
    """Vérifie si l'utilisateur a encore des quotas disponibles"""
    quotas = await safe_json_read(config.QUOTAS_FILE, {})
    
    # Vérification quota quotidien
    daily_key = get_user_quota_key(user_id, quota_type)
    daily_limit = config.DAILY_USER_LIMITS.get(quota_type, 100)
    daily_usage = quotas.get(daily_key, 0)
    
    if daily_usage >= daily_limit:
        return False
    
    # Vérification quota horaire
    hourly_key = get_hourly_quota_key(user_id, quota_type)
    hourly_limit = config.HOURLY_USER_LIMITS.get(quota_type, 20)
    hourly_usage = quotas.get(hourly_key, 0)
    
    if hourly_usage >= hourly_limit:
        return False
    
    return True

async def increment_user_quota(user_id: int, quota_type: str):
    """Incrémente le quota utilisateur"""
    quotas = await safe_json_read(config.QUOTAS_FILE, {})
    
    # Incrémenter quota quotidien
    daily_key = get_user_quota_key(user_id, quota_type)
    quotas[daily_key] = quotas.get(daily_key, 0) + 1
    
    # Incrémenter quota horaire
    hourly_key = get_hourly_quota_key(user_id, quota_type)
    quotas[hourly_key] = quotas.get(hourly_key, 0) + 1
    
    await safe_json_write(config.QUOTAS_FILE, quotas)

def clean_old_quotas():
    """Nettoie les anciens quotas (quotas de plus de 7 jours)"""
    quotas = safe_json_read(config.QUOTAS_FILE, {})
    cutoff_date = datetime.now() - timedelta(days=7)
    
    keys_to_remove = []
    for key in quotas.keys():
        try:
            # Extraire la date de la clé (format: user_id_type_YYYY-MM-DD)
            date_part = key.split('_')[-1]
            if len(date_part) == 10:  # Format YYYY-MM-DD
                key_date = datetime.strptime(date_part, "%Y-%m-%d")
                if key_date < cutoff_date:
                    keys_to_remove.append(key)
        except:
            continue
    
    for key in keys_to_remove:
        del quotas[key]
    
    safe_json_write(config.QUOTAS_FILE, quotas)

async def save_chat_history(user_id: int, message: str, response: str):
    """Sauvegarde l'historique de chat d'un utilisateur"""
    history = await safe_json_read(config.USER_CHAT_HISTORY_FILE, {})
    
    if str(user_id) not in history:
        history[str(user_id)] = []
    
    history[str(user_id)].append({
        "timestamp": datetime.now().isoformat(),
        "message": message,
        "response": response
    })
    
    # Garder seulement les 100 derniers messages
    if len(history[str(user_id)]) > 100:
        history[str(user_id)] = history[str(user_id)][-100:]
    
    await safe_json_write(config.USER_CHAT_HISTORY_FILE, history)

async def get_chat_history(user_id: int, limit: int = 10) -> List[Dict]:
    """Récupère l'historique de chat d'un utilisateur"""
    history = await safe_json_read(config.USER_CHAT_HISTORY_FILE, {})
    user_history = history.get(str(user_id), [])
    return user_history[-limit:] if limit > 0 else user_history

def sanitize_filename(filename: str) -> str:
    """Nettoie un nom de fichier pour éviter les caractères problématiques"""
    import re
    # Remplacer les caractères non autorisés
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    # Limiter la longueur
    if len(filename) > 255:
        name, ext = os.path.splitext(filename)
        filename = name[:255-len(ext)] + ext
    return filename

def create_backup_filename(original_path: Path) -> Path:
    """Crée un nom de fichier de sauvegarde avec timestamp"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return original_path.parent / f"{original_path.stem}_{timestamp}{original_path.suffix}"