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
# Configuration des Modèles IA
# ==============================================================================

# Configuration Gemini
GEMINI_MODEL = "gemini-1.5-pro"
GEMINI_TEMPERATURE = 0.7
GEMINI_MAX_OUTPUT_TOKENS = 2048

# Configuration DeepSeek
DEEPSEEK_MODEL = "deepseek-chat"
DEEPSEEK_TEMPERATURE = 0.7
DEEPSEEK_MAX_TOKENS = 2048

# ==============================================================================
# Configuration des Timeouts et Limites
# ==============================================================================

# Timeouts pour les requêtes API (en secondes)
API_TIMEOUT = 30
WEB_SCRAPING_TIMEOUT = 45
OCR_TIMEOUT = 60

# Limites de requêtes par utilisateur
USER_REQUESTS_PER_MINUTE = 10
USER_REQUESTS_PER_HOUR = 100
USER_REQUESTS_PER_DAY = 500

# Délai minimum entre les requêtes (en secondes)
MIN_REQUEST_INTERVAL = 1

# ==============================================================================
# Configuration des Quotas API
# ==============================================================================

# Quotas journaliers par API
DAILY_QUOTAS = {
    "gemini": 1000,
    "deepseek": 500,
    "ocr": 100,
    "serper": 200,
    "tavily": 150,
    "wolframalpha": 50
}

# Seuils d'alerte (pourcentage du quota)
QUOTA_WARNING_THRESHOLD = 80  # Alerte à 80%
QUOTA_CRITICAL_THRESHOLD = 95  # Alerte critique à 95%

# ==============================================================================
# Configuration de l'Historique de Chat
# ==============================================================================

# Nombre maximum de messages gardés en historique par utilisateur
MAX_CHAT_HISTORY = 50

# Durée de conservation de l'historique (en jours)
CHAT_HISTORY_RETENTION_DAYS = 30

# ==============================================================================
# Configuration des Fonctionnalités
# ==============================================================================

# Fonctionnalités activées/désactivées
FEATURES = {
    "ocr_enabled": True,
    "web_search_enabled": True,
    "web_scraping_enabled": True,
    "wolfram_alpha_enabled": True,
    "language_detection_enabled": True,
    "ip_lookup_enabled": True,
    "shodan_lookup_enabled": True,
    "screenshot_enabled": True,
    "news_search_enabled": True,
    "multi_ia_enabled": True,
    "archive_pages_enabled": True
}

# ==============================================================================
# Configuration des Messages
# ==============================================================================

# Messages par défaut
DEFAULT_MESSAGES = {
    "welcome": "🤖 Salut ! Je suis votre assistant IA. Comment puis-je vous aider aujourd'hui ?",
    "error": "❌ Une erreur s'est produite. Veuillez réessayer plus tard.",
    "quota_exceeded": "⚠️ Quota d'utilisation dépassé. Veuillez attendre ou réessayer plus tard.",
    "feature_disabled": "🚫 Cette fonctionnalité est actuellement désactivée.",
    "processing": "⏳ Traitement en cours...",
    "rate_limit": "🐌 Veuillez patienter avant de faire une nouvelle requête."
}

# ==============================================================================
# Configuration du Logging
# ==============================================================================

# Niveau de log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
LOG_LEVEL = "INFO"

# Format des logs
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# Rotation des logs (taille maximale en MB)
LOG_MAX_SIZE = 10
LOG_BACKUP_COUNT = 5

# ==============================================================================
# Configuration de Sécurité
# ==============================================================================

# Liste des utilisateurs autorisés (laisser vide pour autoriser tous)
AUTHORIZED_USERS = []

# Liste des commandes restreintes aux administrateurs
ADMIN_COMMANDS = ["/status", "/quota", "/reload", "/shutdown"]

# Liste des administrateurs (user IDs Telegram)
ADMIN_USER_IDS = []

# ==============================================================================
# Configuration des Archives Web
# ==============================================================================

# Répertoire des archives web
WEB_ARCHIVES_DIR = BASE_DIR / "web_archives"
WEB_ARCHIVES_DIR.mkdir(parents=True, exist_ok=True)

# Durée de conservation des archives (en jours)
ARCHIVE_RETENTION_DAYS = 7

# Taille maximale du répertoire d'archives (en MB)
MAX_ARCHIVE_SIZE = 500

# ==============================================================================
# Configuration de Monitoring
# ==============================================================================

# Intervalle de vérification de la santé des APIs (en minutes)
HEALTH_CHECK_INTERVAL = 15

# Intervalle d'envoi des rapports de statut (en heures)
STATUS_REPORT_INTERVAL = 24

# Seuils de performance
PERFORMANCE_THRESHOLDS = {
    "response_time_warning": 5.0,  # secondes
    "response_time_critical": 10.0,  # secondes
    "error_rate_warning": 0.05,  # 5%
    "error_rate_critical": 0.10   # 10%
}