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

# Limites par utilisateur par jour
DAILY_USER_LIMITS = {
    "messages": 100,
    "images": 20,
    "web_searches": 30,
    "file_uploads": 10
}

# Limites par utilisateur par heure
HOURLY_USER_LIMITS = {
    "messages": 20,
    "images": 5,
    "web_searches": 8,
    "file_uploads": 3
}

# ==============================================================================
# Configuration des Modèles IA
# ==============================================================================

# Configuration des modèles Gemini
GEMINI_CONFIG = {
    "model": "gemini-1.5-flash",
    "max_tokens": 4096,
    "temperature": 0.7,
    "top_p": 0.9,
    "top_k": 40
}

# Configuration des modèles DeepSeek
DEEPSEEK_CONFIG = {
    "model": "deepseek-chat",
    "max_tokens": 4096,
    "temperature": 0.7,
    "top_p": 0.9
}

# ==============================================================================
# Configuration de Sécurité
# ==============================================================================

# Liste des utilisateurs autorisés (IDs Telegram)
AUTHORIZED_USERS = []

# Liste des utilisateurs bannis (IDs Telegram)
BANNED_USERS = []

# Mots-clés interdits pour la modération
FORBIDDEN_KEYWORDS = [
    "spam", "scam", "malware", "virus", "hack"
]

# ==============================================================================
# Configuration des Timeouts
# ==============================================================================

# Timeouts en secondes
TIMEOUTS = {
    "api_request": 30,
    "file_download": 60,
    "web_search": 45,
    "image_processing": 120
}

# ==============================================================================
# Configuration des Messages
# ==============================================================================

# Messages d'erreur et d'information
MESSAGES = {
    "welcome": "👋 Bienvenue ! Je suis votre assistant IA. Comment puis-je vous aider ?",
    "quota_exceeded": "⚠️ Vous avez atteint votre limite quotidienne. Réessayez demain.",
    "error_generic": "❌ Une erreur s'est produite. Veuillez réessayer.",
    "processing": "⏳ Traitement en cours...",
    "success": "✅ Opération réussie !"
}