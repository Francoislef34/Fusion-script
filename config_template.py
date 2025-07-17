# ==============================================================================
# Template de Configuration du Bot IA Telegram
# ==============================================================================
# 
# Copiez ce fichier vers config.py et remplacez les valeurs par vos propres clés API
# 
# ==============================================================================

import os
from pathlib import Path

# ==============================================================================
# Paramètres Généraux du Bot
# ==============================================================================

# Token de votre bot Telegram (obtenu via @BotFather)
BOT_TOKEN = "VOTRE_TOKEN_BOT_ICI"

# ID du groupe privé où le bot enverra des notifications
PRIVATE_GROUP_ID = "-1001234567890"

# Message de démarrage affiché dans la console
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

# Répertoire de base pour les données du bot
BASE_DIR = Path(__file__).parent.parent / "bot_data"
BASE_DIR.mkdir(parents=True, exist_ok=True)

# Chemins des fichiers de log et données
LOG_FILE = BASE_DIR / "bot_activity.log"
ERROR_LOG_PATH = BASE_DIR / "bot_errors.log"
ENDPOINT_HEALTH_FILE = BASE_DIR / "endpoint_health.json"
QUOTAS_FILE = BASE_DIR / "api_quotas.json"
IA_STATUS_FILE = BASE_DIR / "ia_status.json"
ARCHIVES_DIR = "archives"
USER_CHAT_HISTORY_FILE = "chat_history.json"

# Tailles maximales des fichiers
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
MAX_IMAGE_SIZE = 10 * 1024 * 1024  # 10 MB

# ==============================================================================
# Configuration des APIs (Clés et Paramètres)
# ==============================================================================

# Clés API Gemini (https://makersuite.google.com/app/apikey)
GEMINI_API_KEYS = [
    "VOTRE_CLE_GEMINI_1",
    "VOTRE_CLE_GEMINI_2"  # Optionnel: clé de secours
]

# Clés API OCR.space (https://ocr.space/ocrapi)
OCR_API_KEYS = [
    "VOTRE_CLE_OCR_1",
    "VOTRE_CLE_OCR_2"  # Optionnel: clé de secours
]

# Clés API DeepSeek (https://platform.deepseek.com/)
DEEPSEEK_API_KEYS = [
    "VOTRE_CLE_DEEPSEEK_1",
    "VOTRE_CLE_DEEPSEEK_2"  # Optionnel: clé de secours
]

# Clé API Serper (https://serper.dev/)
SERPER_API_KEY = "VOTRE_CLE_SERPER"

# Clés API Tavily (https://tavily.com/)
TAVILY_API_KEYS = [
    "VOTRE_CLE_TAVILY_1",
    "VOTRE_CLE_TAVILY_2"  # Optionnel: clé de secours
]

# Autres APIs (optionnelles)
WOLFRAMALPHA_APP_IDS = [
    "VOTRE_APP_ID_WOLFRAM_1",
    "VOTRE_APP_ID_WOLFRAM_2"
]
APIFLASH_ACCESS_KEY = "VOTRE_CLE_APIFLASH"
CRAWLBASE_API_KEY = "VOTRE_CLE_CRAWLBASE"
DETECTLANGUAGE_API_KEY = "VOTRE_CLE_DETECTLANGUAGE"
GUARDIAN_API_KEY = "VOTRE_CLE_GUARDIAN"
IP2LOCATION_API_KEY = "VOTRE_CLE_IP2LOCATION"
SHODAN_API_KEY = "VOTRE_CLE_SHODAN"

# ==============================================================================
# Configuration des Limites et Quotas
# ==============================================================================

# Limites par utilisateur par jour
DAILY_USER_LIMITS = {
    "messages": 100,      # Messages par jour
    "images": 20,         # Images par jour
    "web_searches": 30,   # Recherches par jour
    "file_uploads": 10    # Fichiers par jour
}

# Limites par utilisateur par heure
HOURLY_USER_LIMITS = {
    "messages": 20,       # Messages par heure
    "images": 5,          # Images par heure
    "web_searches": 8,    # Recherches par heure
    "file_uploads": 3     # Fichiers par heure
}

# ==============================================================================
# Configuration des Modèles IA
# ==============================================================================

# Configuration des modèles Gemini
GEMINI_CONFIG = {
    "model": "gemini-1.5-flash",  # ou "gemini-1.5-pro"
    "max_tokens": 4096,
    "temperature": 0.7,    # 0.0 = très focalisé, 1.0 = très créatif
    "top_p": 0.9,
    "top_k": 40
}

# Configuration des modèles DeepSeek
DEEPSEEK_CONFIG = {
    "model": "deepseek-chat",  # ou "deepseek-coder"
    "max_tokens": 4096,
    "temperature": 0.7,
    "top_p": 0.9
}

# ==============================================================================
# Configuration de Sécurité
# ==============================================================================

# Liste des utilisateurs autorisés (IDs Telegram)
# Laissez vide [] pour autoriser tous les utilisateurs
AUTHORIZED_USERS = []

# Liste des utilisateurs bannis (IDs Telegram)
BANNED_USERS = []

# Mots-clés interdits pour la modération
FORBIDDEN_KEYWORDS = [
    "spam", "scam", "malware", "virus", "hack",
    "buy now", "limited time", "act fast", "click here",
    "free offer", "money back", "guaranteed",
    "earn money", "work from home", "get rich"
]

# ==============================================================================
# Configuration des Timeouts
# ==============================================================================

# Timeouts en secondes
TIMEOUTS = {
    "api_request": 30,        # Requêtes API générales
    "file_download": 60,      # Téléchargement de fichiers
    "web_search": 45,         # Recherche web
    "image_processing": 120   # Traitement d'images
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

# ==============================================================================
# Instructions de Configuration
# ==============================================================================
#
# 1. Remplacez BOT_TOKEN par votre token Telegram obtenu via @BotFather
# 2. Configurez au moins une clé API Gemini pour les conversations
# 3. Configurez au moins une clé API OCR pour l'extraction de texte
# 4. Configurez au moins une clé API de recherche web (Serper ou Tavily)
# 5. Ajustez les limites selon vos besoins
# 6. Personnalisez les messages si nécessaire
#
# ==============================================================================