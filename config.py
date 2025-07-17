import os
from pathlib import Path

# ==============================================================================
# Paramètres Généraux du Bot
# ==============================================================================

# Token de votre bot Telegram
BOT_TOKEN = "7902342551:AAG6r1QA2GTMZcmcsWHi36Ivd_PVeMXULOs"

# ID du groupe privé où le bot enverra des notifications (ex: alertes quotas, archives)
PRIVATE_GROUP_ID = "-1001234567890"

# Message de démarrage affiché dans la console au lancement du bot
STARTUP_MESSAGE = """
===================================================
🚀 Bot IA Démarré ! 🚀
Version: 1.0.0
Prêt à interagir. Tapez vos commandes ou questions.
===================================================
"""

# ==============================================================================
# Configuration des Chemins de Fichiers
# ==============================================================================

# Répertoire de base pour les données du bot (logs, historiques, quotas, etc.)
BASE_DIR = Path(__file__).parent.parent / "bot_data"
BASE_DIR.mkdir(parents=True, exist_ok=True)

# Chemin du fichier de log principal
LOG_FILE = BASE_DIR / "bot_activity.log"

# Chemin du fichier de log pour les erreurs critiques
ERROR_LOG_PATH = BASE_DIR / "bot_errors.log"

# Fichier pour stocker l'état de santé des endpoints API
ENDPOINT_HEALTH_FILE = BASE_DIR / "endpoint_health.json"

# Fichier pour stocker les informations de quota d'utilisation des APIs
QUOTAS_FILE = BASE_DIR / "api_quotas.json"

# Fichier pour stocker le statut de performance et de diversification des IA
IA_STATUS_FILE = BASE_DIR / "ia_status.json"

# Répertoire pour archiver les pages web
ARCHIVES_DIR = "archives"

# Fichier pour stocker l'historique de chat de chaque utilisateur
USER_CHAT_HISTORY_FILE = "chat_history.json"

# Taille maximale des fichiers (ex: images pour OCR) en octets (10 MB)
MAX_FILE_SIZE = 10 * 1024 * 1024
MAX_IMAGE_SIZE = 10 * 1024 * 1024 # Taille maximale pour les images OCR

# ==============================================================================
# Configuration des APIs (Clés et Paramètres)
# ==============================================================================

# Clés API (Hardcodées comme demandé)
GEMINI_API_KEYS = [
    "YOUR_GEMINI_API_KEY_1",
    "YOUR_GEMINI_API_KEY_2"
]
OCR_API_KEYS = [
    "K8900987654321",
    "K1234567890987"
]
DEEPSEEK_API_KEYS = [
    "sk-ef08317d125947b3a1ce5916592bef00",
    "sk-d73750d96142421cb1098c7056dd7f01"
]
SERPER_API_KEY = "YOUR_SERPER_API_KEY_HERE"
WOLFRAMALPHA_APP_IDS = [
    "YOUR_WOLFRAMALPHA_APP_ID_1",
    "YOUR_WOLFRAMALPHA_APP_ID_2"
]
TAVILY_API_KEYS = [
    "YOUR_TAVILY_API_KEY_1",
    "YOUR_TAVILY_API_KEY_2"
]
APIFLASH_ACCESS_KEY = "YOUR_APIFLASH_ACCESS_KEY_HERE"
CRAWLBASE_API_KEY = "YOUR_CRAWLBASE_API_KEY_HERE"
DETECTLANGUAGE_API_KEY = "YOUR_DETECTLANGUAGE_API_KEY_HERE"
GUARDIAN_API_KEY = "YOUR_GUARDIAN_API_KEY_HERE"
IP2LOCATION_API_KEY = "YOUR_IP2LOCATION_API_KEY_HERE"
SHODAN_API_KEY = "YOUR_SHODAN_API_KEY_HERE"

# ==============================================================================
# Configuration des Limites et Quotas
# ==============================================================================

# Limites d'utilisation par utilisateur (par jour)
DAILY_USER_LIMITS = {
    "messages": 100,
    "api_calls": 50,
    "file_uploads": 10,
    "web_searches": 20
}

# Limites globales du bot (par jour)
DAILY_BOT_LIMITS = {
    "total_messages": 1000,
    "total_api_calls": 500,
    "total_file_uploads": 100
}

# ==============================================================================
# Configuration des Timeouts et Délais
# ==============================================================================

# Timeouts pour les requêtes API (en secondes)
API_TIMEOUTS = {
    "default": 30,
    "gemini": 60,
    "ocr": 45,
    "web_search": 20,
    "file_upload": 120
}

# Délais entre les requêtes pour éviter le rate limiting
RATE_LIMIT_DELAYS = {
    "gemini": 1.0,
    "ocr": 0.5,
    "web_search": 0.3,
    "file_upload": 2.0
}

# ==============================================================================
# Configuration des Modèles IA
# ==============================================================================

# Modèles disponibles pour chaque API
AI_MODELS = {
    "gemini": {
        "default": "gemini-1.5-pro",
        "fast": "gemini-1.5-flash",
        "vision": "gemini-1.5-pro-vision"
    },
    "deepseek": {
        "default": "deepseek-chat",
        "fast": "deepseek-chat-fast"
    }
}

# Paramètres par défaut pour les modèles
DEFAULT_MODEL_PARAMS = {
    "temperature": 0.7,
    "max_tokens": 2048,
    "top_p": 0.9,
    "frequency_penalty": 0.0,
    "presence_penalty": 0.0
}

# ==============================================================================
# Configuration de la Sécurité
# ==============================================================================

# Liste des utilisateurs autorisés (IDs Telegram)
AUTHORIZED_USERS = [
    # Ajoutez ici les IDs des utilisateurs autorisés
]

# Mots-clés sensibles à filtrer
SENSITIVE_KEYWORDS = [
    "password", "token", "key", "secret", "private"
]

# ==============================================================================
# Configuration des Logs
# ==============================================================================

# Niveau de log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
LOG_LEVEL = "INFO"

# Format des logs
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Rotation des logs (taille maximale en MB)
LOG_MAX_SIZE = 10  # MB
LOG_BACKUP_COUNT = 5

# ==============================================================================
# Configuration des Notifications
# ==============================================================================

# Fréquence des notifications de santé (en heures)
HEALTH_CHECK_INTERVAL = 6

# Seuils d'alerte pour les quotas (en pourcentage)
QUOTA_ALERT_THRESHOLDS = {
    "warning": 80,
    "critical": 95
}

# ==============================================================================
# Configuration du Cache
# ==============================================================================

# Taille maximale du cache en MB
CACHE_MAX_SIZE = 100

# Durée de vie du cache en secondes
CACHE_TTL = 3600  # 1 heure

# ==============================================================================
# Configuration des Extensions
# ==============================================================================

# Extensions activées
ENABLED_EXTENSIONS = [
    "web_search",
    "ocr",
    "file_upload",
    "image_generation",
    "code_execution"
]

# Configuration spécifique aux extensions
EXTENSION_CONFIG = {
    "web_search": {
        "max_results": 5,
        "search_engines": ["google", "bing"]
    },
    "ocr": {
        "supported_languages": ["en", "fr", "es", "de"],
        "confidence_threshold": 0.8
    },
    "file_upload": {
        "allowed_extensions": [".txt", ".pdf", ".doc", ".docx", ".jpg", ".png"],
        "max_file_size": MAX_FILE_SIZE
    }
}

# ==============================================================================
# Configuration de l'Interface Utilisateur
# ==============================================================================

# Messages d'aide et d'interface
UI_MESSAGES = {
    "welcome": "👋 Bienvenue ! Je suis votre assistant IA. Comment puis-je vous aider ?",
    "help": """
🤖 **Commandes disponibles :**
• /start - Démarrer le bot
• /help - Afficher cette aide
• /status - Statut du bot et des APIs
• /quota - Voir vos quotas d'utilisation
• /reset - Réinitialiser votre session
• /settings - Configurer vos préférences
    """,
    "error": "❌ Une erreur s'est produite. Veuillez réessayer.",
    "quota_exceeded": "⚠️ Vous avez atteint votre limite quotidienne.",
    "processing": "⏳ Traitement en cours...",
    "success": "✅ Opération réussie !"
}

# ==============================================================================
# Configuration des Tests
# ==============================================================================

# Mode test (désactive certaines fonctionnalités)
TEST_MODE = False

# APIs de test (utilisées en mode test)
TEST_API_KEYS = {
    "gemini": "test_key",
    "ocr": "test_key",
    "deepseek": "test_key"
}

# ==============================================================================
# Configuration de la Sauvegarde
# ==============================================================================

# Fréquence de sauvegarde automatique (en heures)
BACKUP_INTERVAL = 24

# Nombre de sauvegardes à conserver
BACKUP_RETENTION = 7

# Répertoire de sauvegarde
BACKUP_DIR = BASE_DIR / "backups"
BACKUP_DIR.mkdir(exist_ok=True)