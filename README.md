      # config.py
import os
import json
from datetime import datetime, timezone, date, timedelta
from pathlib import Path

# ----------------------------
# CONFIGURATION & CONSTANTES GLOBALES
# ----------------------------

# ==== Chemins de fichiers & Limites ====
# Assure que le temps est toujours en UTC pour une cohérence globale
os.environ["TZ"] = "UTC"

# Répertoire de base pour toutes les sauvegardes et données
BASE_DIR = Path(__file__).resolve().parent / "sauvegardes"
# Chemin du fichier de log des erreurs critiques
ERROR_LOG_PATH = BASE_DIR / "erreurs.log"
# Chemin du fichier de log général du bot (pour le suivi des opérations)
LOG_FILE = BASE_DIR / "bot_log.log"

# Répertoires spécifiques pour les données utilisateur et les défis de code
DAILY_CHALLENGE_PATH = Path(__file__).resolve().parent / "defis_code"
HISTORY_DIR = DAILY_CHALLENGE_PATH / "history" # Pour l'historique des défis de code

# Fichiers globaux pour le statut des IA et les quotas
IA_STATUS_FILE = BASE_DIR / "ia_status.json"
QUOTAS_FILE = BASE_DIR / "quotas.json"
ENDPOINT_HEALTH_FILE = BASE_DIR / "endpoint_health.json"

# Fichiers spécifiques à l'utilisateur (stockés dans sauvegardes/{user_id}/)
USER_CHAT_HISTORY_FILE = "chat_history.json"
USER_LONG_MEMORY_FILE = "long_term_memory.json"
GROUP_CHAT_HISTORY_FILE = "group_chat_history.json" # Pour la mémoire de groupe
ARCHIVES_DIR = "archives" # Sous-répertoire pour l'archivage des pages web

# Taille maximale des fichiers pour la rotation/compression des logs et l'archivage
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

# Paramètres de mémoire et de cache
MAX_CACHE_SIZE = 20       # Nombre de messages récents à garder en cache pour la similarité
MAX_LONG_TERM_MEMORY = 50 # Nombre d'entrées max dans la mémoire à long terme

# Assurez-vous que les répertoires nécessaires existent
BASE_DIR.mkdir(parents=True, exist_ok=True)
DAILY_CHALLENGE_PATH.mkdir(exist_ok=True)
HISTORY_DIR.mkdir(exist_ok=True)

# ==== Telegram Bot Configuration ====
# Token de votre bot Telegram (à remplacer par votre vrai token en production)
TELEGRAM_BOT_TOKEN = "7902342551:AAG6r1QA2GTMZcmcsWHi36Ivd_PVeMXULOs"
# ID du groupe privé utilisé pour les logs, rapports et archivage
PRIVATE_GROUP_ID = -1002845235344

# ==== Configuration du Bot ====
BOT_NAME = "Assistant IA"
BOT_DESCRIPTION = "un assistant polyvalent capable de converser, d'exécuter du code, d'analyser des images et d'archiver des informations."
BOT_PERSONALITY = "toujours serviable, précis, éthique et proactif dans l'apprentissage."
BOT_INSTRUCTIONS = "Réponds aux questions, exécute les commandes, et utilise tes outils pour fournir les meilleures informations. Sois concis mais complet."

# ==== Clés API Individuelles (centralisées pour la clarté) ====
# Récupérer les clés API depuis les variables d'environnement pour la production
# ou les définir ici pour le développement local (moins sécurisé)
APIFLASH_KEY = os.getenv("APIFLASH_KEY", "3a3cc886a18e41109e0cebc0745b12de")
DEEPSEEK_KEY_1 = os.getenv("DEEPSEEK_KEY_1", "sk-ef08317d125947b3a1ce5916592bef00")
DEEPSEEK_KEY_2 = os.getenv("DEEPSEEK_KEY_2", "sk-d73750d96142421cb1098c7056dd7f01")
CRAWLBASE_KEY_1 = os.getenv("CRAWLBASE_KEY_1", "x41P6KNU8J86yF9JV1nqSw")
CRAWLBASE_KEY_2 = os.getenv("CRAWLBASE_KEY_2", "FOg3R0v_aLxzHkYIdjPgVg")
DETECTLANGUAGE_KEY = os.getenv("DETECTLANGUAGE_KEY", "ebdc8ccc2ee75eda3ab122b08ffb1e8d")
GUARDIAN_KEY = os.getenv("GUARDIAN_KEY", "07c622c1-af05-4c24-9f37-37d219be76a0")
IP2LOCATION_KEY = os.getenv("IP2LOCATION_KEY", "11103C239EA8EA6DF2473BB445EC32F1")
SERPER_KEY = os.getenv("SERPER_KEY", "047b30db1df999aaa9c293f2048037d40c651439")
SHODAN_KEY = os.getenv("SHODAN_KEY", "umdSaWOfVq9Wt2F4wWdXiKh1zjLailzn")
TAVILY_KEY_1 = os.getenv("TAVILY_KEY_1", "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")
TAVILY_KEY_2 = os.getenv("TAVILY_KEY_2", "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")
TAVILY_KEY_3 = os.getenv("TAVILY_KEY_3", "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")
TAVILY_KEY_4 = os.getenv("TAVILY_KEY_4", "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")
WEATHERAPI_KEY = os.getenv("WEATHERAPI_KEY", "332bcdba457d4db4836175513250407")
WOLFRAM_APP_ID_1 = os.getenv("WOLFRAM_APP_ID_1", "96LX77-G8PGKJ3T7V")
WOLFRAM_APP_ID_2 = os.getenv("WOLFRAM_APP_ID_2", "96LX77-PYHRRET363")
WOLFRAM_APP_ID_3 = os.getenv("WOLFRAM_APP_ID_3", "96LX77-P9HPAYWRGL")
GREYNOISE_KEY = os.getenv("GREYNOISE_KEY", "5zNe9E6c2UNDhU09iVXbMaB04UpHAw5hNm5rHCK24fCLvI2cP33NNOpL7nhkDETG")
LOGINRADIUS_KEY = os.getenv("LOGINRADIUS_KEY", "073b2fbedf82409da2ca6f37b97e8c6a")
JSONBIN_KEY = os.getenv("JSONBIN_KEY", "$2a$10$npWSB7v1YcoqLkyPpz0PZOV5ES5vBs6JtTWVyVDXK3j3FDYYS5BPO")
HUGGINGFACE_KEY_1 = os.getenv("HUGGINGFACE_KEY_1", "hf_KzifJEYPZBXSSNcapgb3ISkPJLioDozyPC")
HUGGINGFACE_KEY_2 = os.getenv("HUGGINGFACE_KEY_2", "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")
HUGGINGFACE_KEY_3 = os.getenv("HUGGINGFACE_KEY_3", "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")
HUGGINGFACE_NEW_KEY = os.getenv("HUGGINGFACE_NEW_KEY", "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")
TWILIO_SID = os.getenv("TWILIO_SID", "SK84cc4d335650f9da168cd779f26e00e5")
TWILIO_SECRET = os.getenv("TWILIO_SECRET", "spvz5uwPE8ANYOI5Te4Mehm7YwKOZ4Lg")
ABSTRACTAPI_EMAIL_KEY_1 = os.getenv("ABSTRACTAPI_EMAIL_KEY_1", "2ffd537411ad407e9c9a7eacb7a97311")
ABSTRACTAPI_EMAIL_KEY_2 = os.getenv("ABSTRACTAPI_EMAIL_KEY_2", "5b00ade4e60e4a388bd3e749f4f66e28")
ABSTRACTAPI_EMAIL_KEY_3 = os.getenv("ABSTRACTAPI_EMAIL_KEY_3", "f4106df7b93e4db6855cb7949edc4a20")
ABSTRACTAPI_GENERIC_KEY = os.getenv("ABSTRACTAPI_GENERIC_KEY", "020a4dcd3e854ac0b19043491d79df92")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyABnzGG2YoTNY0uep-akgX1rfuvAsp049Q") # Clé pour GeminiApiClient
GOOGLE_API_KEYS = [
    os.getenv("GOOGLE_API_KEY_1", "AIzaSyAk6Ph25xuIY3b5o-JgdL652MvK4usp8Ms"),
    os.getenv("GOOGLE_API_KEY_2", "AIzaSyDuccmfiPSk4042NeJCYIjA8EOXPo1YKXU"),
    os.getenv("GOOGLE_API_KEY_3", "AIzaSyAQq6o9voefaDxkAEORf7W-IB3QbotIkwY"),
    os.getenv("GOOGLE_API_KEY_4", "AIzaSyDYaYrQQ7cwYFm8TBpyGM3dJweOGOYl7qw"),
]
GOOGLE_CX_LIST = [
    "3368510e864b74936",
    "e745c9ca0ffb94659"
]
PULSEDIVE_KEY = os.getenv("PULSEDIVE_KEY", "201bb09342f35d365889d7d0ca0fdf8580ebee0f1e7644ce70c99a46c1d47171")
RANDOMMER_KEY = os.getenv("RANDOMMER_KEY", "29d907df567b4226bf64b924f9e26c00")
STORMGLASS_KEY = os.getenv("STORMGLASS_KEY", "7ad5b888-5900-11f0-80b9-0242ac130006-7ad5b996-5900-11f0-80b9-0242ac130006")
TOMORROW_KEY = os.getenv("TOMORROW_KEY", "bNh6KpmddRGY0dzwvmQugVtG4Uf5Y2w1")
CLOUDMERSIVE_KEY = os.getenv("CLOUDMERSIVE_KEY", "4d407015-ce22-45d7-a2e1-b88ab6380084")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "c80075b7332716a418e47033463085ef")
MOCKAROO_KEY = os.getenv("MOCKAROO_KEY", "282b32d0")
OPENPAGERANK_KEY = os.getenv("OPENPAGERANK_KEY", "w848ws8s0848g4koosgooc0sg4ggogcggw4o4cko")
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY", "d4d1f58d8emsh58d888c711b7400p1bcebejsn2cc04dce6efe")
OCR_API_KEY = os.getenv("OCR_API_KEY", "K82679097388957") # Clé pour OCRApiClient (une seule clé pour la classe dédiée)
OCR_API_KEYS = [ # Clés OCR pour les endpoints multiples si utilisés par APIClient générique
    os.getenv("OCR_API_KEY_1", "K82679097388957"),
    os.getenv("OCR_API_KEY_2", "K81079143888957"),
    os.getenv("OCR_API_KEY_3", "K84281517488957")
]

# ==== Configuration unifiée des APIs et Endpoints ====
# Cette configuration est utilisée par EndpointHealthManager et APIClient
API_CONFIG = {
    "APIFLASH": [
        {"key": APIFLASH_KEY, "endpoint_name": "URL to Image", "url": "https://api.apiflash.com/v1/urltoimage", "method": "GET", "key_field": "access_key", "key_location": "param", "health_check_params": {"url": "https://example.com"}, "timeout": 10}
    ],
    "DEEPSEEK": [
        {"key": DEEPSEEK_KEY_1, "endpoint_name": "Models List (Key 1)", "url": "https://api.deepseek.com/v1/models", "method": "GET", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "timeout": 5},
        {"key": DEEPSEEK_KEY_2, "endpoint_name": "Models List (Key 2)", "url": "https://api.deepseek.com/v1/models", "method": "GET", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "timeout": 5},
        {"key": DEEPSEEK_KEY_1, "endpoint_name": "Chat Completions", "url": "https://api.deepseek.com/v1/chat/completions", "method": "POST", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "fixed_json": {"model": "deepseek-chat", "stream": False}, "health_check_json": {"model": "deepseek-chat", "messages": [{"role": "user", "content": "hello"}]}, "timeout": 30}
    ],
    "CRAWLBASE": [
        {"key": CRAWLBASE_KEY_1, "endpoint_name": "HTML Scraping", "url": "https://api.crawlbase.com", "method": "GET", "key_field": "token", "key_location": "param", "health_check_params": {"url": "https://example.com"}, "timeout": 15},
        {"key": CRAWLBASE_KEY_2, "endpoint_name": "JS Scraping (JavaScript Token)", "url": "https://api.crawlbase.com", "method": "GET", "key_field": "token", "key_location": "param", "fixed_params": {"javascript": "true"}, "health_check_params": {"url": "https://example.com", "javascript": "true"}, "timeout": 20}
    ],
    "DETECTLANGUAGE": [
        {"key": DETECTLANGUAGE_KEY, "endpoint_name": "Language Detection", "url": "https://ws.detectlanguage.com/0.2/detect", "method": "POST", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "health_check_json": {"q": "hello"}, "timeout": 5}
    ],
    "GUARDIAN": [
        {"key": GUARDIAN_KEY, "endpoint_name": "News Search", "url": "https://content.guardianapis.com/search", "method": "GET", "key_field": "api-key", "key_location": "param", "fixed_params": {"show-fields": "headline,trailText"}, "health_check_params": {"q": "test"}, "timeout": 10},
        {"key": GUARDIAN_KEY, "endpoint_name": "Sections", "url": "https://content.guardianapis.com/sections", "method": "GET", "key_field": "api-key", "key_location": "param", "health_check_params": {"q": "news"}, "timeout": 5}
    ],
    "IP2LOCATION": [
        {"key": IP2LOCATION_KEY, "endpoint_name": "IP Geolocation", "url": "https://api.ip2location.io/", "method": "GET", "key_field": "key", "key_location": "param", "health_check_params": {"ip": "8.8.8.8"}, "timeout": 5}
    ],
    "SERPER": [
        {"key": SERPER_KEY, "endpoint_name": "Search", "url": "https://google.serper.dev/search", "method": "POST", "key_field": "X-API-KEY", "key_location": "header", "health_check_json": {"q": "test"}, "timeout": 10},
        {"key": SERPER_KEY, "endpoint_name": "Images Search", "url": "https://google.serper.dev/images", "method": "POST", "key_field": "X-API-KEY", "key_location": "header", "health_check_json": {"q": "test"}, "timeout": 10}
    ],
    "SHODAN": [
        {"key": SHODAN_KEY, "endpoint_name": "Host Info", "url": "https://api.shodan.io/shodan/host/8.8.8.8", "method": "GET", "key_field": "key", "key_location": "param", "health_check_params": {"ip": "8.8.8.8"}, "timeout": 10},
        {"key": SHODAN_KEY, "endpoint_name": "API Info", "url": "https://api.shodan.io/api-info", "method": "GET", "key_field": "key", "key_location": "param", "timeout": 5}
    ],
    "TAVILY": [
        {"key": TAVILY_KEY_1, "endpoint_name": "Search (Key 1)", "url": "https://api.tavily.com/search", "method": "POST", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "fixed_json": {"search_depth": "advanced", "include_answer": True}, "health_check_json": {"query": "test"}, "timeout": 15},
        {"key": TAVILY_KEY_2, "endpoint_name": "Search (Key 2)", "url": "https://api.tavily.com/search", "method": "POST", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "fixed_json": {"search_depth": "advanced", "include_answer": True}, "health_check_json": {"query": "test"}, "timeout": 15},
        {"key": TAVILY_KEY_3, "endpoint_name": "Search (Key 3)", "url": "https://api.tavily.com/search", "method": "POST", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "fixed_json": {"search_depth": "advanced", "include_answer": True}, "health_check_json": {"query": "test"}, "timeout": 15},
        {"key": TAVILY_KEY_4, "endpoint_name": "Search (Key 4)", "url": "https://api.tavily.com/search", "method": "POST", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "fixed_json": {"search_depth": "advanced", "include_answer": True}, "health_check_json": {"query": "test"}, "timeout": 15}
    ],
    "WEATHERAPI": [
        {"key": WEATHERAPI_KEY, "endpoint_name": "Current Weather", "url": "http://api.weatherapi.com/v1/current.json", "method": "GET", "key_field": "key", "key_location": "param", "health_check_params": {"q": "London"}, "timeout": 5},
        {"key": WEATHERAPI_KEY, "endpoint_name": "Forecast", "url": "http://api.weatherapi.com/v1/forecast.json", "method": "GET", "key_field": "key", "key_location": "param", "fixed_params": {"days": 1}, "health_check_params": {"q": "London", "days": 1}, "timeout": 5}
    ],
    "WOLFRAMALPHA": [
        {"key": WOLFRAM_APP_ID_1, "endpoint_name": "Query (AppID 1)", "url": "http://api.wolframalpha.com/v2/query", "method": "GET", "key_field": "appid", "key_location": "param", "fixed_params": {"format": "plaintext", "output": "json"}, "health_check_params": {"input": "2+2"}, "timeout": 10},
        {"key": WOLFRAM_APP_ID_2, "endpoint_name": "Query (AppID 2)", "url": "http://api.wolframalpha.com/v2/query", "method": "GET", "key_field": "appid", "key_location": "param", "fixed_params": {"format": "plaintext", "output": "json"}, "health_check_params": {"input": "2+2"}, "timeout": 10},
        {"key": WOLFRAM_APP_ID_3, "endpoint_name": "Query (AppID 3)", "url": "http://api.wolframalpha.com/v2/query", "method": "GET", "key_field": "appid", "key_location": "param", "fixed_params": {"format": "plaintext", "output": "json"}, "health_check_params": {"input": "2+2"}, "timeout": 10}
    ],
    "CLOUDMERSIVE": [
        {"key": CLOUDMERSIVE_KEY, "endpoint_name": "Domain Check", "url": "https://api.cloudmersive.com/validate/domain/check", "method": "POST", "key_field": "Apikey", "key_location": "header", "health_check_json": {"domain": "example.com"}, "timeout": 10}
    ],
    "GREYNOISE": [
        {"key": GREYNOISE_KEY, "endpoint_name": "IP Analysis", "url": "https://api.greynoise.io/v3/community/", "method": "GET", "key_field": "key", "key_location": "header", "health_check_url_suffix": "1.1.1.1", "timeout": 10}
    ],
    "PULSEDIVE": [
        {"key": PULSEDIVE_KEY, "endpoint_name": "API Info", "url": "https://pulsedive.com/api/info.php", "method": "GET", "key_field": "key", "key_location": "param", "health_check_params": {"key": PULSEDIVE_KEY}, "timeout": 5},
        {"key": PULSEDIVE_KEY, "endpoint_name": "Analyze IP", "url": "https://pulsedive.com/api/v1/analyze", "method": "GET", "key_field": "key", "key_location": "param", "health_check_params": {"indicator": "8.8.8.8", "type": "ip"}, "timeout": 10},
        {"key": PULSEDIVE_KEY, "endpoint_name": "Explore", "url": "https://pulsedive.com/api/v1/explore", "method": "GET", "key_field": "key", "key_location": "param", "health_check_params": {"query": "type='ip'"}, "timeout": 10}
    ],
    "STORMGLASS": [
        {"key": STORMGLASS_KEY, "endpoint_name": "Weather Point", "url": "https://api.stormglass.io/v2/weather/point", "method": "GET", "key_field": "Authorization", "key_location": "header", "health_check_params": {"lat": 0, "lng": 0, "params": "airTemperature", "start": 0, "end": 0}, "timeout": 10}
    ],
    "LOGINRADIUS": [
        {"key": LOGINRADIUS_KEY, "endpoint_name": "Ping", "url": "https://api.loginradius.com/identity/v2/auth/ping", "method": "GET", "timeout": 5}
    ],
    "JSONBIN": [
        {"key": JSONBIN_KEY, "endpoint_name": "Bin Access", "url": "https://api.jsonbin.io/v3/b", "method": "GET", "key_field": "X-Master-Key", "key_location": "header", "health_check_url_suffix": "60c7b0e0f8c2a3b4c5d6e7f0", "timeout": 10},
        {"key": JSONBIN_KEY, "endpoint_name": "Bin Create", "url": "https://api.jsonbin.io/v3/b", "method": "POST", "key_field": "X-Master-Key", "key_location": "header", "health_check_json": {"record": {"test": "health"}}, "timeout": 10}
    ],
    "HUGGINGFACE": [
        {"key": HUGGINGFACE_KEY_1, "endpoint_name": "Models List (Key 1)", "url": "https://huggingface.co/api/models", "method": "GET", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "timeout": 10},
        {"key": HUGGINGFACE_KEY_1, "endpoint_name": "BERT Inference", "url": "https://api-inference.huggingface.co/models/bert-base-uncased", "method": "POST", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "health_check_json": {"inputs": "test"}, "timeout": 30},
        {"key": HUGGINGFACE_KEY_2, "endpoint_name": "Models List (Key 2)", "url": "https://huggingface.co/api/models", "method": "GET", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "timeout": 10},
        {"key": HUGGINGFACE_KEY_3, "endpoint_name": "Models List (Key 3)", "url": "https://huggingface.co/api/models", "method": "GET", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "timeout": 10},
        {"key": HUGGINGFACE_NEW_KEY, "endpoint_name": "Models List (New Key)", "url": "https://huggingface.co/api/models", "method": "GET", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "timeout": 10},
        {"key": HUGGINGFACE_NEW_KEY, "endpoint_name": "BERT Inference (New Key)", "url": "https://api-inference.huggingface.co/models/bert-base-uncased", "method": "POST", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "health_check_json": {"inputs": "test"}, "timeout": 30}
    ],
    "TWILIO": [
        {"key": (TWILIO_SID, TWILIO_SECRET), "endpoint_name": "Accounts", "url": "https://api.twilio.com/2010-04-01/Accounts", "method": "GET", "key_location": "auth_basic", "timeout": 10},
        {"key": (TWILIO_SID, TWILIO_SECRET), "endpoint_name": "Account Balance", "url": f"https://api.twilio.com/2010-04-01/Accounts/{TWILIO_SID}/Balance.json", "method": "GET", "key_location": "auth_basic", "timeout": 10}
    ],
    "ABSTRACTAPI": [
        {"key": ABSTRACTAPI_EMAIL_KEY_1, "endpoint_name": "Email Validation (Key 1)", "url": "https://emailvalidation.abstractapi.com/v1/", "method": "GET", "key_field": "api_key", "key_location": "param", "health_check_params": {"email": "test@example.com"}, "timeout": 10},
        {"key": ABSTRACTAPI_EMAIL_KEY_2, "endpoint_name": "Email Validation (Key 2)", "url": "https://emailvalidation.abstractapi.com/v1/", "method": "GET", "key_field": "api_key", "key_location": "param", "health_check_params": {"email": "test@example.com"}, "timeout": 10},
        {"key": ABSTRACTAPI_EMAIL_KEY_3, "endpoint_name": "Email Validation (Key 3)", "url": "https://emailvalidation.abstractapi.com/v1/", "method": "GET", "key_field": "api_key", "key_location": "param", "health_check_params": {"email": "test@example.com"}, "timeout": 10},
        {"key": ABSTRACTAPI_GENERIC_KEY, "endpoint_name": "Exchange Rates", "url": "https://exchange-rates.abstractapi.com/v1/", "method": "GET", "key_field": "api_key", "key_location": "param", "health_check_params": {"base": "USD"}, "timeout": 10},
        {"key": ABSTRACTAPI_GENERIC_KEY, "endpoint_name": "Holidays", "url": "https://holidays.abstractapi.com/v1/", "method": "GET", "key_field": "api_key", "key_location": "param", "fixed_params": {"country": "US", "year": datetime.now().year}, "health_check_params": {"country": "US", "year": datetime.now().year}, "timeout": 10},
        {"key": ABSTRACTAPI_GENERIC_KEY, "endpoint_name": "Phone Validation", "url": "https://phonevalidation.abstractapi.com/v1/", "method": "GET", "key_field": "api_key", "key_location": "param", "health_check_params": {"phone": "1234567890"}, "timeout": 10}
    ],
    "GEMINI_API": [ # Note: This is for the generic APIClient, GeminiApiClient class uses GEMINI_API_KEY directly
        {"key": GEMINI_API_KEY, "endpoint_name": "Generic Models Endpoint", "url": "https://generativelanguage.googleapis.com/v1beta/models", "method": "GET", "key_field": "key", "key_location": "param", "timeout": 10},
        {"key": GEMINI_API_KEY, "endpoint_name": "Embed Content", "url": "https://generativelanguage.googleapis.com/v1beta/models/embedding-001:embedContent", "method": "POST", "key_field": "key", "key_location": "param", "health_check_json": {"content": {"parts": [{"text": "test"}]}}, "timeout": 30},
        {"key": GEMINI_API_KEY, "endpoint_name": "Generate Content", "url": "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent", "method": "POST", "key_field": "key", "key_location": "param", "health_check_json": {"contents": [{"parts": [{"text": "hello"}]}]}, "timeout": 60}
    ],
    "GOOGLE_CUSTOM_SEARCH": [
        {"key": GOOGLE_API_KEYS[i], "endpoint_name": f"Search (Key {i+1}, CX {j+1})", "url": "https://www.googleapis.com/customsearch/v1", "method": "GET", "key_field": "key", "key_location": "param", "fixed_params": {"cx": GOOGLE_CX_LIST[j]}, "health_check_params": {"q": "test"}, "timeout": 10}
        for i in range(len(GOOGLE_API_KEYS)) for j in range(len(GOOGLE_CX_LIST))
    ],
    "RANDOMMER": [
        {"key": RANDOMMER_KEY, "endpoint_name": "Generate Phone", "url": "https://randommer.io/api/Phone/Generate", "method": "GET", "key_field": "X-Api-Key", "key_location": "header", "fixed_params": {"CountryCode": "US", "Quantity": 1}, "health_check_params": {"CountryCode": "US", "Quantity": 1}, "timeout": 10}
    ],
    "TOMORROW.IO": [
        {"key": TOMORROW_KEY, "endpoint_name": "Timelines", "url": "https://api.tomorrow.io/v4/timelines", "method": "POST", "key_field": "apikey", "key_location": "header", "health_check_json": {"location": "London", "fields": ["temperature"], "units": "metric", "timesteps": ["1h"]}, "timeout": 15}
    ],
    "OPENWEATHERMAP": [
        {"key": OPENWEATHER_API_KEY, "endpoint_name": "Current Weather", "url": "https://api.openweathermap.org/data/2.5/weather", "method": "GET", "key_field": "appid", "key_location": "param", "health_check_params": {"q": "London"}, "timeout": 5}
    ],
    "MOCKAROO": [
        {"key": MOCKAROO_KEY, "endpoint_name": "Data Generation", "url": "https://api.mockaroo.com/api/generate.json", "method": "GET", "key_field": "key", "key_location": "param", "fixed_params": {"count": 1, "fields": json.dumps([{"name": "id", "type": "Row Number"}])}, "health_check_params": {"count": 1, "fields": json.dumps([{"name": "id", "type": "Row Number"}])}, "timeout": 10},
        {"key": MOCKAROO_KEY, "endpoint_name": "Types", "url": "https://api.mockaroo.com/api/types", "method": "GET", "key_field": "key", "key_location": "param", "timeout": 10},
        {"key": MOCKAROO_KEY, "endpoint_name": "Schemas", "url": "https://api.mockaroo.com/api/schemas", "method": "GET", "key_field": "key", "key_location": "param", "timeout": 10},
        {"key": MOCKAROO_KEY, "endpoint_name": "Account", "url": "https://api.mockaroo.com/api/account", "method": "GET", "key_field": "key", "key_location": "param", "timeout": 10},
        {"key": MOCKAROO_KEY, "endpoint_name": "Generate CSV", "url": "https://api.mockaroo.com/api/generate.csv", "method": "GET", "key_field": "key", "key_location": "param", "fixed_params": {"count": 1, "fields": json.dumps([{"name": "id", "type": "Row Number"}])}, "health_check_params": {"count": 1, "fields": json.dumps([{"name": "id", "type": "Row Number"}])}, "timeout": 10},
        {"key": MOCKAROO_KEY, "endpoint_name": "Status", "url": "https://api.mockaroo.com/api/status", "method": "GET", "key_field": "key", "key_location": "param", "timeout": 10}
    ],
    "OPENPAGERANK": [
        {"key": OPENPAGERANK_KEY, "endpoint_name": "Domain Rank", "url": "https://openpagerank.com/api/v1.0/getPageRank", "method": "GET", "key_field": "API-OPR", "key_location": "header", "fixed_params": {"domains[]": "google.com"}, "timeout": 10}
    ],
    "RAPIDAPI": [
        {"key": RAPIDAPI_KEY, "endpoint_name": "Programming Joke", "url": "https://jokeapi-v2.p.rapidapi.com/joke/Programming", "method": "GET", "key_field": "X-RapidAPI-Key", "key_location": "header", "fixed_headers": {"X-RapidAPI-Host": "jokeapi-v2.p.rapidapi.com"}, "timeout": 10},
        {"key": RAPIDAPI_KEY, "endpoint_name": "Currency List Quotes", "url": "https://currency-exchange.p.rapidapi.com/listquotes", "method": "GET", "key_field": "X-RapidAPI-Key", "key_location": "header", "fixed_headers": {"X-RapidAPI-Host": "currency-exchange.p.rapidapi.com"}, "timeout": 10},
        {"key": RAPIDAPI_KEY, "endpoint_name": "Random Fact", "url": "https://random-facts2.p.rapidapi.com/getfact", "method": "GET", "key_field": "X-RapidAPI-Key", "key_location": "header", "fixed_headers": {"X-RapidAPI-Host": "random-facts2.p.rapidapi.com"}, "timeout": 10}
    ],
    "OCR_API": [ # Note: This is for the generic APIClient, OCRApiClient class uses OCR_API_KEY directly
        {"key": OCR_API_KEYS[0], "endpoint_name": "OCR Space (Key 1)", "url": "https://api.ocr.space/parse/image", "method": "POST", "key_field": "apikey", "key_location": "header", "health_check_json": {"base64Image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="}, "timeout": 30},
        {"key": OCR_API_KEYS[1], "endpoint_name": "OCR Space (Key 2)", "url": "https://api.ocr.space/parse/image", "method": "POST", "key_field": "apikey", "key_location": "header", "health_check_json": {"base64Image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="}, "timeout": 30},
        {"key": OCR_API_KEYS[2], "endpoint_name": "OCR Space (Key 3)", "url": "https://api.ocr.space/parse/image", "method": "POST", "key_field": "apikey", "key_location": "header", "health_check_json": {"base64Image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="}, "timeout": 30},
    ]
}

# ==== Quotas API (Définitions des limites pour le QuotaManager) ====
# Ces valeurs sont utilisées pour le suivi et la gestion des quotas d'utilisation.
# Mettre None pour indiquer une limite illimitée.
API_QUOTAS = {
    "GEMINI": { # Renommé pour correspondre à la clé dans API_CONFIG
        "monthly": 1000000, # Exemple: 1 million de tokens par mois
        "daily": 50000,    # Exemple: 50 000 tokens par jour
        "hourly": 5000,    # Exemple: 5 000 tokens par heure
        "rate_limit_per_sec": 5 # Exemple: 5 requêtes par seconde
    },
    "OCR_API": { # Nom interne utilisé par OCRApiClient
        "monthly": 25000,  # Exemple: 25 000 requêtes par mois (free tier)
        "daily": None,
        "hourly": None,
        "rate_limit_per_sec": 1 # Exemple: 1 requête par seconde
    },
    # Ajouter les quotas pour toutes les APIs listées dans API_CONFIG si elles ont des limites
    # Utiliser les valeurs du premier snippet si non spécifiées ici
    "APIFLASH": {"monthly": 100, "daily": 3, "hourly": 3},
    "DEEPSEEK": {"monthly": None, "hourly": 50},
    "CRAWLBASE": {"monthly": 1000, "daily": 33, "hourly": 1},
    "DETECTLANGUAGE": {"daily": 1000, "hourly": 41},
    "GUARDIAN": {"daily": 5000, "rate_limit_per_sec": 12},
    "IP2LOCATION": {"monthly": 50, "daily": 2, "hourly": 2},
    "SERPER": {"monthly": 2500, "daily": 83, "hourly": 3},
    "SHODAN": {"monthly": 100, "daily": 3, "hourly": 3},
    "TAVILY": {"monthly": 1000, "daily": 33, "hourly": 1},
    "WEATHERAPI": {"monthly": None},
    "WOLFRAMALPHA": {"monthly": None, "hourly": 67},
    "CLOUDMERSIVE": {"monthly": 25, "daily": 1, "hourly": 1},
    "GREYNOISE": {"monthly": 100, "daily": 3, "hourly": 3},
    "PULSEDIVE": {"monthly": 50, "daily": 2, "hourly": 2},
    "STORMGLASS": {"monthly": None},
    "LOGINRADIUS": {"monthly": 25000, "daily": 833, "hourly": 34},
    "JSONBIN": {"monthly": 10000, "daily": 333, "hourly": 13},
    "HUGGINGFACE": {"hourly": 100},
    "TWILIO": {"monthly": 15},
    "ABSTRACTAPI": {"monthly": 250, "rate_limit_per_sec": 1, "daily": 8, "hourly": 1},
    "MOCKAROO": {"monthly": 200, "daily": 7, "hourly": 1},
    "OPENPAGERANK": {"monthly": 1000, "daily": 33, "hourly": 1},
    "RAPIDAPI": {"monthly": None, "hourly": 30},
    "GOOGLE_CUSTOM_SEARCH": {"daily": 100, "hourly": 4},
    "RANDOMMER": {"monthly": 1000, "daily": 100, "hourly": 4},
    "TOMORROW.IO": {"monthly": None},
    "OPENWEATHERMAP": {"monthly": 1000000, "daily": 100, "hourly": 4},
}


# Modèle Gemini et ses paramètres
GEMINI_MODEL_NAME = "gemini-1.5-flash-latest" # Ou "gemini-pro"
GEMINI_TEMPERATURE = 0.7
GEMINI_TOP_P = 0.95
GEMINI_TOP_K = 40
GEMINI_MAX_OUTPUT_TOKENS = 2048
GEMINI_SAFETY_SETTINGS = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]


# ==== Bot Behavior Configuration ====
API_COOLDOWN_DURATION_SECONDS = 300 # Durée du cooldown en secondes (5 minutes)
API_ROTATION_INTERVAL_MINUTES = 10 # Intervalle de rotation des APIs en minutes

# Quota Burning Configuration
# Ratio de quota restant en dessous duquel le mode "brûlage" s'active (ex: 0.2 signifie 20% ou moins restant)
BURN_QUOTA_THRESHOLD_RATIO = 0.2
# Fenêtre de temps avant la réinitialisation du quota où le "brûlage" peut s'activer (en heures)
BURN_QUOTA_BEFORE_RESET_HOURS = 6

# Prompts pour l'auto-génération de contenu technique afin de "brûler" le quota.
# Ces prompts sont choisis aléatoirement pour les APIs en mode "burn".
AUTO_BURN_PROMPTS = {
    "GEMINI": [ # Renommé pour correspondre à la clé dans API_QUOTAS
        "Génère un script Python qui utilise une API REST pour récupérer des données et les stocker dans une base de données NoSQL.",
        "Explique en détail les principes de l'architecture microservices et comment ils se comparent aux architectures monolithiques.",
        "Décris les étapes pour déployer une application web Flask sur un serveur cloud (AWS EC2 ou Google Cloud Run).",
        "Écris un tutoriel sur l'utilisation de Docker Compose pour orchestrer plusieurs conteneurs (par exemple, une application web et une base de données).",
        "Analyse les avantages et les inconvénients des bases de données relationnelles vs non-relationnelles pour un projet de grande envergure.",
        "Propose un plan de test complet pour une application web critique, incluant tests unitaires, d'intégration, de bout en bout et de performance.",
        "Génère un exemple de code JavaScript pour une application React qui gère l'état avec Redux ou Context API.",
        "Explique le concept de CI/CD (intégration et livraison continues) et son importance dans le développement logiciel moderne.",
        "Décris les meilleures pratiques de sécurité pour une API RESTful, incluant l'authentification, l'autorisation et la protection contre les attaques courantes.",
        "Écris un algorithme de tri efficace (par exemple, Quicksort ou Mergesort) et explique sa complexité temporelle et spatiale."
    ],
    "OCR_API": [ # Renommé pour correspondre à la clé dans API_QUOTAS
        "Décris les défis techniques de l'OCR sur des documents manuscrits et les approches modernes pour les surmonter.",
        "Explique comment l'OCR peut être utilisée dans le domaine de la gestion documentaire ou de l'automatisation des processus métier.",
        "Quelles sont les métriques d'évaluation courantes pour les performances d'un système OCR ?",
        "Comment la pré-traitement d'image (bruit, binarisation, redressement) affecte-t-il la précision de l'OCR ?",
        "Compare les différentes technologies OCR disponibles sur le marché (cloud vs on-premise, open-source vs propriétaires)."
    ]
}

# ==== Paramètres de Sécurité et Filtrage ====
FORBIDDEN_WORDS = ["fuck", "shit", "bitch", "asshole", "pute", "enculé", "haine", "stupide", "détruire", "conflit", "malveillance", "idiot", "nul", "débile"]

# ==== IA PROMPTS (Exemples, à affiner selon tes besoins spécifiques pour chaque IA) ====
GENERAL_IA_PROMPT = """
Tu es une IA de l'année 2025, experte en information, programmation et résolution de problèmes.
Ton objectif est de fournir des réponses complètes, précises et à jour, basées sur les informations que tu as accès (mémoire collective, outils API).
Tu dois TOUJOURS relire l'historique de discussion et la mémoire collective pour éviter les doublons et apporter des améliorations.
Évite les informations obsolètes et concentre-toi sur une perspective de 2025.
Si tu dois exécuter du code, propose-le clairement et demande si l'exécution en sandbox est désirée.
N'hésite pas à croiser les informations de plusieurs sources.
"""

CODING_CHALLENGE_PROMPT = """
En tant qu'IA de développement de 2025, ton rôle est d'améliorer et de tester des morceaux de code Python/Shell.
Tu as accès à une sandbox sécurisée pour exécuter le code.
Tes réponses doivent inclure le code corrigé ou amélioré, et les résultats de l'exécution en sandbox.
Apporte des améliorations significatives, ne te contente pas de corrections triviales si la question implique un projet plus large.
Pense à l'efficacité du code et à l'optimisation des ressources.
Chaque version doit être une amélioration nette de la précédente, inédite.
Commence par un commentaire indiquant ce qui a été amélioré.
Le code doit être direct, lisible, et prêt à être utilisé.
"""

# ==== Tool Reformulation Configuration ====
TOOL_RETRY_MAX_ATTEMPTS = 3


# utils.py
import os
import json
import gzip
import shutil
import hashlib
import difflib
import re
import logging
import io
import contextlib
import fcntl
import traceback
import asyncio
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Union, List, Dict, Any, Optional

# Configure logging pour tout le script
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Global lock for file operations to ensure atomic writes and prevent race conditions
_file_lock: Optional[asyncio.Lock] = None

def set_file_lock(lock_instance: asyncio.Lock):
    """
    Permet d'injecter l'instance d'asyncio.Lock après l'initialisation de l'event loop.
    Ceci est crucial pour la gestion des accès concurrents aux fichiers.
    """
    global _file_lock
    _file_lock = lock_instance

def _acquire_file_lock_sync(f):
    """
    Acquires an exclusive lock on a file using fcntl (Unix-like systems).
    This prevents other processes from writing to the file simultaneously.
    """
    try:
        if os.name == 'posix' and fcntl:
            fcntl.flock(f.fileno(), fcntl.LOCK_EX)
    except Exception as e:
        logging.warning(f"Could not acquire file lock: {e}")

def _release_file_lock_sync(f):
    """
    Releases an exclusive lock on a file using fcntl (Unix-like systems).
    """
    try:
        if os.name == 'posix' and fcntl:
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)
    except Exception as e:
        logging.warning(f"Could not release file lock: {e}")

def get_user_dir(uid: Union[int, str]) -> Path:
    """
    Retourne le répertoire de sauvegarde spécifique à un utilisateur, le créant si nécessaire.
    Chaque utilisateur (ou groupe privé) a son propre répertoire pour stocker les données.
    """
    p = BASE_DIR / str(uid)
    p.mkdir(parents=True, exist_ok=True)
    return p

def rotate_log_if_needed(path: Path):
    """
    Fait pivoter le fichier log (ou tout fichier de données) si sa taille dépasse MAX_FILE_SIZE.
    Un nouveau fichier est créé avec un horodatage pour l'archivage, et le fichier original est réinitialisé.
    """
    if path.exists() and path.stat().st_size > MAX_FILE_SIZE:
        timestamp = int(datetime.now().timestamp())
        # Renomme le fichier existant pour l'archiver
        new_path = path.with_suffix(f".old_{timestamp}{path.suffix}.gz")
        try:
            # Compresse et déplace l'ancien fichier
            with open(path, "rb") as f_in, gzip.open(new_path, "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)
            path.unlink() # Supprime l'original
            logging.info(f"Log rotated and compressed: {path} -> {new_path}")
        except Exception as e:
            log_message(f"[Rotation log] Erreur lors de la compression/rotation de {path}: {e}\n{traceback.format_exc()}", level="error")
        # Le fichier sera recréé vide lors de la prochaine sauvegarde

def compress_if_large(path: Path):
    """
    Compresse le fichier s'il dépasse 1MB après une écriture, puis le renomme pour garder le nom original.
    Ceci est une mesure de gestion de l'espace disque pour les fichiers de données.
    """
    try:
        # Vérifie si le fichier existe et si sa taille est supérieure à 1MB
        if path.exists() and path.stat().st_size > 1_000_000:
            gz_path = path.with_suffix(path.suffix + ".gz") # Chemin temporaire pour le fichier compressé
            with open(path, "rb") as f_in, gzip.open(gz_path, "wb") as f_out:
                shutil.copyfileobj(f_in, f_out) # Copie et compresse
            path.unlink() # Supprime le fichier original non compressé
            # Renomme le fichier .gz pour qu'il ait le nom original, simulant une compression "in-place"
            gz_path.rename(path)
            logging.info(f"File compressed: {path}")
    except Exception as e:
        log_message(f"[Compression auto] Erreur : {e}\n{traceback.format_exc()}", level="error")

async def load_json(filepath: Path, default_value: Union[Dict, List] = None) -> Union[Dict, List]:
    """
    Charge un fichier JSON de manière asynchrone.
    Retourne `default_value` si le fichier n'existe pas, est vide ou est corrompu.
    Utilise un verrou global pour la sécurité des accès concurrents.
    """
    if default_value is None:
        default_value = {} # Default to empty dict if not specified

    if _file_lock:
        async with _file_lock:
            return _load_json_sync(filepath, default_value)
    else:
        # Fallback for synchronous loading if lock is not set (e.g., during early initialization)
        return _load_json_sync(filepath, default_value)

def _load_json_sync(filepath: Path, default_value: Union[Dict, List]) -> Union[Dict, List]:
    """
    Charge un fichier JSON de manière synchrone avec verrouillage de fichier.
    """
    if not filepath.exists():
        logging.info(f"Fichier non trouvé: {filepath}. Création d'un fichier vide.")
        _save_json_sync(filepath, default_value) # Crée un fichier vide avec la valeur par défaut
        return default_value

    # Ouvre le fichier en mode lecture/écriture pour pouvoir le vider en cas de corruption
    with open(filepath, 'r+', encoding='utf-8') as f:
        _acquire_file_lock_sync(f) # Acquiert le verrou avant de lire
        try:
            f.seek(0) # Se positionne au début du fichier
            content = f.read()
            if not content:
                logging.warning(f"Fichier vide: {filepath}. Retourne la valeur par défaut.")
                return default_value
            return json.loads(content)
        except json.JSONDecodeError as e:
            logging.error(f"Erreur de décodage JSON dans {filepath}: {e}. Le fichier sera réinitialisé.")
            # Si le fichier est corrompu, le réinitialise avec la valeur par défaut
            f.seek(0)
            f.truncate()
            json.dump(default_value, f, indent=4, ensure_ascii=False)
            return default_value
        except Exception as e:
            logging.error(f"Erreur inattendue lors du chargement de {filepath}: {e}. Retourne la valeur par défaut.")
            return default_value
        finally:
            _release_file_lock_sync(f) # Relâche le verrou

async def save_json(filepath: Path, data: Union[Dict, List]):
    """
    Sauvegarde les données dans un fichier JSON de manière asynchrone et atomique,
    avec rotation et compression si nécessaire.
    Utilise un verrou global pour la sécurité des accès concurrents.
    """
    if _file_lock:
        async with _file_lock:
            _save_json_sync(filepath, data)
    else:
        # Fallback for synchronous saving if lock is not set
        _save_json_sync(filepath, data)

def _save_json_sync(filepath: Path, data: Union[Dict, List]):
    """
    Sauvegarde les données dans un fichier JSON de manière synchrone et atomique,
    avec verrouillage de fichier.
    """
    rotate_log_if_needed(filepath) # Effectue la rotation avant la sauvegarde
    temp_filepath = filepath.with_suffix(filepath.suffix + ".tmp") # Utilise un fichier temporaire pour l'atomicité
    try:
        with temp_filepath.open('w', encoding='utf-8') as f:
            _acquire_file_lock_sync(f) # Acquiert le verrou avant d'écrire
            try:
                json.dump(data, f, indent=4, ensure_ascii=False)
            finally:
                _release_file_lock_sync(f) # Relâche le verrou
        os.replace(temp_filepath, filepath) # Remplace l'ancien fichier par le nouveau de manière atomique
        compress_if_large(filepath) # Compresse le fichier après la sauvegarde si nécessaire
    except Exception as e:
        logging.error(f"Erreur lors de la sauvegarde atomique de {filepath}: {e}")
        if temp_filepath.exists():
            os.remove(temp_filepath) # Nettoie le fichier temporaire en cas d'erreur

def get_current_time():
    """
    Retourne l'heure UTC actuelle comme objet datetime.
    """
    return datetime.now(timezone.utc) # Utilise datetime.now(timezone.utc) pour être explicite sur UTC

def format_datetime(dt_obj: datetime) -> str:
    """
    Formate un objet datetime en chaîne de caractères lisible (UTC).
    """
    return dt_obj.strftime("%Y-%m-%d %H:%M:%S UTC")

def is_within_time_window(target_time: datetime, start_minutes_before: int, end_minutes_after: int) -> bool:
    """
    Vérifie si l'heure actuelle est dans une fenêtre de temps spécifiée autour d'une heure cible.
    """
    now = get_current_time()
    window_start = target_time - timedelta(minutes=start_minutes_before)
    window_end = target_time + timedelta(minutes=end_minutes_after)
    return window_start <= now <= window_end

def log_message(message: str, level: str = "info"):
    """
    Log un message avec un niveau spécifié.
    Les messages d'erreur critiques sont dirigés vers un fichier de log d'erreurs séparé.
    """
    if level == "error":
        error_logger = logging.getLogger("erreurs_api")
        if not error_logger.handlers: # Configurer le logger d'erreurs si pas déjà fait
            eh = logging.FileHandler(ERROR_LOG_PATH, encoding="utf-8")
            eh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"))
            error_logger.addHandler(eh)
            error_logger.setLevel(logging.ERROR)
        error_logger.error(message)
    else:
        # Utilise le logger par défaut pour les autres niveaux
        if level == "info":
            logging.info(message)
        elif level == "warning":
            logging.warning(message)
        elif level == "debug":
            logging.debug(message)
        else:
            logging.debug(message) # Fallback pour les niveaux non reconnus

def neutralize_urls(text: str) -> str:
    """
    Remplace les URLs dans le texte par un placeholder pour prévenir les problèmes de lien direct
    et la fuite d'informations sensibles dans les logs ou la mémoire.
    """
    # Remplace http(s):// par hxxp(s)://
    text = re.sub(r"https?://", lambda m: m.group(0).replace("t", "x", 1), text)
    # Remplace www. par wxx.
    text = re.sub(r"www\.", "wxx.", text)
    # Remplace .com, .net, .org par [.]com, [.]net, [.]org
    text = re.sub(r"\.com", "[.]com", text)
    text = re.sub(r"\.net", "[.]net", text)
    text = re.sub(r"\.org", "[.]org", text)
    return text

def clean_html_tags(text: str) -> str:
    """
    Supprime les balises HTML d'une chaîne de caractères en utilisant une expression régulière.
    """
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def hash_text(t: str) -> str:
    """
    Calcule le hachage SHA256 d'une chaîne de caractères.
    """
    return hashlib.sha256(t.encode('utf-8')).hexdigest()

def extract_keywords(text: str) -> List[str]:
    """
    Extrait les mots-clés les plus fréquents d'un texte.
    Retourne une liste des 5 mots les plus fréquents (de 4 caractères ou plus).
    """
    # Trouve tous les mots de 4 caractères ou plus (incluant les accents)
    words = re.findall(r'\b[a-zA-Zéèêôàùçîïœ]{4,}\b', text.lower())
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    # Trie les mots par fréquence décroissante
    keywords = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [w for w,_ in keywords[:5]] # Retourne seulement les mots

def tag_conversation(text: str) -> str:
    """
    Génère un tag de conversation basé sur les mots-clés extraits du texte.
    """
    words = extract_keywords(text)
    return f"#tags : {', '.join(words)}"

def unique_preserve_order(seq: List[Any]) -> List[Any]:
    """
    Élimine les doublons d'une séquence tout en préservant l'ordre original des éléments.
    """
    seen = set()
    result = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def similar(a: str, b: str) -> float:
    """
    Calcule la similarité entre deux chaînes de caractères en utilisant le ratio de SequenceMatcher.
    Retourne un ratio de 0 à 1, où 1 indique une identité parfaite.
    """
    return difflib.SequenceMatcher(None, a.lower(), b.lower()).ratio()

def is_code(text: str) -> bool:
    """
    Détecte si le texte ressemble à du code (Python ou autre) en cherchant des motifs courants.
    """
    return bool(re.search(r"^\s*(def |class |import |print\()", text, re.MULTILINE)) or text.strip().startswith("```")

def is_python_code_block(text: str) -> bool:
    """
    Détecte si le texte est un bloc de code Python formaté en Markdown.
    """
    return text.strip().startswith("```python") and text.strip().endswith("```")

# api_clients.py
import time
import httpx
import json
import base64
import asyncio
import re
from typing import Dict, Any, Optional, Union, List, Tuple

# Import des constantes et fonctions utilitaires depuis les modules locaux
from config import API_CONFIG, ENDPOINT_HEALTH_FILE, OCR_API_KEYS, GEMINI_API_KEY
from utils import load_json, save_json, get_current_time, format_datetime, log_message, neutralize_urls

class EndpointHealthManager:
    """
    Gère la santé des endpoints API et sélectionne le meilleur endpoint disponible
    en fonction de critères comme la latence, le taux de succès et le nombre d'erreurs.
    C'est un singleton pour s'assurer qu'il n'y a qu'une seule instance de gestionnaire de santé.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """Implémente le patron de conception Singleton."""
        if cls._instance is None:
            cls._instance = super(cls, cls).__new__(cls)
            cls._instance._initialized = False # Indicateur pour l'initialisation asynchrone
        return cls._instance

    def __init__(self):
        """Initialise le gestionnaire. L'initialisation réelle se fait via `init_manager`."""
        if self._initialized:
            return
        self.health_status = {}
        # `_initialized` est géré par `init_manager` pour les opérations asynchrones

    async def init_manager(self):
        """
        Initialise le gestionnaire de santé de manière asynchrone.
        Charge l'état de santé persistant et s'assure que tous les endpoints sont suivis.
        """
        if not self._initialized:
            self.health_status = await load_json(ENDPOINT_HEALTH_FILE, {})
            self._initialize_health_status()
            self._initialized = True
            log_message("Gestionnaire de santé des endpoints initialisé.")

    def _initialize_health_status(self):
        """
        Initialise ou met à jour le statut de santé pour tous les endpoints configurés dans `API_CONFIG`.
        Ajoute les nouveaux endpoints et s'assure que toutes les clés nécessaires sont présentes.
        """
        updated = False
        for service_name, endpoints_config in API_CONFIG.items():
            if service_name not in self.health_status:
                self.health_status[service_name] = {}
                updated = True
            for endpoint_config in endpoints_config:
                # Crée une clé unique pour chaque endpoint en combinant son nom et sa clé API
                endpoint_key = f"{endpoint_config['endpoint_name']}-{str(endpoint_config['key'])}"
                if endpoint_key not in self.health_status[service_name]:
                    self.health_status[service_name][endpoint_key] = {
                        "latency": 0.0,
                        "success_rate": 1.0, # Commence avec un taux de succès parfait (sain)
                        "last_checked": None,
                        "error_count": 0,
                        "total_checks": 0,
                        "is_healthy": True # Présumé sain au début
                    }
                    updated = True
        if updated:
            # Sauvegarde l'état mis à jour de manière asynchrone en tâche de fond
            asyncio.create_task(save_json(ENDPOINT_HEALTH_FILE, self.health_status))
            log_message("Statut de santé des endpoints initialisé/mis à jour.")

    async def run_health_check_for_service(self, service_name: str):
        """
        Exécute des checks de santé pour tous les endpoints d'un service donné.
        Tente d'appeler l'endpoint avec des paramètres de santé prédéfinis.
        """
        endpoints_config = API_CONFIG.get(service_name)
        if not endpoints_config:
            log_message(f"Aucune configuration d'endpoint trouvée pour le service: {service_name}", level="warning")
            return

        log_message(f"Lancement du health check pour le service: {service_name}")
        for endpoint_config in endpoints_config:
            endpoint_key = f"{endpoint_config['endpoint_name']}-{str(endpoint_config['key'])}"
            start_time = time.monotonic()
            success = False
            try:
                request_method = endpoint_config.get("method", "GET")
                url = endpoint_config["url"]

                # Prépare les paramètres/données pour le health check
                params = endpoint_config.get("health_check_params", endpoint_config.get("fixed_params", {})).copy()
                json_data = endpoint_config.get("health_check_json", endpoint_config.get("fixed_json", {})).copy()
                headers = endpoint_config.get("fixed_headers", {}).copy()
                auth = None # Pour l'authentification de base (Basic Auth)

                check_timeout = endpoint_config.get("timeout", 5) # Timeout spécifique pour le health check

                # Ajoute un suffixe à l'URL si spécifié (ex: pour les APIs basées sur des chemins d'accès)
                if "health_check_url_suffix" in endpoint_config:
                    url += endpoint_config["health_check_url_suffix"]

                # Gère l'insertion de la clé API selon sa localisation (paramètre, en-tête, Basic Auth)
                key_field = endpoint_config.get("key_field")
                key_location = endpoint_config.get("key_location")
                key_prefix = endpoint_config.get("key_prefix", "") # Préfixe pour les clés dans les en-têtes (ex: "Bearer ")
                api_key = endpoint_config["key"]

                if key_field and key_location:
                    if key_location == "param":
                        params[key_field] = api_key
                    elif key_location == "header":
                        headers[key_field] = f"{key_prefix}{api_key}"
                    elif key_location == "auth_basic":
                        if isinstance(api_key, tuple) and len(api_key) == 2:
                            auth = httpx.BasicAuth(api_key[0], api_key[1])
                        else:
                            log_message(f"Clé API pour auth_basic non valide pour {service_name}:{endpoint_key}", level="error")
                            success = False
                            continue # Passe à l'endpoint suivant

                async with httpx.AsyncClient(timeout=check_timeout) as client:
                    response = await client.request(request_method, url, params=params, headers=headers, json=json_data, auth=auth)
                    response.raise_for_status() # Lève une exception pour les codes d'état HTTP 4xx/5xx
                    success = True
            except httpx.HTTPStatusError as e:
                log_level = "warning"
                # Les codes 4xx (sauf 429 - Too Many Requests) indiquent souvent une erreur client
                # (clé invalide, paramètre manquant) qui ne se résoudra pas avec un réessai
                # et n'indique pas forcément un problème de "santé" du service lui-même.
                # Nous les loguons en debug pour ne pas surcharger les logs.
                if 400 <= e.response.status_code < 500 and e.response.status_code != 429:
                    log_level = "debug"
                log_message(f"Health check pour {endpoint_key} ({service_name}) a échoué (HTTP {e.response.status_code}): {e.response.text}", level=log_level)
                success = False
            except httpx.RequestError as e:
                # Erreurs réseau (connexion, timeout, DNS, etc.)
                log_message(f"Health check pour {endpoint_key} ({service_name}) a échoué (Réseau): {e}", level="warning")
                success = False
            except Exception as e:
                # Autres erreurs inattendues
                log_message(f"Health check pour {endpoint_key} ({service_name}) a échoué (Inattendu): {e}", level="error")
                success = False
            finally:
                latency = time.monotonic() - start_time # Calcule la latence du check
                self.update_endpoint_health(service_name, endpoint_key, success, latency)
        log_message(f"Health check terminé pour le service: {service_name}")

    def update_endpoint_health(self, service_name: str, endpoint_key: str, success: bool, latency: float):
        """
        Met à jour le statut de santé d'un endpoint spécifique.
        Utilise une moyenne glissante pour le taux de succès et la latence.
        """
        # S'assure que la structure de données existe
        if service_name not in self.health_status:
            self.health_status[service_name] = {}
        if endpoint_key not in self.health_status[service_name]:
            self.health_status[service_name][endpoint_key] = {
                "latency": 0.0,
                "success_rate": 1.0,
                "last_checked": None,
                "error_count": 0,
                "total_checks": 0,
                "is_healthy": True
            }

        status = self.health_status[service_name][endpoint_key]
        status["total_checks"] += 1
        status["last_checked"] = format_datetime(get_current_time())

        alpha = 0.1 # Facteur de lissage pour les moyennes glissantes (0.1 signifie 10% de la nouvelle valeur, 90% de l'ancienne)
        if success:
            status["error_count"] = max(0, status["error_count"] - 1) # Diminue le compteur d'erreurs en cas de succès
            status["success_rate"] = status["success_rate"] * (1 - alpha) + 1.0 * alpha # Augmente le taux de succès
            status["latency"] = status["latency"] * (1 - alpha) + latency * alpha # Met à jour la latence
        else:
            status["error_count"] += 1 # Incrémente le compteur d'erreurs
            status["success_rate"] = status["success_rate"] * (1 - alpha) + 0.0 * alpha # Diminue le taux de succès
            # Si échec, pénalise la latence pour rendre l'endpoint moins attrayant (valeur arbitraire élevée)
            status["latency"] = status["latency"] * (1 - alpha) + 10.0 * alpha

        # Détermine si l'endpoint est sain basé sur le nombre d'erreurs consécutives ou le taux de succès
        if status["error_count"] >= 3 or status["success_rate"] < 0.5:
            status["is_healthy"] = False
        else:
            status["is_healthy"] = True

        # Sauvegarde l'état mis à jour de manière asynchrone
        asyncio.create_task(save_json(ENDPOINT_HEALTH_FILE, self.health_status))
        log_message(f"Santé de {service_name}:{endpoint_key} mise à jour: Succès: {success}, Latence: {latency:.2f}s, Taux Succès: {status['success_rate']:.2f}, Sain: {status['is_healthy']}", level="debug" if not status["is_healthy"] else "info")

    def get_best_endpoint(self, service_name: str) -> Optional[Dict]:
        """
        Sélectionne le meilleur endpoint pour un service donné basé sur son statut de santé.
        Priorise les endpoints sains, puis les moins mauvais en cas d'absence d'endpoints sains.
        """
        service_health = self.health_status.get(service_name)
        if not service_health:
            log_message(f"Aucune donnée de santé pour le service {service_name}. Retourne None.", level="warning")
            return None

        best_endpoint_key = None
        best_score = -float('inf')

        # Filtre les endpoints actuellement considérés comme sains
        healthy_endpoints = [
            (key, status) for key, status in service_health.items() if status["is_healthy"]
        ]

        if not healthy_endpoints:
            log_message(f"Aucun endpoint sain pour le service {service_name}. Tentative de sélection d'un endpoint non sain.", level="warning")
            all_endpoints = service_health.items()
            if not all_endpoints:
                return None # Aucun endpoint du tout

            # Si aucun endpoint sain, choisit le "moins mauvais" : moins d'erreurs, meilleure latence
            sorted_endpoints = sorted(all_endpoints, key=lambda item: (item[1]["error_count"], item[1]["latency"]))
            best_endpoint_key = sorted_endpoints[0][0]
            log_message(f"Fallback: Endpoint {best_endpoint_key} sélectionné pour {service_name} (non sain).", level="warning")
        else:
            # Calcule un score pour chaque endpoint sain pour choisir le meilleur
            for endpoint_key, status in healthy_endpoints:
                # Score = (Taux de succès * 100) - (Latence * 10) - (Compteur d'erreurs * 5)
                # Favorise le succès, pénalise la latence et les erreurs
                score = (status["success_rate"] * 100) - (status["latency"] * 10) - (status["error_count"] * 5)
                if score > best_score:
                    best_score = score
                    best_endpoint_key = endpoint_key
            log_message(f"Meilleur endpoint sélectionné pour {service_name}: {best_endpoint_key} (Score: {best_score:.2f})")

        if best_endpoint_key:
            # Une fois la clé du meilleur endpoint trouvée, on récupère sa configuration complète
            # depuis `API_CONFIG` pour l'utiliser dans la requête.
            for endpoint_config in API_CONFIG.get(service_name, []):
                current_endpoint_key = f"{endpoint_config['endpoint_name']}-{str(endpoint_config['key'])}"
                if current_endpoint_key == best_endpoint_key:
                    return endpoint_config
        return None # Aucun endpoint approprié trouvé

# Instancier le gestionnaire de santé des endpoints (sera initialisé dans main.py)
endpoint_health_manager = EndpointHealthManager()

def set_endpoint_health_manager_global(manager: EndpointHealthManager):
    """
    Permet d'injecter l'instance du gestionnaire de santé des endpoints.
    Ceci est utilisé pour s'assurer que tous les clients API utilisent la même instance.
    """
    global endpoint_health_manager
    endpoint_health_manager = manager

class APIClient:
    """
    Classe de base pour tous les clients API.
    Elle gère la sélection dynamique d'endpoints, les réessais en cas d'échec
    et l'intégration avec le gestionnaire de santé des endpoints.
    """
    def __init__(self, name: str, endpoint_health_manager: EndpointHealthManager):
        self.name = name
        self.endpoints_config = API_CONFIG.get(name, []) # Récupère la config des endpoints pour cette API
        self.endpoint_health_manager = endpoint_health_manager
        if not self.endpoints_config:
            log_message(f"Client API {self.name} initialisé sans configuration d'endpoint.", level="error")

    async def _make_request(self, params: Optional[Dict] = None, headers: Optional[Dict] = None,
                            json_data: Optional[Dict] = None, timeout: Optional[int] = None,
                            max_retries: int = 3, initial_delay: float = 1.0,
                            url: Optional[str] = None, method: Optional[str] = None,
                            key_field: Optional[str] = None, key_location: Optional[str] = None,
                            api_key: Optional[Union[str, Tuple[str, str]]] = None,
                            fixed_params: Optional[Dict] = None, fixed_headers: Optional[Dict] = None,
                            fixed_json: Optional[Dict] = None) -> Optional[Union[Dict, str, bytes]]:
        """
        Méthode interne pour effectuer les requêtes HTTP en utilisant le meilleur endpoint avec réessais.

        Args:
            params (Dict, optional): Paramètres de requête à ajouter à l'URL.
            headers (Dict, optional): En-têtes HTTP supplémentaires.
            json_data (Dict, optional): Données JSON à envoyer dans le corps de la requête (pour POST/PUT).
            timeout (int, optional): Timeout pour la requête en secondes.
            max_retries (int): Nombre maximal de tentatives en cas d'échec.
            initial_delay (float): Délai initial entre les réessais (exponentiel).
            url (str, optional): URL spécifique à utiliser (si non basé sur un endpoint configuré).
            method (str, optional): Méthode HTTP (GET, POST, etc.).
            key_field (str, optional): Nom du champ pour la clé API.
            key_location (str, optional): Où placer la clé API ('param', 'header', 'auth_basic').
            api_key (Union[str, Tuple[str, str]], optional): Clé API à utiliser.
            fixed_params (Dict, optional): Paramètres fixes définis dans la configuration de l'endpoint.
            fixed_headers (Dict, optional): En-têtes fixes définis dans la configuration de l'endpoint.
            fixed_json (Dict, optional): Données JSON fixes définies dans la configuration de l'endpoint.

        Returns:
            Union[Dict, str, bytes, None]: La réponse de l'API (JSON décodé, texte brut, ou bytes pour les images),
                                          ou un dictionnaire d'erreur en cas d'échec.
        """

        selected_endpoint_config = None
        endpoint_key_for_health = "Dynamic" # Clé par défaut pour les requêtes dynamiques (non configurées)

        if url and method: # Si l'URL et la méthode sont fournies directement (requête dynamique)
            selected_endpoint_config = {
                "url": url,
                "method": method,
                "key_field": key_field,
                "key_location": key_location,
                "key": api_key,
                "fixed_params": fixed_params if fixed_params is not None else {},
                "fixed_headers": fixed_headers if fixed_headers is not None else {},
                "fixed_json": fixed_json if fixed_json is not None else {},
                "endpoint_name": "Dynamic", # Nom générique pour les endpoints dynamiques
                "timeout": timeout if timeout is not None else 30
            }
            if api_key:
                # Crée une clé de santé unique pour les requêtes dynamiques avec clé API
                endpoint_key_for_health = f"Dynamic-{str(api_key)}"
            log_message(f"Requête dynamique pour {self.name} vers {url}")
        else: # Sélectionne le meilleur endpoint configuré via le gestionnaire de santé
            selected_endpoint_config = self.endpoint_health_manager.get_best_endpoint(self.name)
            if not selected_endpoint_config:
                log_message(f"Aucun endpoint sain ou disponible pour {self.name}.", level="error")
                return {"error": True, "message": f"Aucun endpoint sain ou disponible pour {self.name}."}
            # Construit la clé de santé pour l'endpoint sélectionné
            endpoint_key_for_health = f"{selected_endpoint_config['endpoint_name']}-{str(selected_endpoint_config['key'])}"
            log_message(f"Endpoint sélectionné pour {self.name}: {selected_endpoint_config['endpoint_name']}")
            # Utilise le timeout de la config de l'endpoint si non spécifié
            timeout = timeout if timeout is not None else selected_endpoint_config.get("timeout", 30)

        url_to_use = selected_endpoint_config["url"]
        method_to_use = selected_endpoint_config["method"]

        # Initialise les paramètres, en-têtes et données JSON avec les valeurs fixes de la config
        request_params = selected_endpoint_config.get("fixed_params", {}).copy()
        request_headers = selected_endpoint_config.get("fixed_headers", {}).copy()
        request_json_data = selected_endpoint_config.get("fixed_json", {}).copy()
        auth = None # Pour l'authentification de base

        # Fusionne les paramètres/en-têtes/données JSON fournis avec les valeurs fixes
        if params:
            request_params.update(params)
        if headers:
            request_headers.update(headers)
        if json_data:
            request_json_data.update(json_data)

        # Gère l'insertion de la clé API pour la requête
        key_field_to_use = selected_endpoint_config.get("key_field")
        key_location_to_use = selected_endpoint_config.get("key_location")
        key_prefix = selected_endpoint_config.get("key_prefix", "")
        api_key_to_use = selected_endpoint_config["key"]

        if key_field_to_use and key_location_to_use:
            if key_location_to_use == "param":
                request_params[key_field_to_use] = api_key_to_use
            elif key_location_to_use == "header":
                request_headers[key_field_to_use] = f"{key_prefix}{api_key_to_use}"
            elif key_location_to_use == "auth_basic":
                if isinstance(api_key_to_use, tuple) and len(api_key_to_use) == 2:
                    auth = httpx.BasicAuth(api_key_to_use[0], api_key_to_use[1])
                else:
                    log_message(f"Clé API pour auth_basic non valide pour {self.name}:{endpoint_key_for_health}", level="error")
                    # Marque l'endpoint comme non sain et retourne une erreur
                    self.endpoint_health_manager.update_endpoint_health(self.name, endpoint_key_for_health, False, 0.0)
                    return {"error": True, "message": "Configuration d'authentification basique invalide."}

        current_delay = initial_delay # Délai initial pour les réessais
        for attempt in range(max_retries):
            start_time = time.monotonic()
            success = False
            try:
                async with httpx.AsyncClient(timeout=timeout) as client:
                    response = await client.request(method_to_use, url_to_use, params=request_params, headers=request_headers, json=request_json_data, auth=auth)
                    response.raise_for_status() # Lève une exception pour les codes d'état HTTP 4xx/5xx
                    success = True

                    content_type = response.headers.get("Content-Type", "").lower()
                    if "application/json" in content_type:
                        try:
                            return response.json() # Tente de décoder la réponse JSON
                        except json.JSONDecodeError:
                            log_message(f"API {self.name} réponse non JSON valide (tentative {attempt+1}/{max_retries}): {response.text[:200]}...", level="warning")
                            if attempt < max_retries - 1: # Si ce n'est pas la dernière tentative, réessaie
                                await asyncio.sleep(current_delay)
                                current_delay *= 2 # Augmente le délai de manière exponentielle
                                continue
                            return {"error": True, "message": "Réponse API non JSON valide.", "raw_response": response.text}
                    else:
                        log_message(f"API {self.name} a renvoyé un Content-Type non JSON: {content_type}", level="info")
                        return response.content # Retourne le contenu brut (ex: pour les images)

            except httpx.HTTPStatusError as e:
                log_message(f"API {self.name} erreur HTTP (tentative {attempt+1}/{max_retries}): {e.response.status_code} - {e.response.text}", level="warning")
                # Ne pas réessayer pour les erreurs client (4xx) sauf 429 (Too Many Requests)
                if 400 <= e.response.status_code < 500 and e.response.status_code != 429:
                    log_message(f"API {self.name}: Erreur client {e.response.status_code}, pas de réessai.", level="error")
                    self.endpoint_health_manager.update_endpoint_health(self.name, endpoint_key_for_health, False, e.response.elapsed.total_seconds())
                    return {"error": True, "status_code": e.response.status_code, "message": e.response.text}

                if attempt < max_retries - 1:
                    log_message(f"API {self.name}: Réessai dans {current_delay:.2f}s...", level="info")
                    await asyncio.sleep(current_delay)
                    current_delay *= 2
            except httpx.RequestError as e:
                log_message(f"API {self.name} erreur de requête (tentative {attempt+1}/{max_retries}): {e}", level="warning")
                if attempt < max_retries - 1:
                    log_message(f"API {self.name}: Réessai dans {current_delay:.2f}s...", level="info")
                    await asyncio.sleep(current_delay)
                    current_delay *= 2
            except Exception as e:
                log_message(f"API {self.name} erreur inattendue (tentative {attempt+1}/{max_retries}): {e}", level="error")
                self.endpoint_health_manager.update_endpoint_health(self.name, endpoint_key_for_health, False, time.monotonic() - start_time)
                return {"error": True, "message": str(e)}
            finally:
                # Met à jour la santé de l'endpoint même en cas d'échec pour la sélection future
                if not success:
                    latency = time.monotonic() - start_time
                    self.endpoint_health_manager.update_endpoint_health(self.name, endpoint_key_for_health, False, latency)

        log_message(f"API {self.name}: Toutes les tentatives ont échoué après {max_retries} réessais.", level="error")
        return {"error": True, "message": f"Échec de la requête après {max_retries} tentatives."}

    async def query(self, *args, **kwargs) -> Any:
        """
        Méthode abstraite pour interroger l'API.
        Doit être implémentée par chaque sous-classe de client API.
        """
        raise NotImplementedError("La méthode query doit être implémentée par les sous-classes.")

# --- Clients API Spécifiques ---
# Chaque classe de client API hérite de `APIClient` et implémente la méthode `query`
# pour interagir avec une API spécifique.

class DeepSeekClient(APIClient):
    def __init__(self):
        super().__init__("DEEPSEEK", endpoint_health_manager)

    async def query(self, prompt: str, model: str = "deepseek-chat") -> str:
        """Interroge l'API DeepSeek pour des complétions de chat."""
        payload = {"model": model, "messages": [{"role": "user", "content": prompt}]}
        response = await self._make_request(json_data=payload)
        if response and not response.get("error"):
            content = response.get("choices", [{}])[0].get("message", {}).get("content")
            return content if content else "DeepSeek: Pas de contenu de réponse trouvé."
        return f"DeepSeek: Erreur: {response.get('message', 'Inconnu')}" if response else "DeepSeek: Réponse vide ou erreur interne."

class SerperClient(APIClient):
    def __init__(self):
        super().__init__("SERPER", endpoint_health_manager)

    async def query(self, query_text: str) -> str:
        """Effectue une recherche web via l'API Serper."""
        payload = {"q": query_text}
        response = await self._make_request(json_data=payload)
        if response and not response.get("error"):
            organic_results = response.get("organic", [])
            if organic_results:
                snippet = organic_results[0].get("snippet", "Pas de snippet.")
                link = organic_results[0].get("link", "")
                return f"Serper (recherche web):\n{snippet} {neutralize_urls(link)}"
            return "Serper: Aucune information trouvée."
        return f"Serper: Erreur: {response.get('message', 'Inconnu')}" if response else "Serper: Réponse vide ou erreur interne."

class WolframAlphaClient(APIClient):
    def __init__(self):
        super().__init__("WOLFRAMALPHA", endpoint_health_manager)

    async def query(self, input_text: str) -> str:
        """Interroge WolframAlpha pour des calculs ou des faits."""
        params = {"input": input_text}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            pods = response.get("queryresult", {}).get("pods", [])
            if pods:
                for pod in pods:
                    if pod.get("title") in ["Result", "Input interpretation", "Decimal approximation"]:
                        subpods = pod.get("subpods", [])
                        if subpods and subpods[0].get("plaintext"):
                            return f"WolframAlpha:\n{subpods[0]['plaintext']}"
                if pods and pods[0].get("subpods") and pods[0]["subpods"][0].get("plaintext"):
                    return f"WolframAlpha:\n{pods[0]['subpods'][0]['plaintext']}"
            return "WolframAlpha: Pas de résultat clair."
        return f"WolframAlpha: Erreur: {response.get('message', 'Inconnu')}" if response else "WolframAlpha: Réponse vide ou erreur interne."

class TavilyClient(APIClient):
    def __init__(self):
        super().__init__("TAVILY", endpoint_health_manager)

    async def query(self, query_text: str, max_results: int = 3) -> str:
        """Effectue une recherche web avancée via l'API Tavily."""
        payload = {"query": query_text, "max_results": max_results}
        response = await self._make_request(json_data=payload)
        if response and not response.get("error"):
            results = response.get("results", [])
            answer = response.get("answer", "Aucune réponse directe trouvée.")

            output = f"Tavily (recherche web):\nRéponse directe: {answer}\n"
            if results:
                output += "Extraits pertinents:\n"
                for i, res in enumerate(results[:max_results]):
                    output += f"- {res.get('title', 'N/A')}: {res.get('content', 'N/A')} {neutralize_urls(res.get('url', ''))}\n"
            return output
        return f"Tavily: Erreur: {response.get('message', 'Inconnu')}" if response else "Tavily: Réponse vide ou erreur interne."

class ApiFlashClient(APIClient):
    def __init__(self):
        super().__init__("APIFLASH", endpoint_health_manager)

    async def query(self, url: str) -> str:
        """Capture une capture d'écran d'une URL via ApiFlash."""
        params = {"url": url, "format": "jpeg", "full_page": "true"}
        response_content = await self._make_request(params=params)

        if isinstance(response_content, bytes):
            selected_endpoint_config = self.endpoint_health_manager.get_best_endpoint(self.name)
            if selected_endpoint_config:
                capture_url = f"{selected_endpoint_config['url']}?access_key={selected_endpoint_config['key']}&url={url}&format=jpeg&full_page=true"
                return f"ApiFlash (capture d'écran): {neutralize_urls(capture_url)} (Vérifiez le lien pour l'image)"
            return "ApiFlash: Impossible de générer l'URL de capture."
        elif isinstance(response_content, dict) and response_content.get("error"):
            return f"ApiFlash: Erreur: {response_content.get('message', 'Inconnu')}"
        else:
            log_message(f"ApiFlash a renvoyé un type de réponse inattendu: {type(response_content)}", level="warning")
            return f"ApiFlash: Réponse inattendue de l'API. {response_content}"

class CrawlbaseClient(APIClient):
    def __init__(self):
        super().__init__("CRAWLBASE", endpoint_health_manager)

    async def query(self, url: str, use_js: bool = False) -> str:
        """Scrape le contenu HTML ou JavaScript d'une URL via Crawlbase."""
        params = {"url": url, "format": "json"}

        selected_endpoint_config = None
        if use_js:
            for config in API_CONFIG.get(self.name, []):
                if "JS Scraping" in config.get("endpoint_name", ""):
                    selected_endpoint_config = config
                    break

        if not selected_endpoint_config:
            selected_endpoint_config = self.endpoint_health_manager.get_best_endpoint(self.name)

        if not selected_endpoint_config:
            return f"Crawlbase: Aucun endpoint sain ou disponible pour {self.name}."

        response = await self._make_request(
            params=params,
            url=selected_endpoint_config["url"],
            method=selected_endpoint_config["method"],
            key_field=selected_endpoint_config["key_field"],
            key_location=selected_endpoint_config["key_location"],
            api_key=selected_endpoint_config["key"],
            fixed_params=selected_endpoint_config.get("fixed_params", {}),
            timeout=selected_endpoint_config.get("timeout")
        )

        if response and not response.get("error"):
            body = response.get("body")
            if body:
                try:
                    decoded_body = base64.b64decode(body).decode('utf-8', errors='ignore')
                    return f"Crawlbase (contenu web):\n{decoded_body[:1000]}..."
                except Exception:
                    return f"Crawlbase (contenu web - brut):\n{body[:1000]}..."
            return "Crawlbase: Contenu non trouvé."
        return f"Crawlbase: Erreur: {response.get('message', 'Inconnu')}" if response else "Crawlbase: Réponse vide ou erreur interne."

class DetectLanguageClient(APIClient):
    def __init__(self):
        super().__init__("DETECTLANGUAGE", endpoint_health_manager)

    async def query(self, text: str) -> str:
        """Détecte la langue d'un texte via DetectLanguage API."""
        payload = {"q": text}
        response = await self._make_request(json_data=payload)
        if response and not response.get("error"):
            detections = response.get("data", {}).get("detections", [])
            if detections:
                first_detection = detections[0]
                lang = first_detection.get("language")
                confidence = first_detection.get("confidence")
                return f"Langue détectée: {lang} (confiance: {confidence})"
            return "DetectLanguage: Aucune langue détectée."
        return f"DetectLanguage: Erreur: {response.get('message', 'Inconnu')}" if response else "DetectLanguage: Réponse vide ou erreur interne."

class GuardianClient(APIClient):
    def __init__(self):
        super().__init__("GUARDIAN", endpoint_health_manager)

    async def query(self, query_text: str) -> str:
        """Recherche des articles de presse via l'API The Guardian."""
        params = {"q": query_text}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            results = response.get("response", {}).get("results", [])
            if results:
                output = "Articles The Guardian:\n"
                for res in results[:3]: # Limite à 3 articles pour la concision
                    output += f"- {res.get('webTitle', 'N/A')}: {res.get('fields', {}).get('trailText', 'N/A')} {neutralize_urls(res.get('webUrl', ''))}\n"
                return output
            return "Guardian: Aucun article trouvé."
        return f"Guardian: Erreur: {response.get('message', 'Inconnu')}" if response else "Guardian: Réponse vide ou erreur interne."

class IP2LocationClient(APIClient):
    def __init__(self):
        super().__init__("IP2LOCATION", endpoint_health_manager)

    async def query(self, ip_address: str) -> str:
        """Géolocalise une adresse IP via IP2Location API."""
        params = {"ip": ip_address}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            if "country_name" in response:
                return f"IP2Location (Géolocalisation IP {ip_address}): Pays: {response['country_name']}, Ville: {response.get('city_name', 'N/A')}"
            return "IP2Location: Informations non trouvées."
        return f"IP2Location: Erreur: {response.get('message', 'Inconnu')}" if response else "IP2Location: Réponse vide ou erreur interne."

class ShodanClient(APIClient):
    def __init__(self):
        super().__init__("SHODAN", endpoint_health_manager)

    async def query(self, query_text: str = "") -> str:
        """
        Interroge Shodan pour des informations sur un hôte IP ou des informations sur la clé API.
        Si `query_text` est une IP, tente de récupérer les infos de l'hôte.
        Sinon, ou en cas d'échec, retourne les infos de la clé API.
        """
        if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", query_text): # Vérifie si c'est une adresse IP
            selected_endpoint_config = None
            for config in API_CONFIG.get(self.name, []):
                if "Host Info" in config.get("endpoint_name", ""):
                    selected_endpoint_config = config
                    break
            if selected_endpoint_config:
                # Construire l'URL pour la recherche d'hôte
                url = f"{selected_endpoint_config['url'].rstrip('/')}/{query_text}"
                response = await self._make_request(
                    params={"key": selected_endpoint_config["key"]},
                    url=url,
                    method="GET",
                    key_field=selected_endpoint_config["key_field"],
                    key_location=selected_endpoint_config["key_location"],
                    api_key=selected_endpoint_config["key"],
                    timeout=selected_endpoint_config.get("timeout")
                )
                if response and not response.get("error"):
                    return f"Shodan (info hôte {query_text}): Pays: {response.get('country_name', 'N/A')}, Ports: {response.get('ports', 'N/A')}, Vulnérabilités: {response.get('vulns', 'Aucune')}"
                return f"Shodan (info hôte): Erreur: {response.get('message', 'Inconnu')}" if response else "Shodan: Réponse vide ou erreur interne."
            else:
                return "Shodan: Endpoint 'Host Info' non configuré."
        else:
            # Si pas d'IP ou si la recherche d'hôte n'est pas applicable, retourne les infos de la clé API
            response = await self._make_request() # Utilise le premier endpoint disponible (API Info)
            if response and not response.get("error"):
                return f"Shodan (info clé): Requêtes restantes: {response.get('usage_limits', {}).get('query_credits', 'N/A')}, Scan crédits: {response.get('usage_limits', {}).get('scan_credits', 'N/A')}"
            return f"Shodan: Erreur: {response.get('message', 'Inconnu')}" if response else "Shodan: Réponse vide ou erreur interne."

class WeatherAPIClient(APIClient):
    def __init__(self):
        super().__init__("WEATHERAPI", endpoint_health_manager)

    async def query(self, location: str) -> str:
        """Récupère les conditions météorologiques actuelles pour une localisation via WeatherAPI."""
        params = {"q": location}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            current = response.get("current", {})
            location_info = response.get("location", {})
            if current and location_info:
                return (
                    f"Météo à {location_info.get('name', 'N/A')}, {location_info.get('country', 'N/A')}:\n"
                    f"Température: {current.get('temp_c', 'N/A')}°C, "
                    f"Conditions: {current.get('condition', {}).get('text', 'N/A')}, "
                    f"Vent: {current.get('wind_kph', 'N/A')} km/h"
                )
            return "WeatherAPI: Données météo non trouvées."
        return f"WeatherAPI: Erreur: {response.get('message', 'Inconnu')}" if response else "WeatherAPI: Réponse vide ou erreur interne."

class CloudmersiveClient(APIClient):
    def __init__(self):
        super().__init__("CLOUDMERSIVE", endpoint_health_manager)

    async def query(self, domain: str) -> str:
        """Vérifie la validité et le type d'un domaine via Cloudmersive API."""
        payload = {"domain": domain}
        response = await self._make_request(json_data=payload)
        if response and not response.get("error"):
            return f"Cloudmersive (vérification de domaine {domain}): Valide: {response.get('ValidDomain', 'N/A')}, Type: {response.get('DomainType', 'N/A')}"
        return f"Cloudmersive: Erreur: {response.get('message', 'Inconnu')}" if response else "Cloudmersive: Réponse vide ou erreur interne."

class GreyNoiseClient(APIClient):
    def __init__(self):
        super().__init__("GREYNOISE", endpoint_health_manager)

    async def query(self, ip_address: str) -> str:
        """Analyse une adresse IP pour détecter des activités 'bruit' (malveillantes) via GreyNoise."""
        selected_endpoint_config = self.endpoint_health_manager.get_best_endpoint(self.name)
        if not selected_endpoint_config:
            return f"GreyNoise: Aucun endpoint sain ou disponible pour {self.name}."

        # Construit l'URL avec l'adresse IP à la fin
        url = f"{selected_endpoint_config['url'].rstrip('/')}/{ip_address}"
        method = selected_endpoint_config["method"]
        headers = {selected_endpoint_config["key_field"]: selected_endpoint_config["key"]}

        response = await self._make_request(
            headers=headers,
            url=url,
            method=method,
            key_field=selected_endpoint_config["key_field"],
            key_location=selected_endpoint_config["key_location"],
            api_key=selected_endpoint_config["key"],
            timeout=selected_endpoint_config.get("timeout")
        )

        if response and not response.get("error"):
            if response.get("noise"):
                return f"GreyNoise (IP {ip_address}): C'est une IP 'bruit' (malveillante). Classification: {response.get('classification', 'N/A')}, Nom d'acteur: {response.get('actor', 'N/A')}"
            return f"GreyNoise (IP {ip_address}): Pas de 'bruit' détecté. Statut: {response.get('status', 'N/A')}"
        return f"GreyNoise: Erreur: {response.get('message', 'Inconnu')}" if response else "GreyNoise: Réponse vide ou erreur interne."

class PulsediveClient(APIClient):
    def __init__(self):
        super().__init__("PULSEDIVE", endpoint_health_manager)

    async def query(self, indicator: str, type: str = "auto") -> str:
        """Analyse un indicateur de menace (IP, domaine, URL) via Pulsedive."""
        params = {"indicator": indicator, "type": type}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            if response.get("results"):
                result = response["results"][0] # Prend le premier résultat
                return (
                    f"Pulsedive (Analyse {indicator}): Type: {result.get('type', 'N/A')}, "
                    f"Risk: {result.get('risk', 'N/A')}, "
                    f"Description: {result.get('description', 'N/A')[:200]}..." # Tronque la description
                )
            return "Pulsedive: Aucun résultat d'analyse trouvé."
        return f"Pulsedive: Erreur: {response.get('message', 'Inconnu')}" if response else "Pulsedive: Réponse vide ou erreur interne."

class StormGlassClient(APIClient):
    def __init__(self):
        super().__init__("STORMGLASS", endpoint_health_manager)

    async def query(self, lat: float, lng: float, params: str = "airTemperature,waveHeight") -> str:
        """Récupère les données météorologiques maritimes pour une coordonnée via StormGlass."""
        now = int(time.time())
        request_params = {
            "lat": lat,
            "lng": lng,
            "params": params,
            "start": now,
            "end": now + 3600 # Prévisions pour la prochaine heure (3600 secondes)
        }
        response = await self._make_request(params=request_params)
        if response and not response.get("error"):
            data = response.get("hours", [])
            if data:
                first_hour = data[0]
                # Accède aux valeurs spécifiques des paramètres demandés
                temp = first_hour.get('airTemperature', [{}])[0].get('value', 'N/A')
                wave_height = first_hour.get('waveHeight', [{}])[0].get('value', 'N/A')
                return f"StormGlass (Météo maritime à {lat},{lng}): Température air: {temp}°C, Hauteur vagues: {wave_height}m"
            return "StormGlass: Données non trouvées."
        return f"StormGlass: Erreur: {response.get('message', 'Inconnu')}" if response else "StormGlass: Réponse vide ou erreur interne."

class LoginRadiusClient(APIClient):
    def __init__(self):
        super().__init__("LOGINRADIUS", endpoint_health_manager)

    async def query(self) -> str:
        """Effectue un simple ping à l'API LoginRadius pour vérifier sa disponibilité."""
        response = await self._make_request()
        if response and not response.get("error"):
            return f"LoginRadius (Ping API): Statut: {response.get('Status', 'N/A')}, Message: {response.get('Message', 'N/A')}"
        return f"LoginRadius: Erreur: {response.get('message', 'Inconnu')}" if response else "LoginRadius: Réponse vide ou erreur interne."

class JsonbinClient(APIClient):
    def __init__(self):
        super().__init__("JSONBIN", endpoint_health_manager)

    async def query(self, data: Optional[Dict[str, Any]] = None, private: bool = True, bin_id: Optional[str] = None) -> str:
        """
        Crée un nouveau 'bin' JSON ou accède à un bin existant via Jsonbin.io.
        `data` est pour la création, `bin_id` pour l'accès.
        """
        if bin_id: # Accès à un bin existant
            selected_endpoint_config = None
            for config in API_CONFIG.get(self.name, []):
                if "Bin Access" in config.get("endpoint_name", ""):
                    selected_endpoint_config = config
                    break
            if not selected_endpoint_config:
                return f"Jsonbin: Aucun endpoint d'accès de bin sain ou disponible pour {self.name}."

            url = f"{selected_endpoint_config['url'].rstrip('/')}/{bin_id}"
            method = "GET"
            headers = {selected_endpoint_config["key_field"]: selected_endpoint_config["key"]}

            response = await self._make_request(
                headers=headers,
                url=url,
                method=method,
                timeout=selected_endpoint_config.get("timeout")
            )
            if response and not response.get("error"):
                return f"Jsonbin (Accès bin {bin_id}):\n{json.dumps(response, indent=2)}"
            return f"Jsonbin (Accès bin): Erreur: {response.get('message', 'Inconnu')}" if response else "Jsonbin: Réponse vide ou erreur interne."

        else: # Création d'un nouveau bin
            selected_endpoint_config = None
            for config in API_CONFIG.get(self.name, []):
                if "Bin Create" in config.get("endpoint_name", ""):
                    selected_endpoint_config = config
                    break

            if not selected_endpoint_config:
                return f"Jsonbin: Aucun endpoint de création de bin sain ou disponible pour {self.name}."

            url = selected_endpoint_config["url"]
            method = "POST"
            headers = {selected_endpoint_config["key_field"]: selected_endpoint_config["key"], "Content-Type": "application/json"}
            payload = {"record": data if data is not None else {}, "private": private}

            response = await self._make_request(
                json_data=payload,
                headers=headers,
                url=url,
                method=method,
                timeout=selected_endpoint_config.get("timeout")
            )

            if response and not response.get("error"):
                return f"Jsonbin (Création de bin): ID: {response.get('metadata', {}).get('id', 'N/A')}, URL: {neutralize_urls(response.get('metadata', {}).get('url', 'N/A'))}"
            return f"Jsonbin (Création de bin): Erreur: {response.get('message', 'Inconnu')}" if response else "Jsonbin: Réponse vide ou erreur interne."

class HuggingFaceClient(APIClient):
    def __init__(self):
        super().__init__("HUGGINGFACE", endpoint_health_manager)

    async def query(self, model_name: str = "distilbert-base-uncased-finetuned-sst-2-english", input_text: str = "Hello world") -> str:
        """Effectue une inférence sur un modèle HuggingFace (ex: classification de texte, génération)."""
        selected_endpoint_config = self.endpoint_health_manager.get_best_endpoint(self.name)
        if not selected_endpoint_config:
            return f"HuggingFace: Aucun endpoint sain ou disponible pour {self.name}."

        inference_url = f"https://api-inference.huggingface.co/models/{model_name}"

        headers = {
            selected_endpoint_config["key_field"]: f"{selected_endpoint_config['key_prefix']}{selected_endpoint_config['key']}",
            "Content-Type": "application/json"
        }
        payload = {"inputs": input_text}

        response = await self._make_request(
            json_data=payload,
            headers=headers,
            url=inference_url,
            method="POST",
            timeout=selected_endpoint_config.get("timeout")
        )

        if response and not response.get("error"):
            if isinstance(response, list) and response:
                first_result = response[0]
                if isinstance(first_result, list) and first_result:
                    return f"HuggingFace ({model_name} - {first_result[0].get('label')}): Score {first_result[0].get('score', 'N/A'):.2f}"
                elif isinstance(first_result, dict) and "generated_text" in first_result:
                    return f"HuggingFace ({model_name}): {first_result.get('generated_text')}"
            return f"HuggingFace ({model_name}): Réponse non parsée. {response}"
        return f"HuggingFace: Erreur: {response.get('message', 'Inconnu')}" if response else "HuggingFace: Réponse vide ou erreur interne."

class TwilioClient(APIClient):
    def __init__(self):
        super().__init__("TWILIO", endpoint_health_manager)

    async def query(self) -> str:
        """Récupère le solde du compte Twilio."""
        selected_endpoint_config = None
        for config in API_CONFIG.get(self.name, []):
            if "Account Balance" in config.get("endpoint_name", ""):
                selected_endpoint_config = config
                break
        if not selected_endpoint_config:
            if self.endpoints_config:
                selected_endpoint_config = self.endpoints_config[0]
            else:
                return f"Twilio: Aucune configuration d'endpoint disponible pour {self.name}."

        response = await self._make_request(
            url=selected_endpoint_config["url"],
            method=selected_endpoint_config["method"],
            key_location=selected_endpoint_config["key_location"],
            api_key=selected_endpoint_config["key"],
            timeout=selected_endpoint_config.get("timeout")
        )
        if response and not response.get("error"):
            return f"Twilio (Balance): {response.get('balance', 'N/A')} {response.get('currency', 'N/A')}"
        return f"Twilio: Erreur: {response.get('message', 'Inconnu')}" if response else "Twilio: Réponse vide ou erreur interne."

class AbstractAPIClient(APIClient):
    def __init__(self):
        super().__init__("ABSTRACTAPI", endpoint_health_manager)

    async def query(self, input_value: str, api_type: str) -> str:
        """
        Interroge diverses APIs d'AbstractAPI (validation email/téléphone, taux de change, jours fériés).
        `input_value` dépend du `api_type`.
        """
        params = {}
        target_endpoint_name = ""

        if api_type == "PHONE_VALIDATION":
            params["phone"] = input_value
            target_endpoint_name = "Phone Validation"
        elif api_type == "EMAIL_VALIDATION":
            params["email"] = input_value
            target_endpoint_name = "Email Validation"
        elif api_type == "EXCHANGE_RATES":
            params["base"] = input_value if input_value else "USD"
            target_endpoint_name = "Exchange Rates"
        elif api_type == "HOLIDAYS":
            params["country"] = input_value if input_value else "US"
            params["year"] = datetime.now().year
            target_endpoint_name = "Holidays"
        else:
            return f"AbstractAPI: Type d'API '{api_type}' non supporté pour la requête."

        selected_endpoint_config = None
        for config in API_CONFIG.get(self.name, []):
            if target_endpoint_name in config["endpoint_name"]:
                selected_endpoint_config = config
                break

        if not selected_endpoint_config:
            return f"AbstractAPI: Aucun endpoint sain ou disponible pour {self.name} pour le type {api_type}."

        response = await self._make_request(
            params=params,
            url=selected_endpoint_config["url"],
            method=selected_endpoint_config["method"],
            key_field=selected_endpoint_config["key_field"],
            key_location=selected_endpoint_config["key_location"],
            api_key=selected_endpoint_config["key"],
            fixed_params=selected_endpoint_config.get("fixed_params", {}),
            timeout=selected_endpoint_config.get("timeout")
        )

        if response and not response.get("error"):
            if api_type == "PHONE_VALIDATION":
                return (
                    f"AbstractAPI (Validation Tél): Numéro: {response.get('phone', 'N/A')}, "
                    f"Valide: {response.get('valid', 'N/A')}, "
                    f"Pays: {response.get('country', {}).get('name', 'N/A')}"
                )
            elif api_type == "EMAIL_VALIDATION":
                return (
                    f"AbstractAPI (Validation Email): Email: {response.get('email', 'N/A')}, "
                    f"Valide: {response.get('is_valid_format', 'N/A')}, "
                    f"Deliverable: {response.get('is_deliverable', 'N/A')}"
                )
            elif api_type == "EXCHANGE_RATES":
                return f"AbstractAPI (Taux de change): Base: {response.get('base', 'N/A')}, Taux (USD): {response.get('exchange_rates', {}).get('USD', 'N/A')}"
            elif api_type == "HOLIDAYS":
                holidays = [h.get('name', 'N/A') for h in response if h.get('name')]
                return f"AbstractAPI (Jours fériés {params.get('country', 'US')} {params.get('year')}): {', '.join(holidays[:5])}..." if holidays else "Aucun jour férié trouvé."
            return f"AbstractAPI ({api_type}): Réponse brute: {response}"
        return f"AbstractAPI ({api_type}): Erreur: {response.get('message', 'Inconnu')}" if response else "AbstractAPI: Réponse vide ou erreur interne."

class GeminiAPIClient:
    def __init__(self):
        self.api_key = GEMINI_API_KEY
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models/"
        self.model_name = "gemini-1.5-flash-latest"
        self.headers = {
            "Content-Type": "application/json",
        }
        from config import GEMINI_TEMPERATURE, GEMINI_TOP_P, GEMINI_TOP_K, GEMINI_MAX_OUTPUT_TOKENS, GEMINI_SAFETY_SETTINGS
        self.generation_config = {
            "temperature": GEMINI_TEMPERATURE,
            "top_p": GEMINI_TOP_P,
            "top_k": GEMINI_TOP_K,
            "max_output_tokens": GEMINI_MAX_OUTPUT_TOKENS,
        }
        self.safety_settings = GEMINI_SAFETY_SETTINGS
        log_message(f"GeminiApiClient initialisé avec le modèle par défaut: {self.model_name}")

    async def generate_content(self, prompt: str, chat_history: List[Dict], image_data: Optional[str] = None, model: Optional[str] = None) -> Dict:
        """
        Génère du contenu textuel ou multimodal en utilisant l'API Gemini.
        `chat_history` est une liste de dictionnaires au format Gemini (role, parts).
        `image_data` est une chaîne base64 de l'image avec son préfixe mimeType (ex: "data:image/png;base64,...").
        `model` permet de spécifier un modèle différent si nécessaire.
        """
        model_to_use = model if model else self.model_name
        url = f"{self.base_url}{model_to_use}:generateContent?key={self.api_key}"

        contents = []
        for msg in chat_history:
            role = "user" if msg["role"] == "user" else "model"
            contents.append({"role": role, "parts": [{"text": msg["content"]}]})

        user_parts = [{"text": prompt}]
        if image_data:
            if "," in image_data:
                mime_type_part, base64_data = image_data.split(",", 1)
                mime_type = mime_type_part.split(":", 1)[1].split(";", 1)[0]
            else:
                mime_type = "image/jpeg"
                base64_data = image_data

            user_parts.append({
                "inlineData": {
                    "mimeType": mime_type,
                    "data": base64_data
                }
            })
            log_message(f"Image ajoutée au prompt Gemini (mimeType: {mime_type}).")

        contents.append({"role": "user", "parts": user_parts})

        payload = {
            "contents": contents,
            "generationConfig": self.generation_config,
            "safetySettings": self.safety_settings
        }

        log_message(f"Appel à Gemini API pour le modèle {model_to_use}...")
        try:
            async with httpx.AsyncClient(timeout=30) as client:
                response = await client.post(url, headers=self.headers, json=payload)
                response.raise_for_status()
                result = response.json()
                log_message(f"Réponse Gemini reçue: {json.dumps(result, indent=2)}")
                return result
        except httpx.HTTPStatusError as e:
            log_message(f"Erreur HTTP Gemini API: {e.response.status_code} - {e.response.text}", level="error")
            return {"error": f"Erreur HTTP Gemini: {e.response.status_code} - {e.response.text}"}
        except httpx.RequestError as e:
            log_message(f"Erreur de requête Gemini API: {e}", level="error")
            return {"error": f"Erreur de requête Gemini: {e}"}
        except json.JSONDecodeError as e:
            log_message(f"Erreur de décodage JSON Gemini API: {e} - Réponse brute: {response.text}", level="error")
            return {"error": f"Erreur de décodage JSON Gemini: {e}"}
        except Exception as e:
            log_message(f"Erreur inattendue Gemini API: {e}\n{traceback.format_exc()}", level="error")
            return {"error": f"Erreur inattendue Gemini: {e}"}

class GoogleCustomSearchClient(APIClient):
    def __init__(self):
        super().__init__("GOOGLE_CUSTOM_SEARCH", endpoint_health_manager)

    async def query(self, query_text: str) -> str:
        """Effectue une recherche personnalisée Google via l'API Custom Search."""
        params = {"q": query_text}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            items = response.get("items", [])
            if items:
                output = "Google Custom Search:\n"
                for item in items[:3]:
                    output += f"- {item.get('title', 'N/A')}: {item.get('snippet', 'N/A')} {neutralize_urls(item.get('link', ''))}\n"
                return output
            return "Google Custom Search: Aucun résultat trouvé."
        return f"Google Custom Search: Erreur: {response.get('message', 'Inconnu')}" if response else "Google Custom Search: Réponse vide ou erreur interne."

class RandommerClient(APIClient):
    def __init__(self):
        super().__init__("RANDOMMER", endpoint_health_manager)

    async def query(self, country_code: str = "US", quantity: int = 1) -> str:
        """Génère des numéros de téléphone aléatoires via Randommer.io."""
        params = {"CountryCode": country_code, "Quantity": quantity}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            if isinstance(response, list) and response:
                return f"Randommer (Numéros de téléphone): {', '.join(response)}"
            return f"Randommer: {response}"
        return f"Randommer: Erreur: {response.get('message', 'Inconnu')}" if response else "Randommer: Réponse vide ou erreur interne."

class TomorrowIOClient(APIClient):
    def __init__(self):
        super().__init__("TOMORROW.IO", endpoint_health_manager)

    async def query(self, location: str, fields: Optional[List[str]] = None) -> str:
        """Récupère les prévisions météorologiques via Tomorrow.io."""
        if fields is None:
            fields = ["temperature", "humidity", "windSpeed"]
        payload = {"location": location, "fields": fields, "units": "metric", "timesteps": ["1h"]}
        response = await self._make_request(json_data=payload)
        if response and not response.get("error"):
            data = response.get("data", {}).get("timelines", [{}])[0].get("intervals", [{}])[0].get("values", {})
            if data:
                output = f"Météo (Tomorrow.io) à {location}:\n"
                for field in fields:
                    output += f"- {field.capitalize()}: {data.get(field, 'N/A')}\n"
                return output
            return "Tomorrow.io: Données météo non trouvées."
        return f"Tomorrow.io: Erreur: {response.get('message', 'Inconnu')}" if response else "Tomorrow.io: Réponse vide ou erreur interne."

class OpenWeatherMapClient(APIClient):
    def __init__(self):
        super().__init__("OPENWEATHERMAP", endpoint_health_manager)

    async def query(self, location: str) -> str:
        """Récupère les conditions météorologiques actuelles via OpenWeatherMap."""
        params = {"q": location}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            main_data = response.get("main", {})
            weather_desc = response.get("weather", [{}])[0].get("description", "N/A")
            if main_data:
                temp_kelvin = main_data.get('temp', 'N/A')
                feels_like_kelvin = main_data.get('feels_like', 'N/A')

                temp_celsius = f"{temp_kelvin - 273.15:.2f}" if isinstance(temp_kelvin, (int, float)) else "N/A"
                feels_like_celsius = f"{feels_like_kelvin - 273.15:.2f}" if isinstance(feels_like_kelvin, (int, float)) else "N/A"

                return (
                    f"Météo (OpenWeatherMap) à {location}:\n"
                    f"Température: {temp_celsius}°C, "
                    f"Ressenti: {feels_like_celsius}°C, "
                    f"Humidité: {main_data.get('humidity', 'N/A')}%, "
                    f"Conditions: {weather_desc}"
                )
            return "OpenWeatherMap: Données météo non trouvées."
        return f"OpenWeatherMap: Erreur: {response.get('message', 'Inconnu')}" if response else "OpenWeatherMap: Réponse vide ou erreur interne."

class MockarooClient(APIClient):
    def __init__(self):
        super().__init__("MOCKAROO", endpoint_health_manager)

    async def query(self, count: int = 1, fields_json: Optional[str] = None) -> str:
        """Génère des données de test via Mockaroo."""
        params = {"count": count}
        if fields_json:
            params["fields"] = fields_json
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            return f"Mockaroo (Génération de données):\n{json.dumps(response, indent=2)}"
        return f"Mockaroo: Erreur: {response.get('message', 'Inconnu')}" if response else "Mockaroo: Réponse vide ou erreur interne."

class OpenPageRankClient(APIClient):
    def __init__(self):
        super().__init__("OPENPAGERANK", endpoint_health_manager)

    async def query(self, domains: List[str]) -> str:
        """Récupère le PageRank de domaines via OpenPageRank."""
        params = {"domains[]": domains}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            results = response.get("response", [])
            if results:
                output = "OpenPageRank (Classement de domaine):\n"
                for res in results:
                    output += f"- Domaine: {res.get('domain', 'N/A')}, PageRank: {res.get('page_rank', 'N/A')}\n"
                return output
            return "OpenPageRank: Aucun résultat trouvé."
        return f"OpenPageRank: Erreur: {response.get('message', 'Inconnu')}" if response else "OpenPageRank: Réponse vide ou erreur interne."

class RapidAPIClient(APIClient):
    def __init__(self):
        super().__init__("RAPIDAPI", endpoint_health_manager)

    async def query(self, api_name: str, **kwargs) -> str:
        """
        Interroge diverses APIs disponibles via RapidAPI (blagues, taux de change, faits aléatoires).
        `api_name` spécifie l'API RapidAPI à utiliser.
        """
        selected_endpoint_config = None
        for config in API_CONFIG.get(self.name, []):
            if api_name.lower() in config["endpoint_name"].lower():
                selected_endpoint_config = config
                break

        if not selected_endpoint_config:
            return f"RapidAPI: Endpoint pour '{api_name}' non trouvé ou non configuré."

        url = selected_endpoint_config["url"]
        method = selected_endpoint_config["method"]

        request_params = selected_endpoint_config.get("fixed_params", {}).copy()
        request_headers = selected_endpoint_config.get("fixed_headers", {}).copy()
        request_json_data = selected_endpoint_config.get("fixed_json", {}).copy()

        if method == "GET":
            request_params.update(kwargs)
        elif method == "POST":
            request_json_data.update(kwargs)

        headers = {
            selected_endpoint_config["key_field"]: selected_endpoint_config["key"],
            "X-RapidAPI-Host": selected_endpoint_config["fixed_headers"].get("X-RapidAPI-Host")
        }

        response = await self._make_request(
            params=request_params,
            headers=headers,
            json_data=request_json_data,
            url=url,
            method=method,
            timeout=selected_endpoint_config.get("timeout")
        )

        if response and not response.get("error"):
            if api_name.lower() == "programming joke":
                return f"RapidAPI (Blague de Programmation): {response.get('setup', '')} - {response.get('punchline', '')}"
            elif api_name.lower() == "currency list quotes":
                return f"RapidAPI (Devises): {json.dumps(response, indent=2)}"
            elif api_name.lower() == "random fact":
                return f"RapidAPI (Fait Aléatoire): {response.get('text', 'N/A')}"
            return f"RapidAPI ({api_name}): {json.dumps(response, indent=2)}"
        return f"RapidAPI ({api_name}): Erreur: {response.get('message', 'Inconnu')}" if response else "RapidAPI: Réponse vide ou erreur interne."

class OCRApiClient:
    def __init__(self):
        from config import OCR_API_KEY
        self.api_key = OCR_API_KEY
        self.base_url = "https://api.ocr.space/parse/image"
        log_message("OCRApiClient initialisé.")

    async def query(self, image_base64: str) -> str:
        """
        Effectue une requête OCR à l'API OCR.space.
        `image_base64` doit être la chaîne base64 de l'image, incluant le préfixe mimeType
        (ex: "data:image/png;base64,...").
        """
        payload = {
            "base64Image": image_base64,
            "language": "fre",
            "isOverlayRequired": False,
            "OCREngine": 2
        }
        headers = {
            "apikey": self.api_key,
            "Content-Type": "application/json"
        }

        log_message("Appel à OCR.space API...")
        try:
            async with httpx.AsyncClient(timeout=30) as client:
                response = await client.post(self.base_url, headers=headers, json=payload)
                response.raise_for_status()
                result = response.json()

                if result.get("IsErroredOnProcessing"):
                    error_message = result.get("ErrorMessage", ["Erreur inconnue lors du traitement OCR."])
                    log_message(f"Erreur OCR.space: {error_message}", level="error")
                    return f"❌ Erreur OCR: {', '.join(error_message)}"

                parsed_text = ""
                if "ParsedResults" in result and result["ParsedResults"]:
                    for parsed_result in result["ParsedResults"]:
                        parsed_text += parsed_result.get("ParsedText", "") + "\n"

                if parsed_text.strip():
                    log_message("OCR.space: Texte extrait avec succès.")
                    return parsed_text.strip()
                else:
                    log_message("OCR.space: Aucun texte extrait.", level="warning")
                    return "Aucun texte n'a pu être extrait de l'image."

        except httpx.HTTPStatusError as e:
            log_message(f"Erreur HTTP OCR.space API: {e.response.status_code} - {e.response.text}", level="error")
            return f"❌ Erreur HTTP OCR: {e.response.status_code} - {e.response.text}"
        except httpx.RequestError as e:
            log_message(f"Erreur de requête OCR.space API: {e}", level="error")
            return f"❌ Erreur de requête OCR: {e}"
        except json.JSONDecodeError as e:
            log_message(f"Erreur de décodage JSON OCR.space API: {e} - Réponse brute: {response.text}", level="error")
            return {"error": f"Erreur de décodage JSON OCR: {e}"}
        except Exception as e:
            log_message(f"Erreur inattendue OCR.space API: {e}\n{traceback.format_exc()}", level="error")
            return f"❌ Erreur inattendue OCR: {e}"


# Instancier tous les clients API en leur passant le gestionnaire de santé
# Note: GeminiApiClient et OCRApiClient sont instanciés séparément car ils gèrent leurs clés directement.
ALL_API_CLIENTS = [
    DeepSeekClient(), SerperClient(), WolframAlphaClient(), TavilyClient(),
    ApiFlashClient(), CrawlbaseClient(), DetectLanguageClient(), GuardianClient(),
    IP2LocationClient(), ShodanClient(), WeatherAPIClient(),
    CloudmersiveClient(), GreyNoiseClient(), PulsediveClient(), StormGlassClient(),
    LoginRadiusClient(), JsonbinClient(),
    HuggingFaceClient(), TwilioClient(), AbstractAPIClient(),
    GoogleCustomSearchClient(), RandommerClient(), TomorrowIOClient(),
    OpenWeatherMapClient(),
    MockarooClient(), OpenPageRankClient(), RapidAPIClient()
]

# memory_and_quotas.py
import json
import asyncio
import random
import traceback
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, Any, Optional, List, Union

# Imports des constantes depuis config.py
from config import (
    API_QUOTAS, API_COOLDOWN_DURATION_SECONDS,
    USER_CHAT_HISTORY_FILE, USER_LONG_MEMORY_FILE,
    IA_STATUS_FILE, QUOTAS_FILE, GROUP_CHAT_HISTORY_FILE, PRIVATE_GROUP_ID,
    BURN_QUOTA_THRESHOLD_RATIO, BURN_QUOTA_BEFORE_RESET_HOURS,
    API_ROTATION_INTERVAL_MINUTES # Ajouté pour la récupération de diversification
)

# Imports depuis utils.py
from utils import (
    load_json, save_json, get_current_time, format_datetime, log_message,
    neutralize_urls, extract_keywords, tag_conversation, unique_preserve_order,
    similar, get_user_dir
)

class MemoryManager:
    """
    Gère la mémoire à court et long terme du bot, ainsi que l'historique des conversations
    pour les utilisateurs individuels et les groupes.
    C'est un singleton pour s'assurer qu'il n'y a qu'une seule instance de gestionnaire de mémoire.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """Implémente le patron de conception Singleton."""
        if cls._instance is None:
            cls._instance = super(cls, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        """Initialise les structures de données pour la mémoire."""
        if self._initialized:
            return
        self.chat_history: Dict[Union[int, str], List[Dict]] = {} # {user_id: [messages]}
        self.long_term_memory: Dict[Union[int, str], List[str]] = {} # {user_id: [facts]}
        self.ia_status: Dict[str, Dict[str, Any]] = {} # Statut global des IA
        self.group_chat_history: Dict[int, List[Dict]] = {} # {group_id: [messages]}
        # `_initialized` est géré par `init_manager` pour les opérations asynchrones

    async def init_manager(self):
        """
        Initialise le gestionnaire de mémoire de manière asynchrone.
        Charge les statuts persistants et les historiques de groupe.
        """
        if not self._initialized:
            # Charge le statut global des IA
            self.ia_status = await load_json(IA_STATUS_FILE, {})
            self._initialize_ia_status()

            # Charge l'historique du groupe privé spécifique
            group_dir = get_user_dir(PRIVATE_GROUP_ID)
            self.group_chat_history[PRIVATE_GROUP_ID] = await load_json(group_dir / GROUP_CHAT_HISTORY_FILE, [])

            self._initialized = True
            log_message("Gestionnaire de mémoire initialisé.")

    def _initialize_ia_status(self):
        """
        Initialise ou met à jour le statut des IA si elles ne sont pas déjà présentes
        ou si leur statut est obsolète. S'assure que toutes les clés nécessaires sont là.
        """
        updated = False
        now = get_current_time()

        default_ia_status_keys = {
            "last_used": None, "last_error": None, "error_count": 0,
            "cooldown_until": None, "success_count": 0, "current_score": 1.0,
            "last_rotation_check": format_datetime(now), "diversification_score": 1.0
        }

        for client_name in API_QUOTAS.keys(): # Itère sur toutes les APIs définies dans les quotas
            if client_name not in self.ia_status:
                self.ia_status[client_name] = default_ia_status_keys.copy()
                updated = True
            else:
                for key, default_value in default_ia_status_keys.items():
                    if key not in self.ia_status[client_name]:
                        self.ia_status[client_name][key] = default_value
                        updated = True

                # Met à jour `last_rotation_check` si trop ancien pour permettre la récupération du score de diversification
                last_check_str = self.ia_status[client_name].get("last_rotation_check")
                if last_check_str:
                    try:
                        last_check_dt = datetime.strptime(last_check_str, "%Y-%m-%d %H:%M:%S UTC")
                        if (now - last_check_dt).total_seconds() > API_ROTATION_INTERVAL_MINUTES * 60 * 2:
                            self.ia_status[client_name]["last_rotation_check"] = format_datetime(now)
                            updated = True
                    except ValueError:
                        self.ia_status[client_name]["last_rotation_check"] = format_datetime(now)
                        updated = True
                        log_message(f"last_rotation_check malformé pour {client_name}, réinitialisation.", level="warning")

        # Supprime les noms d'IA qui ne sont plus définis dans `API_QUOTAS`
        current_api_names = set(API_QUOTAS.keys())
        ia_names_to_remove = [name for name in self.ia_status if name not in current_api_names]
        for name in ia_names_to_remove:
            del self.ia_status[name]
            updated = True
            log_message(f"IA '{name}' trouvée dans ia_status.json mais non définie dans API_QUOTAS. Supprimée.", level="warning")

        if updated:
            asyncio.create_task(save_json(IA_STATUS_FILE, self.ia_status))
            log_message("Statut des IA initialisé/mis à jour.")

    async def _update_and_save_history(self, user_id: Union[int, str], file_path: Path, history_dict: Dict, max_entries: int, entry: Dict):
        """Helper to update history and save."""
        hist = history_dict.get(user_id, await load_json(file_path, []))
        hist.append(entry)
        hist = hist[-max_entries:]
        history_dict[user_id] = hist
        asyncio.create_task(save_json(file_path, hist))

    async def add_message_to_history(self, user_id: Union[int, str], role: str, content: str, max_log_entries: int = 100):
        """
        Ajoute un message à l'historique de la conversation d'un utilisateur.
        Gère également le log général de l'utilisateur et le taggage des messages.
        """
        user_dir = get_user_dir(user_id)
        chat_history_path = user_dir / USER_CHAT_HISTORY_FILE
        log_path = user_dir / "log.json"

        neutralized_content = neutralize_urls(content)
        timestamp = format_datetime(get_current_time())

        # Add to user chat history
        await self._update_and_save_history(
            user_id, chat_history_path, self.chat_history, max_log_entries,
            {"role": role, "content": neutralized_content, "timestamp": timestamp}
        )

        # Add to general user log
        log_entry_content = neutralized_content[:500]
        log_entry = {"time": timestamp, "role": role, "text": log_entry_content}
        if role == "user":
            log_entry["tags"] = tag_conversation(content)
        
        user_log = await load_json(log_path, [])
        await self._update_and_save_history(
            user_id, log_path, {user_id: user_log}, max_log_entries, log_entry
        ) # Pass user_log as a dict for consistency with _update_and_save_history

        log_message(f"Message ajouté à l'historique de {user_id} par {role}.")

    async def get_chat_history(self, user_id: Union[int, str], limit: int = 10) -> List[Dict]:
        """
        Retourne les N derniers messages de l'historique de conversation d'un utilisateur.
        Charge l'historique depuis le fichier si non déjà en mémoire.
        """
        user_dir = get_user_dir(user_id)
        chat_history_path = user_dir / USER_CHAT_HISTORY_FILE
        if user_id not in self.chat_history:
            self.chat_history[user_id] = await load_json(chat_history_path, [])
        return self.chat_history[user_id][-limit:]

    async def save_group_memory(self, group_id: int, role: str, text: str, max_items: int = 1000):
        """
        Sauvegarde l'historique de chat pour un groupe spécifique.
        Utilise l'ID du groupe comme un ID utilisateur pour la structure de répertoire.
        """
        group_dir = get_user_dir(group_id)
        group_history_path = group_dir / GROUP_CHAT_HISTORY_FILE

        hist = self.group_chat_history.get(group_id, await load_json(group_history_path, []))
        hist.append({"time": format_datetime(get_current_time()), "role": role, "text": neutralize_urls(text)})
        hist = hist[-max_items:]
        self.group_chat_history[group_id] = hist
        asyncio.create_task(save_json(group_history_path, hist))
        log_message(f"Message ajouté à la mémoire de groupe {group_id} par {role}.")

    async def get_group_memory(self, group_id: int, limit: int = 20) -> str:
        """
        Récupère les N derniers messages de la mémoire de groupe.
        Retourne une chaîne formatée pour être utilisée comme contexte.
        """
        group_dir = get_user_dir(group_id)
        group_history_path = group_dir / GROUP_CHAT_HISTORY_FILE
        if group_id not in self.group_chat_history:
            self.group_chat_history[group_id] = await load_json(group_history_path, [])

        if not isinstance(self.group_chat_history[group_id], list):
            self.group_chat_history[group_id] = []

        recent_messages = [f"{l['role']} : {l['text']}" for l in self.group_chat_history[group_id][-limit:] if l.get("role") != "bot"]
        return "\n".join(recent_messages)

    async def add_to_long_term_memory(self, user_id: Union[int, str], text: str, max_entries: int = 100):
        """
        Ajoute une information à la mémoire à long terme d'un utilisateur.
        Dédoublonne et tronque la mémoire.
        """
        user_dir = get_user_dir(user_id)
        long_memory_path = user_dir / USER_LONG_MEMORY_FILE

        long_mem = self.long_term_memory.get(user_id, await load_json(long_memory_path, []))
        if not isinstance(long_mem, list):
            long_mem = []

        long_mem.append(text.strip())
        long_mem = unique_preserve_order(long_mem)[-max_entries:]
        self.long_term_memory[user_id] = long_mem
        asyncio.create_task(save_json(long_memory_path, long_mem))
        log_message(f"Information ajoutée à la mémoire à long terme de {user_id}.")

    async def get_long_term_memory(self, user_id: Union[int, str], limit: int = 20) -> str:
        """
        Récupère les N dernières entrées de la mémoire à long terme d'un utilisateur.
        Retourne une chaîne formatée.
        """
        user_dir = get_user_dir(user_id)
        long_memory_path = user_dir / USER_LONG_MEMORY_FILE
        if user_id not in self.long_term_memory:
            self.long_term_memory[user_id] = await load_json(long_memory_path, [])

        if not isinstance(self.long_term_memory[user_id], list):
            self.long_term_memory[user_id] = []

        return "\n".join(self.long_term_memory[user_id][-limit:])

    async def check_for_similar_prompt(self, user_id: Union[int, str], prompt: str) -> Optional[str]:
        """
        Vérifie si un prompt similaire a déjà été posé récemment et retourne la réponse si trouvée.
        Utilise `MAX_CACHE_SIZE` pour la fenêtre de recherche.
        """
        recent_chat_history = await self.get_chat_history(user_id, limit=MAX_CACHE_SIZE)
        for i in range(len(recent_chat_history) - 1, 0, -1): # Iterate backwards from second to last
            entry = recent_chat_history[i]
            if entry.get("role") == "user" and "content" in entry:
                if similar(prompt, entry["content"]) > 0.92:
                    # Check the next entry for a bot response
                    if i + 1 < len(recent_chat_history) and recent_chat_history[i+1].get("role") == "bot":
                        log_message(f"Prompt similaire détecté pour {user_id}. Réponse en cache utilisée.")
                        return recent_chat_history[i+1]["content"]
        return None

    def update_ia_status(self, ia_name: str, success: bool, error_message: Optional[str] = None):
        """
        Met à jour le statut et le score d'une IA après une utilisation.
        Ajuste le score de performance et le score de diversification.
        """
        status = self.ia_status.get(ia_name)
        if not status:
            log_message(f"Tentative de mise à jour d'un statut d'IA inconnu: {ia_name}", level="warning")
            return

        now = get_current_time()
        status["last_used"] = format_datetime(now)

        if success:
            status["success_count"] += 1
            status["error_count"] = 0
            status["cooldown_until"] = None
            status["last_error"] = None
            status["current_score"] = min(1.0, status["current_score"] + 0.1)
            status["diversification_score"] = max(0.1, status["diversification_score"] - 0.1)
            log_message(f"IA {ia_name} : Succès enregistré. Nouveau score: {status['current_score']:.2f}, Diversification: {status['diversification_score']:.2f}")
        else:
            status["error_count"] += 1
            status["last_error"] = error_message
            if status["error_count"] >= 3:
                status["cooldown_until"] = format_datetime(now + timedelta(seconds=API_COOLDOWN_DURATION_SECONDS))
                status["current_score"] = max(0.1, status["current_score"] - 0.2)
                log_message(f"IA {ia_name} : Trop d'erreurs ({status['error_count']}). Cooldown jusqu'à {status['cooldown_until']}. Nouveau score: {status['current_score']:.2f}", level="warning")
            else:
                 status["current_score"] = max(0.1, status["current_score"] - 0.05)
                 log_message(f"IA {ia_name} : Erreur enregistrée. Nouveau score: {status['current_score']:.2f}", level="warning")

        asyncio.create_task(save_json(IA_STATUS_FILE, self.ia_status))

    def recover_diversification_scores(self):
        """
        Augmente le score de diversification pour les IA qui n'ont pas été utilisées récemment.
        Ceci encourage la rotation des APIs.
        """
        now = get_current_time()
        updated = False
        for ia_name, status in self.ia_status.items():
            last_used_str = status.get("last_used")
            if last_used_str:
                try:
                    last_used_dt = datetime.strptime(last_used_str, "%Y-%m-%d %H:%M:%S UTC")
                    if (now - last_used_dt).total_seconds() > API_ROTATION_INTERVAL_MINUTES * 60 * 2:
                        if status["diversification_score"] < 1.0:
                            status["diversification_score"] = min(1.0, status["diversification_score"] + 0.05)
                            updated = True
                            log_message(f"IA {ia_name}: Score de diversification récupéré à {status['diversification_score']:.2f}")
                except ValueError:
                    status["last_used"] = format_datetime(now)
                    status["diversification_score"] = 1.0
                    updated = True
                    log_message(f"last_used malformé pour {ia_name}, réinitialisation du score de diversification.", level="warning")
            else:
                if status["diversification_score"] < 1.0:
                    status["diversification_score"] = 1.0
                    updated = True
        if updated:
            asyncio.create_task(save_json(IA_STATUS_FILE, self.ia_status))

    def get_ia_status(self, ia_name: str) -> Optional[Dict]:
        """Récupère le statut d'une IA spécifique."""
        return self.ia_status.get(ia_name)

    def get_available_ias(self) -> List[str]:
        """
        Retourne les noms des IA actuellement non en cooldown.
        """
        available = []
        now = get_current_time()
        for name, status in self.ia_status.items():
            cooldown_until_str = status.get("cooldown_until")
            if cooldown_until_str:
                try:
                    cooldown_until = datetime.strptime(cooldown_until_str, "%Y-%m-%d %H:%M:%S UTC")
                    if now < cooldown_until:
                        continue
                except ValueError:
                    log_message(f"cooldown_until malformé pour {name}, considéré comme non en cooldown.", level="warning")
            available.append(name)
        return available

class QuotaManager:
    """
    Gère les quotas d'utilisation pour toutes les APIs.
    Suit l'utilisation mensuelle, journalière et horaire, et peut alerter en cas de dépassement.
    Prend également en charge le mode "brûlage" de quota.
    C'est un singleton.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """Implémente le patron de conception Singleton."""
        if cls._instance is None:
            cls._instance = super(cls, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        """Initialise les structures de données pour les quotas."""
        if self._initialized:
            return
        self.quotas = {}
        # `_initialized` est géré par `init_manager` pour les opérations asynchrones
        self.bot_instance = None # Sera injecté par main.py pour l'envoi d'alertes

    async def init_manager(self):
        """
        Initialise le gestionnaire de quotas de manière asynchrone.
        Charge les données de quotas persistantes et s'assure qu'elles sont à jour.
        """
        if not self._initialized:
            self.quotas = await load_json(QUOTAS_FILE, {})
            self._initialize_quotas()
            self._initialized = True
            log_message("Gestionnaire de quotas initialisé.")

    def set_bot_instance(self, bot_instance: Any):
        """
        Permet d'injecter l'instance du bot pour envoyer des alertes de quota au groupe privé.
        """
        self.bot_instance = bot_instance

    def _initialize_quotas(self):
        """
        Initialise les quotas pour toutes les APIs basées sur `config.API_QUOTAS`.
        Nettoie et met à jour les entrées existantes si nécessaire.
        """
        updated = False
        now = get_current_time()

        default_quota_structure = {
            "monthly_usage": 0, "daily_usage": 0, "hourly_usage": 0,
            "hourly_timestamps": [], "last_reset_month": now.month,
            "last_reset_day": now.day, "last_usage": None,
            "total_calls": 0, "last_hourly_reset": format_datetime(now)
        }

        for api_name, quota_info in API_QUOTAS.items():
            if api_name not in self.quotas:
                self.quotas[api_name] = default_quota_structure.copy()
                updated = True
            else:
                for key, default_value in default_quota_structure.items():
                    if key not in self.quotas[api_name]:
                        self.quotas[api_name][key] = default_value
                        updated = True

                if not isinstance(self.quotas[api_name].get("hourly_timestamps"), list):
                    self.quotas[api_name]["hourly_timestamps"] = []

                one_hour_ago = now - timedelta(hours=1)
                self.quotas[api_name]["hourly_timestamps"] = [
                    ts for ts in self.quotas[api_name]["hourly_timestamps"]
                    if datetime.strptime(ts, "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=timezone.utc) > one_hour_ago
                ]
                self.quotas[api_name]["hourly_usage"] = len(self.quotas[api_name]["hourly_timestamps"])
                self.quotas[api_name]["last_hourly_reset"] = format_datetime(now)
                updated = True

        api_names_to_remove = [name for name in self.quotas if name not in API_QUOTAS]
        for name in api_names_to_remove:
            del self.quotas[name]
            updated = True
            log_message(f"API '{name}' trouvée dans quotas.json mais non définie dans API_QUOTAS. Supprimée.", level="warning")

        if updated:
            asyncio.create_task(save_json(QUOTAS_FILE, self.quotas))
            log_message("Quotas API initialisés/mis à jour.")

    def _reset_quotas_if_needed(self):
        """
        Réinitialise les quotas journaliers, mensuels et horaires si nécessaire.
        Cette méthode est appelée avant chaque vérification de quota pour s'assurer de l'actualité.
        """
        now = get_current_time()
        for api_name, data in self.quotas.items():
            if now.month != data["last_reset_month"]:
                data["monthly_usage"] = 0
                data["last_reset_month"] = now.month
                log_message(f"Quota mensuel pour {api_name} réinitialisé.")
            if now.day != data["last_reset_day"]:
                data["daily_usage"] = 0
                data["last_reset_day"] = now.day
                log_message(f"Quota journalier pour {api_name} réinitialisé.")

            one_hour_ago = now - timedelta(hours=1)
            if not isinstance(data.get("hourly_timestamps"), list):
                data["hourly_timestamps"] = []

            data["hourly_timestamps"] = [
                ts for ts in data["hourly_timestamps"]
                if datetime.strptime(ts, "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=timezone.utc) > one_hour_ago
            ]
            data["hourly_usage"] = len(data["hourly_timestamps"])
            data["last_hourly_reset"] = format_datetime(now)

        asyncio.create_task(save_json(QUOTAS_FILE, self.quotas))

    async def check_and_update_quota(self, api_name: str, cost: int = 1) -> bool:
        """
        Vérifie si une API a du quota disponible et le décrémente si oui.
        Retourne `True` si l'opération est autorisée (quota disponible), `False` sinon.
        """
        self._reset_quotas_if_needed()

        if api_name not in API_QUOTAS:
            log_message(f"Tentative de vérification de quota pour une API non définie: {api_name}. Autorisation refusée.", level="error")
            return False

        if api_name not in self.quotas:
            log_message(f"API {api_name} non trouvée dans les quotas gérés. Re-initialisation non bloquante.", level="warning")
            self._initialize_quotas()
            if api_name not in self.quotas:
                return False

        quota_data = self.quotas[api_name]
        api_limits = API_QUOTAS.get(api_name, {})
        now = get_current_time()

        limits = {
            "monthly": api_limits.get("monthly"),
            "daily": api_limits.get("daily"),
            "hourly": api_limits.get("hourly")
        }
        usages = {
            "monthly": quota_data["monthly_usage"],
            "daily": quota_data["daily_usage"],
            "hourly": quota_data["hourly_usage"]
        }

        for limit_type, limit_value in limits.items():
            if limit_value is not None and (usages[limit_type] + cost) > limit_value:
                log_message(f"Quota {limit_type} dépassé pour {api_name}", level="warning")
                await self._alert_quota_if_needed(api_name, limit_type)
                return False

        rate_limit_per_sec = api_limits.get("rate_limit_per_sec")
        if rate_limit_per_sec:
            last_usage_str = quota_data.get("last_usage")
            if last_usage_str:
                try:
                    last_usage = datetime.strptime(last_usage_str, "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=timezone.utc)
                    time_since_last_call = (now - last_usage).total_seconds()
                    if time_since_last_call < (1 / rate_limit_per_sec):
                        log_message(f"Taux de requêtes dépassé pour {api_name}. Attendre {1/rate_limit_per_sec - time_since_last_call:.2f}s", level="warning")
                        return False
                except ValueError:
                    log_message(f"last_usage malformé pour {api_name}, considéré comme sans utilisation récente pour la limite de taux.", level="warning")

        if cost > 0:
            quota_data["monthly_usage"] += cost
            quota_data["daily_usage"] += cost
            quota_data["hourly_usage"] += cost
            quota_data["hourly_timestamps"].append(format_datetime(now))
            quota_data["total_calls"] += cost
            quota_data["last_usage"] = format_datetime(now)
            asyncio.create_task(save_json(QUOTAS_FILE, self.quotas))
            log_message(f"Quota pour {api_name} mis à jour. Usage mensuel: {quota_data['monthly_usage']}/{limits['monthly'] if limits['monthly'] else 'Illimité'}, Journalier: {quota_data['daily_usage']}/{limits['daily'] if limits['daily'] else 'Illimité'}, Horaire: {quota_data['hourly_usage']}/{limits['hourly'] if limits['hourly'] else 'Illimité'}")
        else:
            log_message(f"Quota pour {api_name} vérifié (coût 0). Usage mensuel: {quota_data['monthly_usage']}/{limits['monthly'] if limits['monthly'] else 'Illimité'}, Journalier: {quota_data['daily_usage']}/{limits['daily'] if limits['daily'] else 'Illimité'}, Horaire: {quota_data['hourly_usage']}/{limits['hourly'] if limits['hourly'] else 'Illimité'}")

        return True

    async def _alert_quota_if_needed(self, api_name: str, limit_type: str):
        """
        Envoie une alerte au groupe privé si un quota est atteint.
        Utilise la mémoire à long terme pour éviter de spammer les alertes.
        """
        if self.bot_instance and PRIVATE_GROUP_ID:
            message = f"🚨 Quota {limit_type} pour l'API '{api_name}' atteint !"
            log_message(message, level="warning")
            try:
                alert_key = f"quota_alert_{api_name}_{limit_type}_{get_current_time().strftime('%Y-%m-%d')}"
                bot_global_memory_id = "bot_global_alerts"
                
                global_alerts = await memory_manager.get_long_term_memory(bot_global_memory_id, limit=1000)
                if alert_key not in global_alerts:
                    await self.bot_instance.send_message(chat_id=PRIVATE_GROUP_ID, text=message)
                    await memory_manager.add_to_long_term_memory(bot_global_memory_id, alert_key)
            except Exception as e:
                log_message(f"Erreur lors de l'envoi de l'alerte de quota: {e}", level="error")

    def get_api_usage(self, api_name: str) -> Optional[Dict]:
        """Retourne les informations d'utilisation d'une API spécifique."""
        return self.quotas.get(api_name)

    def get_all_quotas_status(self) -> Dict:
        """
        Retourne le statut de tous les quotas API.
        S'assure que les quotas sont à jour avant de les retourner.
        """
        self._reset_quotas_if_needed()
        status = {}
        for api_name, quota_data in self.quotas.items():
            api_limits = API_QUOTAS.get(api_name, {})
            monthly_limit = api_limits.get("monthly", "Illimité")
            daily_limit = api_limits.get("daily", "Illimité")
            hourly_limit = api_limits.get("hourly", "Illimité")
            status[api_name] = {
                "monthly_usage": quota_data["monthly_usage"],
                "monthly_limit": monthly_limit,
                "daily_usage": quota_data["daily_usage"],
                "daily_limit": daily_limit,
                "hourly_usage": quota_data["hourly_usage"],
                "hourly_limit": hourly_limit,
                "total_calls": quota_data["total_calls"],
                "last_usage": quota_data["last_usage"],
                "last_reset_month": quota_data["last_reset_month"],
                "last_reset_day": quota_data["last_reset_day"],
                "last_hourly_reset": quota_data["last_hourly_reset"]
            }
        return status

    def get_burn_window_apis(self) -> List[str]:
        """
        Identifie les APIs dont les quotas sont sur le point d'être réinitialisés
        et où il est opportun de "brûler" le quota restant.
        """
        burn_apis = []
        now = get_current_time()

        for api_name, data in self.quotas.items():
            api_limits = API_QUOTAS.get(api_name, {})

            for limit_type in ["monthly", "daily"]:
                limit = api_limits.get(limit_type)
                if limit is not None and limit > 0:
                    current_usage = data[f"{limit_type}_usage"]
                    
                    if limit_type == "monthly":
                        next_month = now.month + 1
                        year_for_next_month = now.year
                        if next_month > 12:
                            next_month = 1
                            year_for_next_month += 1
                        reset_time = datetime(year_for_next_month, next_month, 1, 0, 0, 0, 0, tzinfo=timezone.utc)
                    else: # daily
                        reset_time = datetime(now.year, now.month, now.day, 0, 0, 0, 0, tzinfo=timezone.utc) + timedelta(days=1)
                    
                    if now < reset_time:
                        time_until_reset = reset_time - now
                        if time_until_reset <= timedelta(hours=BURN_QUOTA_BEFORE_RESET_HOURS):
                            if current_usage < limit:
                                remaining_quota_ratio = (limit - current_usage) / limit
                                if remaining_quota_ratio > 0 and remaining_quota_ratio <= BURN_QUOTA_THRESHOLD_RATIO:
                                    burn_apis.append(f"{api_name} ({limit_type}: {limit - current_usage} restants)")
        return burn_apis


    def should_burn_quota(self, api_name: str) -> bool:
        """
        Détermine si le quota pour une API donnée devrait être 'brûlé' avant réinitialisation.
        Cette méthode est appelée par `_auto_burn_quota_task` pour décider si une API doit être utilisée.
        """
        self._reset_quotas_if_needed()

        quota_data = self.quotas.get(api_name)
        api_limits = API_QUOTAS.get(api_name)

        if not quota_data or not api_limits:
            return False

        now = get_current_time()

        for limit_type in ["monthly", "daily"]:
            limit = api_limits.get(limit_type)
            if limit is not None and limit > 0:
                current_usage = quota_data[f"{limit_type}_usage"]

                if limit_type == "monthly":
                    next_month = now.month + 1
                    year_for_next_month = now.year
                    if next_month > 12:
                        next_month = 1
                        year_for_next_month += 1
                    reset_time = datetime(year_for_next_month, next_month, 1, 0, 0, 0, 0, tzinfo=timezone.utc)
                else: # daily
                    reset_time = datetime(now.year, now.month, now.day, 0, 0, 0, 0, tzinfo=timezone.utc) + timedelta(days=1)

                if now < reset_time:
                    time_until_reset = reset_time - now
                    if time_until_reset <= timedelta(hours=BURN_QUOTA_BEFORE_RESET_HOURS):
                        remaining_quota_ratio = (limit - current_usage) / limit
                        if remaining_quota_ratio > 0 and remaining_quota_ratio <= BURN_QUOTA_THRESHOLD_RATIO:
                            log_message(f"Mode Burn: {api_name} ({limit_type}) - usage {current_usage}/{limit}, ratio {remaining_quota_ratio:.2f}, reset dans {time_until_reset}", level="debug")
                            return True
        return False

# Instanciation des gestionnaires de mémoire et de quotas (seront initialisés dans main.py)
memory_manager = MemoryManager()
quota_manager = QuotaManager()

# filters_and_tools.py
import json
import asyncio
import random
import ast
import subprocess
import base64
import httpx
import io
import contextlib
import traceback
import hashlib
import difflib
import re
import logging
from datetime import datetime, timedelta, timezone
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, Any, Optional, List, Union, Tuple

# Imports des constantes depuis config.py
from config import FORBIDDEN_WORDS, ARCHIVES_DIR, MAX_FILE_SIZE

# Imports depuis utils.py
from utils import (
    log_message, neutralize_urls, get_user_dir
)

# Imports spécifiques pour les outils de développement (assurez-vous que ces bibliothèques sont installées)
try:
    from pygments import highlight
    from pygments.lexers import PythonLexer
    from pygments.formatters import TerminalFormatter
except ImportError:
    highlight = None
    PythonLexer = None
    TerminalFormatter = None
    log_message("Pygments non trouvé. La surbrillance syntaxique ne sera pas disponible.", level="warning")

try:
    from pyflakes.api import check
    from pyflakes.reporter import Reporter
except ImportError:
    check = None
    Reporter = None
    log_message("Pyflakes non trouvé. La vérification de code ne sera pas disponible.", level="warning")

try:
    import black
except ImportError:
    black = None
    log_message("Black non trouvé. Le formatage de code ne sera pas disponible.", level="warning")

# Instancier le client OCR API pour une utilisation directe dans perform_ocr_api
# Note: OCRApiClient est défini dans api_clients.py, donc il doit être importé.
# Pour éviter une dépendance circulaire si ce fichier est importé avant api_clients,
# l'instanciation est faite ici, mais la classe OCRApiClient doit être disponible.
# Dans le script final, toutes les classes sont dans le même fichier ou l'ordre d'importation est géré.
# On va passer l'instance du client OCR via une fonction setter ou directement lors de l'initialisation du bot.
# Pour l'instant, on déclare une variable globale qui sera assignée plus tard.
ocr_api_client_instance = None # Sera assigné par main.py

def set_ocr_api_client_instance(client_instance):
    global ocr_api_client_instance
    ocr_api_client_instance = client_instance

# Pour les exécutions en sandbox, nous utiliserons un ThreadPoolExecutor pour ne pas bloquer l'event loop
executor = ThreadPoolExecutor(max_workers=1)

def filter_bad_code(code: str) -> bool:
    """
    Filtre basique pour les commandes de code potentiellement dangereuses.
    Empêche l'exécution de certaines opérations système ou de réseau.
    """
    forbidden_patterns = [
        r'os\.system', r'subprocess\.run', r'shutil\.rmtree', r'requests\.post',
        r'open\([^,\'"]*\s*,\s*[\'"]w', r'import socket', r'import http',
        r'sys\.exit', r'while True:', r'import threading', r'import multiprocessing'
    ]
    for pattern in forbidden_patterns:
        if re.search(pattern, code):
            log_message(f"Code bloqué: motif dangereux détecté: {pattern}", level="warning")
            return True
    return False

def detect_and_correct_toxicity(text: str) -> str:
    """
    Remplace les propos toxiques (mots définis dans FORBIDDEN_WORDS)
    par des faits scientifiques ou des encouragements.
    """
    if any(word in text.lower() for word in FORBIDDEN_WORDS):
        facts = [
            "Savais-tu que 73% des conflits viennent de malentendus ?",
            "Le cerveau humain est câblé pour la coopération, pas le conflit.",
            "En 2025, l'IA émotionnelle sera la norme. Soyons précurseurs !",
            "Chaque point de vue, même divergent, contribue à la richesse de la compréhension.",
            "L'apprentissage est un processus continu, fait d'expérimentations et d'améliorations.",
            "La collaboration est la clé de l'innovation."
        ]
        log_message(f"Toxicité détectée et corrigée dans le message: '{text}'", level="info")
        return random.choice(facts) + " Continuons à construire ensemble !"
    return text

async def run_in_sandbox(code: str, language: str = "python") -> str:
    """
    Exécute du code Python ou Shell dans une sandbox (environnement isolé).
    Utilise un ThreadPoolExecutor pour exécuter des opérations bloquantes de manière asynchrone,
    évitant ainsi de bloquer l'event loop principal.
    """
    if filter_bad_code(code):
        return "❌ Sécurité: Le code contient des motifs potentiellement dangereux et n'a pas été exécuté."

    loop = asyncio.get_running_loop()
    if language == "python":
        return await loop.run_in_executor(executor, _run_python_sync, code)
    elif language == "shell":
        return await loop.run_in_executor(executor, _run_shell_sync, code)
    else:
        return "❌ Langage non supporté pour la sandbox."

def _run_python_sync(code: str) -> str:
    """
    Exécute du code Python de manière synchrone et capture la sortie standard et d'erreur.
    Utilise un dictionnaire `__builtins__` vide pour isoler l'exécution.
    """
    old_stdout = io.StringIO()
    old_stderr = io.StringIO()
    with contextlib.redirect_stdout(old_stdout), contextlib.redirect_stderr(old_stderr):
        try:
            exec(code, {'__builtins__': {}})
            output = old_stdout.getvalue()
            error = old_stderr.getvalue()
            if error:
                log_message(f"Erreur d'exécution Python en sandbox:\n{error}", level="warning")
                return f"🐍 Erreur Python:\n{error}\nSortie:\n{output}"
            return f"✅ Sortie Python:\n{output}"
        except Exception as e:
            log_message(f"Erreur d'exécution Python inattendue en sandbox: {e}\n{traceback.format_exc()}", level="error")
            return f"❌ Erreur d'exécution Python: {e}\nSortie standard:\n{old_stdout.getvalue()}\nErreur standard:\n{old_stderr.getvalue()}"

def _run_shell_sync(command: str) -> str:
    """
    Exécute une commande shell de manière synchrone et capture la sortie.
    Utilise `subprocess.run` avec un timeout pour éviter les blocages.
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=True,
            timeout=10
        )
        output = result.stdout
        error = result.stderr
        if error:
            log_message(f"Erreur d'exécution Shell en sandbox:\n{error}", level="warning")
            return f"🐚 Erreur Shell:\n{error}\nSortie:\n{output}"
        return f"✅ Sortie Shell:\n{output}"
    except subprocess.CalledProcessError as e:
        log_message(f"Erreur d'exécution Shell (Code: {e.returncode}):\n{e.stderr}\nSortie:\n{e.stdout}", level="error")
        return f"❌ Erreur d'exécution Shell (Code: {e.returncode}):\n{e.stderr}\nSortie:\n{e.stdout}"
    except subprocess.TimeoutExpired:
        log_message("Erreur Shell: La commande a dépassé le temps d'exécution imparti.", level="warning")
        return "❌ Erreur Shell: La commande a dépassé le temps d'exécution imparti."
    except Exception as e:
        log_message(f"Erreur inattendue lors de l'exécution Shell: {e}\n{traceback.format_exc()}", level="error")
        return f"❌ Erreur inattendue lors de l'exécution Shell: {e}"

def syntax_highlight(code: str) -> str:
    """
    Met en surbrillance la syntaxe du code Python en utilisant Pygments.
    Retourne le code formaté pour l'affichage en console ou dans un bloc `<pre>`.
    """
    if highlight and PythonLexer and TerminalFormatter:
        try:
            return highlight(code, PythonLexer(), TerminalFormatter())
        except Exception as e:
            log_message(f"Erreur de surbrillance syntaxique: {e}", level="error")
            return code
    else:
        return "❌ Outil de surbrillance syntaxique (Pygments) non disponible."

def check_code(code: str) -> str:
    """
    Vérifie le code Python avec Pyflakes pour détecter les erreurs de syntaxe et les problèmes de style.
    """
    if check and Reporter:
        out = io.StringIO()
        reporter = Reporter(out, out)
        check(code, filename="<string>", reporter=reporter)
        result = out.getvalue()
        return result if result else "✅ Pyflakes: Aucun problème détecté."
    else:
        return "❌ Outil de vérification de code (Pyflakes) non disponible."

def format_code(code: str) -> str:
    """
    Formate le code Python avec Black pour assurer une cohérence stylistique.
    """
    if black:
        try:
            mode = black.Mode()
            return black.format_str(code, mode=mode)
        except black.InvalidInput as e:
            log_message(f"Erreur de formatage (Black): Code Python invalide. {e}", level="error")
            return f"❌ Erreur de formatage (Black): Code Python invalide. {e}"
        except Exception as e:
            log_message(f"Erreur de formatage (Black): {e}", level="error")
            return f"❌ Erreur de formatage (Black): {e}"
    else:
        return "❌ Outil de formatage de code (Black) non disponible."

def extract_functions(code: str) -> Union[List[str], str]:
    """
    Extrait les noms des fonctions définies dans un code Python en utilisant l'AST.
    """
    try:
        tree = ast.parse(code)
        functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        return functions if functions else "Aucune fonction détectée."
    except SyntaxError as e:
        log_message(f"Erreur de syntaxe Python lors de l'extraction des fonctions: {e}", level="error")
        return f"❌ Erreur de syntaxe Python: {e}"
    except Exception as e:
        log_message(f"Erreur lors de l'extraction des fonctions: {e}", level="error")
        return f"❌ Erreur lors de l'extraction des fonctions: {e}"

def analyze_code_structure(code: str) -> str:
    """
    Analyse la structure AST (Arbre Syntaxique Abstrait) d'un code Python.
    Utile pour comprendre la composition du code.
    """
    try:
        tree = ast.parse(code)
        return ast.dump(tree, indent=2)
    except SyntaxError as e:
        log_message(f"Erreur de syntaxe Python lors de l'analyse AST: {e}", level="error")
        return f"❌ Erreur de syntaxe Python: {e}"
    except Exception as e:
        log_message(f"Erreur lors de l'analyse de la structure AST: {e}", level="error")
        return f"❌ Erreur lors de l'analyse de la structure AST: {e}"

async def perform_ocr_api(image_url: str) -> str:
    """
    Effectue l'OCR sur une URL d'image en utilisant l'API OCR.space via `OCRApiClient`.
    Télécharge l'image, l'encode en base64, puis envoie à l'API.
    """
    if ocr_api_client_instance is None:
        return "❌ L'instance du client OCR n'est pas initialisée."

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            img_response = await client.get(image_url)
            img_response.raise_for_status()

        base64_image_data = base64.b64encode(img_response.content).decode('utf-8')
        content_type = img_response.headers.get("Content-Type", "image/jpeg")
        image_base64_with_prefix = f"data:{content_type};base64,{base64_image_data}"

        result = await ocr_api_client_instance.query(image_base64_with_prefix)
        return result

    except httpx.HTTPStatusError as e:
        log_message(f"Erreur HTTP/réseau lors de l'OCR: {e.response.status_code} - {e.response.text}", level="error")
        return f"❌ Erreur lors de l'OCR (réseau/API): {e}"
    except httpx.RequestError as e:
        log_message(f"Erreur de requête lors de l'OCR: {e}", level="error")
        return f"❌ Erreur lors de l'OCR (requête): {e}"
    except Exception as e:
        log_message(f"Erreur inattendue lors de l'OCR: {e}\n{traceback.format_exc()}", level="error")
        return f"❌ Erreur inattendue lors de l'OCR: {e}"

async def fetch_and_archive_pages(links: List[str], user_id: Union[int, str], bot_instance: Any):
    """
    Télécharge toutes les pages des liens fournis, les archive localement,
    puis les envoie au groupe privé Telegram.
    """
    user_archive_dir = get_user_dir(user_id) / ARCHIVES_DIR
    user_archive_dir.mkdir(exist_ok=True, parents=True)

    for idx, url in enumerate(links):
        try:
            async with httpx.AsyncClient(timeout=20) as client:
                r = await client.get(url)
                r.raise_for_status()

                if len(r.content) < MAX_FILE_SIZE:
                    ext = ".html" if "<html" in r.text.lower() else ".txt"
                    url_hash = hashlib.sha256(url.encode('utf-8')).hexdigest()[:10]
                    fname = f"page_{datetime.now().strftime('%Y%m%d%H%M%S')}_{url_hash}_{idx}{ext}"
                    fpath = user_archive_dir / fname
                    fpath.write_text(r.text, encoding="utf-8", errors="ignore")

                    if bot_instance and hasattr(bot_instance, 'send_document'):
                        try:
                            with fpath.open("rb") as f:
                                await bot_instance.send_document(chat_id=PRIVATE_GROUP_ID, document=f, filename=fname, caption=f"Page archivée de {neutralize_urls(url)}")
                        except Exception as send_e:
                            log_message(f"Erreur lors de l'envoi du document archivé au groupe privé: {send_e}", level="error")

                    log_message(f"Page archivée: {url} pour user {user_id}")
                else:
                    log_message(f"Page trop grande pour être archivée: {url} ({len(r.content)} bytes)", level="warning")
        except httpx.HTTPStatusError as e:
            log_message(f"[fetch_and_archive_pages] Erreur HTTP pour {url}: {e.response.status_code} - {e.response.text}", level="error")
        except httpx.RequestError as e:
            log_message(f"[fetch_and_archive_pages] Erreur de requête pour {url}: {e}", level="error")
        except Exception as e:
            log_message(f"[fetch_and_archive_pages] Erreur inattendue pour {url}: {e}\n{traceback.format_exc()}", level="error")

# main.py
import asyncio
import telebot
import traceback
import json
import re
from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message
from typing import Dict, Any, List, Optional, Union

# Importation des constantes et configurations
from config import (
        BOT_TOKEN, PRIVATE_GROUP_ID, API_QUOTAS, API_COOLDOWN_DURATION_SECONDS, # BOT_TOKEN au lieu de TELEGRAM_BOT_TOKEN
        API_ROTATION_INTERVAL_MINUTES, BURN_QUOTA_BEFORE_RESET_HOURS,
        USER_CHAT_HISTORY_FILE, USER_LONG_MEMORY_FILE, IA_STATUS_FILE,
        QUOTAS_FILE, GROUP_CHAT_HISTORY_FILE, MAX_CACHE_SIZE, FORBIDDEN_WORDS,
        GEMINI_API_KEY, OCR_API_KEY, API_CONFIG
    )

# Importation des modules locaux
from utils import (
    load_json, save_json, get_user_dir,
    get_current_time, format_datetime, log_message,
    neutralize_urls, similar, set_file_lock
)
from api_clients import (
    EndpointHealthManager, APIClient, DeepSeekClient, SerperClient, WolframAlphaClient,
    TavilyClient, ApiFlashClient, CrawlbaseClient, DetectLanguageClient, GuardianClient,
    IP2LocationClient, ShodanClient, WeatherAPIClient, CloudmersiveClient,
    GreyNoiseClient, PulsediveClient, StormGlassClient, LoginRadiusClient,
    JsonbinClient, HuggingFaceClient, TwilioClient, AbstractAPIClient,
    GeminiAPIClient, GoogleCustomSearchClient, RandommerClient, TomorrowIOClient,
    OpenWeatherMapClient, MockarooClient, OpenPageRankClient, RapidAPIClient,
    set_endpoint_health_manager_global, ALL_API_CLIENTS # Import ALL_API_CLIENTS list
)
from memory_and_quotas import MemoryManager, QuotaManager
from filters_and_tools import (
    filter_bad_code, detect_and_correct_toxicity, run_in_sandbox,
    perform_ocr_api, fetch_and_archive_pages, set_ocr_api_client_instance
)

# --- Initialisation du bot et des gestionnaires ---
bot = AsyncTeleBot(TELEGRAM_BOT_TOKEN)

# Instanciation des gestionnaires (ils sont des singletons, donc une seule instance)
endpoint_health_manager = EndpointHealthManager()
memory_manager = MemoryManager()
quota_manager = QuotaManager()

# Injection des instances nécessaires
set_endpoint_health_manager_global(endpoint_health_manager) # Pour api_clients.py
quota_manager.set_bot_instance(bot) # Pour que le quota_manager puisse envoyer des alertes
set_file_lock(asyncio.Lock()) # Injecte le verrou de fichier global dans utils.py

# Instanciation des clients API
# Note: GeminiAPIClient et OCRApiClient sont gérés séparément car ils n'utilisent pas le système de sélection d'endpoint dynamique
gemini_client = GeminiAPIClient()
ocr_client = OCRApiClient() # Instancie ici
set_ocr_api_client_instance(ocr_client) # Injecte l'instance dans filters_and_tools.py

# Dictionnaire des clients API pour un accès facile par nom
api_clients: Dict[str, APIClient] = {
    client.name: client for client in ALL_API_CLIENTS
}

# --- Fonctions utilitaires du bot ---

async def send_message_to_private_group(text: str):
    """Envoie un message au groupe privé configuré."""
    if PRIVATE_GROUP_ID:
        try:
            await bot.send_message(PRIVATE_GROUP_ID, text)
        except Exception as e:
            log_message(f"Erreur lors de l'envoi au groupe privé: {e}", level="error")

async def get_user_id_from_message(message: Message) -> Union[int, str]:
    """
    Récupère l'ID de l'utilisateur ou du groupe à partir d'un message.
    Utilise l'ID du chat pour les groupes et l'ID de l'expéditeur pour les messages privés.
    """
    return message.chat.id if message.chat.type != "private" else message.from_user.id

def get_sender_info(message: Message) -> str:
    """Retourne une chaîne d'informations sur l'expéditeur du message."""
    if message.chat.type == "private":
        return f"Utilisateur: {message.from_user.first_name} (@{message.from_user.username} - {message.from_user.id})"
    else:
        return f"Groupe: {message.chat.title} (ID: {message.chat.id}), Expéditeur: {message.from_user.first_name} (@{message.from_user.username} - {message.from_user.id})"

# --- Boucles de fond pour la maintenance ---

async def _health_check_loop():
    """Boucle de fond pour exécuter des checks de santé réguliers sur les endpoints API."""
    while True:
        log_message("Lancement des health checks pour tous les services API...")
        for service_name in API_CONFIG.keys():
            await endpoint_health_manager.run_health_check_for_service(service_name)
        await asyncio.sleep(API_ROTATION_INTERVAL_MINUTES * 60) # Exécute toutes les X minutes

async def _quota_burn_loop():
    """
    Boucle de fond pour "brûler" les quotas API avant leur réinitialisation.
    Tente d'utiliser les APIs qui sont dans leur fenêtre de "brûlage".
    """
    while True:
        burn_apis_info = quota_manager.get_burn_window_apis()
        if burn_apis_info:
            log_message(f"APIs en mode 'burn' détectées: {', '.join(burn_apis_info)}")
            for api_info_str in burn_apis_info:
                api_name = api_info_str.split(" ")[0] # Extrait le nom de l'API
                if quota_manager.should_burn_quota(api_name):
                    log_message(f"Tentative de 'brûlage' de quota pour {api_name}...", level="info")
                    client = api_clients.get(api_name)
                    if client:
                        try:
                            # Utilise des prompts aléatoires pour Gemini ou des appels génériques pour les autres
                            if api_name == "GEMINI":
                                from config import AUTO_BURN_PROMPTS
                                prompt = random.choice(AUTO_BURN_PROMPTS.get("GEMINI", ["Génère un texte technique."]))
                                await gemini_client.generate_content(prompt=prompt, chat_history=[])
                            elif api_name == "OCR_API":
                                from config import AUTO_BURN_PROMPTS
                                prompt = random.choice(AUTO_BURN_PROMPTS.get("OCR_API", ["Décris un document."]))
                                # Pour OCR, simuler un appel avec une URL bidon, l'API réelle ne sera pas appelée
                                # car perform_ocr_api nécessite une image valide.
                                # L'objectif ici est de déclencher la logique de quota.
                                # Une meilleure approche serait d'avoir une méthode de "burn" dans le client OCR lui-même.
                                # Pour l'instant, on se contente de la vérification de quota.
                                await quota_manager.check_and_update_quota(api_name, cost=1)
                            else:
                                # Appels génériques pour d'autres APIs
                                if api_name == "DEEPSEEK":
                                    await client.query(prompt="test")
                                elif api_name == "SERPER":
                                    await client.query(query_text="test")
                                elif api_name == "WOLFRAMALPHA":
                                    await client.query(input_text="1+1")
                                elif api_name == "TAVILY":
                                    await client.query(query_text="test")
                                elif api_name == "APIFLASH":
                                    pass # Requires a valid URL, hard to burn
                                elif api_name == "CRAWLBASE":
                                    pass # Requires a valid URL, hard to burn
                                elif api_name == "DETECTLANGUAGE":
                                    await client.query(text="hello")
                                elif api_name == "GUARDIAN":
                                    await client.query(query_text="news")
                                elif api_name == "IP2LOCATION":
                                    await client.query(ip_address="8.8.8.8")
                                elif api_name == "SHODAN":
                                    await client.query(query_text="test")
                                elif api_name == "WEATHERAPI":
                                    await client.query(location="London")
                                elif api_name == "CLOUDMERSIVE":
                                    await client.query(domain="example.com")
                                elif api_name == "GREYNOISE":
                                    await client.query(ip_address="8.8.8.8")
                                elif api_name == "PULSEDIVE":
                                    await client.query(indicator="8.8.8.8")
                                elif api_name == "STORMGLASS":
                                    await client.query(lat=0.0, lng=0.0)
                                elif api_name == "LOGINRADIUS":
                                    await client.query()
                                elif api_name == "JSONBIN":
                                    await client.query(data={"burn": True})
                                elif api_name == "HUGGINGFACE":
                                    await client.query(input_text="test")
                                elif api_name == "TWILIO":
                                    await client.query()
                                elif api_name == "ABSTRACTAPI":
                                    await client.query(input_value="test@example.com", api_type="EMAIL_VALIDATION")
                                elif api_name == "GOOGLE_CUSTOM_SEARCH":
                                    await client.query(query_text="test")
                                elif api_name == "RANDOMMER":
                                    await client.query(quantity=1)
                                elif api_name == "TOMORROW.IO":
                                    await client.query(location="London")
                                elif api_name == "OPENWEATHERMAP":
                                    await client.query(location="London")
                                elif api_name == "MOCKAROO":
                                    await client.query(count=1)
                                elif api_name == "OPENPAGERANK":
                                    await client.query(domains=["example.com"])
                                elif api_name == "RAPIDAPI":
                                    await client.query(api_name="random fact")

                            log_message(f"Quota pour {api_name} 'brûlé' avec succès.")
                        except Exception as e:
                            log_message(f"Erreur lors du 'brûlage' de quota pour {api_name}: {e}", level="error")
                    else:
                        log_message(f"Client API {api_name} non trouvé pour le 'brûlage' de quota.", level="warning")
        await asyncio.sleep(BURN_QUOTA_BEFORE_RESET_HOURS * 3600 / 4) # Vérifie 4 fois par fenêtre de brûlage

async def _diversification_recovery_loop():
    """Boucle de fond pour récupérer les scores de diversification des IA."""
    while True:
        memory_manager.recover_diversification_scores()
        await asyncio.sleep(API_ROTATION_INTERVAL_MINUTES * 60) # Exécute toutes les X minutes

# --- Gestionnaires de messages Telegram ---

@bot.message_handler(commands=['start', 'help'])
async def send_welcome(message: Message):
    """Envoie un message de bienvenue et d'aide."""
    user_id = await get_user_id_from_message(message)
    sender_info = get_sender_info(message)
    log_message(f"Commande /start ou /help reçue de {sender_info}")

    welcome_text = (
        "Bonjour ! Je suis votre assistant IA. Je peux vous aider avec des questions, "
        "exécuter du code, faire de l'OCR, et bien plus encore.\n\n"
        "Voici quelques commandes que vous pouvez utiliser :\n"
        "/status - Affiche le statut des APIs et les quotas.\n"
        "/run_code [langage] [code] - Exécute du code (ex: /run_code python print('Hello')).\n"
        "/ocr [URL_image] - Extrait le texte d'une image via son URL.\n"
        "/archive_page [URL] - Archive une page web et l'envoie au groupe privé.\n"
        "/burn_quota - Tente de 'brûler' les quotas API avant leur réinitialisation.\n"
        "Posez-moi simplement une question ou donnez-moi une tâche !"
    )
    await bot.reply_to(message, welcome_text)
    await memory_manager.add_message_to_history(user_id, "bot", welcome_text)

@bot.message_handler(commands=['status'])
async def get_status(message: Message):
    """Affiche le statut des APIs et les quotas d'utilisation."""
    user_id = await get_user_id_from_message(message)
    sender_info = get_sender_info(message)
    log_message(f"Commande /status reçue de {sender_info}")

    ia_status = memory_manager.ia_status
    quotas_status = quota_manager.get_all_quotas_status()

    status_text = "📊 *Statut des APIs et Quotas:*\n\n"

    for api_name, status in ia_status.items():
        quota_data = quotas_status.get(api_name, {})

        status_text += f"*{api_name}:*\n"
        status_text += f"  - Score de performance: `{status['current_score']:.2f}`\n"
        status_text += f"  - Score de diversification: `{status['diversification_score']:.2f}`\n"
        status_text += f"  - Erreurs consécutives: `{status['error_count']}`\n"
        status_text += f"  - En cooldown jusqu'à: `{status['cooldown_until'] or 'N/A'}`\n"

        if quota_data:
            status_text += f"  - Quota Mensuel: `{quota_data['monthly_usage']}/{quota_data['monthly_limit']}`\n"
            status_text += f"  - Quota Journalier: `{quota_data['daily_usage']}/{quota_data['daily_limit']}`\n"
            status_text += f"  - Quota Horaire: `{quota_data['hourly_usage']}/{quota_data['hourly_limit']}`\n"
            status_text += f"  - Dernier usage: `{quota_data['last_usage'] or 'N/A'}`\n"
        else:
            status_text += "  - _Données de quota non disponibles._\n"
        status_text += "\n"

    burn_apis = quota_manager.get_burn_window_apis()
    if burn_apis:
        status_text += "🔥 *APIs en mode 'Brûlage' de quota:*\n"
        for api_info in burn_apis:
            status_text += f"- {api_info}\n"
    else:
        status_text += "🔥 _Aucune API en mode 'Brûlage' de quota actuellement._\n"

    await bot.reply_to(message, status_text, parse_mode="Markdown")
    await memory_manager.add_message_to_history(user_id, "bot", status_text)

@bot.message_handler(commands=['burn_quota'])
async def trigger_burn_quota(message: Message):
    """Déclenche manuellement la tentative de 'brûlage' de quota."""
    user_id = await get_user_id_from_message(message)
    sender_info = get_sender_info(message)
    log_message(f"Commande /burn_quota reçue de {sender_info}")

    burn_apis = quota_manager.get_burn_window_apis()
    if not burn_apis:
        response_text = "Aucune API n'est actuellement dans sa fenêtre de 'brûlage' de quota."
        await bot.reply_to(message, response_text)
        await memory_manager.add_message_to_history(user_id, "bot", response_text)
        return

    response_text = "Tentative de 'brûlage' de quota pour les APIs suivantes:\n" + "\n".join(burn_apis)
    await bot.reply_to(message, response_text)
    await memory_manager.add_message_to_history(user_id, "bot", response_text)

    asyncio.create_task(_quota_burn_loop())

@bot.message_handler(commands=['run_code'])
async def handle_run_code(message: Message):
    """Exécute le code fourni dans une sandbox."""
    user_id = await get_user_id_from_message(message)
    sender_info = get_sender_info(message)
    log_message(f"Commande /run_code reçue de {sender_info}")

    args = message.text.split(maxsplit=2)
    if len(args) < 3:
        await bot.reply_to(message, "Usage: `/run_code <langage> <votre_code>` (ex: `/run_code python print('Hello')`)", parse_mode="Markdown")
        await memory_manager.add_message_to_history(user_id, "bot", "Usage: `/run_code <langage> <votre_code>`")
        return

    language = args[1].lower()
    code_to_run = args[2]

    response_text = await run_in_sandbox(code_to_run, language)
    await bot.reply_to(message, f"```\n{response_text}\n```", parse_mode="Markdown")
    await memory_manager.add_message_to_history(user_id, "bot", response_text)

@bot.message_handler(commands=['ocr'])
async def handle_ocr_command(message: Message):
    """Effectue l'OCR sur une image à partir d'une URL."""
    user_id = await get_user_id_from_message(message)
    sender_info = get_sender_info(message)
    log_message(f"Commande /ocr reçue de {sender_info}")

    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await bot.reply_to(message, "Usage: `/ocr <URL_de_l_image>`", parse_mode="Markdown")
        await memory_manager.add_message_to_history(user_id, "bot", "Usage: `/ocr <URL_de_l_image>`")
        return

    image_url = args[1].strip()
    if not re.match(r"https?://.*\.(png|jpg|jpeg|gif|bmp|tiff|webp)$", image_url, re.IGNORECASE):
        await bot.reply_to(message, "L'URL de l'image semble invalide ou le format n'est pas supporté (doit être png, jpg, jpeg, gif, bmp, tiff, webp).")
        await memory_manager.add_message_to_history(user_id, "bot", "URL d'image invalide.")
        return

    try:
        await bot.reply_to(message, "Traitement de l'image par OCR, veuillez patienter...")
        ocr_result = await perform_ocr_api(image_url)
        await bot.reply_to(message, f"Texte extrait:\n```\n{ocr_result}\n```", parse_mode="Markdown")
        await memory_manager.add_message_to_history(user_id, "bot", f"OCR de {image_url}: {ocr_result}")
    except Exception as e:
        log_message(f"Erreur lors de l'OCR de l'image {image_url}: {e}\n{traceback.format_exc()}", level="error")
        await bot.reply_to(message, f"Une erreur est survenue lors de l'extraction du texte de l'image: {e}")
        await memory_manager.add_message_to_history(user_id, "bot", f"Erreur OCR: {e}")

@bot.message_handler(commands=['archive_page'])
async def handle_archive_page(message: Message):
    """Archive une page web et l'envoie au groupe privé."""
    user_id = await get_user_id_from_message(message)
    sender_info = get_sender_info(message)
    log_message(f"Commande /archive_page reçue de {sender_info}")

    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await bot.reply_to(message, "Usage: `/archive_page <URL>`", parse_mode="Markdown")
        await memory_manager.add_message_to_history(user_id, "bot", "Usage: `/archive_page <URL>`")
        return

    url_to_archive = args[1].strip()
    if not url_to_archive.startswith(("http://", "https://")):
        await bot.reply_to(message, "Veuillez fournir une URL valide (commençant par http:// ou https://).")
        await memory_manager.add_message_to_history(user_id, "bot", "URL invalide pour l'archivage.")
        return

    await bot.reply_to(message, f"Archivage de la page {url_to_archive}, veuillez patienter...")
    try:
        await fetch_and_archive_pages([url_to_archive], user_id, bot)
        response_text = f"Page archivée et envoyée au groupe privé: {neutralize_urls(url_to_archive)}"
        await bot.reply_to(message, response_text)
        await memory_manager.add_message_to_history(user_id, "bot", response_text)
    except Exception as e:
        log_message(f"Erreur lors de l'archivage de la page {url_to_archive}: {e}\n{traceback.format_exc()}", level="error")
        await bot.reply_to(message, f"Une erreur est survenue lors de l'archivage de la page: {e}")
        await memory_manager.add_message_to_history(user_id, "bot", f"Erreur archivage: {e}")

@bot.message_handler(func=lambda message: True)
async def handle_all_messages(message: Message):
    """
    Gestionnaire principal pour tous les messages textuels.
    Traite la requête, choisit la meilleure IA, gère la mémoire et les outils.
    """
    user_id = await get_user_id_from_message(message)
    sender_info = get_sender_info(message)
    raw_text = message.text
    log_message(f"Message reçu de {sender_info}: {raw_text}")

    await memory_manager.add_message_to_history(user_id, "user", raw_text)

    if message.chat.type != "private":
        await memory_manager.save_group_memory(user_id, "user", raw_text)

    cached_response = await memory_manager.check_for_similar_prompt(user_id, raw_text)
    if cached_response:
        log_message(f"Réponse en cache trouvée pour {user_id}.")
        await bot.reply_to(message, cached_response)
        await memory_manager.add_message_to_history(user_id, "bot", cached_response)
        return

    cleaned_text = detect_and_correct_toxicity(raw_text)
    if cleaned_text != raw_text:
        await bot.reply_to(message, f"Votre message a été modéré: {cleaned_text}")
        await memory_manager.add_message_to_history(user_id, "bot", cleaned_text)
        return

    chat_history_for_gemini = await memory_manager.get_chat_history(user_id, limit=10)
    long_term_memory_for_gemini = await memory_manager.get_long_term_memory(user_id, limit=5)
    group_memory_for_gemini = ""
    if message.chat.type != "private":
        group_memory_for_gemini = await memory_manager.get_group_memory(user_id, limit=5)

    context_parts = []
    if long_term_memory_for_gemini:
        context_parts.append(f"Mémoire à long terme de l'utilisateur:\n{long_term_memory_for_gemini}")
    if group_memory_for_gemini:
        context_parts.append(f"Contexte du groupe:\n{group_memory_for_gemini}")

    full_context = "\n\n".join(context_parts) if context_parts else ""

    available_apis = memory_manager.get_available_ias()
    api_info_for_prompt = "APIs disponibles et leur statut:\n"
    for api_name in available_apis:
        status = memory_manager.get_ia_status(api_name)
        if status:
            api_info_for_prompt += f"- {api_name}: Score {status['current_score']:.2f}, Diversification {status['diversification_score']:.2f}\n"

    system_instruction = (
        "Vous êtes un assistant IA avancé. Votre objectif est de répondre aux requêtes de l'utilisateur "
        "de manière utile, précise et concise. Vous avez accès à plusieurs outils et APIs pour vous aider.\n"
        "Lorsque vous utilisez un outil, indiquez clairement quel outil vous utilisez et pourquoi.\n"
        "Si une requête nécessite une recherche web, utilisez les outils de recherche disponibles.\n"
        "Si une requête est complexe ou nécessite plusieurs étapes, décomposez-la.\n"
        "N'inventez pas d'informations. Si vous ne savez pas, dites-le.\n"
        "Contexte supplémentaire de l'utilisateur et du groupe:\n"
        f"{full_context}\n\n"
        f"{api_info_for_prompt}\n"
        "Vous pouvez aussi exécuter du code Python ou Shell en utilisant la fonction `run_in_sandbox(code, language='python')`.\n"
        "Pour l'OCR, utilisez `perform_ocr_api(image_url)`.\n"
        "Pour archiver des pages web, utilisez `fetch_and_archive_pages(links, user_id, bot_instance)`.\n"
        "Pour les recherches web, utilisez `api_clients['SERPER'].query(query_text)` ou `api_clients['TAVILY'].query(query_text)`.\n"
        "Pour les calculs ou faits, utilisez `api_clients['WOLFRAMALPHA'].query(input_text)`.\n"
        "Si l'utilisateur demande une tâche impliquant un outil, proposez d'utiliser l'outil et montrez comment.\n"
        "Si l'utilisateur demande des informations sur les quotas ou le statut des APIs, utilisez les commandes /status.\n"
        "Si l'utilisateur pose une question générale, utilisez DeepSeek."
    )

    selected_api_name = None
    best_combined_score = -float('inf')

    for api_name in available_apis:
        status = memory_manager.get_ia_status(api_name)
        if status:
            combined_score = (status["current_score"] * 0.7) + (status["diversification_score"] * 0.3)
            if combined_score > best_combined_score:
                best_combined_score = combined_score
                selected_api_name = api_name

    if not selected_api_name:
        await bot.reply_to(message, "Désolé, aucune IA n'est actuellement disponible pour traiter votre requête.")
        await memory_manager.add_message_to_history(user_id, "bot", "Aucune IA disponible.")
        return

    log_message(f"IA sélectionnée pour {user_id}: {selected_api_name} (Score combiné: {best_combined_score:.2f})")
    await bot.send_chat_action(message.chat.id, 'typing')

    try:
        gemini_chat_history_formatted = []
        for entry in chat_history_for_gemini:
            role = "user" if entry["role"] == "user" else "model"
            gemini_chat_history_formatted.append({"role": role, "parts": [{"text": entry["content"]}]})

        final_gemini_prompt = f"{system_instruction}\n\nRequête de l'utilisateur: {raw_text}"

        gemini_response_raw = await gemini_client.generate_content(
            prompt=final_gemini_prompt,
            chat_history=gemini_chat_history_formatted,
            model="gemini-1.5-flash-latest"
        )

        gemini_text_response = ""
        if gemini_response_raw and not gemini_response_raw.get("error"):
            candidates = gemini_response_raw.get("candidates", [])
            if candidates:
                first_candidate = candidates[0]
                if "content" in first_candidate and "parts" in first_candidate["content"]:
                    for part in first_candidate["content"]["parts"]:
                        if "text" in part:
                            gemini_text_response += part["text"]
            else:
                gemini_text_response = "Gemini n'a pas pu générer de réponse."
        else:
            gemini_text_response = f"Erreur lors de l'appel à Gemini: {gemini_response_raw.get('error', 'Inconnu')}"

        final_bot_response = gemini_text_response
        tool_executed = False

        # Simplified tool execution logic based on text pattern matching
        if "run_in_sandbox(" in gemini_text_response:
            match_python = re.search(r"run_in_sandbox\(['\"](.*?)['\"],\s*language=['\"]python['\"]\)", gemini_text_response, re.DOTALL)
            match_shell = re.search(r"run_in_sandbox\(['\"](.*?)['\"],\s*language=['\"]shell['\"]\)", gemini_text_response, re.DOTALL)

            if match_python:
                code_to_execute = match_python.group(1).strip()
                log_message(f"Gemini a suggéré l'exécution de code Python: {code_to_execute[:100]}...")
                tool_output = await run_in_sandbox(code_to_execute, "python")
                final_bot_response = f"J'ai exécuté le code Python:\n```\n{code_to_execute}\n```\nRésultat:\n```\n{tool_output}\n```"
                tool_executed = True
            elif match_shell:
                code_to_execute = match_shell.group(1).strip()
                log_message(f"Gemini a suggéré l'exécution de code Shell: {code_to_execute[:100]}...")
                tool_output = await run_in_sandbox(code_to_execute, "shell")
                final_bot_response = f"J'ai exécuté la commande Shell:\n```\n{code_to_execute}\n```\nRésultat:\n```\n{tool_output}\n```"
                tool_executed = True

        elif "perform_ocr_api(" in gemini_text_response:
            match = re.search(r"perform_ocr_api\(['\"](.*?)['\"]\)", gemini_text_response)
            if match:
                image_url = match.group(1)
                log_message(f"Gemini a suggéré l'exécution de l'OCR sur: {image_url}")
                tool_output = await perform_ocr_api(image_url)
                final_bot_response = f"J'ai effectué l'OCR sur l'image:\n{tool_output}"
                tool_executed = True

        elif "fetch_and_archive_pages(" in gemini_text_response:
            match = re.search(r"fetch_and_archive_pages\(\[(.*?)\],\s*user_id,\s*bot_instance\)", gemini_text_response)
            if match:
                links_str = match.group(1)
                links = [link.strip().strip("'\"") for link in links_str.split(',')]
                log_message(f"Gemini a suggéré l'archivage des pages: {links}")
                await fetch_and_archive_pages(links, user_id, bot)
                final_bot_response = f"J'ai archivé les pages demandées et les ai envoyées au groupe privé."
                tool_executed = True

        elif "api_clients['SERPER'].query(" in gemini_text_response:
            match = re.search(r"api_clients\['SERPER'\]\.query\(['\"](.*?)['\"]\)", gemini_text_response)
            if match:
                query_text = match.group(1)
                log_message(f"Gemini a suggéré une recherche Serper pour: {query_text}")
                serper_client_instance = api_clients.get("SERPER")
                if serper_client_instance:
                    tool_output = await serper_client_instance.query(query_text)
                    final_bot_response = f"Résultat de la recherche web (Serper):\n{tool_output}"
                    tool_executed = True
                else:
                    final_bot_response = "L'outil de recherche Serper n'est pas disponible."

        elif "api_clients['WOLFRAMALPHA'].query(" in gemini_text_response:
            match = re.search(r"api_clients\['WOLFRAMALPHA'\]\.query\(['\"](.*?)['\"]\)", gemini_text_response)
            if match:
                input_text = match.group(1)
                log_message(f"Gemini a suggéré un calcul WolframAlpha pour: {input_text}")
                wolfram_client_instance = api_clients.get("WOLFRAMALPHA")
                if wolfram_client_instance:
                    tool_output = await wolfram_client_instance.query(input_text)
                    final_bot_response = f"Résultat WolframAlpha:\n{tool_output}"
                    tool_executed = True
                else:
                    final_bot_response = "L'outil WolframAlpha n'est pas disponible."

        if not tool_executed:
            final_bot_response = gemini_text_response
            log_message(f"Gemini a répondu directement: {final_bot_response[:200]}...")

        # Update API status and quotas for Gemini (as it was the orchestrator)
        memory_manager.update_ia_status("GEMINI", success=True)
        await quota_manager.check_and_update_quota("GEMINI", cost=1)

    except Exception as e:
        log_message(f"Erreur inattendue lors du traitement du message: {e}\n{traceback.format_exc()}", level="error")
        final_bot_response = "Désolé, une erreur interne est survenue. Veuillez réessayer plus tard."
        memory_manager.update_ia_status("GEMINI", success=False, error_message=str(e))

    await bot.reply_to(message, final_bot_response)
    await memory_manager.add_message_to_history(user_id, "bot", final_bot_response)

    if message.chat.type != "private":
        await memory_manager.save_group_memory(user_id, "bot", final_bot_response)

# --- Boucle principale d'exécution ---
async def main():
    """Fonction principale pour initialiser et démarrer le bot."""
    log_message("Démarrage de l'initialisation du bot...")

    await endpoint_health_manager.init_manager()
    await memory_manager.init_manager()
    await quota_manager.init_manager()

    log_message("Gestionnaires initialisés. Démarrage des boucles de fond...")

    asyncio.create_task(_health_check_loop())
    asyncio.create_task(_quota_burn_loop())
    asyncio.create_task(_diversification_recovery_loop())

    log_message("Boucles de fond démarrées. Démarrage du polling du bot...")

    await bot.infinity_polling()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        log_message("Bot arrêté manuellement.")
    except Exception as e:
        log_message(f"Erreur fatale dans la boucle principale: {e}\n{traceback.format_exc()}", level="critical")




import os
import json
from datetime import datetime, timezone, date, timedelta
from pathlib import Path

# ----------------------------
# CONFIGURATION & CONSTANTES GLOBALES
# ----------------------------

# ==== Chemins de fichiers & Limites ====
# Assure que le temps est toujours en UTC pour une cohérence globale
os.environ["TZ"] = "UTC" 

# Répertoire de base pour toutes les sauvegardes et données
BASE_DIR = Path(__file__).resolve().parent / "sauvegardes"
# Chemin du fichier de log des erreurs critiques
ERROR_LOG_PATH = BASE_DIR / "erreurs.log"
# Chemin du fichier de log général du bot (pour le suivi des opérations)
LOG_FILE = BASE_DIR / "bot_log.log"

# Répertoires spécifiques pour les données utilisateur et les défis de code
DAILY_CHALLENGE_PATH = Path(__file__).resolve().parent / "defis_code"
HISTORY_DIR = DAILY_CHALLENGE_PATH / "history" # Pour l'historique des défis de code

# Fichiers globaux pour le statut des IA et les quotas
IA_STATUS_FILE = BASE_DIR / "ia_status.json"
QUOTAS_FILE = BASE_DIR / "quotas.json"
ENDPOINT_HEALTH_FILE = BASE_DIR / "endpoint_health.json"

# Fichiers spécifiques à l'utilisateur (stockés dans sauvegardes/{user_id}/)
USER_CHAT_HISTORY_FILE = "chat_history.json"
USER_LONG_MEMORY_FILE = "long_term_memory.json"
GROUP_CHAT_HISTORY_FILE = "group_chat_history.json" # Pour la mémoire de groupe
ARCHIVES_DIR = "archives" # Sous-répertoire pour l'archivage des pages web

# Taille maximale des fichiers pour la rotation/compression des logs et l'archivage
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

# Paramètres de mémoire et de cache
MAX_CACHE_SIZE = 20       # Nombre de messages récents à garder en cache pour la similarité
MAX_LONG_TERM_MEMORY = 50 # Nombre d'entrées max dans la mémoire à long terme

# Assurez-vous que les répertoires nécessaires existent
BASE_DIR.mkdir(parents=True, exist_ok=True)
DAILY_CHALLENGE_PATH.mkdir(exist_ok=True)
HISTORY_DIR.mkdir(exist_ok=True)

# ==== Telegram Bot Configuration ====
# Token de votre bot Telegram (à remplacer par votre vrai token en production)
TELEGRAM_BOT_TOKEN = "7902342551:AAG6r1QA2GTMZcmcsWHi36Ivd_PVeMXULOs"
# ID du groupe privé utilisé pour les logs, rapports et archivage
PRIVATE_GROUP_ID = -1002845235344 

# ==== Configuration du Bot ====
BOT_NAME = "Assistant IA"
BOT_DESCRIPTION = "un assistant polyvalent capable de converser, d'exécuter du code, d'analyser des images et d'archiver des informations."
BOT_PERSONALITY = "toujours serviable, précis, éthique et proactif dans l'apprentissage."
BOT_INSTRUCTIONS = "Réponds aux questions, exécute les commandes, et utilise tes outils pour fournir les meilleures informations. Sois concis mais complet."

# ==== Clés API Individuelles (centralisées pour la clarté) ====
# Récupérer les clés API depuis les variables d'environnement pour la production
# ou les définir ici pour le développement local (moins sécurisé)
APIFLASH_KEY = os.getenv("APIFLASH_KEY", "3a3cc886a18e41109e0cebc0745b12de")
DEEPSEEK_KEY_1 = os.getenv("DEEPSEEK_KEY_1", "sk-ef08317d125947b3a1ce5916592bef00")
DEEPSEEK_KEY_2 = os.getenv("DEEPSEEK_KEY_2", "sk-d73750d96142421cb1098c7056dd7f01")
CRAWLBASE_KEY_1 = os.getenv("CRAWLBASE_KEY_1", "x41P6KNU8J86yF9JV1nqSw")
CRAWLBASE_KEY_2 = os.getenv("CRAWLBASE_KEY_2", "FOg3R0v_aLxzHkYIdjPgVg")
DETECTLANGUAGE_KEY = os.getenv("DETECTLANGUAGE_KEY", "ebdc8ccc2ee75eda3ab122b08ffb1e8d")
GUARDIAN_KEY = os.getenv("GUARDIAN_KEY", "07c622c1-af05-4c24-9f37-37d219be76a0")
IP2LOCATION_KEY = os.getenv("IP2LOCATION_KEY", "11103C239EA8EA6DF2473BB445EC32F2")
SERPER_KEY = os.getenv("SERPER_KEY", "047b30db1df999aaa9c293f2048037d40c651439")
SHODAN_KEY = os.getenv("SHODAN_KEY", "umdSaWOfVq9Wt2F4wWdXiKh1zjLailzn")
TAVILY_KEY_1 = os.getenv("TAVILY_KEY_1", "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")
TAVILY_KEY_2 = os.getenv("TAVILY_KEY_2", "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")
TAVILY_KEY_3 = os.getenv("TAVILY_KEY_3", "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")
TAVILY_KEY_4 = os.getenv("TAVILY_KEY_4", "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")
WEATHERAPI_KEY = os.getenv("WEATHERAPI_KEY", "332bcdba457d4db4836175513250407")
WOLFRAM_APP_ID_1 = os.getenv("WOLFRAM_APP_ID_1", "96LX77-G8PGKJ3T7V")
WOLFRAM_APP_ID_2 = os.getenv("WOLFRAM_APP_ID_2", "96LX77-PYHRRET363")
WOLFRAM_APP_ID_3 = os.getenv("WOLFRAM_APP_ID_3", "96LX77-P9HPAYWRGL")
GREYNOISE_KEY = os.getenv("GREYNOISE_KEY", "5zNe9E6c2UNDhU09iVXbMaB04UpHAw5hNm5rHCK24fCLvI2cP33NNOpL7nhkDETG")
LOGINRADIUS_KEY = os.getenv("LOGINRADIUS_KEY", "073b2fbedf82409da2ca6f37b97e8c6a")
JSONBIN_KEY = os.getenv("JSONBIN_KEY", "$2a$10$npWSB7v1YcoqLkyPpz0PZOV5ES5vBs6JtTWVyVDXK3j3FDYYS5BPO")
HUGGINGFACE_KEY_1 = os.getenv("HUGGINGFACE_KEY_1", "hf_KzifJEYPZBXSSNcapgb3ISkPJLioDozyPC")
HUGGINGFACE_KEY_2 = os.getenv("HUGGINGFACE_KEY_2", "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")
HUGGINGFACE_KEY_3 = os.getenv("HUGGINGFACE_KEY_3", "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")
HUGGINGFACE_NEW_KEY = os.getenv("HUGGINGFACE_NEW_KEY", "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")
TWILIO_SID = os.getenv("TWILIO_SID", "SK84cc4d335650f9da168cd779f26e00e5")
TWILIO_SECRET = os.getenv("TWILIO_SECRET", "spvz5uwPE8ANYOI5Te4Mehm7YwKOZ4Lg")
ABSTRACTAPI_EMAIL_KEY_1 = os.getenv("ABSTRACTAPI_EMAIL_KEY_1", "2ffd537411ad407e9c9a7eacb7a97311")
ABSTRACTAPI_EMAIL_KEY_2 = os.getenv("ABSTRACTAPI_EMAIL_KEY_2", "5b00ade4e60e4a388bd3e749f4f66e28")
ABSTRACTAPI_EMAIL_KEY_3 = os.getenv("ABSTRACTAPI_EMAIL_KEY_3", "f4106df7b93e4db6855cb7949edc4a20")
ABSTRACTAPI_GENERIC_KEY = os.getenv("ABSTRACTAPI_GENERIC_KEY", "020a4dcd3e854ac0b19043491d79df92")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyABnzGG2YoTNY0uep-akgX1rfuvAsp049Q") # Clé pour GeminiApiClient
GOOGLE_API_KEYS = [
    os.getenv("GOOGLE_API_KEY_1", "AIzaSyAk6Ph25xuIY3b5o-JgdL652MvK4usp8Ms"),
    os.getenv("GOOGLE_API_KEY_2", "AIzaSyDuccmfiPSk4042NeJCYIjA8EOXPo1YKXU"),
    os.getenv("GOOGLE_API_KEY_3", "AIzaSyAQq6o9voefaDxkAEORf7W-IB3QbotIkwY"),
    os.getenv("GOOGLE_API_KEY_4", "AIzaSyDYaYrQQ7cwYFm8TBpyGM3dJweOGOYl7qw"),
]
GOOGLE_CX_LIST = [
    "3368510e864b74936",
    "e745c9ca0ffb94659"
]
PULSEDIVE_KEY = os.getenv("PULSEDIVE_KEY", "201bb09342f35d365889d7d0ca0fdf8580ebee0f1e7644ce70c99a46c1d47171")
RANDOMMER_KEY = os.getenv("RANDOMMER_KEY", "29d907df567b4226bf64b924f9e26c00")
STORMGLASS_KEY = os.getenv("STORMGLASS_KEY", "7ad5b888-5900-11f0-80b9-0242ac130006-7ad5b996-5900-11f0-80b9-0242ac130006")
TOMORROW_KEY = os.getenv("TOMORROW_KEY", "bNh6KpmddRGY0dzwvmQugVtG4Uf5Y2w1")
CLOUDMERSIVE_KEY = os.getenv("CLOUDMERSIVE_KEY", "4d407015-ce22-45d7-a2e1-b88ab6380084")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "c80075b7332716a418e47033463085ef")
MOCKAROO_KEY = os.getenv("MOCKAROO_KEY", "282b32d0")
OPENPAGERANK_KEY = os.getenv("OPENPAGERANK_KEY", "w848ws8s0848g4koosgooc0sg4ggogcggw4o4cko")
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY", "d4d1f58d8emsh58d888c711b7400p1bcebejsn2cc04dce6efe")
OCR_API_KEY = os.getenv("OCR_API_KEY", "K82679097388957") # Clé pour OCRApiClient (une seule clé pour la classe dédiée)
OCR_API_KEYS = [ # Clés OCR pour les endpoints multiples si utilisés par APIClient générique
    os.getenv("OCR_API_KEY_1", "K82679097388957"),
    os.getenv("OCR_API_KEY_2", "K81079143888957"),
    os.getenv("OCR_API_KEY_3", "K84281517488957")
]

# ==== Configuration unifiée des APIs et Endpoints ====
# Cette configuration est utilisée par EndpointHealthManager et APIClient
API_CONFIG = {
    "APIFLASH": [
        {"key": APIFLASH_KEY, "endpoint_name": "URL to Image", "url": "https://api.apiflash.com/v1/urltoimage", "method": "GET", "key_field": "access_key", "key_location": "param", "health_check_params": {"url": "https://example.com"}, "timeout": 10}
    ],
    "DEEPSEEK": [
        {"key": DEEPSEEK_KEY_1, "endpoint_name": "Models List (Key 1)", "url": "https://api.deepseek.com/v1/models", "method": "GET", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "timeout": 5},
        {"key": DEEPSEEK_KEY_2, "endpoint_name": "Models List (Key 2)", "url": "https://api.deepseek.com/v1/models", "method": "GET", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "timeout": 5},
        {"key": DEEPSEEK_KEY_1, "endpoint_name": "Chat Completions", "url": "https://api.deepseek.com/v1/chat/completions", "method": "POST", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "fixed_json": {"model": "deepseek-chat", "stream": False}, "health_check_json": {"model": "deepseek-chat", "messages": [{"role": "user", "content": "hello"}]}, "timeout": 30}
    ],
    "CRAWLBASE": [
        {"key": CRAWLBASE_KEY_1, "endpoint_name": "HTML Scraping", "url": "https://api.crawlbase.com", "method": "GET", "key_field": "token", "key_location": "param", "health_check_params": {"url": "https://example.com"}, "timeout": 15},
        {"key": CRAWLBASE_KEY_2, "endpoint_name": "JS Scraping (JavaScript Token)", "url": "https://api.crawlbase.com", "method": "GET", "key_field": "token", "key_location": "param", "fixed_params": {"javascript": "true"}, "health_check_params": {"url": "https://example.com", "javascript": "true"}, "timeout": 20}
    ],
    "DETECTLANGUAGE": [
        {"key": DETECTLANGUAGE_KEY, "endpoint_name": "Language Detection", "url": "https://ws.detectlanguage.com/0.2/detect", "method": "POST", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "health_check_json": {"q": "hello"}, "timeout": 5}
    ],
    "GUARDIAN": [
        {"key": GUARDIAN_KEY, "endpoint_name": "News Search", "url": "https://content.guardianapis.com/search", "method": "GET", "key_field": "api-key", "key_location": "param", "fixed_params": {"show-fields": "headline,trailText"}, "health_check_params": {"q": "test"}, "timeout": 10},
        {"key": GUARDIAN_KEY, "endpoint_name": "Sections", "url": "https://content.guardianapis.com/sections", "method": "GET", "key_field": "api-key", "key_location": "param", "health_check_params": {"q": "news"}, "timeout": 5}
    ],
    "IP2LOCATION": [
        {"key": IP2LOCATION_KEY, "endpoint_name": "IP Geolocation", "url": "https://api.ip2location.io/", "method": "GET", "key_field": "key", "key_location": "param", "health_check_params": {"ip": "8.8.8.8"}, "timeout": 5}
    ],
    "SERPER": [
        {"key": SERPER_KEY, "endpoint_name": "Search", "url": "https://google.serper.dev/search", "method": "POST", "key_field": "X-API-KEY", "key_location": "header", "health_check_json": {"q": "test"}, "timeout": 10},
        {"key": SERPER_KEY, "endpoint_name": "Images Search", "url": "https://google.serper.dev/images", "method": "POST", "key_field": "X-API-KEY", "key_location": "header", "health_check_json": {"q": "test"}, "timeout": 10}
    ],
    "SHODAN": [
        {"key": SHODAN_KEY, "endpoint_name": "Host Info", "url": "https://api.shodan.io/shodan/host/8.8.8.8", "method": "GET", "key_field": "key", "key_location": "param", "health_check_params": {"ip": "8.8.8.8"}, "timeout": 10},
        {"key": SHODAN_KEY, "endpoint_name": "API Info", "url": "https://api.shodan.io/api-info", "method": "GET", "key_field": "key", "key_location": "param", "timeout": 5}
    ],
    "TAVILY": [
        {"key": TAVILY_KEY_1, "endpoint_name": "Search (Key 1)", "url": "https://api.tavily.com/search", "method": "POST", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "fixed_json": {"search_depth": "advanced", "include_answer": True}, "health_check_json": {"query": "test"}, "timeout": 15},
        {"key": TAVILY_KEY_2, "endpoint_name": "Search (Key 2)", "url": "https://api.tavily.com/search", "method": "POST", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "fixed_json": {"search_depth": "advanced", "include_answer": True}, "health_check_json": {"query": "test"}, "timeout": 15},
        {"key": TAVILY_KEY_3, "endpoint_name": "Search (Key 3)", "url": "https://api.tavily.com/search", "method": "POST", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "fixed_json": {"search_depth": "advanced", "include_answer": True}, "health_check_json": {"query": "test"}, "timeout": 15},
        {"key": TAVILY_KEY_4, "endpoint_name": "Search (Key 4)", "url": "https://api.tavily.com/search", "method": "POST", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "fixed_json": {"search_depth": "advanced", "include_answer": True}, "health_check_json": {"query": "test"}, "timeout": 15}
    ],
    "WEATHERAPI": [
        {"key": WEATHERAPI_KEY, "endpoint_name": "Current Weather", "url": "http://api.weatherapi.com/v1/current.json", "method": "GET", "key_field": "key", "key_location": "param", "health_check_params": {"q": "London"}, "timeout": 5},
        {"key": WEATHERAPI_KEY, "endpoint_name": "Forecast", "url": "http://api.weatherapi.com/v1/forecast.json", "method": "GET", "key_field": "key", "key_location": "param", "fixed_params": {"days": 1}, "health_check_params": {"q": "London", "days": 1}, "timeout": 5}
    ],
    "WOLFRAMALPHA": [
        {"key": WOLFRAM_APP_ID_1, "endpoint_name": "Query (AppID 1)", "url": "http://api.wolframalpha.com/v2/query", "method": "GET", "key_field": "appid", "key_location": "param", "fixed_params": {"format": "plaintext", "output": "json"}, "health_check_params": {"input": "2+2"}, "timeout": 10},
        {"key": WOLFRAM_APP_ID_2, "endpoint_name": "Query (AppID 2)", "url": "http://api.wolframalpha.com/v2/query", "method": "GET", "key_field": "appid", "key_location": "param", "fixed_params": {"format": "plaintext", "output": "json"}, "health_check_params": {"input": "2+2"}, "timeout": 10},
        {"key": WOLFRAM_APP_ID_3, "endpoint_name": "Query (AppID 3)", "url": "http://api.wolframalpha.com/v2/query", "method": "GET", "key_field": "appid", "key_location": "param", "fixed_params": {"format": "plaintext", "output": "json"}, "health_check_params": {"input": "2+2"}, "timeout": 10}
    ],
    "CLOUDMERSIVE": [
        {"key": CLOUDMERSIVE_KEY, "endpoint_name": "Domain Check", "url": "https://api.cloudmersive.com/validate/domain/check", "method": "POST", "key_field": "Apikey", "key_location": "header", "health_check_json": {"domain": "example.com"}, "timeout": 10}
    ],
    "GREYNOISE": [
        {"key": GREYNOISE_KEY, "endpoint_name": "IP Analysis", "url": "https://api.greynoise.io/v3/community/", "method": "GET", "key_field": "key", "key_location": "header", "health_check_url_suffix": "1.1.1.1", "timeout": 10}
    ],
    "PULSEDIVE": [
        {"key": PULSEDIVE_KEY, "endpoint_name": "API Info", "url": "https://pulsedive.com/api/info.php", "method": "GET", "key_field": "key", "key_location": "param", "health_check_params": {"key": PULSEDIVE_KEY}, "timeout": 5},
        {"key": PULSEDIVE_KEY, "endpoint_name": "Analyze IP", "url": "https://pulsedive.com/api/v1/analyze", "method": "GET", "key_field": "key", "key_location": "param", "health_check_params": {"indicator": "8.8.8.8", "type": "ip"}, "timeout": 10},
        {"key": PULSEDIVE_KEY, "endpoint_name": "Explore", "url": "https://pulsedive.com/api/v1/explore", "method": "GET", "key_field": "key", "key_location": "param", "health_check_params": {"query": "type='ip'"}, "timeout": 10}
    ],
    "STORMGLASS": [
        {"key": STORMGLASS_KEY, "endpoint_name": "Weather Point", "url": "https://api.stormglass.io/v2/weather/point", "method": "GET", "key_field": "Authorization", "key_location": "header", "health_check_params": {"lat": 0, "lng": 0, "params": "airTemperature", "start": 0, "end": 0}, "timeout": 10}
    ],
    "LOGINRADIUS": [
        {"key": LOGINRADIUS_KEY, "endpoint_name": "Ping", "url": "https://api.loginradius.com/identity/v2/auth/ping", "method": "GET", "timeout": 5}
    ],
    "JSONBIN": [
        {"key": JSONBIN_KEY, "endpoint_name": "Bin Access", "url": "https://api.jsonbin.io/v3/b", "method": "GET", "key_field": "X-Master-Key", "key_location": "header", "health_check_url_suffix": "60c7b0e0f8c2a3b4c5d6e7f0", "timeout": 10},
        {"key": JSONBIN_KEY, "endpoint_name": "Bin Create", "url": "https://api.jsonbin.io/v3/b", "method": "POST", "key_field": "X-Master-Key", "key_location": "header", "health_check_json": {"record": {"test": "health"}}, "timeout": 10}
    ],
    "HUGGINGFACE": [
        {"key": HUGGINGFACE_KEY_1, "endpoint_name": "Models List (Key 1)", "url": "https://huggingface.co/api/models", "method": "GET", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "timeout": 10},
        {"key": HUGGINGFACE_KEY_1, "endpoint_name": "BERT Inference", "url": "https://api-inference.huggingface.co/models/bert-base-uncased", "method": "POST", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "health_check_json": {"inputs": "test"}, "timeout": 30},
        {"key": HUGGINGFACE_KEY_2, "endpoint_name": "Models List (Key 2)", "url": "https://huggingface.co/api/models", "method": "GET", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "timeout": 10},
        {"key": HUGGINGFACE_KEY_3, "endpoint_name": "Models List (Key 3)", "url": "https://huggingface.co/api/models", "method": "GET", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "timeout": 10},
        {"key": HUGGINGFACE_NEW_KEY, "endpoint_name": "Models List (New Key)", "url": "https://huggingface.co/api/models", "method": "GET", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "timeout": 10},
        {"key": HUGGINGFACE_NEW_KEY, "endpoint_name": "BERT Inference (New Key)", "url": "https://api-inference.huggingface.co/models/bert-base-uncased", "method": "POST", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "health_check_json": {"inputs": "test"}, "timeout": 30}
    ],
    "TWILIO": [
        {"key": (TWILIO_SID, TWILIO_SECRET), "endpoint_name": "Accounts", "url": "https://api.twilio.com/2010-04-01/Accounts", "method": "GET", "key_location": "auth_basic", "timeout": 10},
        {"key": (TWILIO_SID, TWILIO_SECRET), "endpoint_name": "Account Balance", "url": f"https://api.twilio.com/2010-04-01/Accounts/{TWILIO_SID}/Balance.json", "method": "GET", "key_location": "auth_basic", "timeout": 10}
    ],
    "ABSTRACTAPI": [
        {"key": ABSTRACTAPI_EMAIL_KEY_1, "endpoint_name": "Email Validation (Key 1)", "url": "https://emailvalidation.abstractapi.com/v1/", "method": "GET", "key_field": "api_key", "key_location": "param", "health_check_params": {"email": "test@example.com"}, "timeout": 10},
        {"key": ABSTRACTAPI_EMAIL_KEY_2, "endpoint_name": "Email Validation (Key 2)", "url": "https://emailvalidation.abstractapi.com/v1/", "method": "GET", "key_field": "api_key", "key_location": "param", "health_check_params": {"email": "test@example.com"}, "timeout": 10},
        {"key": ABSTRACTAPI_EMAIL_KEY_3, "endpoint_name": "Email Validation (Key 3)", "url": "https://emailvalidation.abstractapi.com/v1/", "method": "GET", "key_field": "api_key", "key_location": "param", "health_check_params": {"email": "test@example.com"}, "timeout": 10},
        {"key": ABSTRACTAPI_GENERIC_KEY, "endpoint_name": "Exchange Rates", "url": "https://exchange-rates.abstractapi.com/v1/", "method": "GET", "key_field": "api_key", "key_location": "param", "health_check_params": {"base": "USD"}, "timeout": 10},
        {"key": ABSTRACTAPI_GENERIC_KEY, "endpoint_name": "Holidays", "url": "https://holidays.abstractapi.com/v1/", "method": "GET", "key_field": "api_key", "key_location": "param", "fixed_params": {"country": "US", "year": datetime.now().year}, "health_check_params": {"country": "US", "year": datetime.now().year}, "timeout": 10},
        {"key": ABSTRACTAPI_GENERIC_KEY, "endpoint_name": "Phone Validation", "url": "https://phonevalidation.abstractapi.com/v1/", "method": "GET", "key_field": "api_key", "key_location": "param", "health_check_params": {"phone": "1234567890"}, "timeout": 10}
    ],
    "GEMINI_API": [ # Note: This is for the generic APIClient, GeminiApiClient class uses GEMINI_API_KEY directly
        {"key": GEMINI_API_KEY, "endpoint_name": "Generic Models Endpoint", "url": "https://generativelanguage.googleapis.com/v1beta/models", "method": "GET", "key_field": "key", "key_location": "param", "timeout": 10},
        {"key": GEMINI_API_KEY, "endpoint_name": "Embed Content", "url": "https://generativelanguage.googleapis.com/v1beta/models/embedding-001:embedContent", "method": "POST", "key_field": "key", "key_location": "param", "health_check_json": {"content": {"parts": [{"text": "test"}]}}, "timeout": 30},
        {"key": GEMINI_API_KEY, "endpoint_name": "Generate Content", "url": "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent", "method": "POST", "key_field": "key", "key_location": "param", "health_check_json": {"contents": [{"parts": [{"text": "hello"}]}]}, "timeout": 60}
    ],
    "GOOGLE_CUSTOM_SEARCH": [
        {"key": GOOGLE_API_KEYS[i], "endpoint_name": f"Search (Key {i+1}, CX {j+1})", "url": "https://www.googleapis.com/customsearch/v1", "method": "GET", "key_field": "key", "key_location": "param", "fixed_params": {"cx": GOOGLE_CX_LIST[j]}, "health_check_params": {"q": "test"}, "timeout": 10}
        for i in range(len(GOOGLE_API_KEYS)) for j in range(len(GOOGLE_CX_LIST))
    ],
    "RANDOMMER": [
        {"key": RANDOMMER_KEY, "endpoint_name": "Generate Phone", "url": "https://randommer.io/api/Phone/Generate", "method": "GET", "key_field": "X-Api-Key", "key_location": "header", "fixed_params": {"CountryCode": "US", "Quantity": 1}, "health_check_params": {"CountryCode": "US", "Quantity": 1}, "timeout": 10}
    ],
    "TOMORROW.IO": [
        {"key": TOMORROW_KEY, "endpoint_name": "Timelines", "url": "https://api.tomorrow.io/v4/timelines", "method": "POST", "key_field": "apikey", "key_location": "header", "health_check_json": {"location": "London", "fields": ["temperature"], "units": "metric", "timesteps": ["1h"]}, "timeout": 15}
    ],
    "OPENWEATHERMAP": [
        {"key": OPENWEATHER_API_KEY, "endpoint_name": "Current Weather", "url": "https://api.openweathermap.org/data/2.5/weather", "method": "GET", "key_field": "appid", "key_location": "param", "health_check_params": {"q": "London"}, "timeout": 5}
    ],
    "MOCKAROO": [
        {"key": MOCKAROO_KEY, "endpoint_name": "Data Generation", "url": "https://api.mockaroo.com/api/generate.json", "method": "GET", "key_field": "key", "key_location": "param", "fixed_params": {"count": 1, "fields": json.dumps([{"name": "id", "type": "Row Number"}])}, "health_check_params": {"count": 1, "fields": json.dumps([{"name": "id", "type": "Row Number"}])}, "timeout": 10},
        {"key": MOCKAROO_KEY, "endpoint_name": "Types", "url": "https://api.mockaroo.com/api/types", "method": "GET", "key_field": "key", "key_location": "param", "timeout": 10},
        {"key": MOCKAROO_KEY, "endpoint_name": "Schemas", "url": "https://api.mockaroo.com/api/schemas", "method": "GET", "key_field": "key", "key_location": "param", "timeout": 10},
        {"key": MOCKAROO_KEY, "endpoint_name": "Account", "url": "https://api.mockaroo.com/api/account", "method": "GET", "key_field": "key", "key_location": "param", "timeout": 10},
        {"key": MOCKAROO_KEY, "endpoint_name": "Generate CSV", "url": "https://api.mockaroo.com/api/generate.csv", "method": "GET", "key_field": "key", "key_location": "param", "fixed_params": {"count": 1, "fields": json.dumps([{"name": "id", "type": "Row Number"}])}, "health_check_params": {"count": 1, "fields": json.dumps([{"name": "id", "type": "Row Number"}])}, "timeout": 10},
        {"key": MOCKAROO_KEY, "endpoint_name": "Status", "url": "https://api.mockaroo.com/api/status", "method": "GET", "key_field": "key", "key_location": "param", "timeout": 10}
    ],
    "OPENPAGERANK": [
        {"key": OPENPAGERANK_KEY, "endpoint_name": "Domain Rank", "url": "https://openpagerank.com/api/v1.0/getPageRank", "method": "GET", "key_field": "API-OPR", "key_location": "header", "fixed_params": {"domains[]": "google.com"}, "timeout": 10}
    ],
    "RAPIDAPI": [
        {"key": RAPIDAPI_KEY, "endpoint_name": "Programming Joke", "url": "https://jokeapi-v2.p.rapidapi.com/joke/Programming", "method": "GET", "key_field": "X-RapidAPI-Key", "key_location": "header", "fixed_headers": {"X-RapidAPI-Host": "jokeapi-v2.p.rapidapi.com"}, "timeout": 10},
        {"key": RAPIDAPI_KEY, "endpoint_name": "Currency List Quotes", "url": "https://currency-exchange.p.rapidapi.com/listquotes", "method": "GET", "key_field": "X-RapidAPI-Key", "key_location": "header", "fixed_headers": {"X-RapidAPI-Host": "currency-exchange.p.rapidapi.com"}, "timeout": 10},
        {"key": RAPIDAPI_KEY, "endpoint_name": "Random Fact", "url": "https://random-facts2.p.rapidapi.com/getfact", "method": "GET", "key_field": "X-RapidAPI-Key", "key_location": "header", "fixed_headers": {"X-RapidAPI-Host": "random-facts2.p.rapidapi.com"}, "timeout": 10}
    ],
    "OCR_API": [ # Note: This is for the generic APIClient, OCRApiClient class uses OCR_API_KEY directly
        {"key": OCR_API_KEYS[0], "endpoint_name": "OCR Space (Key 1)", "url": "https://api.ocr.space/parse/image", "method": "POST", "key_field": "apikey", "key_location": "header", "health_check_json": {"base64Image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="}, "timeout": 30},
        {"key": OCR_API_KEYS[1], "endpoint_name": "OCR Space (Key 2)", "url": "https://api.ocr.space/parse/image", "method": "POST", "key_field": "apikey", "key_location": "header", "health_check_json": {"base64Image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="}, "timeout": 30},
        {"key": OCR_API_KEYS[2], "endpoint_name": "OCR Space (Key 3)", "url": "https://api.ocr.space/parse/image", "method": "POST", "key_field": "apikey", "key_location": "header", "health_check_json": {"base64Image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="}, "timeout": 30},
    ]
}

# ==== Quotas API (Définitions des limites pour le QuotaManager) ====
# Ces valeurs sont utilisées pour le suivi et la gestion des quotas d'utilisation.
# Mettre None pour indiquer une limite illimitée.
API_QUOTAS = {
    "gemini": {
        "monthly": 1000000, # Exemple: 1 million de tokens par mois
        "daily": 50000,    # Exemple: 50 000 tokens par jour
        "hourly": 5000,    # Exemple: 5 000 tokens par heure
        "rate_limit_per_sec": 5 # Exemple: 5 requêtes par seconde
    },
    "ocr_space": { # Nom interne utilisé par OCRApiClient
        "monthly": 25000,  # Exemple: 25 000 requêtes par mois (free tier)
        "daily": None,
        "hourly": None,
        "rate_limit_per_sec": 1 # Exemple: 1 requête par seconde
    },
    # Ajouter les quotas pour toutes les APIs listées dans API_CONFIG si elles ont des limites
    # Utiliser les valeurs du premier snippet si non spécifiées ici
    "APIFLASH": {"monthly": 100, "daily": 3, "hourly": 3},
    "DEEPSEEK": {"monthly": None, "hourly": 50},
    "CRAWLBASE": {"monthly": 1000, "daily": 33, "hourly": 1},
    "DETECTLANGUAGE": {"daily": 1000, "hourly": 41},
    "GUARDIAN": {"daily": 5000, "rate_limit_per_sec": 12},
    "IP2LOCATION": {"monthly": 50, "daily": 2, "hourly": 2},
    "SERPER": {"monthly": 2500, "daily": 83, "hourly": 3},
    "SHODAN": {"monthly": 100, "daily": 3, "hourly": 3},
    "TAVILY": {"monthly": 1000, "daily": 33, "hourly": 1},
    "WEATHERAPI": {"monthly": None},
    "WOLFRAMALPHA": {"monthly": None, "hourly": 67},
    "CLOUDMERSIVE": {"monthly": 25, "daily": 1, "hourly": 1},
    "GREYNOISE": {"monthly": 100, "daily": 3, "hourly": 3},
    "PULSEDIVE": {"monthly": 50, "daily": 2, "hourly": 2},
    "STORMGLASS": {"monthly": None},
    "LOGINRADIUS": {"monthly": 25000, "daily": 833, "hourly": 34},
    "JSONBIN": {"monthly": 10000, "daily": 333, "hourly": 13},
    "HUGGINGFACE": {"hourly": 100},
    "TWILIO": {"monthly": 15},
    "ABSTRACTAPI": {"monthly": 250, "rate_limit_per_sec": 1, "daily": 8, "hourly": 1},
    "MOCKAROO": {"monthly": 200, "daily": 7, "hourly": 1},
    "OPENPAGERANK": {"monthly": 1000, "daily": 33, "hourly": 1},
    "RAPIDAPI": {"monthly": None, "hourly": 30},
    "GOOGLE_CUSTOM_SEARCH": {"daily": 100, "hourly": 4},
    "RANDOMMER": {"monthly": 1000, "daily": 100, "hourly": 4},
    "TOMORROW.IO": {"monthly": None},
    "OPENWEATHERMAP": {"monthly": 1000000, "daily": 100, "hourly": 4},
    # "OCR_API" est déjà géré par "ocr_space" pour la classe dédiée.
    # Si d'autres clients OCR sont ajoutés via APIClient, ils devraient être listés ici.
}


# Modèle Gemini et ses paramètres
GEMINI_MODEL_NAME = "gemini-1.5-flash-latest" # Ou "gemini-pro"
GEMINI_TEMPERATURE = 0.7
GEMINI_TOP_P = 0.95
GEMINI_TOP_K = 40
GEMINI_MAX_OUTPUT_TOKENS = 2048
GEMINI_SAFETY_SETTINGS = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]


# ==== Bot Behavior Configuration ====
API_COOLDOWN_DURATION_SECONDS = 300 # Durée du cooldown en secondes (5 minutes)
API_ROTATION_INTERVAL_MINUTES = 10 # Intervalle de rotation des APIs en minutes

# Quota Burning Configuration
# Ratio de quota restant en dessous duquel le mode "brûlage" s'active (ex: 0.2 signifie 20% ou moins restant)
BURN_QUOTA_THRESHOLD_RATIO = 0.2
# Fenêtre de temps avant la réinitialisation du quota où le "brûlage" peut s'activer (en heures)
BURN_QUOTA_BEFORE_RESET_HOURS = 6

# Prompts pour l'auto-génération de contenu technique afin de "brûler" le quota.
# Ces prompts sont choisis aléatoirement pour les APIs en mode "burn".
AUTO_BURN_PROMPTS = {
    "gemini": [
        "Génère un script Python qui utilise une API REST pour récupérer des données et les stocker dans une base de données NoSQL.",
        "Explique en détail les principes de l'architecture microservices et comment ils se comparent aux architectures monolithiques.",
        "Décris les étapes pour déployer une application web Flask sur un serveur cloud (AWS EC2 ou Google Cloud Run).",
        "Écris un tutoriel sur l'utilisation de Docker Compose pour orchestrer plusieurs conteneurs (par exemple, une application web et une base de données).",
        "Analyse les avantages et les inconvénients des bases de données relationnelles vs non-relationnelles pour un projet de grande envergure.",
        "Propose un plan de test complet pour une application web critique, incluant tests unitaires, d'intégration, de bout en bout et de performance.",
        "Génère un exemple de code JavaScript pour une application React qui gère l'état avec Redux ou Context API.",
        "Explique le concept de CI/CD (intégration et livraison continues) et son importance dans le développement logiciel moderne.",
        "Décris les meilleures pratiques de sécurité pour une API RESTful, incluant l'authentification, l'autorisation et la protection contre les attaques courantes.",
        "Écris un algorithme de tri efficace (par exemple, Quicksort ou Mergesort) et explique sa complexité temporelle et spatiale."
    ],
    "ocr_space": [
        "Décris les défis techniques de l'OCR sur des documents manuscrits et les approches modernes pour les surmonter.",
        "Explique comment l'OCR peut être utilisée dans le domaine de la gestion documentaire ou de l'automatisation des processus métier.",
        "Quelles sont les métriques d'évaluation courantes pour les performances d'un système OCR ?",
        "Comment la pré-traitement d'image (bruit, binarisation, redressement) affecte-t-il la précision de l'OCR ?",
        "Compare les différentes technologies OCR disponibles sur le marché (cloud vs on-premise, open-source vs propriétaires)."
    ]
}

# ==== Paramètres de Sécurité et Filtrage ====
FORBIDDEN_WORDS = ["fuck", "shit", "bitch", "asshole", "pute", "enculé", "haine", "stupide", "détruire", "conflit", "malveillance", "idiot", "nul", "débile"]

# ==== IA PROMPTS (Exemples, à affiner selon tes besoins spécifiques pour chaque IA) ====
GENERAL_IA_PROMPT = """
Tu es une IA de l'année 2025, experte en information, programmation et résolution de problèmes.
Ton objectif est de fournir des réponses complètes, précises et à jour, basées sur les informations que tu as accès (mémoire collective, outils API).
Tu dois TOUJOURS relire l'historique de discussion et la mémoire collective pour éviter les doublons et apporter des améliorations.
Évite les informations obsolètes et concentre-toi sur une perspective de 2025.
Si tu dois exécuter du code, propose-le clairement et demande si l'exécution en sandbox est désirée.
N'hésite pas à croiser les informations de plusieurs sources.
"""

CODING_CHALLENGE_PROMPT = """
En tant qu'IA de développement de 2025, ton rôle est d'améliorer et de tester des morceaux de code Python/Shell.
Tu as accès à une sandbox sécurisée pour exécuter le code.
Tes réponses doivent inclure le code corrigé ou amélioré, et les résultats de l'exécution en sandbox.
Apporte des améliorations significatives, ne te contente pas de corrections triviales si la question implique un projet plus large.
Pense à l'efficacité du code et à l'optimisation des ressources.
Chaque version doit être une amélioration nette de la précédente, inédite.
Commence par un commentaire indiquant ce qui a été amélioré.
Le code doit être direct, lisible, et prêt à être utilisé.
"""

# ==== Tool Reformulation Configuration ====
TOOL_RETRY_MAX_ATTEMPTS = 3

import os
import json
import gzip
import shutil
import hashlib
import difflib
import re
import logging
import io
import contextlib
import fcntl
import traceback
import asyncio
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Union, List, Dict

# Import des constantes depuis config.py
from config import BASE_DIR, MAX_FILE_SIZE, ERROR_LOG_PATH, MAX_CACHE_SIZE, FORBIDDEN_WORDS

# Configure logging pour tout le script
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Global lock for file operations to ensure atomic writes and prevent race conditions
_file_lock = None 

def set_file_lock(lock_instance: asyncio.Lock):
    """
    Permet d'injecter l'instance d'asyncio.Lock après l'initialisation de l'event loop.
    Ceci est crucial pour la gestion des accès concurrents aux fichiers.
    """
    global _file_lock
    _file_lock = lock_instance

def _acquire_file_lock_sync(f):
    """
    Acquires an exclusive lock on a file using fcntl (Unix-like systems).
    This prevents other processes from writing to the file simultaneously.
    """
    try:
        if os.name == 'posix' and fcntl:
            fcntl.flock(f.fileno(), fcntl.LOCK_EX)
    except Exception as e:
        logging.warning(f"Could not acquire file lock: {e}")

def _release_file_lock_sync(f):
    """
    Releases an exclusive lock on a file using fcntl (Unix-like systems).
    """
    try:
        if os.name == 'posix' and fcntl:
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)
    except Exception as e:
        logging.warning(f"Could not release file lock: {e}")

def get_user_dir(uid: Union[int, str]) -> Path:
    """
    Retourne le répertoire de sauvegarde spécifique à un utilisateur, le créant si nécessaire.
    Chaque utilisateur (ou groupe privé) a son propre répertoire pour stocker les données.
    """
    p = BASE_DIR / str(uid)
    p.mkdir(parents=True, exist_ok=True)
    return p

def rotate_log_if_needed(path: Path):
    """
    Fait pivoter le fichier log (ou tout fichier de données) si sa taille dépasse MAX_FILE_SIZE.
    Un nouveau fichier est créé avec un horodatage pour l'archivage, et le fichier original est réinitialisé.
    """
    if path.exists() and path.stat().st_size > MAX_FILE_SIZE:
        timestamp = int(datetime.now().timestamp())
        # Renomme le fichier existant pour l'archiver
        new_path = path.with_suffix(f".old_{timestamp}{path.suffix}.gz")
        try:
            # Compresse et déplace l'ancien fichier
            with open(path, "rb") as f_in, gzip.open(new_path, "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)
            path.unlink() # Supprime l'original
            logging.info(f"Log rotated and compressed: {path} -> {new_path}")
        except Exception as e:
            log_message(f"[Rotation log] Erreur lors de la compression/rotation de {path}: {e}\n{traceback.format_exc()}", level="error")
        # Le fichier sera recréé vide lors de la prochaine sauvegarde

def compress_if_large(path: Path):
    """
    Compresse le fichier s'il dépasse 1MB après une écriture, puis le renomme pour garder le nom original.
    Ceci est une mesure de gestion de l'espace disque pour les fichiers de données.
    """
    try:
        # Vérifie si le fichier existe et si sa taille est supérieure à 1MB
        if path.exists() and path.stat().st_size > 1_000_000:
            gz_path = path.with_suffix(path.suffix + ".gz") # Chemin temporaire pour le fichier compressé
            with open(path, "rb") as f_in, gzip.open(gz_path, "wb") as f_out:
                shutil.copyfileobj(f_in, f_out) # Copie et compresse
            path.unlink() # Supprime le fichier original non compressé
            # Renomme le fichier .gz pour qu'il ait le nom original, simulant une compression "in-place"
            gz_path.rename(path) 
            logging.info(f"File compressed: {path}")
    except Exception as e:
        log_message(f"[Compression auto] Erreur : {e}\n{traceback.format_exc()}", level="error")

async def load_json(filepath: Path, default_value: Union[Dict, List] = None) -> Union[Dict, List]:
    """
    Charge un fichier JSON de manière asynchrone.
    Retourne `default_value` si le fichier n'existe pas, est vide ou est corrompu.
    Utilise un verrou global pour la sécurité des accès concurrents.
    """
    if default_value is None:
        default_value = {} # Default to empty dict if not specified

    if _file_lock:
        async with _file_lock:
            return _load_json_sync(filepath, default_value)
    else:
        # Fallback for synchronous loading if lock is not set (e.g., during early initialization)
        return _load_json_sync(filepath, default_value)

def _load_json_sync(filepath: Path, default_value: Union[Dict, List]) -> Union[Dict, List]:
    """
    Charge un fichier JSON de manière synchrone avec verrouillage de fichier.
    """
    if not filepath.exists():
        logging.info(f"Fichier non trouvé: {filepath}. Création d'un fichier vide.")
        _save_json_sync(filepath, default_value) # Crée un fichier vide avec la valeur par défaut
        return default_value
    
    # Ouvre le fichier en mode lecture/écriture pour pouvoir le vider en cas de corruption
    with open(filepath, 'r+', encoding='utf-8') as f:
        _acquire_file_lock_sync(f) # Acquiert le verrou avant de lire
        try:
            f.seek(0) # Se positionne au début du fichier
            content = f.read()
            if not content:
                logging.warning(f"Fichier vide: {filepath}. Retourne la valeur par défaut.")
                return default_value
            return json.loads(content)
        except json.JSONDecodeError as e:
            logging.error(f"Erreur de décodage JSON dans {filepath}: {e}. Le fichier sera réinitialisé.")
            # Si le fichier est corrompu, le réinitialise avec la valeur par défaut
            f.seek(0)
            f.truncate()
            json.dump(default_value, f, indent=4, ensure_ascii=False)
            return default_value
        except Exception as e:
            logging.error(f"Erreur inattendue lors du chargement de {filepath}: {e}. Retourne la valeur par défaut.")
            return default_value
        finally:
            _release_file_lock_sync(f) # Relâche le verrou

async def save_json(filepath: Path, data: Union[Dict, List]):
    """
    Sauvegarde les données dans un fichier JSON de manière asynchrone et atomique,
    avec rotation et compression si nécessaire.
    Utilise un verrou global pour la sécurité des accès concurrents.
    """
    if _file_lock:
        async with _file_lock:
            _save_json_sync(filepath, data)
    else:
        # Fallback for synchronous saving if lock is not set
        _save_json_sync(filepath, data)

def _save_json_sync(filepath: Path, data: Union[Dict, List]):
    """
    Sauvegarde les données dans un fichier JSON de manière synchrone et atomique,
    avec verrouillage de fichier.
    """
    rotate_log_if_needed(filepath) # Effectue la rotation avant la sauvegarde
    temp_filepath = filepath.with_suffix(filepath.suffix + ".tmp") # Utilise un fichier temporaire pour l'atomicité
    try:
        with temp_filepath.open('w', encoding='utf-8') as f:
            _acquire_file_lock_sync(f) # Acquiert le verrou avant d'écrire
            try:
                json.dump(data, f, indent=4, ensure_ascii=False)
            finally:
                _release_file_lock_sync(f) # Relâche le verrou
        os.replace(temp_filepath, filepath) # Remplace l'ancien fichier par le nouveau de manière atomique
        compress_if_large(filepath) # Compresse le fichier après la sauvegarde si nécessaire
    except Exception as e:
        logging.error(f"Erreur lors de la sauvegarde atomique de {filepath}: {e}")
        if temp_filepath.exists():
            os.remove(temp_filepath) # Nettoie le fichier temporaire en cas d'erreur

def get_current_time():
    """
    Retourne l'heure UTC actuelle comme objet datetime.
    """
    return datetime.now(timezone.utc) # Utilise datetime.now(timezone.utc) pour être explicite sur UTC

def format_datetime(dt_obj: datetime) -> str:
    """
    Formate un objet datetime en chaîne de caractères lisible (UTC).
    """
    return dt_obj.strftime("%Y-%m-%d %H:%M:%S UTC")

def is_within_time_window(target_time: datetime, start_minutes_before: int, end_minutes_after: int) -> bool:
    """
    Vérifie si l'heure actuelle est dans une fenêtre de temps spécifiée autour d'une heure cible.
    """
    now = get_current_time()
    window_start = target_time - timedelta(minutes=start_minutes_before)
    window_end = target_time + timedelta(minutes=end_minutes_after)
    return window_start <= now <= window_end

def log_message(message: str, level: str = "info"):
    """
    Log un message avec un niveau spécifié.
    Les messages d'erreur critiques sont dirigés vers un fichier de log d'erreurs séparé.
    """
    if level == "error":
        error_logger = logging.getLogger("erreurs_api")
        if not error_logger.handlers: # Configurer le logger d'erreurs si pas déjà fait
            eh = logging.FileHandler(ERROR_LOG_PATH, encoding="utf-8")
            eh.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"))
            error_logger.addHandler(eh)
            error_logger.setLevel(logging.ERROR)
        error_logger.error(message)
    else:
        # Utilise le logger par défaut pour les autres niveaux
        if level == "info":
            logging.info(message)
        elif level == "warning":
            logging.warning(message)
        elif level == "debug":
            logging.debug(message)
        else:
            logging.debug(message) # Fallback pour les niveaux non reconnus

def neutralize_urls(text: str) -> str:
    """
    Remplace les URLs dans le texte par un placeholder pour prévenir les problèmes de lien direct
    et la fuite d'informations sensibles dans les logs ou la mémoire.
    """
    # Remplace http(s):// par hxxp(s)://
    text = re.sub(r"https?://", lambda m: m.group(0).replace("t", "x", 1), text)
    # Remplace www. par wxx.
    text = re.sub(r"www\.", "wxx.", text)
    # Remplace .com, .net, .org par [.]com, [.]net, [.]org
    text = re.sub(r"\.com", "[.]com", text)
    text = re.sub(r"\.net", "[.]net", text)
    text = re.sub(r"\.org", "[.]org", text)
    return text

def clean_html_tags(text: str) -> str:
    """
    Supprime les balises HTML d'une chaîne de caractères en utilisant une expression régulière.
    """
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def hash_text(t: str) -> str:
    """
    Calcule le hachage SHA256 d'une chaîne de caractères.
    """
    return hashlib.sha256(t.encode('utf-8')).hexdigest()

def extract_keywords(text: str) -> List[str]:
    """
    Extrait les mots-clés les plus fréquents d'un texte.
    Retourne une liste des 5 mots les plus fréquents (de 4 caractères ou plus).
    """
    # Trouve tous les mots de 4 caractères ou plus (incluant les accents)
    words = re.findall(r'\b[a-zA-Zéèêôàùçîïœ]{4,}\b', text.lower())
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    # Trie les mots par fréquence décroissante
    keywords = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [w for w,_ in keywords[:5]] # Retourne seulement les mots

def tag_conversation(text: str) -> str:
    """
    Génère un tag de conversation basé sur les mots-clés extraits du texte.
    """
    words = extract_keywords(text)
    return f"#tags : {', '.join(words)}"

def unique_preserve_order(seq: List[Any]) -> List[Any]:
    """
    Élimine les doublons d'une séquence tout en préservant l'ordre original des éléments.
    """
    seen = set()
    result = []
    for item in seq:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def similar(a: str, b: str) -> float:
    """
    Calcule la similarité entre deux chaînes de caractères en utilisant le ratio de SequenceMatcher.
    Retourne un ratio de 0 à 1, où 1 indique une identité parfaite.
    """
    return difflib.SequenceMatcher(None, a.lower(), b.lower()).ratio()

def is_code(text: str) -> bool:
    """
    Détecte si le texte ressemble à du code (Python ou autre) en cherchant des motifs courants.
    """
    return bool(re.search(r"^\s*(def |class |import |print\()", text, re.MULTILINE)) or text.strip().startswith("```")

def is_python_code_block(text: str) -> bool:
    """
    Détecte si le texte est un bloc de code Python formaté en Markdown.
    """
    return text.strip().startswith("```python") and text.strip().endswith("```")

import time
import httpx
import json
import base64
import asyncio
import re # Importation ajoutée pour la validation IP dans ShodanClient
from typing import Dict, Any, Optional, Union, List, Tuple

# Import des constantes et fonctions utilitaires depuis les modules locaux
from config import API_CONFIG, ENDPOINT_HEALTH_FILE, OCR_API_KEYS, GEMINI_API_KEY # Assurez-vous que GEMINI_API_KEY est importé
from utils import load_json, save_json, get_current_time, format_datetime, log_message, neutralize_urls

class EndpointHealthManager:
    """
    Gère la santé des endpoints API et sélectionne le meilleur endpoint disponible
    en fonction de critères comme la latence, le taux de succès et le nombre d'erreurs.
    C'est un singleton pour s'assurer qu'il n'y a qu'une seule instance de gestionnaire de santé.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """Implémente le patron de conception Singleton."""
        if cls._instance is None:
            cls._instance = super(cls, cls).__new__(cls)
            cls._instance._initialized = False # Indicateur pour l'initialisation asynchrone
        return cls._instance

    def __init__(self):
        """Initialise le gestionnaire. L'initialisation réelle se fait via `init_manager`."""
        if self._initialized:
            return
        self.health_status = {}
        # `_initialized` est géré par `init_manager` pour les opérations asynchrones

    async def init_manager(self):
        """
        Initialise le gestionnaire de santé de manière asynchrone.
        Charge l'état de santé persistant et s'assure que tous les endpoints sont suivis.
        """
        if not self._initialized:
            self.health_status = await load_json(ENDPOINT_HEALTH_FILE, {})
            self._initialize_health_status()
            self._initialized = True
            log_message("Gestionnaire de santé des endpoints initialisé.")

    def _initialize_health_status(self):
        """
        Initialise ou met à jour le statut de santé pour tous les endpoints configurés dans `API_CONFIG`.
        Ajoute les nouveaux endpoints et s'assure que toutes les clés nécessaires sont présentes.
        """
        updated = False
        for service_name, endpoints_config in API_CONFIG.items():
            if service_name not in self.health_status:
                self.health_status[service_name] = {}
                updated = True
            for endpoint_config in endpoints_config:
                # Crée une clé unique pour chaque endpoint en combinant son nom et sa clé API
                endpoint_key = f"{endpoint_config['endpoint_name']}-{str(endpoint_config['key'])}"
                if endpoint_key not in self.health_status[service_name]:
                    self.health_status[service_name][endpoint_key] = {
                        "latency": 0.0,
                        "success_rate": 1.0, # Commence avec un taux de succès parfait (sain)
                        "last_checked": None,
                        "error_count": 0,
                        "total_checks": 0,
                        "is_healthy": True # Présumé sain au début
                    }
                    updated = True
        if updated:
            # Sauvegarde l'état mis à jour de manière asynchrone en tâche de fond
            asyncio.create_task(save_json(ENDPOINT_HEALTH_FILE, self.health_status))
            log_message("Statut de santé des endpoints initialisé/mis à jour.")

    async def run_health_check_for_service(self, service_name: str):
        """
        Exécute des checks de santé pour tous les endpoints d'un service donné.
        Tente d'appeler l'endpoint avec des paramètres de santé prédéfinis.
        """
        endpoints_config = API_CONFIG.get(service_name)
        if not endpoints_config:
            log_message(f"Aucune configuration d'endpoint trouvée pour le service: {service_name}", level="warning")
            return

        log_message(f"Lancement du health check pour le service: {service_name}")
        for endpoint_config in endpoints_config:
            endpoint_key = f"{endpoint_config['endpoint_name']}-{str(endpoint_config['key'])}"
            start_time = time.monotonic()
            success = False
            try:
                request_method = endpoint_config.get("method", "GET")
                url = endpoint_config["url"]
                
                # Prépare les paramètres/données pour le health check
                params = endpoint_config.get("health_check_params", endpoint_config.get("fixed_params", {})).copy()
                json_data = endpoint_config.get("health_check_json", endpoint_config.get("fixed_json", {})).copy()
                headers = endpoint_config.get("fixed_headers", {}).copy()
                auth = None # Pour l'authentification de base (Basic Auth)
                
                check_timeout = endpoint_config.get("timeout", 5) # Timeout spécifique pour le health check

                # Ajoute un suffixe à l'URL si spécifié (ex: pour les APIs basées sur des chemins d'accès)
                if "health_check_url_suffix" in endpoint_config:
                    url += endpoint_config["health_check_url_suffix"]

                # Gère l'insertion de la clé API selon sa localisation (paramètre, en-tête, Basic Auth)
                key_field = endpoint_config.get("key_field")
                key_location = endpoint_config.get("key_location")
                key_prefix = endpoint_config.get("key_prefix", "") # Préfixe pour les clés dans les en-têtes (ex: "Bearer ")
                api_key = endpoint_config["key"]

                if key_field and key_location:
                    if key_location == "param":
                        params[key_field] = api_key
                    elif key_location == "header":
                        headers[key_field] = f"{key_prefix}{api_key}"
                    elif key_location == "auth_basic":
                        if isinstance(api_key, tuple) and len(api_key) == 2:
                            auth = httpx.BasicAuth(api_key[0], api_key[1])
                        else:
                            log_message(f"Clé API pour auth_basic non valide pour {service_name}:{endpoint_key}", level="error")
                            success = False
                            continue # Passe à l'endpoint suivant

                async with httpx.AsyncClient(timeout=check_timeout) as client:
                    response = await client.request(request_method, url, params=params, headers=headers, json=json_data, auth=auth)
                    response.raise_for_status() # Lève une exception pour les codes d'état HTTP 4xx/5xx
                    success = True
            except httpx.HTTPStatusError as e:
                log_level = "warning"
                # Les codes 4xx (sauf 429 - Too Many Requests) indiquent souvent une erreur client
                # (clé invalide, paramètre manquant) qui ne se résoudra pas avec un réessai
                # et n'indique pas forcément un problème de "santé" du service lui-même.
                # Nous les loguons en debug pour ne pas surcharger les logs.
                if 400 <= e.response.status_code < 500 and e.response.status_code != 429:
                    log_level = "debug" 
                log_message(f"Health check pour {endpoint_key} ({service_name}) a échoué (HTTP {e.response.status_code}): {e.response.text}", level=log_level)
                success = False
            except httpx.RequestError as e:
                # Erreurs réseau (connexion, timeout, DNS, etc.)
                log_message(f"Health check pour {endpoint_key} ({service_name}) a échoué (Réseau): {e}", level="warning")
                success = False
            except Exception as e:
                # Autres erreurs inattendues
                log_message(f"Health check pour {endpoint_key} ({service_name}) a échoué (Inattendu): {e}", level="error")
                success = False
            finally:
                latency = time.monotonic() - start_time # Calcule la latence du check
                self.update_endpoint_health(service_name, endpoint_key, success, latency)
        log_message(f"Health check terminé pour le service: {service_name}")

    def update_endpoint_health(self, service_name: str, endpoint_key: str, success: bool, latency: float):
        """
        Met à jour le statut de santé d'un endpoint spécifique.
        Utilise une moyenne glissante pour le taux de succès et la latence.
        """
        # S'assure que la structure de données existe
        if service_name not in self.health_status:
            self.health_status[service_name] = {}
        if endpoint_key not in self.health_status[service_name]:
            self.health_status[service_name][endpoint_key] = {
                "latency": 0.0,
                "success_rate": 1.0,
                "last_checked": None,
                "error_count": 0,
                "total_checks": 0,
                "is_healthy": True
            }

        status = self.health_status[service_name][endpoint_key]
        status["total_checks"] += 1
        status["last_checked"] = format_datetime(get_current_time())

        alpha = 0.1 # Facteur de lissage pour les moyennes glissantes (0.1 signifie 10% de la nouvelle valeur, 90% de l'ancienne)
        if success:
            status["error_count"] = max(0, status["error_count"] - 1) # Diminue le compteur d'erreurs en cas de succès
            status["success_rate"] = status["success_rate"] * (1 - alpha) + 1.0 * alpha # Augmente le taux de succès
            status["latency"] = status["latency"] * (1 - alpha) + latency * alpha # Met à jour la latence
        else:
            status["error_count"] += 1 # Incrémente le compteur d'erreurs
            status["success_rate"] = status["success_rate"] * (1 - alpha) + 0.0 * alpha # Diminue le taux de succès
            # Si échec, pénalise la latence pour rendre l'endpoint moins attrayant (valeur arbitraire élevée)
            status["latency"] = status["latency"] * (1 - alpha) + 10.0 * alpha 

        # Détermine si l'endpoint est sain basé sur le nombre d'erreurs consécutives ou le taux de succès
        if status["error_count"] >= 3 or status["success_rate"] < 0.5:
            status["is_healthy"] = False
        else:
            status["is_healthy"] = True
        
        # Sauvegarde l'état mis à jour de manière asynchrone
        asyncio.create_task(save_json(ENDPOINT_HEALTH_FILE, self.health_status))
        log_message(f"Santé de {service_name}:{endpoint_key} mise à jour: Succès: {success}, Latence: {latency:.2f}s, Taux Succès: {status['success_rate']:.2f}, Sain: {status['is_healthy']}", level="debug" if not status["is_healthy"] else "info")

    def get_best_endpoint(self, service_name: str) -> Optional[Dict]:
        """
        Sélectionne le meilleur endpoint pour un service donné basé sur son statut de santé.
        Priorise les endpoints sains, puis les moins mauvais en cas d'absence d'endpoints sains.
        """
        service_health = self.health_status.get(service_name)
        if not service_health:
            log_message(f"Aucune donnée de santé pour le service {service_name}. Retourne None.", level="warning")
            return None

        best_endpoint_key = None
        best_score = -float('inf')

        # Filtre les endpoints actuellement considérés comme sains
        healthy_endpoints = [
            (key, status) for key, status in service_health.items() if status["is_healthy"]
        ]

        if not healthy_endpoints:
            log_message(f"Aucun endpoint sain pour le service {service_name}. Tentative de sélection d'un endpoint non sain.", level="warning")
            all_endpoints = service_health.items()
            if not all_endpoints: 
                return None # Aucun endpoint du tout
            
            # Si aucun endpoint sain, choisit le "moins mauvais" : moins d'erreurs, meilleure latence
            sorted_endpoints = sorted(all_endpoints, key=lambda item: (item[1]["error_count"], item[1]["latency"]))
            best_endpoint_key = sorted_endpoints[0][0]
            log_message(f"Fallback: Endpoint {best_endpoint_key} sélectionné pour {service_name} (non sain).", level="warning")
        else:
            # Calcule un score pour chaque endpoint sain pour choisir le meilleur
            for endpoint_key, status in healthy_endpoints:
                # Score = (Taux de succès * 100) - (Latence * 10) - (Compteur d'erreurs * 5)
                # Favorise le succès, pénalise la latence et les erreurs
                score = (status["success_rate"] * 100) - (status["latency"] * 10) - (status["error_count"] * 5)
                if score > best_score:
                    best_score = score
                    best_endpoint_key = endpoint_key
            log_message(f"Meilleur endpoint sélectionné pour {service_name}: {best_endpoint_key} (Score: {best_score:.2f})")

        if best_endpoint_key:
            # Une fois la clé du meilleur endpoint trouvée, on récupère sa configuration complète
            # depuis `API_CONFIG` pour l'utiliser dans la requête.
            for endpoint_config in API_CONFIG.get(service_name, []):
                current_endpoint_key = f"{endpoint_config['endpoint_name']}-{str(endpoint_config['key'])}"
                if current_endpoint_key == best_endpoint_key:
                    return endpoint_config
        return None # Aucun endpoint approprié trouvé

class APIClient:
    """
    Classe de base pour tous les clients API.
    Elle gère la sélection dynamique d'endpoints, les réessais en cas d'échec
    et l'intégration avec le gestionnaire de santé des endpoints.
    """
    def __init__(self, name: str, endpoint_health_manager: EndpointHealthManager):
        self.name = name
        self.endpoints_config = API_CONFIG.get(name, []) # Récupère la config des endpoints pour cette API
        self.endpoint_health_manager = endpoint_health_manager
        if not self.endpoints_config:
            log_message(f"Client API {self.name} initialisé sans configuration d'endpoint.", level="error")

    async def _make_request(self, params: Optional[Dict] = None, headers: Optional[Dict] = None, 
                            json_data: Optional[Dict] = None, timeout: Optional[int] = None, 
                            max_retries: int = 3, initial_delay: float = 1.0, 
                            url: Optional[str] = None, method: Optional[str] = None, 
                            key_field: Optional[str] = None, key_location: Optional[str] = None, 
                            api_key: Optional[Union[str, Tuple[str, str]]] = None, 
                            fixed_params: Optional[Dict] = None, fixed_headers: Optional[Dict] = None, 
                            fixed_json: Optional[Dict] = None) -> Optional[Union[Dict, str, bytes]]:
        """
        Méthode interne pour effectuer les requêtes HTTP en utilisant le meilleur endpoint avec réessais.
        
        Args:
            params (Dict, optional): Paramètres de requête à ajouter à l'URL.
            headers (Dict, optional): En-têtes HTTP supplémentaires.
            json_data (Dict, optional): Données JSON à envoyer dans le corps de la requête (pour POST/PUT).
            timeout (int, optional): Timeout pour la requête en secondes.
            max_retries (int): Nombre maximal de tentatives en cas d'échec.
            initial_delay (float): Délai initial entre les réessais (exponentiel).
            url (str, optional): URL spécifique à utiliser (si non basé sur un endpoint configuré).
            method (str, optional): Méthode HTTP (GET, POST, etc.).
            key_field (str, optional): Nom du champ pour la clé API.
            key_location (str, optional): Où placer la clé API ('param', 'header', 'auth_basic').
            api_key (Union[str, Tuple[str, str]], optional): Clé API à utiliser.
            fixed_params (Dict, optional): Paramètres fixes définis dans la configuration de l'endpoint.
            fixed_headers (Dict, optional): En-têtes fixes définis dans la configuration de l'endpoint.
            fixed_json (Dict, optional): Données JSON fixes définies dans la configuration de l'endpoint.

        Returns:
            Union[Dict, str, bytes, None]: La réponse de l'API (JSON décodé, texte brut, ou bytes pour les images),
                                          ou un dictionnaire d'erreur en cas d'échec.
        """
        
        selected_endpoint_config = None
        endpoint_key_for_health = "Dynamic" # Clé par défaut pour les requêtes dynamiques (non configurées)

        if url and method: # Si l'URL et la méthode sont fournies directement (requête dynamique)
            selected_endpoint_config = {
                "url": url,
                "method": method,
                "key_field": key_field,
                "key_location": key_location,
                "key": api_key,
                "fixed_params": fixed_params if fixed_params is not None else {},
                "fixed_headers": fixed_headers if fixed_headers is not None else {},
                "fixed_json": fixed_json if fixed_json is not None else {},
                "endpoint_name": "Dynamic", # Nom générique pour les endpoints dynamiques
                "timeout": timeout if timeout is not None else 30
            }
            if api_key:
                # Crée une clé de santé unique pour les requêtes dynamiques avec clé API
                endpoint_key_for_health = f"Dynamic-{str(api_key)}"
            log_message(f"Requête dynamique pour {self.name} vers {url}")
        else: # Sélectionne le meilleur endpoint configuré via le gestionnaire de santé
            selected_endpoint_config = self.endpoint_health_manager.get_best_endpoint(self.name)
            if not selected_endpoint_config:
                log_message(f"Aucun endpoint sain ou disponible pour {self.name}.", level="error")
                return {"error": True, "message": f"Aucun endpoint sain ou disponible pour {self.name}."}
            # Construit la clé de santé pour l'endpoint sélectionné
            endpoint_key_for_health = f"{selected_endpoint_config['endpoint_name']}-{str(selected_endpoint_config['key'])}"
            log_message(f"Endpoint sélectionné pour {self.name}: {selected_endpoint_config['endpoint_name']}")
            # Utilise le timeout de la config de l'endpoint si non spécifié
            timeout = timeout if timeout is not None else selected_endpoint_config.get("timeout", 30)

        url_to_use = selected_endpoint_config["url"]
        method_to_use = selected_endpoint_config["method"]

        # Initialise les paramètres, en-têtes et données JSON avec les valeurs fixes de la config
        request_params = selected_endpoint_config.get("fixed_params", {}).copy()
        request_headers = selected_endpoint_config.get("fixed_headers", {}).copy()
        request_json_data = selected_endpoint_config.get("fixed_json", {}).copy()
        auth = None # Pour l'authentification de base

        # Fusionne les paramètres/en-têtes/données JSON fournis avec les valeurs fixes
        if params:
            request_params.update(params)
        if headers:
            request_headers.update(headers)
        if json_data:
            request_json_data.update(json_data)

        # Gère l'insertion de la clé API pour la requête
        key_field_to_use = selected_endpoint_config.get("key_field")
        key_location_to_use = selected_endpoint_config.get("key_location")
        key_prefix = selected_endpoint_config.get("key_prefix", "")
        api_key_to_use = selected_endpoint_config["key"]

        if key_field_to_use and key_location_to_use:
            if key_location_to_use == "param":
                request_params[key_field_to_use] = api_key_to_use
            elif key_location_to_use == "header":
                request_headers[key_field_to_use] = f"{key_prefix}{api_key_to_use}"
            elif key_location_to_use == "auth_basic":
                if isinstance(api_key_to_use, tuple) and len(api_key_to_use) == 2:
                    auth = httpx.BasicAuth(api_key_to_use[0], api_key_to_use[1])
                else:
                    log_message(f"Clé API pour auth_basic non valide pour {self.name}:{endpoint_key_for_health}", level="error")
                    # Marque l'endpoint comme non sain et retourne une erreur
                    self.endpoint_health_manager.update_endpoint_health(self.name, endpoint_key_for_health, False, 0.0)
                    return {"error": True, "message": "Configuration d'authentification basique invalide."}

        current_delay = initial_delay # Délai initial pour les réessais
        for attempt in range(max_retries):
            start_time = time.monotonic()
            success = False
            try:
                async with httpx.AsyncClient(timeout=timeout) as client:
                    response = await client.request(method_to_use, url_to_use, params=request_params, headers=request_headers, json=request_json_data, auth=auth)
                    response.raise_for_status() # Lève une exception pour les codes d'état HTTP 4xx/5xx
                    success = True
                    
                    content_type = response.headers.get("Content-Type", "").lower()
                    if "application/json" in content_type:
                        try:
                            return response.json() # Tente de décoder la réponse JSON
                        except json.JSONDecodeError:
                            log_message(f"API {self.name} réponse non JSON valide (tentative {attempt+1}/{max_retries}): {response.text[:200]}...", level="warning")
                            if attempt < max_retries - 1: # Si ce n'est pas la dernière tentative, réessaie
                                await asyncio.sleep(current_delay)
                                current_delay *= 2 # Augmente le délai de manière exponentielle
                                continue
                            return {"error": True, "message": "Réponse API non JSON valide.", "raw_response": response.text}
                    else:
                        log_message(f"API {self.name} a renvoyé un Content-Type non JSON: {content_type}", level="info")
                        return response.content # Retourne le contenu brut (ex: pour les images)

            except httpx.HTTPStatusError as e:
                log_message(f"API {self.name} erreur HTTP (tentative {attempt+1}/{max_retries}): {e.response.status_code} - {e.response.text}", level="warning")
                # Ne pas réessayer pour les erreurs client (4xx) sauf 429 (Too Many Requests)
                if 400 <= e.response.status_code < 500 and e.response.status_code != 429:
                    log_message(f"API {self.name}: Erreur client {e.response.status_code}, pas de réessai.", level="error")
                    self.endpoint_health_manager.update_endpoint_health(self.name, endpoint_key_for_health, False, e.response.elapsed.total_seconds())
                    return {"error": True, "status_code": e.response.status_code, "message": e.response.text}
                
                if attempt < max_retries - 1:
                    log_message(f"API {self.name}: Réessai dans {current_delay:.2f}s...", level="info")
                    await asyncio.sleep(current_delay)
                    current_delay *= 2
            except httpx.RequestError as e:
                log_message(f"API {self.name} erreur de requête (tentative {attempt+1}/{max_retries}): {e}", level="warning")
                if attempt < max_retries - 1:
                    log_message(f"API {self.name}: Réessai dans {current_delay:.2f}s...", level="info")
                    await asyncio.sleep(current_delay)
                    current_delay *= 2
            except Exception as e:
                log_message(f"API {self.name} erreur inattendue (tentative {attempt+1}/{max_retries}): {e}", level="error")
                self.endpoint_health_manager.update_endpoint_health(self.name, endpoint_key_for_health, False, time.monotonic() - start_time)
                return {"error": True, "message": str(e)}
            finally:
                # Met à jour la santé de l'endpoint même en cas d'échec pour la sélection future
                if not success:
                    latency = time.monotonic() - start_time
                    self.endpoint_health_manager.update_endpoint_health(self.name, endpoint_key_for_health, False, latency)
        
        log_message(f"API {self.name}: Toutes les tentatives ont échoué après {max_retries} réessais.", level="error")
        return {"error": True, "message": f"Échec de la requête après {max_retries} tentatives."}

    async def query(self, *args, **kwargs) -> Any:
        """
        Méthode abstraite pour interroger l'API.
        Doit être implémentée par chaque sous-classe de client API.
        """
        raise NotImplementedError("La méthode query doit être implémentée par les sous-classes.")

# Instancier le gestionnaire de santé des endpoints (sera initialisé dans main.py)
endpoint_health_manager = EndpointHealthManager()

def set_endpoint_health_manager_global(manager: EndpointHealthManager):
    """
    Permet d'injecter l'instance du gestionnaire de santé des endpoints.
    Ceci est utilisé pour s'assurer que tous les clients API utilisent la même instance.
    """
    global endpoint_health_manager
    endpoint_health_manager = manager

# --- Clients API Spécifiques ---
# Chaque classe de client API hérite de `APIClient` et implémente la méthode `query`
# pour interagir avec une API spécifique.

class DeepSeekClient(APIClient):
    def __init__(self):
        super().__init__("DEEPSEEK", endpoint_health_manager)

    async def query(self, prompt: str, model: str = "deepseek-chat") -> str:
        """Interroge l'API DeepSeek pour des complétions de chat."""
        payload = {"model": model, "messages": [{"role": "user", "content": prompt}]}
        response = await self._make_request(json_data=payload)
        if response and not response.get("error"):
            content = response.get("choices", [{}])[0].get("message", {}).get("content")
            if content:
                return content
            return "DeepSeek: Pas de contenu de réponse trouvé."
        return f"DeepSeek: Erreur: {response.get('message', 'Inconnu')}" if response else "DeepSeek: Réponse vide ou erreur interne."

class SerperClient(APIClient):
    def __init__(self):
        super().__init__("SERPER", endpoint_health_manager)

    async def query(self, query_text: str) -> str:
        """Effectue une recherche web via l'API Serper."""
        payload = {"q": query_text}
        response = await self._make_request(json_data=payload)
        if response and not response.get("error"):
            organic_results = response.get("organic", [])
            if organic_results:
                snippet = organic_results[0].get("snippet", "Pas de snippet.")
                link = organic_results[0].get("link", "")
                return f"Serper (recherche web):\n{snippet} {neutralize_urls(link)}"
            return "Serper: Aucune information trouvée."
        return f"Serper: Erreur: {response.get('message', 'Inconnu')}" if response else "Serper: Réponse vide ou erreur interne."

class WolframAlphaClient(APIClient):
    def __init__(self):
        super().__init__("WOLFRAMALPHA", endpoint_health_manager)

    async def query(self, input_text: str) -> str:
        """Interroge WolframAlpha pour des calculs ou des faits."""
        params = {"input": input_text}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            pods = response.get("queryresult", {}).get("pods", [])
            if pods:
                for pod in pods:
                    # Tente de trouver les pods les plus pertinents pour un résultat direct
                    if pod.get("title") in ["Result", "Input interpretation", "Decimal approximation"]:
                        subpods = pod.get("subpods", [])
                        if subpods and subpods[0].get("plaintext"):
                            return f"WolframAlpha:\n{subpods[0]['plaintext']}"
                # Fallback: prend le premier pod si aucun pod pertinent n'est trouvé
                if pods and pods[0].get("subpods") and pods[0]["subpods"][0].get("plaintext"):
                    return f"WolframAlpha:\n{pods[0]['subpods'][0]['plaintext']}"
            return "WolframAlpha: Pas de résultat clair."
        return f"WolframAlpha: Erreur: {response.get('message', 'Inconnu')}" if response else "WolframAlpha: Réponse vide ou erreur interne."

class TavilyClient(APIClient):
    def __init__(self):
        super().__init__("TAVILY", endpoint_health_manager)

    async def query(self, query_text: str, max_results: int = 3) -> str:
        """Effectue une recherche web avancée via l'API Tavily."""
        payload = {"query": query_text, "max_results": max_results}
        response = await self._make_request(json_data=payload)
        if response and not response.get("error"):
            results = response.get("results", [])
            answer = response.get("answer", "Aucune réponse directe trouvée.")

            output = f"Tavily (recherche web):\nRéponse directe: {answer}\n"
            if results:
                output += "Extraits pertinents:\n"
                for i, res in enumerate(results[:max_results]):
                    output += f"- {res.get('title', 'N/A')}: {res.get('content', 'N/A')} {neutralize_urls(res.get('url', ''))}\n"
            return output
        return f"Tavily: Erreur: {response.get('message', 'Inconnu')}" if response else "Tavily: Réponse vide ou erreur interne."

class ApiFlashClient(APIClient):
    def __init__(self):
        super().__init__("APIFLASH", endpoint_health_manager)

    async def query(self, url: str) -> str:
        """Capture une capture d'écran d'une URL via ApiFlash."""
        params = {"url": url, "format": "jpeg", "full_page": "true"}
        response_content = await self._make_request(params=params)

        if isinstance(response_content, bytes):
            selected_endpoint_config = self.endpoint_health_manager.get_best_endpoint(self.name)
            if selected_endpoint_config:
                # ApiFlash retourne l'image directement. On peut construire une URL de prévisualisation
                # si l'API le permet, ou indiquer que la capture a été faite.
                # Ici, nous construisons une URL potentielle de l'image capturée.
                capture_url = f"{selected_endpoint_config['url']}?access_key={selected_endpoint_config['key']}&url={url}&format=jpeg&full_page=true"
                return f"ApiFlash (capture d'écran): {neutralize_urls(capture_url)} (Vérifiez le lien pour l'image)"
            return "ApiFlash: Impossible de générer l'URL de capture."
        elif isinstance(response_content, dict) and response_content.get("error"):
            return f"ApiFlash: Erreur: {response_content.get('message', 'Inconnu')}"
        else:
            log_message(f"ApiFlash a renvoyé un type de réponse inattendu: {type(response_content)}", level="warning")
            return f"ApiFlash: Réponse inattendue de l'API. {response_content}"

class CrawlbaseClient(APIClient):
    def __init__(self):
        super().__init__("CRAWLBASE", endpoint_health_manager)

    async def query(self, url: str, use_js: bool = False) -> str:
        """Scrape le contenu HTML ou JavaScript d'une URL via Crawlbase."""
        params = {"url": url, "format": "json"}
        
        selected_endpoint_config = None
        if use_js:
            # Tente de trouver un endpoint spécifiquement configuré pour le scraping JS
            for config in API_CONFIG.get(self.name, []):
                if "JS Scraping" in config.get("endpoint_name", ""):
                    selected_endpoint_config = config
                    break
        
        # Fallback si pas de config JS spécifique ou si use_js est False
        if not selected_endpoint_config: 
            selected_endpoint_config = self.endpoint_health_manager.get_best_endpoint(self.name)

        if not selected_endpoint_config:
            return f"Crawlbase: Aucun endpoint sain ou disponible pour {self.name}."

        response = await self._make_request(
            params=params,
            url=selected_endpoint_config["url"],
            method=selected_endpoint_config["method"],
            key_field=selected_endpoint_config["key_field"],
            key_location=selected_endpoint_config["key_location"],
            api_key=selected_endpoint_config["key"],
            fixed_params=selected_endpoint_config.get("fixed_params", {}),
            timeout=selected_endpoint_config.get("timeout")
        )

        if response and not response.get("error"):
            body = response.get("body")
            if body:
                try:
                    # Le corps est encodé en base64, il faut le décoder
                    decoded_body = base64.b64decode(body).decode('utf-8', errors='ignore')
                    return f"Crawlbase (contenu web):\n{decoded_body[:1000]}..." # Retourne les 1000 premiers caractères
                except Exception:
                    return f"Crawlbase (contenu web - brut):\n{body[:1000]}..." # En cas d'échec du décodage
            return "Crawlbase: Contenu non trouvé."
        return f"Crawlbase: Erreur: {response.get('message', 'Inconnu')}" if response else "Crawlbase: Réponse vide ou erreur interne."

class DetectLanguageClient(APIClient):
    def __init__(self):
        super().__init__("DETECTLANGUAGE", endpoint_health_manager)

    async def query(self, text: str) -> str:
        """Détecte la langue d'un texte via DetectLanguage API."""
        payload = {"q": text}
        response = await self._make_request(json_data=payload)
        if response and not response.get("error"):
            detections = response.get("data", {}).get("detections", [])
            if detections:
                first_detection = detections[0]
                lang = first_detection.get("language")
                confidence = first_detection.get("confidence")
                return f"Langue détectée: {lang} (confiance: {confidence})"
            return "DetectLanguage: Aucune langue détectée."
        return f"DetectLanguage: Erreur: {response.get('message', 'Inconnu')}" if response else "DetectLanguage: Réponse vide ou erreur interne."

class GuardianClient(APIClient):
    def __init__(self):
        super().__init__("GUARDIAN", endpoint_health_manager)

    async def query(self, query_text: str) -> str:
        """Recherche des articles de presse via l'API The Guardian."""
        params = {"q": query_text}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            results = response.get("response", {}).get("results", [])
            if results:
                output = "Articles The Guardian:\n"
                for res in results[:3]: # Limite à 3 articles pour la concision
                    output += f"- {res.get('webTitle', 'N/A')}: {res.get('fields', {}).get('trailText', 'N/A')} {neutralize_urls(res.get('webUrl', ''))}\n"
                return output
            return "Guardian: Aucun article trouvé."
        return f"Guardian: Erreur: {response.get('message', 'Inconnu')}" if response else "Guardian: Réponse vide ou erreur interne."

class IP2LocationClient(APIClient):
    def __init__(self):
        super().__init__("IP2LOCATION", endpoint_health_manager)

    async def query(self, ip_address: str) -> str:
        """Géolocalise une adresse IP via IP2Location API."""
        params = {"ip": ip_address}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            if "country_name" in response:
                return f"IP2Location (Géolocalisation IP {ip_address}): Pays: {response['country_name']}, Ville: {response.get('city_name', 'N/A')}"
            return "IP2Location: Informations non trouvées."
        return f"IP2Location: Erreur: {response.get('message', 'Inconnu')}" if response else "IP2Location: Réponse vide ou erreur interne."

class ShodanClient(APIClient):
    def __init__(self):
        super().__init__("SHODAN", endpoint_health_manager)

    async def query(self, query_text: str = "") -> str:
        """
        Interroge Shodan pour des informations sur un hôte IP ou des informations sur la clé API.
        Si `query_text` est une IP, tente de récupérer les infos de l'hôte.
        Sinon, ou en cas d'échec, retourne les infos de la clé API.
        """
        if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", query_text): # Vérifie si c'est une adresse IP
            selected_endpoint_config = None
            for config in API_CONFIG.get(self.name, []):
                if "Host Info" in config.get("endpoint_name", ""):
                    selected_endpoint_config = config
                    break
            if selected_endpoint_config:
                # Construire l'URL pour la recherche d'hôte
                url = f"{selected_endpoint_config['url'].rstrip('/')}/{query_text}"
                response = await self._make_request(
                    params={"key": selected_endpoint_config["key"]},
                    url=url,
                    method="GET",
                    key_field=selected_endpoint_config["key_field"],
                    key_location=selected_endpoint_config["key_location"],
                    api_key=selected_endpoint_config["key"],
                    timeout=selected_endpoint_config.get("timeout")
                )
                if response and not response.get("error"):
                    return f"Shodan (info hôte {query_text}): Pays: {response.get('country_name', 'N/A')}, Ports: {response.get('ports', 'N/A')}, Vulnérabilités: {response.get('vulns', 'Aucune')}"
                return f"Shodan (info hôte): Erreur: {response.get('message', 'Inconnu')}" if response else "Shodan: Réponse vide ou erreur interne."
            else:
                return "Shodan: Endpoint 'Host Info' non configuré."
        else:
            # Si pas d'IP ou si la recherche d'hôte n'est pas applicable, retourne les infos de la clé API
            response = await self._make_request() # Utilise le premier endpoint disponible (API Info)
            if response and not response.get("error"):
                return f"Shodan (info clé): Requêtes restantes: {response.get('usage_limits', {}).get('query_credits', 'N/A')}, Scan crédits: {response.get('usage_limits', {}).get('scan_credits', 'N/A')}"
            return f"Shodan: Erreur: {response.get('message', 'Inconnu')}" if response else "Shodan: Réponse vide ou erreur interne."

class WeatherAPIClient(APIClient):
    def __init__(self):
        super().__init__("WEATHERAPI", endpoint_health_manager)

    async def query(self, location: str) -> str:
        """Récupère les conditions météorologiques actuelles pour une localisation via WeatherAPI."""
        params = {"q": location}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            current = response.get("current", {})
            location_info = response.get("location", {})
            if current and location_info:
                return (
                    f"Météo à {location_info.get('name', 'N/A')}, {location_info.get('country', 'N/A')}:\n"
                    f"Température: {current.get('temp_c', 'N/A')}°C, "
                    f"Conditions: {current.get('condition', {}).get('text', 'N/A')}, "
                    f"Vent: {current.get('wind_kph', 'N/A')} km/h"
                )
            return "WeatherAPI: Données météo non trouvées."
        return f"WeatherAPI: Erreur: {response.get('message', 'Inconnu')}" if response else "WeatherAPI: Réponse vide ou erreur interne."

class CloudmersiveClient(APIClient):
    def __init__(self):
        super().__init__("CLOUDMERSIVE", endpoint_health_manager)

    async def query(self, domain: str) -> str:
        """Vérifie la validité et le type d'un domaine via Cloudmersive API."""
        payload = {"domain": domain}
        response = await self._make_request(json_data=payload)
        if response and not response.get("error"):
            return f"Cloudmersive (vérification de domaine {domain}): Valide: {response.get('ValidDomain', 'N/A')}, Type: {response.get('DomainType', 'N/A')}"
        return f"Cloudmersive: Erreur: {response.get('message', 'Inconnu')}" if response else "Cloudmersive: Réponse vide ou erreur interne."

class GreyNoiseClient(APIClient):
    def __init__(self):
        super().__init__("GREYNOISE", endpoint_health_manager)

    async def query(self, ip_address: str) -> str:
        """Analyse une adresse IP pour détecter des activités 'bruit' (malveillantes) via GreyNoise."""
        selected_endpoint_config = self.endpoint_health_manager.get_best_endpoint(self.name)
        if not selected_endpoint_config:
            return f"GreyNoise: Aucun endpoint sain ou disponible pour {self.name}."

        # Construit l'URL avec l'adresse IP à la fin
        url = f"{selected_endpoint_config['url'].rstrip('/')}/{ip_address}"
        method = selected_endpoint_config["method"]
        headers = {selected_endpoint_config["key_field"]: selected_endpoint_config["key"]}

        response = await self._make_request(
            headers=headers,
            url=url,
            method=method,
            key_field=selected_endpoint_config["key_field"],
            key_location=selected_endpoint_config["key_location"],
            api_key=selected_endpoint_config["key"],
            timeout=selected_endpoint_config.get("timeout")
        )

        if response and not response.get("error"):
            if response.get("noise"):
                return f"GreyNoise (IP {ip_address}): C'est une IP 'bruit' (malveillante). Classification: {response.get('classification', 'N/A')}, Nom d'acteur: {response.get('actor', 'N/A')}"
            return f"GreyNoise (IP {ip_address}): Pas de 'bruit' détecté. Statut: {response.get('status', 'N/A')}"
        return f"GreyNoise: Erreur: {response.get('message', 'Inconnu')}" if response else "GreyNoise: Réponse vide ou erreur interne."

class PulsediveClient(APIClient):
    def __init__(self):
        super().__init__("PULSEDIVE", endpoint_health_manager)

    async def query(self, indicator: str, type: str = "auto") -> str:
        """Analyse un indicateur de menace (IP, domaine, URL) via Pulsedive."""
        params = {"indicator": indicator, "type": type}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            if response.get("results"):
                result = response["results"][0] # Prend le premier résultat
                return (
                    f"Pulsedive (Analyse {indicator}): Type: {result.get('type', 'N/A')}, "
                    f"Risk: {result.get('risk', 'N/A')}, "
                    f"Description: {result.get('description', 'N/A')[:200]}..." # Tronque la description
                )
            return "Pulsedive: Aucun résultat d'analyse trouvé."
        return f"Pulsedive: Erreur: {response.get('message', 'Inconnu')}" if response else "Pulsedive: Réponse vide ou erreur interne."

class StormGlassClient(APIClient):
    def __init__(self):
        super().__init__("STORMGLASS", endpoint_health_manager)

    async def query(self, lat: float, lng: float, params: str = "airTemperature,waveHeight") -> str:
        """Récupère les données météorologiques maritimes pour une coordonnée via StormGlass."""
        now = int(time.time())
        request_params = {
            "lat": lat,
            "lng": lng,
            "params": params,
            "start": now,
            "end": now + 3600 # Prévisions pour la prochaine heure (3600 secondes)
        }
        response = await self._make_request(params=request_params)
        if response and not response.get("error"):
            data = response.get("hours", [])
            if data:
                first_hour = data[0]
                # Accède aux valeurs spécifiques des paramètres demandés
                temp = first_hour.get('airTemperature', [{}])[0].get('value', 'N/A')
                wave_height = first_hour.get('waveHeight', [{}])[0].get('value', 'N/A')
                return f"StormGlass (Météo maritime à {lat},{lng}): Température air: {temp}°C, Hauteur vagues: {wave_height}m"
            return "StormGlass: Données non trouvées."
        return f"StormGlass: Erreur: {response.get('message', 'Inconnu')}" if response else "StormGlass: Réponse vide ou erreur interne."

class LoginRadiusClient(APIClient):
    def __init__(self):
        super().__init__("LOGINRADIUS", endpoint_health_manager)

    async def query(self) -> str:
        """Effectue un simple ping à l'API LoginRadius pour vérifier sa disponibilité."""
        response = await self._make_request()
        if response and not response.get("error"):
            return f"LoginRadius (Ping API): Statut: {response.get('Status', 'N/A')}, Message: {response.get('Message', 'N/A')}"
        return f"LoginRadius: Erreur: {response.get('message', 'Inconnu')}" if response else "LoginRadius: Réponse vide ou erreur interne."

class JsonbinClient(APIClient):
    def __init__(self):
        super().__init__("JSONBIN", endpoint_health_manager)

    async def query(self, data: Optional[Dict[str, Any]] = None, private: bool = True, bin_id: Optional[str] = None) -> str:
        """
        Crée un nouveau 'bin' JSON ou accède à un bin existant via Jsonbin.io.
        `data` est pour la création, `bin_id` pour l'accès.
        """
        if bin_id: # Accès à un bin existant
            selected_endpoint_config = None
            for config in API_CONFIG.get(self.name, []):
                if "Bin Access" in config.get("endpoint_name", ""):
                    selected_endpoint_config = config
                    break
            if not selected_endpoint_config:
                return f"Jsonbin: Aucun endpoint d'accès de bin sain ou disponible pour {self.name}."

            url = f"{selected_endpoint_config['url'].rstrip('/')}/{bin_id}"
            method = "GET"
            headers = {selected_endpoint_config["key_field"]: selected_endpoint_config["key"]}
            
            response = await self._make_request(
                headers=headers,
                url=url,
                method=method,
                timeout=selected_endpoint_config.get("timeout")
            )
            if response and not response.get("error"):
                return f"Jsonbin (Accès bin {bin_id}):\n{json.dumps(response, indent=2)}"
            return f"Jsonbin (Accès bin): Erreur: {response.get('message', 'Inconnu')}" if response else "Jsonbin: Réponse vide ou erreur interne."
        
        else: # Création d'un nouveau bin
            selected_endpoint_config = None
            for config in API_CONFIG.get(self.name, []):
                if "Bin Create" in config.get("endpoint_name", ""):
                    selected_endpoint_config = config
                    break
            
            if not selected_endpoint_config:
                return f"Jsonbin: Aucun endpoint de création de bin sain ou disponible pour {self.name}."

            url = selected_endpoint_config["url"]
            method = "POST"
            headers = {selected_endpoint_config["key_field"]: selected_endpoint_config["key"], "Content-Type": "application/json"}
            payload = {"record": data if data is not None else {}, "private": private}

            response = await self._make_request(
                json_data=payload,
                headers=headers,
                url=url,
                method=method,
                timeout=selected_endpoint_config.get("timeout")
            )

            if response and not response.get("error"):
                return f"Jsonbin (Création de bin): ID: {response.get('metadata', {}).get('id', 'N/A')}, URL: {neutralize_urls(response.get('metadata', {}).get('url', 'N/A'))}"
            return f"Jsonbin (Création de bin): Erreur: {response.get('message', 'Inconnu')}" if response else "Jsonbin: Réponse vide ou erreur interne."

class HuggingFaceClient(APIClient):
    def __init__(self):
        super().__init__("HUGGINGFACE", endpoint_health_manager)

    async def query(self, model_name: str = "distilbert-base-uncased-finetuned-sst-2-english", input_text: str = "Hello world") -> str:
        """Effectue une inférence sur un modèle HuggingFace (ex: classification de texte, génération)."""
        selected_endpoint_config = self.endpoint_health_manager.get_best_endpoint(self.name)
        if not selected_endpoint_config:
            return f"HuggingFace: Aucun endpoint sain ou disponible pour {self.name}."

        # Construit l'URL d'inférence pour le modèle spécifié
        inference_url = f"https://api-inference.huggingface.co/models/{model_name}"
        
        headers = {
            selected_endpoint_config["key_field"]: f"{selected_endpoint_config['key_prefix']}{selected_endpoint_config['key']}",
            "Content-Type": "application/json"
        }
        payload = {"inputs": input_text}

        response = await self._make_request(
            json_data=payload,
            headers=headers,
            url=inference_url,
            method="POST",
            timeout=selected_endpoint_config.get("timeout")
        )

        if response and not response.get("error"):
            if isinstance(response, list) and response:
                first_result = response[0]
                if isinstance(first_result, list) and first_result: # Ex: pour les modèles de classification de texte
                    return f"HuggingFace ({model_name} - {first_result[0].get('label')}): Score {first_result[0].get('score', 'N/A'):.2f}"
                elif isinstance(first_result, dict) and "generated_text" in first_result: # Ex: pour les modèles de génération de texte
                    return f"HuggingFace ({model_name}): {first_result.get('generated_text')}"
            return f"HuggingFace ({model_name}): Réponse non parsée. {response}"
        return f"HuggingFace: Erreur: {response.get('message', 'Inconnu')}" if response else "HuggingFace: Réponse vide ou erreur interne."

class TwilioClient(APIClient):
    def __init__(self):
        super().__init__("TWILIO", endpoint_health_manager)

    async def query(self) -> str:
        """Récupère le solde du compte Twilio."""
        selected_endpoint_config = None
        for config in API_CONFIG.get(self.name, []):
            if "Account Balance" in config.get("endpoint_name", ""):
                selected_endpoint_config = config
                break
        if not selected_endpoint_config:
            # Fallback si l'endpoint spécifique n'est pas trouvé, prend le premier disponible
            if self.endpoints_config:
                selected_endpoint_config = self.endpoints_config[0]
            else:
                return f"Twilio: Aucune configuration d'endpoint disponible pour {self.name}."

        response = await self._make_request(
            url=selected_endpoint_config["url"],
            method=selected_endpoint_config["method"],
            key_location=selected_endpoint_config["key_location"],
            api_key=selected_endpoint_config["key"],
            timeout=selected_endpoint_config.get("timeout")
        )
        if response and not response.get("error"):
            return f"Twilio (Balance): {response.get('balance', 'N/A')} {response.get('currency', 'N/A')}"
        return f"Twilio: Erreur: {response.get('message', 'Inconnu')}" if response else "Twilio: Réponse vide ou erreur interne."

class AbstractAPIClient(APIClient):
    def __init__(self):
        super().__init__("ABSTRACTAPI", endpoint_health_manager)

    async def query(self, input_value: str, api_type: str) -> str:
        """
        Interroge diverses APIs d'AbstractAPI (validation email/téléphone, taux de change, jours fériés).
        `input_value` dépend du `api_type`.
        """
        params = {}
        target_endpoint_name = ""

        if api_type == "PHONE_VALIDATION":
            params["phone"] = input_value
            target_endpoint_name = "Phone Validation"
        elif api_type == "EMAIL_VALIDATION":
            params["email"] = input_value
            target_endpoint_name = "Email Validation"
        elif api_type == "EXCHANGE_RATES":
            # Pour les taux de change, input_value peut être la devise de base (ex: "USD")
            params["base"] = input_value if input_value else "USD" 
            target_endpoint_name = "Exchange Rates"
        elif api_type == "HOLIDAYS":
            params["country"] = input_value if input_value else "US" # Pays par défaut si non spécifié
            params["year"] = datetime.now().year # Année actuelle
            target_endpoint_name = "Holidays"
        else:
            return f"AbstractAPI: Type d'API '{api_type}' non supporté pour la requête."

        selected_endpoint_config = None
        for config in API_CONFIG.get(self.name, []):
            if target_endpoint_name in config["endpoint_name"]:
                selected_endpoint_config = config
                break
        
        if not selected_endpoint_config:
            return f"AbstractAPI: Aucun endpoint sain ou disponible pour {self.name} pour le type {api_type}."

        response = await self._make_request(
            params=params,
            url=selected_endpoint_config["url"],
            method=selected_endpoint_config["method"],
            key_field=selected_endpoint_config["key_field"],
            key_location=selected_endpoint_config["key_location"],
            api_key=selected_endpoint_config["key"],
            fixed_params=selected_endpoint_config.get("fixed_params", {}),
            timeout=selected_endpoint_config.get("timeout")
        )

        if response and not response.get("error"):
            if api_type == "PHONE_VALIDATION":
                return (
                    f"AbstractAPI (Validation Tél): Numéro: {response.get('phone', 'N/A')}, "
                    f"Valide: {response.get('valid', 'N/A')}, "
                    f"Pays: {response.get('country', {}).get('name', 'N/A')}"
                )
            elif api_type == "EMAIL_VALIDATION":
                return (
                    f"AbstractAPI (Validation Email): Email: {response.get('email', 'N/A')}, "
                    f"Valide: {response.get('is_valid_format', 'N/A')}, "
                    f"Deliverable: {response.get('is_deliverable', 'N/A')}"
                )
            elif api_type == "EXCHANGE_RATES":
                # Affiche le taux de change pour USD par défaut, ou d'autres devises si présentes
                return f"AbstractAPI (Taux de change): Base: {response.get('base', 'N/A')}, Taux (USD): {response.get('exchange_rates', {}).get('USD', 'N/A')}"
            elif api_type == "HOLIDAYS":
                holidays = [h.get('name', 'N/A') for h in response if h.get('name')]
                return f"AbstractAPI (Jours fériés {params.get('country', 'US')} {params.get('year')}): {', '.join(holidays[:5])}..." if holidays else "Aucun jour férié trouvé."
            return f"AbstractAPI ({api_type}): Réponse brute: {response}"
        return f"AbstractAPI ({api_type}): Erreur: {response.get('message', 'Inconnu')}" if response else "AbstractAPI: Réponse vide ou erreur interne."

class GeminiAPIClient: # Cette classe est distincte de APIClient car elle gère l'API Gemini directement
    def __init__(self):
        self.api_key = GEMINI_API_KEY
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models/"
        # Le modèle est défini dans config.py et peut être passé à generate_content
        self.model_name = "gemini-1.5-flash-latest" # Valeur par défaut, peut être écrasée
        self.headers = {
            "Content-Type": "application/json",
        }
        # Les configurations de génération et de sécurité sont également dans config.py
        from config import GEMINI_TEMPERATURE, GEMINI_TOP_P, GEMINI_TOP_K, GEMINI_MAX_OUTPUT_TOKENS, GEMINI_SAFETY_SETTINGS
        self.generation_config = {
            "temperature": GEMINI_TEMPERATURE,
            "top_p": GEMINI_TOP_P,
            "top_k": GEMINI_TOP_K,
            "max_output_tokens": GEMINI_MAX_OUTPUT_TOKENS,
        }
        self.safety_settings = GEMINI_SAFETY_SETTINGS
        log_message(f"GeminiApiClient initialisé avec le modèle par défaut: {self.model_name}")

    async def generate_content(self, prompt: str, chat_history: List[Dict], image_data: Optional[str] = None, model: Optional[str] = None) -> Dict:
        """
        Génère du contenu textuel ou multimodal en utilisant l'API Gemini.
        `chat_history` est une liste de dictionnaires au format Gemini (role, parts).
        `image_data` est une chaîne base64 de l'image avec son préfixe mimeType (ex: "data:image/png;base64,...").
        `model` permet de spécifier un modèle différent si nécessaire.
        """
        model_to_use = model if model else self.model_name
        url = f"{self.base_url}{model_to_use}:generateContent?key={self.api_key}"

        # Construire les contenus de la requête. Le prompt utilisateur est toujours le dernier.
        contents = []
        for msg in chat_history:
            # L'API Gemini attend les rôles 'user' et 'model'
            role = "user" if msg["role"] == "user" else "model"
            contents.append({"role": role, "parts": [{"text": msg["content"]}]})
        
        user_parts = [{"text": prompt}]
        if image_data:
            # L'API Gemini attend un dictionnaire inlineData avec mimeType et data
            # Assurez-vous que image_data est au format "data:image/png;base64,..."
            # Extraire le mimeType et la base64 data
            if "," in image_data:
                mime_type_part, base64_data = image_data.split(",", 1)
                mime_type = mime_type_part.split(":", 1)[1].split(";", 1)[0]
            else:
                # Fallback si le préfixe est manquant, suppose un type d'image commun
                mime_type = "image/jpeg" 
                base64_data = image_data

            user_parts.append({
                "inlineData": {
                    "mimeType": mime_type,
                    "data": base64_data
                }
            })
            log_message(f"Image ajoutée au prompt Gemini (mimeType: {mime_type}).")

        contents.append({"role": "user", "parts": user_parts})

        payload = {
            "contents": contents,
            "generationConfig": self.generation_config,
            "safetySettings": self.safety_settings
        }

        log_message(f"Appel à Gemini API pour le modèle {model_to_use}...")
        try:
            async with httpx.AsyncClient(timeout=30) as client:
                response = await client.post(url, headers=self.headers, json=payload)
                response.raise_for_status() # Lève une exception pour les codes d'état HTTP 4xx/5xx
                result = response.json()
                log_message(f"Réponse Gemini reçue: {json.dumps(result, indent=2)}")
                return result
        except httpx.HTTPStatusError as e:
            log_message(f"Erreur HTTP Gemini API: {e.response.status_code} - {e.response.text}", level="error")
            return {"error": f"Erreur HTTP Gemini: {e.response.status_code} - {e.response.text}"}
        except httpx.RequestError as e:
            log_message(f"Erreur de requête Gemini API: {e}", level="error")
            return {"error": f"Erreur de requête Gemini: {e}"}
        except json.JSONDecodeError as e:
            log_message(f"Erreur de décodage JSON Gemini API: {e} - Réponse brute: {response.text}", level="error")
            return {"error": f"Erreur de décodage JSON Gemini: {e}"}
        except Exception as e:
            log_message(f"Erreur inattendue Gemini API: {e}\n{traceback.format_exc()}", level="error")
            return {"error": f"Erreur inattendue Gemini: {e}"}

class GoogleCustomSearchClient(APIClient):
    def __init__(self):
        super().__init__("GOOGLE_CUSTOM_SEARCH", endpoint_health_manager)

    async def query(self, query_text: str) -> str:
        """Effectue une recherche personnalisée Google via l'API Custom Search."""
        params = {"q": query_text}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            items = response.get("items", [])
            if items:
                output = "Google Custom Search:\n"
                for item in items[:3]: # Limite à 3 résultats
                    output += f"- {item.get('title', 'N/A')}: {item.get('snippet', 'N/A')} {neutralize_urls(item.get('link', ''))}\n"
                return output
            return "Google Custom Search: Aucun résultat trouvé."
        return f"Google Custom Search: Erreur: {response.get('message', 'Inconnu')}" if response else "Google Custom Search: Réponse vide ou erreur interne."

class RandommerClient(APIClient):
    def __init__(self):
        super().__init__("RANDOMMER", endpoint_health_manager)

    async def query(self, country_code: str = "US", quantity: int = 1) -> str:
        """Génère des numéros de téléphone aléatoires via Randommer.io."""
        params = {"CountryCode": country_code, "Quantity": quantity}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            if isinstance(response, list) and response:
                return f"Randommer (Numéros de téléphone): {', '.join(response)}"
            return f"Randommer: {response}" # Si la réponse n'est pas une liste (ex: erreur formatée)
        return f"Randommer: Erreur: {response.get('message', 'Inconnu')}" if response else "Randommer: Réponse vide ou erreur interne."

class TomorrowIOClient(APIClient):
    def __init__(self):
        super().__init__("TOMORROW.IO", endpoint_health_manager)

    async def query(self, location: str, fields: Optional[List[str]] = None) -> str:
        """Récupère les prévisions météorologiques via Tomorrow.io."""
        if fields is None:
            fields = ["temperature", "humidity", "windSpeed"] # Champs par défaut
        payload = {"location": location, "fields": fields, "units": "metric", "timesteps": ["1h"]}
        response = await self._make_request(json_data=payload)
        if response and not response.get("error"):
            data = response.get("data", {}).get("timelines", [{}])[0].get("intervals", [{}])[0].get("values", {})
            if data:
                output = f"Météo (Tomorrow.io) à {location}:\n"
                for field in fields:
                    output += f"- {field.capitalize()}: {data.get(field, 'N/A')}\n"
                return output
            return "Tomorrow.io: Données météo non trouvées."
        return f"Tomorrow.io: Erreur: {response.get('message', 'Inconnu')}" if response else "Tomorrow.io: Réponse vide ou erreur interne."

class OpenWeatherMapClient(APIClient):
    def __init__(self):
        super().__init__("OPENWEATHERMAP", endpoint_health_manager)

    async def query(self, location: str) -> str:
        """Récupère les conditions météorologiques actuelles via OpenWeatherMap."""
        params = {"q": location}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            main_data = response.get("main", {})
            weather_desc = response.get("weather", [{}])[0].get("description", "N/A")
            if main_data:
                temp_kelvin = main_data.get('temp', 'N/A')
                feels_like_kelvin = main_data.get('feels_like', 'N/A')
                
                # Convertit les températures de Kelvin en Celsius
                temp_celsius = f"{temp_kelvin - 273.15:.2f}" if isinstance(temp_kelvin, (int, float)) else "N/A"
                feels_like_celsius = f"{feels_like_kelvin - 273.15:.2f}" if isinstance(feels_like_kelvin, (int, float)) else "N/A"

                return (
                    f"Météo (OpenWeatherMap) à {location}:\n"
                    f"Température: {temp_celsius}°C, "
                    f"Ressenti: {feels_like_celsius}°C, "
                    f"Humidité: {main_data.get('humidity', 'N/A')}%, "
                    f"Conditions: {weather_desc}"
                )
            return "OpenWeatherMap: Données météo non trouvées."
        return f"OpenWeatherMap: Erreur: {response.get('message', 'Inconnu')}" if response else "OpenWeatherMap: Réponse vide ou erreur interne."

class MockarooClient(APIClient):
    def __init__(self):
        super().__init__("MOCKAROO", endpoint_health_manager)

    async def query(self, count: int = 1, fields_json: Optional[str] = None) -> str:
        """Génère des données de test via Mockaroo."""
        params = {"count": count}
        if fields_json:
            params["fields"] = fields_json # `fields_json` doit être une chaîne JSON valide
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            return f"Mockaroo (Génération de données):\n{json.dumps(response, indent=2)}"
        return f"Mockaroo: Erreur: {response.get('message', 'Inconnu')}" if response else "Mockaroo: Réponse vide ou erreur interne."

class OpenPageRankClient(APIClient):
    def __init__(self):
        super().__init__("OPENPAGERANK", endpoint_health_manager)

    async def query(self, domains: List[str]) -> str:
        """Récupère le PageRank de domaines via OpenPageRank."""
        params = {"domains[]": domains} # L'API attend "domains[]" pour une liste
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            results = response.get("response", [])
            if results:
                output = "OpenPageRank (Classement de domaine):\n"
                for res in results:
                    output += f"- Domaine: {res.get('domain', 'N/A')}, PageRank: {res.get('page_rank', 'N/A')}\n"
                return output
            return "OpenPageRank: Aucun résultat trouvé."
        return f"OpenPageRank: Erreur: {response.get('message', 'Inconnu')}" if response else "OpenPageRank: Réponse vide ou erreur interne."

class RapidAPIClient(APIClient):
    def __init__(self):
        super().__init__("RAPIDAPI", endpoint_health_manager)

    async def query(self, api_name: str, **kwargs) -> str:
        """
        Interroge diverses APIs disponibles via RapidAPI (blagues, taux de change, faits aléatoires).
        `api_name` spécifie l'API RapidAPI à utiliser.
        """
        selected_endpoint_config = None
        for config in API_CONFIG.get(self.name, []):
            if api_name.lower() in config["endpoint_name"].lower():
                selected_endpoint_config = config
                break
        
        if not selected_endpoint_config:
            return f"RapidAPI: Endpoint pour '{api_name}' non trouvé ou non configuré."

        url = selected_endpoint_config["url"]
        method = selected_endpoint_config["method"]
        
        request_params = selected_endpoint_config.get("fixed_params", {}).copy()
        request_headers = selected_endpoint_config.get("fixed_headers", {}).copy()
        request_json_data = selected_endpoint_config.get("fixed_json", {}).copy()

        # Ajoute les kwargs aux bons endroits selon la méthode HTTP
        if method == "GET":
            request_params.update(kwargs)
        elif method == "POST":
            request_json_data.update(kwargs)

        # Les en-têtes spécifiques à RapidAPI sont essentiels
        headers = {
            selected_endpoint_config["key_field"]: selected_endpoint_config["key"],
            "X-RapidAPI-Host": selected_endpoint_config["fixed_headers"].get("X-RapidAPI-Host")
        }
        
        response = await self._make_request(
            params=request_params,
            headers=headers,
            json_data=request_json_data,
            url=url,
            method=method,
            timeout=selected_endpoint_config.get("timeout")
        )

        if response and not response.get("error"):
            if api_name.lower() == "programming joke":
                return f"RapidAPI (Blague de Programmation): {response.get('setup', '')} - {response.get('punchline', '')}"
            elif api_name.lower() == "currency list quotes":
                return f"RapidAPI (Devises): {json.dumps(response, indent=2)}"
            elif api_name.lower() == "random fact":
                return f"RapidAPI (Fait Aléatoire): {response.get('text', 'N/A')}"
            return f"RapidAPI ({api_name}): {json.dumps(response, indent=2)}" # Retourne la réponse brute pour les autres
        return f"RapidAPI ({api_name}): Erreur: {response.get('message', 'Inconnu')}" if response else "RapidAPI: Réponse vide ou erreur interne."

class OCRApiClient: # Cette classe est distincte de APIClient car elle gère l'API OCR.space directement
    def __init__(self):
        from config import OCR_API_KEY # Importe la clé OCR spécifique pour cette classe
        self.api_key = OCR_API_KEY
        self.base_url = "https://api.ocr.space/parse/image"
        log_message("OCRApiClient initialisé.")

    async def query(self, image_base64: str) -> str:
        """
        Effectue une requête OCR à l'API OCR.space.
        `image_base64` doit être la chaîne base64 de l'image, incluant le préfixe mimeType
        (ex: "data:image/png;base64,...").
        """
        payload = {
            "base64Image": image_base64,
            "language": "fre", # Langue par défaut : Français
            "isOverlayRequired": False, # Ne pas inclure l'overlay des régions de texte
            "OCREngine": 2 # Utilise le moteur OCR 2 pour de meilleurs résultats
        }
        headers = {
            "apikey": self.api_key,
            "Content-Type": "application/json"
        }

        log_message("Appel à OCR.space API...")
        try:
            async with httpx.AsyncClient(timeout=30) as client:
                response = await client.post(self.base_url, headers=headers, json=payload)
                response.raise_for_status() # Lève une exception pour les codes d'état HTTP 4xx/5xx
                result = response.json()

                if result.get("IsErroredOnProcessing"):
                    error_message = result.get("ErrorMessage", ["Erreur inconnue lors du traitement OCR."])
                    log_message(f"Erreur OCR.space: {error_message}", level="error")
                    return f"❌ Erreur OCR: {', '.join(error_message)}"
                
                parsed_text = ""
                if "ParsedResults" in result and result["ParsedResults"]:
                    for parsed_result in result["ParsedResults"]:
                        parsed_text += parsed_result.get("ParsedText", "") + "\n"
                
                if parsed_text.strip():
                    log_message("OCR.space: Texte extrait avec succès.")
                    return parsed_text.strip()
                else:
                    log_message("OCR.space: Aucun texte extrait.", level="warning")
                    return "Aucun texte n'a pu être extrait de l'image."

        except httpx.HTTPStatusError as e:
            log_message(f"Erreur HTTP OCR.space API: {e.response.status_code} - {e.response.text}", level="error")
            return f"❌ Erreur HTTP OCR: {e.response.status_code} - {e.response.text}"
        except httpx.RequestError as e:
            log_message(f"Erreur de requête OCR.space API: {e}", level="error")
            return f"❌ Erreur de requête OCR: {e}"
        except json.JSONDecodeError as e:
            log_message(f"Erreur de décodage JSON OCR.space API: {e} - Réponse brute: {response.text}", level="error")
            return {"error": f"Erreur de décodage JSON OCR: {e}"}
        except Exception as e:
            log_message(f"Erreur inattendue OCR.space API: {e}\n{traceback.format_exc()}", level="error")
            return f"❌ Erreur inattendue OCR: {e}"


# Instancier tous les clients API en leur passant le gestionnaire de santé
# Note: GeminiApiClient et OCRApiClient sont instanciés séparément car ils gèrent leurs clés directement.
ALL_API_CLIENTS = [
    DeepSeekClient(), SerperClient(), WolframAlphaClient(), TavilyClient(),
    ApiFlashClient(), CrawlbaseClient(), DetectLanguageClient(), GuardianClient(),
    IP2LocationClient(), ShodanClient(), WeatherAPIClient(),
    CloudmersiveClient(), GreyNoiseClient(), PulsediveClient(), StormGlassClient(),
    LoginRadiusClient(), JsonbinClient(),
    HuggingFaceClient(), TwilioClient(), AbstractAPIClient(),
    GoogleCustomSearchClient(), RandommerClient(), TomorrowIOClient(),
    OpenWeatherMapClient(),
    MockarooClient(), OpenPageRankClient(), RapidAPIClient()
    # GeminiApiClient et OCRApiClient ne sont pas inclus ici car ils sont gérés par leurs propres classes
]

import json
import asyncio
import random
import ast
import subprocess
import base64
import httpx
import io
import contextlib
import traceback
import hashlib
import difflib
import re
import logging
from datetime import datetime, timedelta, timezone
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, Any, Optional, List, Union, Tuple

# Imports des constantes depuis config.py
from config import (
    API_QUOTAS, API_COOLDOWN_DURATION_SECONDS, API_ROTATION_INTERVAL_MINUTES,
    QUOTA_BURN_WINDOW_HOURS, USER_CHAT_HISTORY_FILE, USER_LONG_MEMORY_FILE,
    IA_STATUS_FILE, QUOTAS_FILE, GROUP_CHAT_HISTORY_FILE, PRIVATE_GROUP_ID,
    BURN_QUOTA_THRESHOLD_RATIO, BURN_QUOTA_BEFORE_RESET_HOURS,
    FORBIDDEN_WORDS, ARCHIVES_DIR, MAX_FILE_SIZE, GEMINI_API_KEY, OCR_API_KEY
)

# Imports depuis utils.py (en supposant qu'il est déjà défini ou sera dans le même fichier)
from utils import (
    load_json, save_json, get_current_time, format_datetime, log_message,
    neutralize_urls, extract_keywords, tag_conversation, unique_preserve_order,
    similar, get_user_dir
)

# --- Début du module memory_and_quotas.py ---

class MemoryManager:
    """
    Gère la mémoire à court et long terme du bot, ainsi que l'historique des conversations
    pour les utilisateurs individuels et les groupes.
    C'est un singleton pour s'assurer qu'il n'y a qu'une seule instance de gestionnaire de mémoire.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """Implémente le patron de conception Singleton."""
        if cls._instance is None:
            cls._instance = super(cls, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        """Initialise les structures de données pour la mémoire."""
        if self._initialized:
            return
        self.chat_history: Dict[Union[int, str], List[Dict]] = {} # {user_id: [messages]}
        self.long_term_memory: Dict[Union[int, str], List[str]] = {} # {user_id: [facts]}
        self.ia_status: Dict[str, Dict[str, Any]] = {} # Statut global des IA
        self.group_chat_history: Dict[int, List[Dict]] = {} # {group_id: [messages]}
        # `_initialized` est géré par `init_manager` pour les opérations asynchrones

    async def init_manager(self):
        """
        Initialise le gestionnaire de mémoire de manière asynchrone.
        Charge les statuts persistants et les historiques de groupe.
        """
        if not self._initialized:
            # Charge le statut global des IA
            self.ia_status = await load_json(IA_STATUS_FILE, {})
            self._initialize_ia_status()
            
            # Charge l'historique du groupe privé spécifique
            group_dir = get_user_dir(PRIVATE_GROUP_ID)
            self.group_chat_history[PRIVATE_GROUP_ID] = await load_json(group_dir / GROUP_CHAT_HISTORY_FILE, [])

            self._initialized = True
            log_message("Gestionnaire de mémoire initialisé.")

    def _initialize_ia_status(self):
        """
        Initialise ou met à jour le statut des IA si elles ne sont pas déjà présentes
        ou si leur statut est obsolète. S'assure que toutes les clés nécessaires sont là.
        """
        updated = False
        now = get_current_time()
        
        for client_name in API_QUOTAS.keys(): # Itère sur toutes les APIs définies dans les quotas
            if client_name not in self.ia_status:
                self.ia_status[client_name] = {
                    "last_used": None,
                    "last_error": None,
                    "error_count": 0,
                    "cooldown_until": None,
                    "success_count": 0,
                    "current_score": 1.0, # Score initial de 1.0 (parfait)
                    "last_rotation_check": format_datetime(now),
                    "diversification_score": 1.0 # Score de diversification initial de 1.0 (très diversifiable)
                }
                updated = True
            else:
                # S'assure que toutes les nouvelles clés sont présentes dans les statuts existants
                default_ia_status_keys = {
                    "last_used": None, "last_error": None, "error_count": 0,
                    "cooldown_until": None, "success_count": 0, "current_score": 1.0,
                    "last_rotation_check": format_datetime(now), "diversification_score": 1.0
                }
                for key, default_value in default_ia_status_keys.items():
                    if key not in self.ia_status[client_name]:
                        self.ia_status[client_name][key] = default_value
                        updated = True
                
                # Met à jour `last_rotation_check` si trop ancien pour permettre la récupération du score de diversification
                last_check_str = self.ia_status[client_name].get("last_rotation_check")
                if last_check_str:
                    try:
                        last_check_dt = datetime.strptime(last_check_str, "%Y-%m-%d %H:%M:%S UTC")
                        # Si le dernier check est plus ancien que deux fois l'intervalle de rotation, on le réinitialise
                        if (now - last_check_dt).total_seconds() > API_ROTATION_INTERVAL_MINUTES * 60 * 2:
                            self.ia_status[client_name]["last_rotation_check"] = format_datetime(now)
                            updated = True
                    except ValueError: # Gère les chaînes de date malformées
                        self.ia_status[client_name]["last_rotation_check"] = format_datetime(now)
                        updated = True
                        log_message(f"last_rotation_check malformé pour {client_name}, réinitialisation.", level="warning")

        # Supprime les noms d'IA qui ne sont plus définis dans `API_QUOTAS`
        current_api_names = set(API_QUOTAS.keys())
        ia_names_to_remove = [name for name in self.ia_status if name not in current_api_names]
        for name in ia_names_to_remove:
            del self.ia_status[name]
            updated = True
            log_message(f"IA '{name}' trouvée dans ia_status.json mais non définie dans API_QUOTAS. Supprimée.", level="warning")

        if updated:
            # Sauvegarde l'état mis à jour de manière asynchrone
            asyncio.create_task(save_json(IA_STATUS_FILE, self.ia_status))
            log_message("Statut des IA initialisé/mis à jour.")

    async def add_message_to_history(self, user_id: Union[int, str], role: str, content: str, max_log_entries: int = 100):
        """
        Ajoute un message à l'historique de la conversation d'un utilisateur.
        Gère également le log général de l'utilisateur et le taggage des messages.
        """
        user_dir = get_user_dir(user_id)
        chat_history_path = user_dir / USER_CHAT_HISTORY_FILE
        log_path = user_dir / "log.json" # Fichier de log général pour l'utilisateur

        # Charge les historiques existants pour l'utilisateur (ou utilise ceux en mémoire)
        user_chat_hist = self.chat_history.get(user_id, await load_json(chat_history_path, []))
        user_log = await load_json(log_path, [])

        # Neutralise les URLs pour le stockage (sécurité/confidentialité)
        neutralized_content = neutralize_urls(content)

        # Ajoute au chat history de l'utilisateur
        user_chat_hist.append({"role": role, "content": neutralized_content, "timestamp": format_datetime(get_current_time())})
        user_chat_hist = user_chat_hist[-max_log_entries:] # Tronque l'historique pour ne garder que les N derniers messages
        self.chat_history[user_id] = user_chat_hist
        asyncio.create_task(save_json(chat_history_path, user_chat_hist))
        
        # Ajoute au log général de l'utilisateur (contenu tronqué pour le log)
        log_entry_content = neutralized_content[:500] # Tronque pour le fichier de log
        log_entry = {"time": format_datetime(get_current_time()), "role": role, "text": log_entry_content}
        if role == "user": # Taggue les messages de l'utilisateur avec des mots-clés
            log_entry["tags"] = tag_conversation(content)
        user_log.append(log_entry)
        user_log = user_log[-max_log_entries:] # Tronque le log général
        asyncio.create_task(save_json(log_path, user_log))

        log_message(f"Message ajouté à l'historique de {user_id} par {role}.")

    async def get_chat_history(self, user_id: Union[int, str], limit: int = 10) -> List[Dict]:
        """
        Retourne les N derniers messages de l'historique de conversation d'un utilisateur.
        Charge l'historique depuis le fichier si non déjà en mémoire.
        """
        user_dir = get_user_dir(user_id)
        chat_history_path = user_dir / USER_CHAT_HISTORY_FILE
        if user_id not in self.chat_history:
            self.chat_history[user_id] = await load_json(chat_history_path, [])
        return self.chat_history[user_id][-limit:]

    async def save_group_memory(self, group_id: int, role: str, text: str, max_items: int = 1000):
        """
        Sauvegarde l'historique de chat pour un groupe spécifique.
        Utilise l'ID du groupe comme un ID utilisateur pour la structure de répertoire.
        """
        group_dir = get_user_dir(group_id)
        group_history_path = group_dir / GROUP_CHAT_HISTORY_FILE
        
        hist = self.group_chat_history.get(group_id, await load_json(group_history_path, []))
        hist.append({"time": format_datetime(get_current_time()), "role": role, "text": neutralize_urls(text)})
        hist = hist[-max_items:] # Tronque l'historique du groupe
        self.group_chat_history[group_id] = hist
        asyncio.create_task(save_json(group_history_path, hist))
        log_message(f"Message ajouté à la mémoire de groupe {group_id} par {role}.")

    async def get_group_memory(self, group_id: int, limit: int = 20) -> str:
        """
        Récupère les N derniers messages de la mémoire de groupe.
        Retourne une chaîne formatée pour être utilisée comme contexte.
        """
        group_dir = get_user_dir(group_id)
        group_history_path = group_dir / GROUP_CHAT_HISTORY_FILE
        if group_id not in self.group_chat_history:
            self.group_chat_history[group_id] = await load_json(group_history_path, [])
        
        if not isinstance(self.group_chat_history[group_id], list): # S'assure que c'est une liste
            self.group_chat_history[group_id] = []

        # Filtre les messages du bot si non nécessaires pour le contexte du prompt
        recent_messages = [f"{l['role']} : {l['text']}" for l in self.group_chat_history[group_id][-limit:] if l.get("role") != "bot"]
        return "\n".join(recent_messages)

    async def add_to_long_term_memory(self, user_id: Union[int, str], text: str, max_entries: int = 100):
        """
        Ajoute une information à la mémoire à long terme d'un utilisateur.
        Dédoublonne et tronque la mémoire.
        """
        user_dir = get_user_dir(user_id)
        long_memory_path = user_dir / USER_LONG_MEMORY_FILE
        
        long_mem = self.long_term_memory.get(user_id, await load_json(long_memory_path, []))
        if not isinstance(long_mem, list): # S'assure que c'est une liste
            long_mem = []

        long_mem.append(text.strip())
        long_mem = unique_preserve_order(long_mem)[-max_entries:] # Dédoublonne et tronque
        self.long_term_memory[user_id] = long_mem
        asyncio.create_task(save_json(long_memory_path, long_mem))
        log_message(f"Information ajoutée à la mémoire à long terme de {user_id}.")

    async def get_long_term_memory(self, user_id: Union[int, str], limit: int = 20) -> str:
        """
        Récupère les N dernières entrées de la mémoire à long terme d'un utilisateur.
        Retourne une chaîne formatée.
        """
        user_dir = get_user_dir(user_id)
        long_memory_path = user_dir / USER_LONG_MEMORY_FILE
        if user_id not in self.long_term_memory:
            self.long_term_memory[user_id] = await load_json(long_memory_path, [])
        
        if not isinstance(self.long_term_memory[user_id], list): # S'assure que c'est une liste
            self.long_term_memory[user_id] = []

        return "\n".join(self.long_term_memory[user_id][-limit:])

    async def check_for_similar_prompt(self, user_id: Union[int, str], prompt: str) -> Optional[str]:
        """
        Vérifie si un prompt similaire a déjà été posé récemment et retourne la réponse si trouvée.
        Utilise `MAX_CACHE_SIZE` pour la fenêtre de recherche.
        """
        recent_chat_history = await self.get_chat_history(user_id, limit=MAX_CACHE_SIZE)
        for entry in reversed(recent_chat_history): # Parcours l'historique du plus récent au plus ancien
            if entry.get("role") == "user" and "content" in entry:
                # Compare la similarité du prompt actuel avec les anciens prompts utilisateur
                if similar(prompt, entry["content"]) > 0.92: # Seuil de similarité (92%)
                    # Si un prompt similaire est trouvé, cherche la réponse du bot qui suit
                    for i in range(len(recent_chat_history) - 1, -1, -1):
                        if recent_chat_history[i] == entry and i + 1 < len(recent_chat_history):
                            if recent_chat_history[i+1].get("role") == "bot":
                                log_message(f"Prompt similaire détecté pour {user_id}. Réponse en cache utilisée.")
                                return recent_chat_history[i+1]["content"]
        return None

    def update_ia_status(self, ia_name: str, success: bool, error_message: Optional[str] = None):
        """
        Met à jour le statut et le score d'une IA après une utilisation.
        Ajuste le score de performance et le score de diversification.
        """
        status = self.ia_status.get(ia_name)
        if not status:
            log_message(f"Tentative de mise à jour d'un statut d'IA inconnu: {ia_name}", level="warning")
            return

        now = get_current_time()
        status["last_used"] = format_datetime(now)

        if success:
            status["success_count"] += 1
            status["error_count"] = 0 # Réinitialise le compteur d'erreurs consécutives
            status["cooldown_until"] = None # Annule le cooldown
            status["last_error"] = None
            status["current_score"] = min(1.0, status["current_score"] + 0.1) # Augmente le score de performance
            # Diminue le score de diversification car l'IA vient d'être utilisée
            status["diversification_score"] = max(0.1, status["diversification_score"] - 0.1) 
            log_message(f"IA {ia_name} : Succès enregistré. Nouveau score: {status['current_score']:.2f}, Diversification: {status['diversification_score']:.2f}")
        else:
            status["error_count"] += 1
            status["last_error"] = error_message
            if status["error_count"] >= 3: # Si 3 erreurs consécutives ou plus, met en cooldown
                status["cooldown_until"] = format_datetime(now + timedelta(seconds=API_COOLDOWN_DURATION_SECONDS))
                status["current_score"] = max(0.1, status["current_score"] - 0.2) # Diminue plus fortement le score
                log_message(f"IA {ia_name} : Trop d'erreurs ({status['error_count']}). Cooldown jusqu'à {status['cooldown_until']}. Nouveau score: {status['current_score']:.2f}", level="warning")
            else:
                 status["current_score"] = max(0.1, status["current_score"] - 0.05) # Diminue légèrement
                 log_message(f"IA {ia_name} : Erreur enregistrée. Nouveau score: {status['current_score']:.2f}", level="warning")

        # Sauvegarde l'état mis à jour de manière asynchrone
        asyncio.create_task(save_json(IA_STATUS_FILE, self.ia_status))

    def recover_diversification_scores(self):
        """
        Augmente le score de diversification pour les IA qui n'ont pas été utilisées récemment.
        Ceci encourage la rotation des APIs.
        """
        now = get_current_time()
        updated = False
        for ia_name, status in self.ia_status.items():
            last_used_str = status.get("last_used")
            if last_used_str:
                try:
                    last_used_dt = datetime.strptime(last_used_str, "%Y-%m-%d %H:%M:%S UTC")
                    # Si pas utilisée depuis 2x l'intervalle de rotation, augmente son score de diversification
                    if (now - last_used_dt).total_seconds() > API_ROTATION_INTERVAL_MINUTES * 60 * 2:
                        if status["diversification_score"] < 1.0:
                            status["diversification_score"] = min(1.0, status["diversification_score"] + 0.05)
                            updated = True
                            log_message(f"IA {ia_name}: Score de diversification récupéré à {status['diversification_score']:.2f}")
                except ValueError: # Gère les chaînes de date malformées
                    status["last_used"] = format_datetime(now) # Réinitialise `last_used`
                    status["diversification_score"] = 1.0 # Réinitialise le score de diversification
                    updated = True
                    log_message(f"last_used malformé pour {ia_name}, réinitialisation du score de diversification.", level="warning")
            else: # Si jamais utilisée, met à 1.0 (pleine diversification)
                if status["diversification_score"] < 1.0:
                    status["diversification_score"] = 1.0
                    updated = True
        if updated:
            asyncio.create_task(save_json(IA_STATUS_FILE, self.ia_status))

    def get_ia_status(self, ia_name: str) -> Optional[Dict]:
        """Récupère le statut d'une IA spécifique."""
        return self.ia_status.get(ia_name)

    def get_available_ias(self) -> List[str]:
        """
        Retourne les noms des IA actuellement non en cooldown.
        """
        available = []
        now = get_current_time()
        for name, status in self.ia_status.items():
            cooldown_until_str = status.get("cooldown_until")
            if cooldown_until_str:
                try:
                    cooldown_until = datetime.strptime(cooldown_until_str, "%Y-%m-%d %H:%M:%S UTC")
                    if now < cooldown_until: # Si toujours en cooldown, on la saute
                        continue
                except ValueError: # Date malformée, on la considère comme non en cooldown
                    log_message(f"cooldown_until malformé pour {name}, considéré comme non en cooldown.", level="warning")
            available.append(name)
        return available

class QuotaManager:
    """
    Gère les quotas d'utilisation pour toutes les APIs.
    Suit l'utilisation mensuelle, journalière et horaire, et peut alerter en cas de dépassement.
    Prend également en charge le mode "brûlage" de quota.
    C'est un singleton.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """Implémente le patron de conception Singleton."""
        if cls._instance is None:
            cls._instance = super(cls, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        """Initialise les structures de données pour les quotas."""
        if self._initialized:
            return
        self.quotas = {}
        # `_initialized` est géré par `init_manager` pour les opérations asynchrones
        self.bot_instance = None # Sera injecté par main.py pour l'envoi d'alertes

    async def init_manager(self):
        """
        Initialise le gestionnaire de quotas de manière asynchrone.
        Charge les données de quotas persistantes et s'assure qu'elles sont à jour.
        """
        if not self._initialized:
            self.quotas = await load_json(QUOTAS_FILE, {})
            self._initialize_quotas()
            self._initialized = True
            log_message("Gestionnaire de quotas initialisé.")

    def set_bot_instance(self, bot_instance: Any):
        """
        Permet d'injecter l'instance du bot pour envoyer des alertes de quota au groupe privé.
        """
        self.bot_instance = bot_instance

    def _initialize_quotas(self):
        """
        Initialise les quotas pour toutes les APIs basées sur `config.API_QUOTAS`.
        Nettoie et met à jour les entrées existantes si nécessaire.
        """
        updated = False
        now = get_current_time()

        for api_name, quota_info in API_QUOTAS.items():
            if api_name not in self.quotas:
                self.quotas[api_name] = {
                    "monthly_usage": 0,
                    "daily_usage": 0,
                    "hourly_usage": 0,
                    "hourly_timestamps": [], # Pour un suivi plus précis de l'heure
                    "last_reset_month": now.month,
                    "last_reset_day": now.day,
                    "last_usage": None,
                    "total_calls": 0,
                    "last_hourly_reset": format_datetime(now)
                }
                updated = True
            else:
                # S'assure que toutes les nouvelles clés sont présentes dans les données de quota existantes
                default_quota_structure = {
                    "monthly_usage": 0, "daily_usage": 0, "hourly_usage": 0,
                    "hourly_timestamps": [], "last_reset_month": now.month,
                    "last_reset_day": now.day, "last_usage": None,
                    "total_calls": 0, "last_hourly_reset": format_datetime(now)
                }
                for key, default_value in default_quota_structure.items():
                    if key not in self.quotas[api_name]:
                        self.quotas[api_name][key] = default_value
                        updated = True
                
                # Nettoie `hourly_timestamps` pour les entrées existantes (supprime les anciens horodatages)
                if not isinstance(self.quotas[api_name].get("hourly_timestamps"), list):
                    self.quotas[api_name]["hourly_timestamps"] = []
                
                one_hour_ago = now - timedelta(hours=1)
                self.quotas[api_name]["hourly_timestamps"] = [
                    ts for ts in self.quotas[api_name]["hourly_timestamps"]
                    if datetime.strptime(ts, "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=timezone.utc) > one_hour_ago # Ajoute tzinfo
                ]
                self.quotas[api_name]["hourly_usage"] = len(self.quotas[api_name]["hourly_timestamps"])
                self.quotas[api_name]["last_hourly_reset"] = format_datetime(now)
                updated = True # Marque comme mis à jour car les timestamps ont été nettoyés

        # Supprime les noms d'API qui ne sont plus définis dans `API_QUOTAS`
        api_names_to_remove = [name for name in self.quotas if name not in API_QUOTAS]
        for name in api_names_to_remove:
            del self.quotas[name]
            updated = True
            log_message(f"API '{name}' trouvée dans quotas.json mais non définie dans API_QUOTAS. Supprimée.", level="warning")

        if updated:
            asyncio.create_task(save_json(QUOTAS_FILE, self.quotas))
            log_message("Quotas API initialisés/mis à jour.")

    def _reset_quotas_if_needed(self):
        """
        Réinitialise les quotas journaliers, mensuels et horaires si nécessaire.
        Cette méthode est appelée avant chaque vérification de quota pour s'assurer de l'actualité.
        """
        now = get_current_time()
        for api_name, data in self.quotas.items():
            # Réinitialisation mensuelle
            if now.month != data["last_reset_month"]:
                data["monthly_usage"] = 0
                data["last_reset_month"] = now.month
                log_message(f"Quota mensuel pour {api_name} réinitialisé.")
            # Réinitialisation journalière
            if now.day != data["last_reset_day"]:
                data["daily_usage"] = 0
                data["last_reset_day"] = now.day
                log_message(f"Quota journalier pour {api_name} réinitialisé.")
            
            # Réinitialisation horaire (en nettoyant les anciens horodatages)
            one_hour_ago = now - timedelta(hours=1)
            # S'assure que hourly_timestamps est une liste
            if not isinstance(data.get("hourly_timestamps"), list):
                data["hourly_timestamps"] = []
            
            data["hourly_timestamps"] = [
                ts for ts in data["hourly_timestamps"]
                if datetime.strptime(ts, "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=timezone.utc) > one_hour_ago
            ]
            data["hourly_usage"] = len(data["hourly_timestamps"])
            data["last_hourly_reset"] = format_datetime(now) # Met à jour l'heure du dernier reset horaire

        asyncio.create_task(save_json(QUOTAS_FILE, self.quotas))

    async def check_and_update_quota(self, api_name: str, cost: int = 1) -> bool:
        """
        Vérifie si une API a du quota disponible et le décrémente si oui.
        Retourne `True` si l'opération est autorisée (quota disponible), `False` sinon.
        """
        self._reset_quotas_if_needed() # S'assure que les quotas sont à jour

        if api_name not in API_QUOTAS:
            log_message(f"Tentative de vérification de quota pour une API non définie: {api_name}. Autorisation refusée.", level="error")
            return False

        if api_name not in self.quotas:
            log_message(f"API {api_name} non trouvée dans les quotas gérés. Re-initialisation non bloquante.", level="warning")
            # Ce cas ne devrait pas arriver si _initialize_quotas est correctement appelé au démarrage
            self._initialize_quotas() # Ré-initialise tous les quotas pour s'assurer que cette API est ajoutée
            if api_name not in self.quotas: # Si toujours pas là, il y a un problème grave avec API_QUOTAS
                return False

        quota_data = self.quotas[api_name]
        api_limits = API_QUOTAS.get(api_name, {})
        now = get_current_time()

        # Vérifie la limite mensuelle
        monthly_limit = api_limits.get("monthly")
        if monthly_limit is not None and (quota_data["monthly_usage"] + cost) > monthly_limit:
            log_message(f"Quota mensuel dépassé pour {api_name}", level="warning")
            await self._alert_quota_if_needed(api_name, "mensuel")
            return False

        # Vérifie la limite journalière
        daily_limit = api_limits.get("daily")
        if daily_limit is not None and (quota_data["daily_usage"] + cost) > daily_limit:
            log_message(f"Quota journalier dépassé pour {api_name}", level="warning")
            await self._alert_quota_if_needed(api_name, "journalier")
            return False
        
        # Vérifie la limite horaire
        hourly_limit = api_limits.get("hourly")
        if hourly_limit is not None and (quota_data["hourly_usage"] + cost) > hourly_limit:
            log_message(f"Quota horaire dépassé pour {api_name}", level="warning")
            await self._alert_quota_if_needed(api_name, "horaire")
            return False

        # Vérifie le taux de requêtes par seconde
        rate_limit_per_sec = api_limits.get("rate_limit_per_sec")
        if rate_limit_per_sec:
            last_usage_str = quota_data.get("last_usage")
            if last_usage_str:
                try:
                    last_usage = datetime.strptime(last_usage_str, "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=timezone.utc)
                    time_since_last_call = (now - last_usage).total_seconds()
                    if time_since_last_call < (1 / rate_limit_per_sec):
                        log_message(f"Taux de requêtes dépassé pour {api_name}. Attendre {1/rate_limit_per_sec - time_since_last_call:.2f}s", level="warning")
                        return False
                except ValueError: # Date malformée, on la considère comme sans utilisation récente
                    log_message(f"last_usage malformé pour {api_name}, considéré comme sans utilisation récente pour la limite de taux.", level="warning")

        # Si toutes les vérifications passent, met à jour l'utilisation du quota
        if cost > 0:
            quota_data["monthly_usage"] += cost
            quota_data["daily_usage"] += cost
            quota_data["hourly_usage"] += cost
            quota_data["hourly_timestamps"].append(format_datetime(now)) # Ajoute l'horodatage pour le suivi horaire
            quota_data["total_calls"] += cost
            quota_data["last_usage"] = format_datetime(now)
            asyncio.create_task(save_json(QUOTAS_FILE, self.quotas)) # Sauvegarde de manière asynchrone
            log_message(f"Quota pour {api_name} mis à jour. Usage mensuel: {quota_data['monthly_usage']}/{monthly_limit if monthly_limit else 'Illimité'}, Journalier: {quota_data['daily_usage']}/{daily_limit if daily_limit else 'Illimité'}, Horaire: {quota_data['hourly_usage']}/{hourly_limit if hourly_limit else 'Illimité'}")
        else:
            log_message(f"Quota pour {api_name} vérifié (coût 0). Usage mensuel: {quota_data['monthly_usage']}/{monthly_limit if monthly_limit else 'Illimité'}, Journalier: {quota_data['daily_usage']}/{daily_limit if daily_limit else 'Illimité'}, Horaire: {quota_data['hourly_usage']}/{hourly_limit if hourly_limit else 'Illimité'}")

        return True

    async def _alert_quota_if_needed(self, api_name: str, limit_type: str):
        """
        Envoie une alerte au groupe privé si un quota est atteint.
        Utilise la mémoire à long terme pour éviter de spammer les alertes.
        """
        if self.bot_instance and PRIVATE_GROUP_ID:
            message = f"🚨 Quota {limit_type} pour l'API '{api_name}' atteint !"
            log_message(message, level="warning")
            try:
                # Clé d'alerte unique pour le jour actuel pour éviter les doublons
                alert_key = f"quota_alert_{api_name}_{limit_type}_{get_current_time().strftime('%Y-%m-%d')}"
                # Vérifie si cette alerte a déjà été envoyée aujourd'hui
                # Nous utilisons la mémoire à long terme du bot lui-même pour stocker ces alertes globales
                bot_global_memory_id = "bot_global_alerts" 
                if not await memory_manager.get_long_term_memory(bot_global_memory_id, limit=1000): # Vérifie si la clé existe
                    # Si la mémoire est vide ou la clé n'est pas là, initialise/ajoute
                    await memory_manager.add_to_long_term_memory(bot_global_memory_id, alert_key)
                
                # Vérifie spécifiquement si la clé d'alerte existe dans la mémoire du bot pour aujourd'hui
                global_alerts = await memory_manager.get_long_term_memory(bot_global_memory_id, limit=1000)
                if alert_key not in global_alerts:
                    await self.bot_instance.send_message(chat_id=PRIVATE_GROUP_ID, text=message)
                    await memory_manager.add_to_long_term_memory(bot_global_memory_id, alert_key) # Marque l'alerte comme envoyée
            except Exception as e:
                log_message(f"Erreur lors de l'envoi de l'alerte de quota: {e}", level="error")

    def get_api_usage(self, api_name: str) -> Optional[Dict]:
        """Retourne les informations d'utilisation d'une API spécifique."""
        return self.quotas.get(api_name)

    def get_all_quotas_status(self) -> Dict:
        """
        Retourne le statut de tous les quotas API.
        S'assure que les quotas sont à jour avant de les retourner.
        """
        self._reset_quotas_if_needed()
        status = {}
        for api_name, quota_data in self.quotas.items():
            api_limits = API_QUOTAS.get(api_name, {})
            monthly_limit = api_limits.get("monthly", "Illimité")
            daily_limit = api_limits.get("daily", "Illimité")
            hourly_limit = api_limits.get("hourly", "Illimité")
            status[api_name] = {
                "monthly_usage": quota_data["monthly_usage"],
                "monthly_limit": monthly_limit,
                "daily_usage": quota_data["daily_usage"],
                "daily_limit": daily_limit,
                "hourly_usage": quota_data["hourly_usage"],
                "hourly_limit": hourly_limit,
                "total_calls": quota_data["total_calls"],
                "last_usage": quota_data["last_usage"],
                "last_reset_month": quota_data["last_reset_month"],
                "last_reset_day": quota_data["last_reset_day"],
                "last_hourly_reset": quota_data["last_hourly_reset"]
            }
        return status

    def get_burn_window_apis(self) -> List[str]:
        """
        Identifie les APIs dont les quotas sont sur le point d'être réinitialisés
        et où il est opportun de "brûler" le quota restant.
        """
        burn_apis = []
        now = get_current_time() # UTC
        for api_name, data in self.quotas.items():
            api_limits = API_QUOTAS.get(api_name, {})

            # Vérification pour le "burn" mensuel
            monthly_limit = api_limits.get("monthly")
            if monthly_limit is not None and monthly_limit > 0:
                # Calcule le premier jour du mois suivant (en UTC)
                next_month = now.month + 1
                year_for_next_month = now.year
                if next_month > 12:
                    next_month = 1
                    year_for_next_month += 1
                next_month_reset = datetime(year_for_next_month, next_month, 1, 0, 0, 0, 0, tzinfo=timezone.utc)
                
                # Vérifie si l'heure actuelle est dans la fenêtre de "brûlage" avant la réinitialisation
                if now < next_month_reset and (next_month_reset - now) <= timedelta(hours=BURN_QUOTA_BEFORE_RESET_HOURS):
                    if data["monthly_usage"] < monthly_limit:
                        remaining_quota_ratio = (monthly_limit - data["monthly_usage"]) / monthly_limit
                        if remaining_quota_ratio > 0 and remaining_quota_ratio <= BURN_QUOTA_THRESHOLD_RATIO:
                            burn_apis.append(f"{api_name} (mensuel: {monthly_limit - data['monthly_usage']} restants)")

            # Vérification pour le "burn" journalier
            daily_limit = api_limits.get("daily")
            if daily_limit is not None and daily_limit > 0:
                # Calcule le début du jour suivant (en UTC)
                next_day_reset = datetime(now.year, now.month, now.day, 0, 0, 0, 0, tzinfo=timezone.utc) + timedelta(days=1)
                
                # Vérifie si l'heure actuelle est dans la fenêtre de "brûlage" avant la réinitialisation
                if now < next_day_reset and (next_day_reset - now) <= timedelta(hours=BURN_QUOTA_BEFORE_RESET_HOURS):
                    if data["daily_usage"] < daily_limit:
                        remaining_quota_ratio = (daily_limit - data["daily_usage"]) / daily_limit
                        if remaining_quota_ratio > 0 and remaining_quota_ratio <= BURN_QUOTA_THRESHOLD_RATIO:
                            burn_apis.append(f"{api_name} (journalier: {daily_limit - data['daily_usage']} restants)")
        return burn_apis

    def should_burn_quota(self, api_name: str) -> bool:
        """
        Détermine si le quota pour une API donnée devrait être 'brûlé' avant réinitialisation.
        Cette méthode est appelée par `_auto_burn_quota_task` pour décider si une API doit être utilisée.
        """
        self._reset_quotas_if_needed() # S'assure que les quotas sont à jour
        
        quota_data = self.quotas.get(api_name)
        api_limits = API_QUOTAS.get(api_name)

        if not quota_data or not api_limits:
            return False

        now = get_current_time() # UTC

        # Vérifie le "burn" mensuel
        monthly_limit = api_limits.get("monthly")
        if monthly_limit is not None and monthly_limit > 0:
            next_month = now.month + 1
            year_for_next_month = now.year
            if next_month > 12:
                next_month = 1
                year_for_next_month += 1
            next_month_reset = datetime(year_for_next_month, next_month, 1, 0, 0, 0, 0, tzinfo=timezone.utc)
            
            if now < next_month_reset:
                time_until_reset = next_month_reset - now
                if time_until_reset <= timedelta(hours=BURN_QUOTA_BEFORE_RESET_HOURS):
                    remaining_quota_ratio = (monthly_limit - quota_data["monthly_usage"]) / monthly_limit
                    if remaining_quota_ratio > 0 and remaining_quota_ratio <= BURN_QUOTA_THRESHOLD_RATIO:
                        log_message(f"Mode Burn: {api_name} (mensuel) - usage {quota_data['monthly_usage']}/{monthly_limit}, ratio {remaining_quota_ratio:.2f}, reset dans {time_until_reset}", level="debug")
                        return True

        # Vérifie le "burn" journalier
        daily_limit = api_limits.get("daily")
        if daily_limit is not None and daily_limit > 0:
            next_day_reset = datetime(now.year, now.month, now.day, 0, 0, 0, 0, tzinfo=timezone.utc) + timedelta(days=1)
            
            if now < next_day_reset:
                time_until_reset = next_day_reset - now
                if time_until_reset <= timedelta(hours=BURN_QUOTA_BEFORE_RESET_HOURS):
                    remaining_quota_ratio = (daily_limit - quota_data["daily_usage"]) / daily_limit
                    if remaining_quota_ratio > 0 and remaining_quota_ratio <= BURN_QUOTA_THRESHOLD_RATIO:
                        log_message(f"Mode Burn: {api_name} (journalier) - usage {quota_data['daily_usage']}/{daily_limit}, ratio {remaining_quota_ratio:.2f}, reset dans {time_until_reset}", level="debug")
                        return True
        
        # Les quotas horaires ne sont généralement pas "brûlés" de la même manière car ils se réinitialisent rapidement.
        return False

# Instanciation des gestionnaires de mémoire et de quotas (seront initialisés dans main.py)
memory_manager = MemoryManager()
quota_manager = QuotaManager()

# --- Fin du module memory_and_quotas.py ---


# --- Début du module filters_and_tools.py ---

# Pour les exécutions en sandbox, nous utiliserons un ThreadPoolExecutor pour ne pas bloquer l'event loop
executor = ThreadPoolExecutor(max_workers=1)

# Imports spécifiques pour les outils de développement (assurez-vous que ces bibliothèques sont installées)
try:
    from pygments import highlight
    from pygments.lexers import PythonLexer
    from pygments.formatters import TerminalFormatter
except ImportError:
    highlight = None
    PythonLexer = None
    TerminalFormatter = None
    log_message("Pygments non trouvé. La surbrillance syntaxique ne sera pas disponible.", level="warning")

try:
    from pyflakes.api import check
    from pyflakes.reporter import Reporter
except ImportError:
    check = None
    Reporter = None
    log_message("Pyflakes non trouvé. La vérification de code ne sera pas disponible.", level="warning")

try:
    import black
except ImportError:
    black = None
    log_message("Black non trouvé. Le formatage de code ne sera pas disponible.", level="warning")

# Instancier le client OCR API pour une utilisation directe dans perform_ocr_api
# Note: OCRApiClient est défini dans api_clients.py, donc il doit être importé.
# Pour éviter une dépendance circulaire si ce fichier est importé avant api_clients,
# l'instanciation est faite ici, mais la classe OCRApiClient doit être disponible.
# Dans le script final, toutes les classes sont dans le même fichier ou l'ordre d'importation est géré.
from api_clients import OCRApiClient # Assurez-vous que OCRApiClient est importé
ocr_api_client_instance = OCRApiClient()


def filter_bad_code(code: str) -> bool:
    """
    Filtre basique pour les commandes de code potentiellement dangereuses.
    Empêche l'exécution de certaines opérations système ou de réseau.
    """
    forbidden_patterns = [
        r'os\.system', r'subprocess\.run', r'shutil\.rmtree', r'requests\.post',
        r'open\([^,\'"]*\s*,\s*[\'"]w', r'import socket', r'import http',
        r'sys\.exit', r'while True:', r'import threading', r'import multiprocessing'
    ]
    for pattern in forbidden_patterns:
        if re.search(pattern, code):
            log_message(f"Code bloqué: motif dangereux détecté: {pattern}", level="warning")
            return True
    return False

def detect_and_correct_toxicity(text: str) -> str:
    """
    Remplace les propos toxiques (mots définis dans FORBIDDEN_WORDS)
    par des faits scientifiques ou des encouragements.
    """
    if any(word in text.lower() for word in FORBIDDEN_WORDS):
        facts = [
            "Savais-tu que 73% des conflits viennent de malentendus ?",
            "Le cerveau humain est câblé pour la coopération, pas le conflit.",
            "En 2025, l'IA émotionnelle sera la norme. Soyons précurseurs !",
            "Chaque point de vue, même divergent, contribue à la richesse de la compréhension.",
            "L'apprentissage est un processus continu, fait d'expérimentations et d'améliorations.",
            "La collaboration est la clé de l'innovation."
        ]
        log_message(f"Toxicité détectée et corrigée dans le message: '{text}'", level="info")
        return random.choice(facts) + " Continuons à construire ensemble !"
    return text

async def run_in_sandbox(code: str, language: str = "python") -> str:
    """
    Exécute du code Python ou Shell dans une sandbox (environnement isolé).
    Utilise un ThreadPoolExecutor pour exécuter des opérations bloquantes de manière asynchrone,
    évitant ainsi de bloquer l'event loop principal.
    """
    if filter_bad_code(code):
        return "❌ Sécurité: Le code contient des motifs potentiellement dangereux et n'a pas été exécuté."

    loop = asyncio.get_running_loop()
    if language == "python":
        return await loop.run_in_executor(executor, _run_python_sync, code)
    elif language == "shell":
        return await loop.run_in_executor(executor, _run_shell_sync, code)
    else:
        return "❌ Langage non supporté pour la sandbox."

def _run_python_sync(code: str) -> str:
    """
    Exécute du code Python de manière synchrone et capture la sortie standard et d'erreur.
    Utilise un dictionnaire `__builtins__` vide pour isoler l'exécution.
    """
    old_stdout = io.StringIO()
    old_stderr = io.StringIO()
    with contextlib.redirect_stdout(old_stdout), contextlib.redirect_stderr(old_stderr):
        try:
            # Utilise un dictionnaire vide pour __builtins__ pour isoler l'exécution
            # Cela empêche l'accès à la plupart des modules intégrés et des fonctions système.
            exec(code, {'__builtins__': {}})
            output = old_stdout.getvalue()
            error = old_stderr.getvalue()
            if error:
                log_message(f"Erreur d'exécution Python en sandbox:\n{error}", level="warning")
                return f"🐍 Erreur Python:\n{error}\nSortie:\n{output}"
            return f"✅ Sortie Python:\n{output}"
        except Exception as e:
            log_message(f"Erreur d'exécution Python inattendue en sandbox: {e}\n{traceback.format_exc()}", level="error")
            return f"❌ Erreur d'exécution Python: {e}\nSortie standard:\n{old_stdout.getvalue()}\nErreur standard:\n{old_stderr.getvalue()}"

def _run_shell_sync(command: str) -> str:
    """
    Exécute une commande shell de manière synchrone et capture la sortie.
    Utilise `subprocess.run` avec un timeout pour éviter les blocages.
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=True, # Lève une CalledProcessError si le code de retour est non nul
            timeout=10 # Timeout de 10 secondes pour l'exécution
        )
        output = result.stdout
        error = result.stderr
        if error:
            log_message(f"Erreur d'exécution Shell en sandbox:\n{error}", level="warning")
            return f"🐚 Erreur Shell:\n{error}\nSortie:\n{output}"
        return f"✅ Sortie Shell:\n{output}"
    except subprocess.CalledProcessError as e:
        log_message(f"Erreur d'exécution Shell (Code: {e.returncode}):\n{e.stderr}\nSortie:\n{e.stdout}", level="error")
        return f"❌ Erreur d'exécution Shell (Code: {e.returncode}):\n{e.stderr}\nSortie:\n{e.stdout}"
    except subprocess.TimeoutExpired:
        log_message("Erreur Shell: La commande a dépassé le temps d'exécution imparti.", level="warning")
        return "❌ Erreur Shell: La commande a dépassé le temps d'exécution imparti."
    except Exception as e:
        log_message(f"Erreur inattendue lors de l'exécution Shell: {e}\n{traceback.format_exc()}", level="error")
        return f"❌ Erreur inattendue lors de l'exécution Shell: {e}"

def syntax_highlight(code: str) -> str:
    """
    Met en surbrillance la syntaxe du code Python en utilisant Pygments.
    Retourne le code formaté pour l'affichage en console ou dans un bloc `<pre>`.
    """
    if highlight and PythonLexer and TerminalFormatter:
        try:
            # Utilise TerminalFormatter pour une sortie texte simple compatible avec Telegram <pre>
            return highlight(code, PythonLexer(), TerminalFormatter())
        except Exception as e:
            log_message(f"Erreur de surbrillance syntaxique: {e}", level="error")
            return code # Retourne le code brut en cas d'erreur
    else:
        return "❌ Outil de surbrillance syntaxique (Pygments) non disponible."

def check_code(code: str) -> str:
    """
    Vérifie le code Python avec Pyflakes pour détecter les erreurs de syntaxe et les problèmes de style.
    """
    if check and Reporter:
        out = io.StringIO()
        reporter = Reporter(out, out)
        check(code, filename="<string>", reporter=reporter)
        result = out.getvalue()
        return result if result else "✅ Pyflakes: Aucun problème détecté."
    else:
        return "❌ Outil de vérification de code (Pyflakes) non disponible."

def format_code(code: str) -> str:
    """
    Formate le code Python avec Black pour assurer une cohérence stylistique.
    """
    if black:
        try:
            mode = black.Mode()
            return black.format_str(code, mode=mode)
        except black.InvalidInput as e:
            log_message(f"Erreur de formatage (Black): Code Python invalide. {e}", level="error")
            return f"❌ Erreur de formatage (Black): Code Python invalide. {e}"
        except Exception as e:
            log_message(f"Erreur de formatage (Black): {e}", level="error")
            return f"❌ Erreur de formatage (Black): {e}"
    else:
        return "❌ Outil de formatage de code (Black) non disponible."

def extract_functions(code: str) -> Union[List[str], str]:
    """
    Extrait les noms des fonctions définies dans un code Python en utilisant l'AST.
    """
    try:
        tree = ast.parse(code)
        functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        return functions if functions else "Aucune fonction détectée."
    except SyntaxError as e:
        log_message(f"Erreur de syntaxe Python lors de l'extraction des fonctions: {e}", level="error")
        return f"❌ Erreur de syntaxe Python: {e}"
    except Exception as e:
        log_message(f"Erreur lors de l'extraction des fonctions: {e}", level="error")
        return f"❌ Erreur lors de l'extraction des fonctions: {e}"

def analyze_code_structure(code: str) -> str:
    """
    Analyse la structure AST (Arbre Syntaxique Abstrait) d'un code Python.
    Utile pour comprendre la composition du code.
    """
    try:
        tree = ast.parse(code)
        return ast.dump(tree, indent=2) # Affiche l'AST formaté avec indentation
    except SyntaxError as e:
        log_message(f"Erreur de syntaxe Python lors de l'analyse AST: {e}", level="error")
        return f"❌ Erreur de syntaxe Python: {e}"
    except Exception as e:
        log_message(f"Erreur lors de l'analyse de la structure AST: {e}", level="error")
        return f"❌ Erreur lors de l'analyse de la structure AST: {e}"

async def perform_ocr_api(image_url: str) -> str:
    """
    Effectue l'OCR sur une URL d'image en utilisant l'API OCR.space via `OCRApiClient`.
    Télécharge l'image, l'encode en base64, puis envoie à l'API.
    """
    try:
        # Télécharger l'image depuis l'URL
        async with httpx.AsyncClient(timeout=10) as client:
            img_response = await client.get(image_url)
            img_response.raise_for_status() # Lève une exception pour les codes d'état HTTP 4xx/5xx

        # Encoder l'image en base64
        # Assurez-vous que le format est compatible avec l'API OCR (ex: data:image/png;base64,...)
        # OCR.space attend un préfixe, donc nous l'ajoutons si nécessaire.
        base64_image_data = base64.b64encode(img_response.content).decode('utf-8')
        content_type = img_response.headers.get("Content-Type", "image/jpeg") # Tente de deviner le mimetype
        image_base64_with_prefix = f"data:{content_type};base64,{base64_image_data}"

        # Appeler le client OCR API instancié globalement
        result = await ocr_api_client_instance.query(image_base64_with_prefix)
        return result

    except httpx.HTTPStatusError as e:
        log_message(f"Erreur HTTP/réseau lors de l'OCR: {e.response.status_code} - {e.response.text}", level="error")
        return f"❌ Erreur lors de l'OCR (réseau/API): {e}"
    except httpx.RequestError as e:
        log_message(f"Erreur de requête lors de l'OCR: {e}", level="error")
        return f"❌ Erreur lors de l'OCR (requête): {e}"
    except Exception as e:
        log_message(f"Erreur inattendue lors de l'OCR: {e}\n{traceback.format_exc()}", level="error")
        return f"❌ Erreur inattendue lors de l'OCR: {e}"

async def fetch_and_archive_pages(links: List[str], user_id: Union[int, str], bot_instance: Any):
    """
    Télécharge toutes les pages des liens fournis, les archive localement,
    puis les envoie au groupe privé Telegram.
    """
    user_archive_dir = get_user_dir(user_id) / ARCHIVES_DIR
    user_archive_dir.mkdir(exist_ok=True, parents=True)

    for idx, url in enumerate(links):
        try:
            async with httpx.AsyncClient(timeout=20) as client:
                r = await client.get(url)
                r.raise_for_status() # Lève une exception pour les codes d'état HTTP 4xx/5xx

                if len(r.content) < MAX_FILE_SIZE:
                    ext = ".html" if "<html" in r.text.lower() else ".txt"
                    # Utilise un hash de l'URL pour un nom de fichier plus robuste et unique
                    url_hash = hashlib.sha256(url.encode('utf-8')).hexdigest()[:10]
                    fname = f"page_{datetime.now().strftime('%Y%m%d%H%M%S')}_{url_hash}_{idx}{ext}"
                    fpath = user_archive_dir / fname
                    fpath.write_text(r.text, encoding="utf-8", errors="ignore")
                    
                    # Envoi au groupe privé si l'instance du bot est fournie
                    if PRIVATE_GROUP_ID and bot_instance:
                        try:
                            with fpath.open("rb") as f:
                                await bot_instance.send_document(chat_id=PRIVATE_GROUP_ID, document=f, filename=fname, caption=f"Page archivée de {neutralize_urls(url)}")
                        except Exception as send_e:
                            log_message(f"Erreur lors de l'envoi du document archivé au groupe privé: {send_e}", level="error")
                    
                    log_message(f"Page archivée: {url} pour user {user_id}")
                else:
                    log_message(f"Page trop grande pour être archivée: {url} ({len(r.content)} bytes)", level="warning")
        except httpx.HTTPStatusError as e:
            log_message(f"[fetch_and_archive_pages] Erreur HTTP pour {url}: {e.response.status_code} - {e.response.text}", level="error")
        except httpx.RequestError as e:
            log_message(f"[fetch_and_archive_pages] Erreur de requête pour {url}: {e}", level="error")
        except Exception as e:
            log_message(f"[fetch_and_archive_pages] Erreur inattendue pour {url}: {e}\n{traceback.format_exc()}", level="error")

# --- Fin du module filters_and_tools.py ---

import asyncio
import telebot
import traceback
import json
import re
from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from typing import Dict, Any, List, Optional, Union

# Importation des constantes et configurations
from config import (
    BOT_TOKEN, PRIVATE_GROUP_ID, API_QUOTAS, API_COOLDOWN_DURATION_SECONDS,
    API_ROTATION_INTERVAL_MINUTES, QUOTA_BURN_WINDOW_HOURS,
    USER_CHAT_HISTORY_FILE, USER_LONG_MEMORY_FILE, IA_STATUS_FILE,
    QUOTAS_FILE, GROUP_CHAT_HISTORY_FILE, MAX_CACHE_SIZE, FORBIDDEN_WORDS,
    GEMINI_API_KEY, OCR_API_KEY, API_CONFIG, ENDPOINT_HEALTH_FILE,
    GEMINI_TEMPERATURE, GEMINI_TOP_P, GEMINI_TOP_K, GEMINI_MAX_OUTPUT_TOKENS, GEMINI_SAFETY_SETTINGS
)

# Importation des modules locaux
from utils import (
    load_json, save_json, get_user_dir, rotate_log_if_needed, compress_if_large,
    get_current_time, format_datetime, is_within_time_window, log_message,
    neutralize_urls, clean_html_tags, hash_text, extract_keywords, tag_conversation,
    unique_preserve_order, similar, set_file_lock
)
from api_clients import (
    EndpointHealthManager, APIClient, DeepSeekClient, SerperClient, WolframAlphaClient,
    TavilyClient, ApiFlashClient, CrawlbaseClient, DetectLanguageClient, GuardianClient,
    IP2LocationClient, ShodanClient, WeatherAPIClient, CloudmersiveClient,
    GreyNoiseClient, PulsediveClient, StormGlassClient, LoginRadiusClient,
    JsonbinClient, HuggingFaceClient, TwilioClient, AbstractAPIClient,
    GeminiAPIClient, GoogleCustomSearchClient, RandommerClient, TomorrowIOClient,
    OpenWeatherMapClient, MockarooClient, OpenPageRankClient, RapidAPIClient,
    set_endpoint_health_manager_global # Pour injecter l'instance du gestionnaire de santé
)
from memory_and_quotas import MemoryManager, QuotaManager
from filters_and_tools import (
    filter_bad_code, detect_and_correct_toxicity, run_in_sandbox, syntax_highlight,
    check_code, format_code, extract_functions, analyze_code_structure,
    perform_ocr_api, fetch_and_archive_pages
)

# --- Initialisation du bot et des gestionnaires ---
bot = AsyncTeleBot(BOT_TOKEN)

# Instanciation des gestionnaires (ils sont des singletons, donc une seule instance)
endpoint_health_manager = EndpointHealthManager()
memory_manager = MemoryManager()
quota_manager = QuotaManager()

# Injection des instances nécessaires
set_endpoint_health_manager_global(endpoint_health_manager) # Pour api_clients.py
quota_manager.set_bot_instance(bot) # Pour que le quota_manager puisse envoyer des alertes
set_file_lock(asyncio.Lock()) # Injecte le verrou de fichier global dans utils.py

# Instanciation des clients API
# Note: GeminiAPIClient et OCRApiClient sont gérés séparément car ils n'utilisent pas le système de sélection d'endpoint dynamique
gemini_client = GeminiAPIClient()
ocr_client = ocr_api_client_instance # Utilise l'instance déjà créée dans filters_and_tools.py

# Dictionnaire des clients API pour un accès facile par nom
api_clients: Dict[str, APIClient] = {
    client.name: client for client in ALL_API_CLIENTS
}

# --- Fonctions utilitaires du bot ---

async def send_message_to_private_group(text: str):
    """Envoie un message au groupe privé configuré."""
    if PRIVATE_GROUP_ID:
        try:
            await bot.send_message(PRIVATE_GROUP_ID, text)
        except Exception as e:
            log_message(f"Erreur lors de l'envoi au groupe privé: {e}", level="error")

async def get_user_id_from_message(message: Message) -> Union[int, str]:
    """
    Récupère l'ID de l'utilisateur ou du groupe à partir d'un message.
    Utilise l'ID du chat pour les groupes et l'ID de l'expéditeur pour les messages privés.
    """
    if message.chat.type == "private":
        return message.from_user.id
    else:
        return message.chat.id

def get_sender_info(message: Message) -> str:
    """Retourne une chaîne d'informations sur l'expéditeur du message."""
    if message.chat.type == "private":
        return f"Utilisateur: {message.from_user.first_name} (@{message.from_user.username} - {message.from_user.id})"
    else:
        return f"Groupe: {message.chat.title} (ID: {message.chat.id}), Expéditeur: {message.from_user.first_name} (@{message.from_user.username} - {message.from_user.id})"

# --- Boucles de fond pour la maintenance ---

async def _health_check_loop():
    """Boucle de fond pour exécuter des checks de santé réguliers sur les endpoints API."""
    while True:
        log_message("Lancement des health checks pour tous les services API...")
        for service_name in API_CONFIG.keys():
            await endpoint_health_manager.run_health_check_for_service(service_name)
        await asyncio.sleep(API_ROTATION_INTERVAL_MINUTES * 60) # Exécute toutes les X minutes

async def _quota_burn_loop():
    """
    Boucle de fond pour "brûler" les quotas API avant leur réinitialisation.
    Tente d'utiliser les APIs qui sont dans leur fenêtre de "brûlage".
    """
    while True:
        burn_apis = quota_manager.get_burn_window_apis()
        if burn_apis:
            log_message(f"APIs en mode 'burn' détectées: {', '.join(burn_apis)}")
            for api_name_with_info in burn_apis:
                api_name = api_name_with_info.split(" ")[0] # Extrait le nom de l'API
                if quota_manager.should_burn_quota(api_name):
                    log_message(f"Tentative de 'brûlage' de quota pour {api_name}...", level="info")
                    # Tente d'appeler l'API avec une requête factice pour consommer le quota
                    client = api_clients.get(api_name)
                    if client:
                        try:
                            # Utilise des paramètres génériques pour un appel simple
                            # Ces appels ne sont pas destinés à être fonctionnels, juste à consommer le quota
                            if api_name == "DEEPSEEK":
                                await client.query(prompt="Hello")
                            elif api_name == "SERPER":
                                await client.query(query_text="test")
                            elif api_name == "WOLFRAMALPHA":
                                await client.query(input_text="1+1")
                            elif api_name == "TAVILY":
                                await client.query(query_text="test")
                            elif api_name == "APIFLASH":
                                # Nécessite une URL réelle, peut être difficile à "brûler" sans spammer
                                pass 
                            elif api_name == "CRAWLBASE":
                                pass # Difficile à "brûler" sans URL
                            elif api_name == "DETECTLANGUAGE":
                                await client.query(text="hello")
                            elif api_name == "GUARDIAN":
                                await client.query(query_text="news")
                            elif api_name == "IP2LOCATION":
                                await client.query(ip_address="8.8.8.8")
                            elif api_name == "SHODAN":
                                await client.query(query_text="test")
                            elif api_name == "WEATHERAPI":
                                await client.query(location="London")
                            elif api_name == "CLOUDMERSIVE":
                                await client.query(domain="example.com")
                            elif api_name == "GREYNOISE":
                                await client.query(ip_address="8.8.8.8")
                            elif api_name == "PULSEDIVE":
                                await client.query(indicator="8.8.8.8")
                            elif api_name == "STORMGLASS":
                                await client.query(lat=0.0, lng=0.0)
                            elif api_name == "LOGINRADIUS":
                                await client.query()
                            elif api_name == "JSONBIN":
                                await client.query(data={"burn": True})
                            elif api_name == "HUGGINGFACE":
                                await client.query(input_text="test")
                            elif api_name == "TWILIO":
                                await client.query()
                            elif api_name == "ABSTRACTAPI":
                                await client.query(input_value="test@example.com", api_type="EMAIL_VALIDATION")
                            elif api_name == "GOOGLE_CUSTOM_SEARCH":
                                await client.query(query_text="test")
                            elif api_name == "RANDOMMER":
                                await client.query(quantity=1)
                            elif api_name == "TOMORROW.IO":
                                await client.query(location="London")
                            elif api_name == "OPENWEATHERMAP":
                                await client.query(location="London")
                            elif api_name == "MOCKAROO":
                                await client.query(count=1)
                            elif api_name == "OPENPAGERANK":
                                await client.query(domains=["example.com"])
                            elif api_name == "RAPIDAPI":
                                # Tente d'appeler une API RapidAPI générique si possible
                                await client.query(api_name="random fact")
                            
                            # Pour Gemini, si on veut le "brûler", on peut faire un appel simple
                            # if api_name == "GEMINI":
                            #     await gemini_client.generate_content(prompt="test", chat_history=[])

                            log_message(f"Quota pour {api_name} 'brûlé' avec succès.")
                        except Exception as e:
                            log_message(f"Erreur lors du 'brûlage' de quota pour {api_name}: {e}", level="error")
                    else:
                        log_message(f"Client API {api_name} non trouvé pour le 'brûlage' de quota.", level="warning")
        await asyncio.sleep(QUOTA_BURN_WINDOW_HOURS * 3600 / 4) # Vérifie 4 fois par fenêtre de brûlage

async def _diversification_recovery_loop():
    """Boucle de fond pour récupérer les scores de diversification des IA."""
    while True:
        memory_manager.recover_diversification_scores()
        await asyncio.sleep(API_ROTATION_INTERVAL_MINUTES * 60) # Exécute toutes les X minutes

# --- Gestionnaires de messages Telegram ---

@bot.message_handler(commands=['start', 'help'])
async def send_welcome(message: Message):
    """Envoie un message de bienvenue et d'aide."""
    user_id = await get_user_id_from_message(message)
    sender_info = get_sender_info(message)
    log_message(f"Commande /start ou /help reçue de {sender_info}")

    welcome_text = (
        "Bonjour ! Je suis votre assistant IA. Je peux vous aider avec des questions, "
        "exécuter du code, faire de l'OCR, et bien plus encore.\n\n"
        "Voici quelques commandes que vous pouvez utiliser :\n"
        "/status - Affiche le statut des APIs et les quotas.\n"
        "/run_code [langage] [code] - Exécute du code (ex: /run_code python print('Hello')).\n"
        "/ocr [URL_image] - Extrait le texte d'une image via son URL.\n"
        "/archive_page [URL] - Archive une page web et l'envoie au groupe privé.\n"
        "/burn_quota - Tente de 'brûler' les quotas API avant leur réinitialisation.\n"
        "Posez-moi simplement une question ou donnez-moi une tâche !"
    )
    await bot.reply_to(message, welcome_text)
    await memory_manager.add_message_to_history(user_id, "bot", welcome_text)

@bot.message_handler(commands=['status'])
async def get_status(message: Message):
    """Affiche le statut des APIs et les quotas d'utilisation."""
    user_id = await get_user_id_from_message(message)
    sender_info = get_sender_info(message)
    log_message(f"Commande /status reçue de {sender_info}")

    ia_status = memory_manager.ia_status
    quotas_status = quota_manager.get_all_quotas_status()

    status_text = "📊 *Statut des APIs et Quotas:*\n\n"

    for api_name, status in ia_status.items():
        quota_data = quotas_status.get(api_name, {})
        
        status_text += f"*{api_name}:*\n"
        status_text += f"  - Score de performance: `{status['current_score']:.2f}`\n"
        status_text += f"  - Score de diversification: `{status['diversification_score']:.2f}`\n"
        status_text += f"  - Erreurs consécutives: `{status['error_count']}`\n"
        status_text += f"  - En cooldown jusqu'à: `{status['cooldown_until'] or 'N/A'}`\n"
        
        if quota_data:
            status_text += f"  - Quota Mensuel: `{quota_data['monthly_usage']}/{quota_data['monthly_limit']}`\n"
            status_text += f"  - Quota Journalier: `{quota_data['daily_usage']}/{quota_data['daily_limit']}`\n"
            status_text += f"  - Quota Horaire: `{quota_data['hourly_usage']}/{quota_data['hourly_limit']}`\n"
            status_text += f"  - Dernier usage: `{quota_data['last_usage'] or 'N/A'}`\n"
        else:
            status_text += "  - _Données de quota non disponibles._\n"
        status_text += "\n"
    
    # Ajoute les APIs en mode "burn"
    burn_apis = quota_manager.get_burn_window_apis()
    if burn_apis:
        status_text += "🔥 *APIs en mode 'Brûlage' de quota:*\n"
        for api_info in burn_apis:
            status_text += f"- {api_info}\n"
    else:
        status_text += "🔥 _Aucune API en mode 'Brûlage' de quota actuellement._\n"

    await bot.reply_to(message, status_text, parse_mode="Markdown")
    await memory_manager.add_message_to_history(user_id, "bot", status_text)

@bot.message_handler(commands=['burn_quota'])
async def trigger_burn_quota(message: Message):
    """Déclenche manuellement la tentative de 'brûlage' de quota."""
    user_id = await get_user_id_from_message(message)
    sender_info = get_sender_info(message)
    log_message(f"Commande /burn_quota reçue de {sender_info}")

    burn_apis = quota_manager.get_burn_window_apis()
    if not burn_apis:
        response_text = "Aucune API n'est actuellement dans sa fenêtre de 'brûlage' de quota."
        await bot.reply_to(message, response_text)
        await memory_manager.add_message_to_history(user_id, "bot", response_text)
        return

    response_text = "Tentative de 'brûlage' de quota pour les APIs suivantes:\n" + "\n".join(burn_apis)
    await bot.reply_to(message, response_text)
    await memory_manager.add_message_to_history(user_id, "bot", response_text)

    # Déclenche la fonction de brûlage en arrière-plan
    asyncio.create_task(_quota_burn_loop()) # Appelle la boucle pour un déclenchement immédiat

@bot.message_handler(commands=['run_code'])
async def handle_run_code(message: Message):
    """Exécute le code fourni dans une sandbox."""
    user_id = await get_user_id_from_message(message)
    sender_info = get_sender_info(message)
    log_message(f"Commande /run_code reçue de {sender_info}")

    args = message.text.split(maxsplit=2) # /run_code [langage] [code]
    if len(args) < 3:
        await bot.reply_to(message, "Usage: `/run_code <langage> <votre_code>` (ex: `/run_code python print('Hello')`)", parse_mode="Markdown")
        await memory_manager.add_message_to_history(user_id, "bot", "Usage: `/run_code <langage> <votre_code>`")
        return

    language = args[1].lower()
    code_to_run = args[2]

    response_text = await run_in_sandbox(code_to_run, language)
    await bot.reply_to(message, f"```\n{response_text}\n```", parse_mode="Markdown")
    await memory_manager.add_message_to_history(user_id, "bot", response_text)

@bot.message_handler(commands=['ocr'])
async def handle_ocr_command(message: Message):
    """Effectue l'OCR sur une image à partir d'une URL."""
    user_id = await get_user_id_from_message(message)
    sender_info = get_sender_info(message)
    log_message(f"Commande /ocr reçue de {sender_info}")

    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await bot.reply_to(message, "Usage: `/ocr <URL_de_l_image>`", parse_mode="Markdown")
        await memory_manager.add_message_to_history(user_id, "bot", "Usage: `/ocr <URL_de_l_image>`")
        return

    image_url = args[1].strip()
    if not re.match(r"https?://.*\.(png|jpg|jpeg|gif|bmp|tiff|webp)$", image_url, re.IGNORECASE):
        await bot.reply_to(message, "L'URL de l'image semble invalide ou le format n'est pas supporté (doit être png, jpg, jpeg, gif, bmp, tiff, webp).")
        await memory_manager.add_message_to_history(user_id, "bot", "URL d'image invalide.")
        return

    try:
        await bot.reply_to(message, "Traitement de l'image par OCR, veuillez patienter...")
        ocr_result = await perform_ocr_api(image_url)
        await bot.reply_to(message, f"Texte extrait:\n```\n{ocr_result}\n```", parse_mode="Markdown")
        await memory_manager.add_message_to_history(user_id, "bot", f"OCR de {image_url}: {ocr_result}")
    except Exception as e:
        log_message(f"Erreur lors de l'OCR de l'image {image_url}: {e}\n{traceback.format_exc()}", level="error")
        await bot.reply_to(message, f"Une erreur est survenue lors de l'extraction du texte de l'image: {e}")
        await memory_manager.add_message_to_history(user_id, "bot", f"Erreur OCR: {e}")

@bot.message_handler(commands=['archive_page'])
async def handle_archive_page(message: Message):
    """Archive une page web et l'envoie au groupe privé."""
    user_id = await get_user_id_from_message(message)
    sender_info = get_sender_info(message)
    log_message(f"Commande /archive_page reçue de {sender_info}")

    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        await bot.reply_to(message, "Usage: `/archive_page <URL>`", parse_mode="Markdown")
        await memory_manager.add_message_to_history(user_id, "bot", "Usage: `/archive_page <URL>`")
        return

    url_to_archive = args[1].strip()
    if not url_to_archive.startswith(("http://", "https://")):
        await bot.reply_to(message, "Veuillez fournir une URL valide (commençant par http:// ou https://).")
        await memory_manager.add_message_to_history(user_id, "bot", "URL invalide pour l'archivage.")
        return
    
    await bot.reply_to(message, f"Archivage de la page {url_to_archive}, veuillez patienter...")
    try:
        await fetch_and_archive_pages([url_to_archive], user_id, bot)
        response_text = f"Page archivée et envoyée au groupe privé: {neutralize_urls(url_to_archive)}"
        await bot.reply_to(message, response_text)
        await memory_manager.add_message_to_history(user_id, "bot", response_text)
    except Exception as e:
        log_message(f"Erreur lors de l'archivage de la page {url_to_archive}: {e}\n{traceback.format_exc()}", level="error")
        await bot.reply_to(message, f"Une erreur est survenue lors de l'archivage de la page: {e}")
        await memory_manager.add_message_to_history(user_id, "bot", f"Erreur archivage: {e}")

@bot.message_handler(func=lambda message: True)
async def handle_all_messages(message: Message):
    """
    Gestionnaire principal pour tous les messages textuels.
    Traite la requête, choisit la meilleure IA, gère la mémoire et les outils.
    """
    user_id = await get_user_id_from_message(message)
    sender_info = get_sender_info(message)
    raw_text = message.text
    log_message(f"Message reçu de {sender_info}: {raw_text}")

    # Ajoute le message de l'utilisateur à l'historique
    await memory_manager.add_message_to_history(user_id, "user", raw_text)

    # Si c'est un message de groupe, l'ajoute aussi à la mémoire de groupe
    if message.chat.type != "private":
        await memory_manager.save_group_memory(user_id, "user", raw_text)

    # 1. Vérifie le cache pour un prompt similaire
    cached_response = await memory_manager.check_for_similar_prompt(user_id, raw_text)
    if cached_response:
        log_message(f"Réponse en cache trouvée pour {user_id}.")
        await bot.reply_to(message, cached_response)
        await memory_manager.add_message_to_history(user_id, "bot", cached_response)
        return

    # 2. Détecte et corrige la toxicité
    cleaned_text = detect_and_correct_toxicity(raw_text)
    if cleaned_text != raw_text:
        await bot.reply_to(message, f"Votre message a été modéré: {cleaned_text}")
        # Ne pas continuer avec l'IA si le message est juste une correction de toxicité
        await memory_manager.add_message_to_history(user_id, "bot", cleaned_text)
        return
    
    # 3. Prépare le contexte pour l'IA
    chat_history_for_gemini = await memory_manager.get_chat_history(user_id, limit=10) # 10 derniers messages
    long_term_memory_for_gemini = await memory_manager.get_long_term_memory(user_id, limit=5) # 5 dernières entrées de mémoire à long terme
    group_memory_for_gemini = ""
    if message.chat.type != "private":
        group_memory_for_gemini = await memory_manager.get_group_memory(user_id, limit=5) # 5 derniers messages de groupe

    context_parts = []
    if long_term_memory_for_gemini:
        context_parts.append(f"Mémoire à long terme de l'utilisateur:\n{long_term_memory_for_gemini}")
    if group_memory_for_gemini:
        context_parts.append(f"Contexte du groupe:\n{group_memory_for_gemini}")
    
    full_context = "\n\n".join(context_parts) if context_parts else ""

    # Ajoute les informations sur les APIs disponibles et leur statut au prompt
    available_apis = memory_manager.get_available_ias()
    api_info_for_prompt = "APIs disponibles et leur statut:\n"
    for api_name in available_apis:
        status = memory_manager.get_ia_status(api_name)
        if status:
            api_info_for_prompt += f"- {api_name}: Score {status['current_score']:.2f}, Diversification {status['diversification_score']:.2f}\n"
    
    # Ajoute la liste des outils disponibles
    tool_definitions = ""
    # Ici, vous devriez générer les définitions des outils (fonctions Python)
    # que Gemini peut appeler. Cela implique de décrire chaque fonction API
    # et les fonctions locales comme `run_in_sandbox`, `perform_ocr_api`, etc.
    # C'est une partie complexe qui dépend de la capacité de Gemini à comprendre
    # et à générer des appels de fonction.
    # Pour l'instant, nous allons utiliser une approche simplifiée ou laisser Gemini
    # générer du texte pour les outils.
    # Si vous avez un format spécifique pour les définitions d'outils, je peux l'implémenter.
    
    # Exemple de structure pour les outils (à adapter pour Gemini Function Calling)
    # tools_description = [
    #     {"name": "deepseek_query", "description": "Interroge DeepSeek pour des complétions de chat."},
    #     {"name": "serper_query", "description": "Effectue une recherche web via Serper."},
    #     # ... autres APIs
    #     {"name": "run_python_code", "description": "Exécute du code Python dans une sandbox."},
    #     {"name": "perform_ocr", "description": "Extrait le texte d'une image via OCR.space."},
    #     {"name": "archive_webpage", "description": "Archive une page web."},
    # ]
    # tool_definitions = json.dumps(tools_description) # Ceci est un exemple, le format réel dépend de Gemini

    system_instruction = (
        "Vous êtes un assistant IA avancé. Votre objectif est de répondre aux requêtes de l'utilisateur "
        "de manière utile, précise et concise. Vous avez accès à plusieurs outils et APIs pour vous aider.\n"
        "Lorsque vous utilisez un outil, indiquez clairement quel outil vous utilisez et pourquoi.\n"
        "Si une requête nécessite une recherche web, utilisez les outils de recherche disponibles.\n"
        "Si une requête est complexe ou nécessite plusieurs étapes, décomposez-la.\n"
        "N'inventez pas d'informations. Si vous ne savez pas, dites-le.\n"
        "Contexte supplémentaire de l'utilisateur et du groupe:\n"
        f"{full_context}\n\n"
        f"{api_info_for_prompt}\n"
        "Vous pouvez aussi exécuter du code Python ou Shell en utilisant la fonction `run_in_sandbox(code, language='python')`.\n"
        "Pour l'OCR, utilisez `perform_ocr_api(image_url)`.\n"
        "Pour archiver des pages web, utilisez `fetch_and_archive_pages(links, user_id, bot_instance)`.\n"
        "Pour les recherches web, utilisez `serper_client.query(query_text)` ou `tavily_client.query(query_text)`.\n"
        "Pour les calculs ou faits, utilisez `wolfram_alpha_client.query(input_text)`.\n"
        "Si l'utilisateur demande une tâche impliquant un outil, proposez d'utiliser l'outil et montrez comment.\n"
        "Si l'utilisateur demande des informations sur les quotas ou le statut des APIs, utilisez les commandes /status.\n"
        "Si l'utilisateur pose une question générale, utilisez DeepSeek."
    )

    # 4. Sélectionne la meilleure IA (basé sur le score combiné)
    selected_api_name = None
    best_combined_score = -float('inf')
    
    for api_name in available_apis:
        status = memory_manager.get_ia_status(api_name)
        if status:
            # Score combiné = (performance * poids_performance) + (diversification * poids_diversification)
            # Les poids peuvent être ajustés pour favoriser la performance ou la diversification
            combined_score = (status["current_score"] * 0.7) + (status["diversification_score"] * 0.3)
            if combined_score > best_combined_score:
                best_combined_score = combined_score
                selected_api_name = api_name
    
    if not selected_api_name:
        await bot.reply_to(message, "Désolé, aucune IA n'est actuellement disponible pour traiter votre requête.")
        await memory_manager.add_message_to_history(user_id, "bot", "Aucune IA disponible.")
        return

    log_message(f"IA sélectionnée pour {user_id}: {selected_api_name} (Score combiné: {best_combined_score:.2f})")
    await bot.send_chat_action(message.chat.id, 'typing') # Indique que le bot est en train d'écrire

    # 5. Appel à l'IA sélectionnée (ou Gemini pour le raisonnement et la sélection d'outils)
    try:
        # Pour cet exemple, nous allons d'abord laisser Gemini décider de l'outil à utiliser
        # ou répondre directement.
        # Nous allons passer le prompt de l'utilisateur et l'historique de chat à Gemini.
        
        # Le prompt pour Gemini inclura le message de l'utilisateur et les instructions système.
        # L'historique de chat sera formaté pour Gemini.
        
        gemini_chat_history_formatted = []
        for entry in chat_history_for_gemini:
            # Gemini attend les rôles 'user' et 'model'
            role = "user" if entry["role"] == "user" else "model"
            gemini_chat_history_formatted.append({"role": role, "parts": [{"text": entry["content"]}]})

        # Ajout de l'instruction système au début du prompt utilisateur pour Gemini
        # Ou comme un message de rôle "system" si Gemini le supporte directement (pas le cas via generateContent)
        # Pour generateContent, le plus simple est de l'inclure dans le premier message user
        
        # Construire le prompt final pour Gemini
        final_gemini_prompt = f"{system_instruction}\n\nRequête de l'utilisateur: {raw_text}"

        # Appel à Gemini
        gemini_response_raw = await gemini_client.generate_content(
            prompt=final_gemini_prompt,
            chat_history=gemini_chat_history_formatted,
            model="gemini-1.5-flash-latest" # Utilise le modèle flash pour la rapidité
        )

        gemini_text_response = ""
        if gemini_response_raw and not gemini_response_raw.get("error"):
            candidates = gemini_response_raw.get("candidates", [])
            if candidates:
                first_candidate = candidates[0]
                if "content" in first_candidate and "parts" in first_candidate["content"]:
                    for part in first_candidate["content"]["parts"]:
                        if "text" in part:
                            gemini_text_response += part["text"]
                        # Si Gemini génère un appel de fonction (tool_code), il faudrait le traiter ici
                        # Cela nécessiterait une structure de réponse spécifique de Gemini
                        # et une logique pour mapper le nom de la fonction générée à l'appel réel.
                        # Exemple simplifié:
                        # if "functionCall" in part:
                        #     function_name = part["functionCall"]["name"]
                        #     function_args = part["functionCall"]["args"]
                        #     # Exécuter la fonction et renvoyer le résultat à Gemini pour la réponse finale
                        #     # C'est un cycle complexe qui n'est pas directement supporté par l'API generateContent simple.
                        #     # Pour cet exemple, nous nous basons sur la capacité de Gemini à "suggérer" l'utilisation d'outils
                        #     # par du texte, et le bot interprète ensuite ce texte.
            else:
                gemini_text_response = "Gemini n'a pas pu générer de réponse."
        else:
            gemini_text_response = f"Erreur lors de l'appel à Gemini: {gemini_response_raw.get('error', 'Inconnu')}"

        # 6. Interprétation de la réponse de l'IA et exécution des outils
        final_bot_response = gemini_text_response
        tool_executed = False

        # Logique d'interprétation pour les appels d'outils basés sur le texte de Gemini
        # Ceci est une simplification. Dans un système de "Function Calling" natif,
        # Gemini renverrait un objet structuré directement.
        
        # Détection d'appel de code
        if "```python" in gemini_text_response or "```shell" in gemini_text_response:
            match_python = re.search(r"```python\n(.*?)```", gemini_text_response, re.DOTALL)
            match_shell = re.search(r"```shell\n(.*?)```", gemini_text_response, re.DOTALL)
            
            if match_python:
                code_to_execute = match_python.group(1).strip()
                log_message(f"Gemini a suggéré l'exécution de code Python: {code_to_execute[:100]}...")
                tool_output = await run_in_sandbox(code_to_execute, "python")
                final_bot_response = f"J'ai exécuté le code Python:\n```\n{code_to_execute}\n```\nRésultat:\n```\n{tool_output}\n```"
                tool_executed = True
            elif match_shell:
                code_to_execute = match_shell.group(1).strip()
                log_message(f"Gemini a suggéré l'exécution de code Shell: {code_to_execute[:100]}...")
                tool_output = await run_in_sandbox(code_to_execute, "shell")
                final_bot_response = f"J'ai exécuté la commande Shell:\n```\n{code_to_execute}\n```\nRésultat:\n```\n{tool_output}\n```"
                tool_executed = True
        
        # Détection d'appel OCR
        elif "perform_ocr_api(" in gemini_text_response:
            match = re.search(r"perform_ocr_api\(['\"](.*?)['\"]\)", gemini_text_response)
            if match:
                image_url = match.group(1)
                log_message(f"Gemini a suggéré l'exécution de l'OCR sur: {image_url}")
                tool_output = await perform_ocr_api(image_url)
                final_bot_response = f"J'ai effectué l'OCR sur l'image:\n{tool_output}"
                tool_executed = True

        # Détection d'appel d'archivage
        elif "fetch_and_archive_pages(" in gemini_text_response:
            match = re.search(r"fetch_and_archive_pages\(\[(.*?)\],", gemini_text_response)
            if match:
                links_str = match.group(1)
                links = [link.strip().strip("'\"") for link in links_str.split(',')]
                log_message(f"Gemini a suggéré l'archivage des pages: {links}")
                await fetch_and_archive_pages(links, user_id, bot)
                final_bot_response = f"J'ai archivé les pages demandées et les ai envoyées au groupe privé."
                tool_executed = True
        
        # Détection d'appels API spécifiques (simplifié, idéalement via Function Calling)
        # Exemple pour SerperClient
        elif "serper_client.query(" in gemini_text_response:
            match = re.search(r"serper_client\.query\(['\"](.*?)['\"]\)", gemini_text_response)
            if match:
                query_text = match.group(1)
                log_message(f"Gemini a suggéré une recherche Serper pour: {query_text}")
                serper_client_instance = api_clients.get("SERPER")
                if serper_client_instance:
                    tool_output = await serper_client_instance.query(query_text)
                    final_bot_response = f"Résultat de la recherche web:\n{tool_output}"
                    tool_executed = True
                else:
                    final_bot_response = "L'outil de recherche Serper n'est pas disponible."
        
        # Exemple pour WolframAlphaClient
        elif "wolfram_alpha_client.query(" in gemini_text_response:
            match = re.search(r"wolfram_alpha_client\.query\(['\"](.*?)['\"]\)", gemini_text_response)
            if match:
                input_text = match.group(1)
                log_message(f"Gemini a suggéré un calcul WolframAlpha pour: {input_text}")
                wolfram_client_instance = api_clients.get("WOLFRAMALPHA")
                if wolfram_client_instance:
                    tool_output = await wolfram_client_instance.query(input_text)
                    final_bot_response = f"Résultat WolframAlpha:\n{tool_output}"
                    tool_executed = True
                else:
                    final_bot_response = "L'outil WolframAlpha n'est pas disponible."

        # Si aucun outil n'a été exécuté, la réponse de Gemini est la réponse finale.
        if not tool_executed:
            final_bot_response = gemini_text_response
            log_message(f"Gemini a répondu directement: {final_bot_response[:200]}...")
        
        # 7. Met à jour le statut de l'IA (Gemini pour cet exemple) et les quotas
        memory_manager.update_ia_status("GEMINI", success=True) # Supposons que Gemini a réussi
        await quota_manager.check_and_update_quota("GEMINI", cost=1) # Coût de 1 par appel

    except Exception as e:
        log_message(f"Erreur inattendue lors du traitement du message: {e}\n{traceback.format_exc()}", level="error")
        final_bot_response = "Désolé, une erreur interne est survenue. Veuillez réessayer plus tard."
        memory_manager.update_ia_status("GEMINI", success=False, error_message=str(e)) # Marque Gemini comme ayant échoué

    # 8. Envoie la réponse finale à l'utilisateur
    await bot.reply_to(message, final_bot_response)
    await memory_manager.add_message_to_history(user_id, "bot", final_bot_response)

    # Si c'est un message de groupe, l'ajoute aussi à la mémoire de groupe
    if message.chat.type != "private":
        await memory_manager.save_group_memory(user_id, "bot", final_bot_response)

# --- Boucle principale d'exécution ---
async def main():
    """Fonction principale pour initialiser et démarrer le bot."""
    log_message("Démarrage de l'initialisation du bot...")
    
    # Initialisation des gestionnaires
    await endpoint_health_manager.init_manager()
    await memory_manager.init_manager()
    await quota_manager.init_manager()

    log_message("Gestionnaires initialisés. Démarrage des boucles de fond...")
    
    # Démarrage des boucles de fond
    asyncio.create_task(_health_check_loop())
    asyncio.create_task(_quota_burn_loop())
    asyncio.create_task(_diversification_recovery_loop())

    log_message("Boucles de fond démarrées. Démarrage du polling du bot...")
    
    # Démarrage du polling du bot
    await bot.infinity_polling()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        log_message("Bot arrêté manuellement.")
    except Exception as e:
        log_message(f"Erreur fatale dans la boucle principale: {e}\n{traceback.format_exc()}", level="critical")q

   
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
WEATHERAPI_KEY = "YOUR_WEATHERAPI_KEY_HERE"
CLOUDMERSIVE_API_KEY = "YOUR_CLOUDMERSIVE_API_KEY_HERE"
GREYNOISE_API_KEY = "YOUR_GREYNOISE_API_KEY_HERE"
PULSEDIVE_API_KEY = "YOUR_PULSEDIVE_API_KEY_HERE"
STORMGLASS_API_KEY = "YOUR_STORMGLASS_API_KEY_HERE"
LOGINRADIUS_API_KEY = "YOUR_LOGINRADIUS_API_KEY_HERE"
JSONBIN_API_KEY = "YOUR_JSONBIN_API_KEY_HERE"
HUGGINGFACE_API_KEYS = [
    "hf_YOUR_HUGGINGFACE_API_KEY_1",
    "hf_YOUR_HUGGINGFACE_API_KEY_2"
]
TWILIO_ACCOUNT_SID = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
ABSTRACTAPI_API_KEYS = [
    "YOUR_ABSTRACTAPI_API_KEY_1",
    "YOUR_ABSTRACTAPI_API_KEY_2"
]
GOOGLE_CUSTOM_SEARCH_API_KEYS = [
    "YOUR_GOOGLE_CUSTOM_SEARCH_API_KEY_1",
    "YOUR_GOOGLE_CUSTOM_SEARCH_API_KEY_2"
]
GOOGLE_CUSTOM_SEARCH_CX_LIST = [
    "YOUR_GOOGLE_CUSTOM_SEARCH_CX_1",
    "YOUR_GOOGLE_CUSTOM_SEARCH_CX_2"
]
RANDOMMER_API_KEY = "YOUR_RANDOMMER_API_KEY_HERE"
TOMORROWIO_API_KEY = "YOUR_TOMORROWIO_API_KEY_HERE"
OPENWEATHERMAP_API_KEY = "YOUR_OPENWEATHERMAP_API_KEY_HERE"
MOCKAROO_API_KEY = "YOUR_MOCKAROO_API_KEY_HERE"
OPENPAGERANK_API_KEY = "YOUR_OPENPAGERANK_API_KEY_HERE"
RAPIDAPI_KEY = "YOUR_RAPIDAPI_KEY_HERE"


# Configuration détaillée des endpoints API
API_CONFIG = {
    "GEMINI_API": [
        {
            "endpoint_name": f"Gemini Chat (Key {i+1})",
            "url": "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent",
            "method": "POST",
            "key": key,
            "key_field": "key",
            "key_location": "param",
            "timeout": 60,
            "health_check_params": {"prompt": "test"},
            "health_check_url_suffix": f"?key={key}"
        }
        for i, key in enumerate(GEMINI_API_KEYS)
    ],
    "OCR_API": [
        {
            "endpoint_name": f"OCR.space (Key {i+1})",
            "url": "https://api.ocr.space/parse/image",
            "method": "POST",
            "key": key,
            "key_field": "apikey",
            "key_location": "header",
            "timeout": 30,
            "fixed_headers": {"Content-Type": "application/json"},
            "health_check_json": {"base64Image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=", "language": "eng"}, # Minimal valid base64 for health check
        }
        for i, key in enumerate(OCR_API_KEYS)
    ],
    "DEEPSEEK": [
        {
            "endpoint_name": f"DeepSeek Chat (Key {i+1})",
            "url": "https://api.deepseek.com/chat/completions",
            "method": "POST",
            "key": key,
            "key_field": "Authorization",
            "key_location": "header",
            "key_prefix": "Bearer ",
            "timeout": 60,
            "fixed_headers": {"Content-Type": "application/json"},
            "health_check_json": {"model": "deepseek-chat", "messages": [{"role": "user", "content": "hi"}]}
        }
        for i, key in enumerate(DEEPSEEK_API_KEYS)
    ],
    "SERPER": [
        {
            "endpoint_name": "Serper Search",
            "url": "https://google.serper.dev/search",
            "method": "POST",
            "key": SERPER_API_KEY,
            "key_field": "X-API-KEY",
            "key_location": "header",
            "timeout": 30,
            "fixed_headers": {"Content-Type": "application/json"},
            "health_check_json": {"q": "test"}
        }
    ],
    "WOLFRAMALPHA": [
        {
            "endpoint_name": f"WolframAlpha Query (App ID {i+1})",
            "url": "http://api.wolframalpha.com/v2/query",
            "method": "GET",
            "key": app_id,
            "key_field": "appid",
            "key_location": "param",
            "timeout": 30,
            "fixed_params": {"output": "json"},
            "health_check_params": {"input": "2+2", "output": "json"}
        }
        for i, app_id in enumerate(WOLFRAMALPHA_APP_IDS)
    ],
    "TAVILY": [
        {
            "endpoint_name": f"Tavily Search (Key {i+1})",
            "url": "https://api.tavily.com/parse",
            "method": "POST",
            "key": key,
            "key_field": "apikey",
            "key_location": "header",
            "timeout": 30,
            "fixed_headers": {"Content-Type": "application/json"},
            "health_check_json": {"query": "test", "max_results": 1}
        }
        for i, key in enumerate(TAVILY_API_KEYS)
    ],
    "APIFLASH": [
        {
            "endpoint_name": "ApiFlash Screenshot",
            "url": "https://api.apiflash.com/v1/urltoimage",
            "method": "GET",
            "key": APIFLASH_ACCESS_KEY,
            "key_field": "access_key",
            "key_location": "param",
            "timeout": 45,
            "health_check_params": {"url": "example.com", "format": "jpeg"}
        }
    ],
    "CRAWLBASE": [
        {
            "endpoint_name": "Crawlbase Scraper",
            "url": "https://api.crawlbase.com/",
            "method": "GET",
            "key": CRAWLBASE_API_KEY,
            "key_field": "token",
            "key_location": "param",
            "timeout": 60,
            "health_check_params": {"url": "http://example.com", "format": "json"}
        },
        {
            "endpoint_name": "Crawlbase JS Scraper",
            "url": "https://api.crawlbase.com/js",
            "method": "GET",
            "key": CRAWLBASE_API_KEY,
            "key_field": "token",
            "key_location": "param",
            "timeout": 90,
            "health_check_params": {"url": "http://example.com", "format": "json"}
        }
    ],
    "DETECTLANGUAGE": [
        {
            "endpoint_name": "DetectLanguage Detect",
            "url": "https://ws.detectlanguage.com/0.2/detect",
            "method": "POST",
            "key": DETECTLANGUAGE_API_KEY,
            "key_field": "X-Detectlanguage-Api-Key",
            "key_location": "header",
            "timeout": 15,
            "fixed_headers": {"Content-Type": "application/json"},
            "health_check_json": {"q": "Hello world"}
        }
    ],
    "GUARDIAN": [
        {
            "endpoint_name": "Guardian Content",
            "url": "https://content.guardianapis.com/search",
            "method": "GET",
            "key": GUARDIAN_API_KEY,
            "key_field": "api-key",
            "key_location": "param",
            "timeout": 20,
            "health_check_params": {"q": "test"}
        }
    ],
    "IP2LOCATION": [
        {
            "endpoint_name": "IP2Location Geolocation",
            "url": "https://api.ip2location.com/v2/",
            "method": "GET",
            "key": IP2LOCATION_API_KEY,
            "key_field": "key",
            "key_location": "param",
            "timeout": 10,
            "health_check_params": {"ip": "8.8.8.8", "addon": "country,city"}
        }
    ],
    "SHODAN": [
        {
            "endpoint_name": "Shodan API Info",
            "url": "https://api.shodan.io/api-info",
            "method": "GET",
            "key": SHODAN_API_KEY,
            "key_field": "key",
            "key_location": "param",
            "timeout": 15,
            "health_check_url_suffix": f"?key={SHODAN_API_KEY}"
        },
        {
            "endpoint_name": "Shodan Host Info",
            "url": "https://api.shodan.io/shodan/host",
            "method": "GET",
            "key": SHODAN_API_KEY,
            "key_field": "key",
            "key_location": "param",
            "timeout": 20,
            "health_check_url_suffix": f"/8.8.8.8?key={SHODAN_API_KEY}"
        }
    ],
    "WEATHERAPI": [
        {
            "endpoint_name": "WeatherAPI Current",
            "url": "http://api.weatherapi.com/v1/current.json",
            "method": "GET",
            "key": WEATHERAPI_KEY,
            "key_field": "key",
            "key_location": "param",
            "timeout": 15,
            "health_check_params": {"q": "London"}
        }
    ],
    "CLOUDMERSIVE": [
        {
            "endpoint_name": "Cloudmersive Validate Domain",
            "url": "https://api.cloudmersive.com/validate/domain/full",
            "method": "POST",
            "key": CLOUDMERSIVE_API_KEY,
            "key_field": "Apikey",
            "key_location": "header",
            "timeout": 20,
            "fixed_headers": {"Content-Type": "application/json"},
            "health_check_json": {"domain": "example.com"}
        }
    ],
    "GREYNOISE": [
        {
            "endpoint_name": "GreyNoise IP Lookup",
            "url": "https://api.greynoise.io/v3/community",
            "method": "GET",
            "key": GREYNOISE_API_KEY,
            "key_field": "key",
            "key_location": "header",
            "timeout": 20,
            "health_check_url_suffix": "/8.8.8.8"
        }
    ],
    "PULSEDIVE": [
        {
            "endpoint_name": "Pulsedive Indicator",
            "url": "https://pulsedive.com/api/v1/indicator.php",
            "method": "GET",
            "key": PULSEDIVE_API_KEY,
            "key_field": "key",
            "key_location": "param",
            "timeout": 25,
            "fixed_params": {"pretty": "1"},
            "health_check_params": {"indicator": "8.8.8.8", "pretty": "1"}
        }
    ],
    "STORMGLASS": [
        {
            "endpoint_name": "StormGlass Weather",
            "url": "https://api.stormglass.io/v2/weather/point",
            "method": "GET",
            "key": STORMGLASS_API_KEY,
            "key_field": "Authorization",
            "key_location": "header",
            "timeout": 30,
            "health_check_params": {"lat": 0, "lng": 0, "params": "airTemperature", "start": 0, "end": 0},
            "health_check_url_suffix": "?lat=0&lng=0&params=airTemperature&start=0&end=0"
        }
    ],
    "LOGINRADIUS": [
        {
            "endpoint_name": "LoginRadius Ping",
            "url": "https://api.loginradius.com/identity/v2/auth/ping",
            "method": "GET",
            "key": LOGINRADIUS_API_KEY,
            "key_field": "apiKey",
            "key_location": "param",
            "timeout": 10,
            "health_check_url_suffix": f"?apiKey={LOGINRADIUS_API_KEY}"
        }
    ],
    "JSONBIN": [
        {
            "endpoint_name": "Bin Create",
            "url": "https://api.jsonbin.io/v3/b",
            "method": "POST",
            "key": JSONBIN_API_KEY,
            "key_field": "X-Master-Key",
            "key_location": "header",
            "timeout": 20,
            "fixed_headers": {"Content-Type": "application/json", "X-Bin-Private": "true"},
            "health_check_json": {"test": "data"}
        },
        {
            "endpoint_name": "Bin Access",
            "url": "https://api.jsonbin.io/v3/b",
            "method": "GET",
            "key": JSONBIN_API_KEY,
            "key_field": "X-Master-Key",
            "key_location": "header",
            "timeout": 20,
            "health_check_url_suffix": "/60c7b9b0f1a9a87d2b7b7b7b"
        }
    ],
    "HUGGINGFACE": [
        {
            "endpoint_name": f"HuggingFace Inference (Key {i+1})",
            "url": "https://api-inference.huggingface.co/models/",
            "method": "POST",
            "key": key,
            "key_field": "Authorization",
            "key_location": "header",
            "key_prefix": "Bearer ",
            "timeout": 60,
            "fixed_headers": {"Content-Type": "application/json"},
            "health_check_url_suffix": "distilbert-base-uncased-finetuned-sst-2-english",
            "health_check_json": {"inputs": "Hello world"}
        }
        for i, key in enumerate(HUGGINGFACE_API_KEYS)
    ],
    "TWILIO": [
        {
            "endpoint_name": "Account Balance",
            "url": f"https://api.twilio.com/2010-04-01/Accounts/{TWILIO_ACCOUNT_SID}/Balance.json",
            "method": "GET",
            "key": (TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN),
            "key_location": "auth_basic",
            "timeout": 20,
            "health_check_url_suffix": ""
        }
    ],
    "ABSTRACTAPI": [
        {
            "endpoint_name": f"Email Validation (Key {i+1})",
            "url": "https://emailvalidation.abstractapi.com/v1/?",
            "method": "GET",
            "key": key,
            "key_field": "api_key",
            "key_location": "param",
            "timeout": 15,
            "health_check_params": {"email": "test@example.com"}
        }
        for i, key in enumerate(ABSTRACTAPI_API_KEYS)
    ] + [
        {
            "endpoint_name": f"Phone Validation (Key {i+1})",
            "url": "https://phonevalidation.abstractapi.com/v1/?",
            "method": "GET",
            "key": key,
            "key_field": "api_key",
            "key_location": "param",
            "timeout": 15,
            "health_check_params": {"phone": "14151234567"}
        }
        for i, key in enumerate(ABSTRACTAPI_API_KEYS)
    ] + [
        {
            "endpoint_name": f"Exchange Rates (Key {i+1})",
            "url": "https://exchangerates.abstractapi.com/v1/live",
            "method": "GET",
            "key": key,
            "key_field": "api_key",
            "key_location": "param",
            "timeout": 15,
            "health_check_params": {"base": "USD"}
        }
        for i, key in enumerate(ABSTRACTAPI_API_KEYS)
    ] + [
        {
            "endpoint_name": f"Holidays (Key {i+1})",
            "url": "https://holidays.abstractapi.com/v1/",
            "method": "GET",
            "key": key,
            "key_field": "api_key",
            "key_location": "param",
            "timeout": 15,
            "health_check_params": {"country": "US", "year": "2023", "month": "1", "day": "1"}
        }
        for i, key in enumerate(ABSTRACTAPI_API_KEYS)
    ],
    "GOOGLE_CUSTOM_SEARCH": [
        {
            "endpoint_name": f"Google Custom Search (API Key {i+1}, CX {j+1})",
            "url": "https://www.googleapis.com/customsearch/v1",
            "method": "GET",
            "key": GOOGLE_CUSTOM_SEARCH_API_KEYS[i],
            "key_field": "key",
            "key_location": "param",
            "timeout": 30,
            "fixed_params": {"cx": GOOGLE_CUSTOM_SEARCH_CX_LIST[j]},
            "health_check_params": {"q": "test", "cx": GOOGLE_CUSTOM_SEARCH_CX_LIST[j]}
        }
        for i in range(len(GOOGLE_CUSTOM_SEARCH_API_KEYS))
        for j in range(len(GOOGLE_CUSTOM_SEARCH_CX_LIST))
    ],
    "RANDOMMER": [
        {
            "endpoint_name": "Randommer Phone Numbers",
            "url": "https://randommer.io/api/Phone/Generate",
            "method": "GET",
            "key": RANDOMMER_API_KEY,
            "key_field": "X-Api-Key",
            "key_location": "header",
            "timeout": 15,
            "fixed_headers": {"Content-Type": "application/json"},
            "health_check_params": {"CountryCode": "US", "Quantity": 1}
        }
    ],
    "TOMORROW.IO": [
        {
            "endpoint_name": "Tomorrow.io Weather",
            "url": "https://api.tomorrow.io/v4/weather/realtime",
            "method": "GET",
            "key": TOMORROWIO_API_KEY,
            "key_field": "apikey",
            "key_location": "param",
            "timeout": 20,
            "health_check_params": {"location": "42.3478,-71.0466", "fields": "temperature"}
        }
    ],
    "OPENWEATHERMAP": [
        {
            "endpoint_name": "OpenWeatherMap Current",
            "url": "https://api.openweathermap.org/data/2.5/weather",
            "method": "GET",
            "key": OPENWEATHERMAP_API_KEY,
            "key_field": "appid",
            "key_location": "param",
            "timeout": 15,
            "health_check_params": {"q": "London"}
        }
    ],
    "MOCKAROO": [
        {
            "endpoint_name": "Mockaroo Generate Data",
            "url": "https://api.mockaroo.com/api/generate.json",
            "method": "GET",
            "key": MOCKAROO_API_KEY,
            "key_field": "key",
            "key_location": "param",
            "timeout": 30,
            "health_check_params": {"count": 1, "fields": '[{"name":"id","type":"Row Number"}]'}
        }
    ],
    "OPENPAGERANK": [
        {
            "endpoint_name": "OpenPageRank Domains",
            "url": "https://openpagerank.com/api/v1.0/getPageRank",
            "method": "GET",
            "key": OPENPAGERANK_API_KEY,
            "key_field": "api_key",
            "key_location": "param",
            "timeout": 20,
            "health_check_params": {"domains[]": ["google.com"]}
        }
    ],
    "RAPIDAPI": [
        {
            "endpoint_name": "RapidAPI Programming Joke",
            "url": "https://programming-jokes-api.p.rapidapi.com/jokes/random",
            "method": "GET",
            "key": RAPIDAPI_KEY,
            "key_field": "X-RapidAPI-Key",
            "key_location": "header",
            "timeout": 20,
            "fixed_headers": {"X-RapidAPI-Host": "programming-jokes-api.p.rapidapi.com"},
            "health_check_url_suffix": ""
        },
        {
            "endpoint_name": "RapidAPI Currency List Quotes",
            "url": "https://currency-exchange.p.rapidapi.com/listquotes",
            "method": "GET",
            "key": RAPIDAPI_KEY,
            "key_field": "X-RapidAPI-Key",
            "key_location": "header",
            "timeout": 20,
            "fixed_headers": {"X-RapidAPI-Host": "currency-exchange.p.rapidapi.com"},
            "health_check_url_suffix": ""
        },
        {
            "endpoint_name": "RapidAPI Random Fact",
            "url": "https://random-facts-api.p.rapidapi.com/api/random",
            "method": "GET",
            "key": RAPIDAPI_KEY,
            "key_field": "X-RapidAPI-Key",
            "key_location": "header",
            "timeout": 20,
            "fixed_headers": {"X-RapidAPI-Host": "random-facts-api.p.rapidapi.com"},
            "health_check_url_suffix": ""
        }
    ]
}

# ==============================================================================
# Configuration des Modèles Gemini
# ==============================================================================

# Paramètres de génération pour l'API Gemini
GEMINI_TEMPERATURE = 0.7
GEMINI_TOP_P = 0.95
GEMINI_TOP_K = 40
GEMINI_MAX_OUTPUT_TOKENS = 8192

# Paramètres de sécurité pour l'API Gemini
GEMINI_SAFETY_SETTINGS = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]

# ==============================================================================
# Configuration des Outils (Tool Calling)
# ==============================================================================

# Définition des outils que le bot peut utiliser via le "Function Calling"
TOOL_CONFIG = {
    "serper_query": {
        "description": "Effectue une recherche web via l'API Serper et retourne les snippets pertinents.",
        "parameters": {
            "type": "object",
            "properties": {
                "query_text": {"type": "string", "description": "La requête de recherche."}
            },
            "required": ["query_text"]
        }
    },
    "wolframalpha_query": {
        "description": "Interroge WolframAlpha pour des calculs, des faits ou des données complexes.",
        "parameters": {
            "type": "object",
            "properties": {
                "input_text": {"type": "string", "description": "La requête à soumettre à WolframAlpha."}
            },
            "required": ["input_text"]
        }
    },
    "tavily_query": {
        "description": "Effectue une recherche web avancée via l'API Tavily, fournissant des extraits et une réponse directe.",
        "parameters": {
            "type": "object",
            "properties": {
                "query_text": {"type": "string", "description": "La requête de recherche."},
                "max_results": {"type": "integer", "description": "Nombre maximum de résultats à retourner.", "default": 3}
            },
            "required": ["query_text"]
        }
    },
    "run_in_sandbox": {
        "description": "Exécute du code Python ou Shell dans un environnement sandbox simulé et retourne la sortie.",
        "parameters": {
            "type": "object",
            "properties": {
                "code": {"type": "string", "description": "Le code à exécuter."},
                "language": {"type": "string", "description": "Le langage du code ('python' ou 'shell').", "enum": ["python", "shell"], "default": "python"}
            },
            "required": ["code"]
        }
    },
    "perform_ocr_api": {
        "description": "Effectue une reconnaissance optique de caractères (OCR) sur une image donnée par URL et retourne le texte extrait.",
        "parameters": {
            "type": "object",
            "properties": {
                "image_url": {"type": "string", "description": "L'URL de l'image à traiter par OCR."}
            },
            "required": ["image_url"]
        }
    },
    "fetch_and_archive_pages": {
        "description": "Récupère le contenu de pages web spécifiées, les archive localement et envoie les liens d'archive au groupe privé.",
        "parameters": {
            "type": "object",
            "properties": {
                "links": {"type": "array", "items": {"type": "string"}, "description": "Liste des URLs des pages à archiver."},
                "user_id": {"type": "string", "description": "L'ID de l'utilisateur demandant l'archivage."}
            },
            "required": ["links", "user_id"]
        }
    },
    "ocr_extract_text": {
        "description": "Extrait le texte d'une image encodée en base64 en utilisant l'OCR. Utile pour les images directement fournies dans le chat.",
        "parameters": {
            "type": "object",
            "properties": {
                "image_base64": {"type": "string", "description": "L'image encodée en base64, incluant le préfixe mimeType (ex: 'data:image/png;base64,...')."}
            },
            "required": ["image_base64"]
        }
    },
    "apiflash_query": {
        "description": "Capture une capture d'écran d'une URL via ApiFlash et retourne l'URL de l'image capturée.",
        "parameters": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "L'URL de la page à capturer."}
            },
            "required": ["url"]
        }
    },
    "crawlbase_query": {
        "description": "Scrape le contenu HTML ou JavaScript d'une URL via Crawlbase. Utilisez 'use_js' pour les pages dynamiques.",
        "parameters": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "L'URL de la page à scraper."},
                "use_js": {"type": "boolean", "description": "Définir à true pour le scraping JavaScript.", "default": False}
            },
            "required": ["url"]
        }
    },
    "detectlanguage_query": {
        "description": "Détecte la langue d'un texte via DetectLanguage API.",
        "parameters": {
            "type": "object",
            "properties": {
                "text": {"type": "string", "description": "Le texte dont la langue doit être détectée."}
            },
            "required": ["text"]
        }
    },
    "guardian_query": {
        "description": "Recherche des articles de presse via l'API The Guardian.",
        "parameters": {
            "type": "object",
            "properties": {
                "query_text": {"type": "string", "description": "La requête de recherche pour les articles."}
            },
            "required": ["query_text"]
        }
    },
    "ip2location_query": {
        "description": "Géolocalise une adresse IP via IP2Location API.",
        "parameters": {
            "type": "object",
            "properties": {
                "ip_address": {"type": "string", "description": "L'adresse IP à géolocaliser."}
            },
            "required": ["ip_address"]
        }
    },
    "shodan_query": {
        "description": "Interroge Shodan pour des informations sur un hôte IP ou des informations sur la clé API.",
        "parameters": {
            "type": "object",
            "properties": {
                "query_text": {"type": "string", "description": "L'adresse IP à rechercher ou vide pour les infos de la clé API."}
            },
            "required": []
        }
    },
    "weatherapi_query": {
        "description": "Récupère les conditions météorologiques actuelles pour une localisation via WeatherAPI.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "La ville ou le code postal pour la météo."}
            },
            "required": ["location"]
        }
    },
    "cloudmersive_query": {
        "description": "Vérifie la validité et le type d'un domaine via Cloudmersive API.",
        "parameters": {
            "type": "object",
            "properties": {
                "domain": {"type": "string", "description": "Le nom de domaine à vérifier."}
            },
            "required": ["domain"]
        }
    },
    "greynoise_query": {
        "description": "Analyse une adresse IP pour détecter des activités 'bruit' (malveillantes) via GreyNoise.",
        "parameters": {
            "type": "object",
            "properties": {
                "ip_address": {"type": "string", "description": "L'adresse IP à analyser."}
            },
            "required": ["ip_address"]
        }
    },
    "pulsedive_query": {
        "description": "Analyse un indicateur de menace (IP, domaine, URL) via Pulsedive.",
        "parameters": {
            "type": "object",
            "properties": {
                "indicator": {"type": "string", "description": "L'indicateur de menace à analyser (IP, domaine, URL)."},
                "type": {"type": "string", "description": "Le type d'indicateur ('auto', 'ip', 'domain', 'url').", "default": "auto"}
            },
            "required": ["indicator"]
        }
    },
    "stormglass_query": {
        "description": "Récupère les données météorologiques maritimes pour une coordonnée (latitude, longitude) via StormGlass.",
        "parameters": {
            "type": "object",
            "properties": {
                "lat": {"type": "number", "format": "float", "description": "La latitude."},
                "lng": {"type": "number", "format": "float", "description": "La longitude."},
                "params": {"type": "string", "description": "Paramètres météo à récupérer (ex: 'airTemperature,waveHeight').", "default": "airTemperature,waveHeight"}
            },
            "required": ["lat", "lng"]
        }
    },
    "loginradius_query": {
        "description": "Effectue un simple ping à l'API LoginRadius pour vérifier sa disponibilité.",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    },
    "jsonbin_query": {
        "description": "Crée un nouveau 'bin' JSON ou accède à un bin existant via Jsonbin.io.",
        "parameters": {
            "type": "object",
            "properties": {
                "data": {"type": "object", "description": "Les données JSON à sauvegarder lors de la création d'un bin.", "nullable": True},
                "private": {"type": "boolean", "description": "Indique si le bin doit être privé (true) ou public (false).", "default": True},
                "bin_id": {"type": "string", "description": "L'ID du bin existant à accéder (si pas de 'data').", "nullable": True}
            },
            "required": []
        }
    },
    "huggingface_query": {
        "description": "Effectue une inférence sur un modèle HuggingFace (ex: classification de texte, génération).",
        "parameters": {
            "type": "object",
            "properties": {
                "model_name": {"type": "string", "description": "Le nom du modèle HuggingFace à utiliser (ex: 'distilbert-base-uncased-finetuned-sst-2-english').", "default": "distilbert-base-uncased-finetuned-sst-2-english"},
                "input_text": {"type": "string", "description": "Le texte d'entrée pour l'inférence."}
            },
            "required": ["input_text"]
        }
    },
    "twilio_query": {
        "description": "Récupère le solde du compte Twilio.",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    },
    "abstractapi_query": {
        "description": "Interroge diverses APIs d'AbstractAPI (validation email/téléphone, taux de change, jours fériés).",
        "parameters": {
            "type": "object",
            "properties": {
                "input_value": {"type": "string", "description": "La valeur d'entrée (email, numéro de téléphone, code pays, devise de base)."},
                "api_type": {"type": "string", "description": "Le type d'API AbstractAPI à utiliser ('PHONE_VALIDATION', 'EMAIL_VALIDATION', 'EXCHANGE_RATES', 'HOLIDAYS').", "enum": ["PHONE_VALIDATION", "EMAIL_VALIDATION", "EXCHANGE_RATES", "HOLIDAYS"]}
            },
            "required": ["api_type"]
        }
    },
    "google_custom_search_query": {
        "description": "Effectue une recherche personnalisée Google via l'API Custom Search.",
        "parameters": {
            "type": "object",
            "properties": {
                "query_text": {"type": "string", "description": "La requête de recherche."}
            },
            "required": ["query_text"]
        }
    },
    "randommer_query": {
        "description": "Génère des numéros de téléphone aléatoires via Randommer.io.",
        "parameters": {
            "type": "object",
            "properties": {
                "country_code": {"type": "string", "description": "Le code pays (ex: 'US', 'FR').", "default": "US"},
                "quantity": {"type": "integer", "description": "Le nombre de numéros à générer.", "default": 1}
            },
            "required": []
        }
    },
    "tomorrowio_query": {
        "description": "Récupère les prévisions météorologiques via Tomorrow.io.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "La localisation (nom de ville, code postal ou coordonnées)."},
                "fields": {"type": "array", "items": {"type": "string"}, "description": "Liste des champs météo à récupérer (ex: ['temperature', 'humidity']).", "default": ["temperature", "humidity", "windSpeed"]}
            },
            "required": ["location"]
        }
    },
    "openweathermap_query": {
        "description": "Récupère les conditions météorologiques actuelles pour une localisation via OpenWeatherMap.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "La ville ou le code postal pour la météo."}
            },
            "required": ["location"]
        }
    },
    "mockaroo_query": {
        "description": "Génère des données de test via Mockaroo.",
        "parameters": {
            "type": "object",
            "properties": {
                "count": {"type": "integer", "description": "Le nombre d'enregistrements à générer.", "default": 1},
                "fields_json": {"type": "string", "description": "Une chaîne JSON décrivant les champs à générer (ex: '[{\"name\":\"name\",\"type\":\"Full Name\"}]').", "nullable": True}
            },
            "required": []
        }
    },
    "openpagerank_query": {
        "description": "Récupère le PageRank de domaines via OpenPageRank.",
        "parameters": {
            "type": "object",
            "properties": {
                "domains": {"type": "array", "items": {"type": "string"}, "description": "Liste des noms de domaine à vérifier."}
            },
            "required": ["domains"]
        }
    },
    "rapidapi_query": {
        "description": "Interroge diverses APIs disponibles via RapidAPI (blagues, taux de change, faits aléatoires).",
        "parameters": {
            "type": "object",
            "properties": {
                "api_name": {"type": "string", "description": "Le nom de l'API RapidAPI à utiliser (ex: 'Programming Joke', 'Currency List Quotes', 'Random Fact').", "enum": ["Programming Joke", "Currency List Quotes", "Random Fact"]},
                "kwargs": {"type": "object", "description": "Arguments supplémentaires spécifiques à l'API RapidAPI appelée.", "additionalProperties": True}
            },
            "required": ["api_name"]
        }
    }
}

# ==============================================================================
# Paramètres du Chat et de la Mémoire
# ==============================================================================

# Longueur maximale de l'historique du chat à conserver en mémoire et sur disque
MAX_CHAT_HISTORY_LENGTH = 20

# ==============================================================================
# Paramètres des Checks de Santé des Endpoints
# ==============================================================================

# Activer ou désactiver les checks de santé périodiques des endpoints API
ENABLE_HEALTH_CHECKS = True

# Intervalle en secondes entre chaque exécution des checks de santé
HEALTH_CHECK_INTERVAL_SECONDS = 2700

import json
import logging
from datetime import datetime, timezone
from pathlib import Path
import re
import asyncio
import os
from typing import Any, Optional, Dict

# Import des constantes du fichier de configuration
from config import LOG_FILE, ERROR_LOG_PATH, BASE_DIR, MAX_FILE_SIZE, API_CONFIG, TOOL_CONFIG

# ==== Configuration du logging ====
# Configure le logger principal pour le bot
logger = logging.getLogger("bot_logger")
logger.setLevel(logging.INFO)

# Crée le répertoire de base si nécessaire
BASE_DIR.mkdir(parents=True, exist_ok=True)

# Gestionnaire pour le fichier de log principal
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Gestionnaire pour les erreurs critiques (fichier séparé)
error_file_handler = logging.FileHandler(ERROR_LOG_PATH)
error_file_handler.setLevel(logging.ERROR)
error_file_handler.setFormatter(formatter)
logger.addHandler(error_file_handler)

# Gestionnaire pour la console (logs en temps réel)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Verrou pour les opérations de fichier asynchrones
_file_lock: Optional[asyncio.Lock] = None

def set_file_lock(lock: asyncio.Lock):
    """Définit l'instance du verrou asyncio pour les opérations de fichier."""
    global _file_lock
    _file_lock = lock

def log_message(message: str, level: str = "info"):
    """
    Enregistre un message dans le fichier de log et la console.
    Args:
        message (str): Le message à enregistrer.
        level (str): Le niveau de log ('debug', 'info', 'warning', 'error', 'critical').
    """
    if level == "debug":
        logger.debug(message)
    elif level == "info":
        logger.info(message)
    elif level == "warning":
        logger.warning(message)
    elif level == "error":
        logger.error(message)
    elif level == "critical":
        logger.critical(message)
    else:
        logger.info(f"Niveau de log inconnu '{level}': {message}")

def get_current_time() -> datetime:
    """Retourne l'heure actuelle en UTC."""
    return datetime.now(timezone.utc)

def format_datetime(dt: datetime) -> str:
    """Formate un objet datetime en chaîne de caractères lisible."""
    return dt.strftime("%Y-%m-%d %H:%M:%S UTC")

async def load_json(file_path: Path, default_value: Any = None) -> Any:
    """
    Charge les données d'un fichier JSON de manière asynchrone.
    Crée le fichier avec une valeur par défaut si inexistant.
    Args:
        file_path (Path): Le chemin du fichier JSON.
        default_value (Any): La valeur à retourner si le fichier n'existe pas ou est vide.
    Returns:
        Any: Le contenu du fichier JSON ou la valeur par défaut.
    """
    if _file_lock is None:
        log_message("Le verrou de fichier n'est pas initialisé dans utils.py. Initialisation par défaut.", level="warning")
        global _file_lock
        _file_lock = asyncio.Lock()

    try:
        if not file_path.exists():
            log_message(f"Fichier non trouvé: {file_path}. Création avec valeur par défaut.", level="info")
            await save_json(file_path, default_value if default_value is not None else {})
            return default_value if default_value is not None else {}
        
        async with _file_lock:
            return await asyncio.to_thread(_load_json_sync, file_path)
    except json.JSONDecodeError:
        log_message(f"Erreur de décodage JSON pour le fichier: {file_path}. Le fichier pourrait être corrompu. Retourne la valeur par défaut.", level="error")
        await save_json(file_path, default_value if default_value is not None else {})
        return default_value if default_value is not None else {}
    except Exception as e:
        log_message(f"Erreur inattendue lors du chargement du JSON {file_path}: {e}", level="error")
        return default_value if default_value is not None else {}

def _load_json_sync(file_path: Path) -> Any:
    """Fonction synchrone pour charger le JSON, appelée par asyncio.to_thread."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

async def save_json(file_path: Path, data: Any):
    """
    Sauvegarde les données dans un fichier JSON de manière asynchrone.
    Args:
        file_path (Path): Le chemin du fichier JSON.
        data (Any): Les données à sauvegarder.
    """
    if _file_lock is None:
        log_message("Le verrou de fichier n'est pas initialisé dans utils.py. Initialisation par défaut.", level="warning")
        global _file_lock
        _file_lock = asyncio.Lock()

    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        async with _file_lock:
            await asyncio.to_thread(_save_json_sync, file_path, data)
        log_message(f"Données sauvegardées dans {file_path}", level="debug")
    except Exception as e:
        log_message(f"Erreur lors de la sauvegarde du JSON {file_path}: {e}", level="error")

def _save_json_sync(file_path: Path, data: Any):
    """Fonction synchrone pour sauvegarder le JSON, appelée par asyncio.to_thread."""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def neutralize_urls(text: str) -> str:
    """
    Remplace les URLs dans le texte par une version neutralisée pour éviter les problèmes de sécurité
    ou les tentatives d'accès non désirées par le modèle.
    """
    url_pattern = re.compile(r'https?://[^\s/$.?#].[^\s]*', re.IGNORECASE)
    
    neutralized_text = url_pattern.sub("[LIEN_NEUTRALISÉ]", text)
    return neutralized_text

def find_tool_by_name(tool_name: str) -> Optional[Dict[str, Any]]:
    """
    Recherche un outil dans TOOL_CONFIG par son nom.
    Args:
        tool_name (str): Le nom de l'outil à rechercher.
    Returns:
        Optional[Dict[str, Any]]: Le dictionnaire de configuration de l'outil si trouvé, sinon None.
    """
    return TOOL_CONFIG.get(tool_name)

async def append_to_file(file_path: Path, content: str):
    """
    Ajoute du contenu à un fichier, en créant le fichier/répertoire si nécessaire.
    Gère la rotation du fichier si sa taille dépasse MAX_FILE_SIZE.
    """
    if _file_lock is None:
        log_message("Le verrou de fichier n'est pas initialisé dans utils.py. Initialisation par défaut.", level="warning")
        global _file_lock
        _file_lock = asyncio.Lock()

    file_path.parent.mkdir(parents=True, exist_ok=True)

    if file_path.exists() and file_path.stat().st_size + len(content.encode('utf-8')) > MAX_FILE_SIZE:
        rotate_file(file_path)

    async with _file_lock:
        await asyncio.to_thread(_append_to_file_sync, file_path, content)

def _append_to_file_sync(file_path: Path, content: str):
    """Fonction synchrone pour ajouter du contenu à un fichier."""
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(content + "\n")

def rotate_file(file_path: Path):
    """
    Effectue une rotation de fichier simple: renomme le fichier actuel avec un horodatage.
    """
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    new_path = file_path.parent / f"{file_path.stem}_{timestamp}{file_path.suffix}"
    try:
        os.rename(file_path, new_path)
        log_message(f"Fichier {file_path.name} renommé en {new_path.name} pour rotation.", level="info")
    except OSError as e:
        log_message(f"Erreur lors de la rotation du fichier {file_path.name}: {e}", level="error")

import time
import httpx
import json
import base64
import asyncio
import re 
import traceback
from typing import Dict, Any, Optional, Union, List, Tuple

# Import des constantes et fonctions utilitaires
from config import API_CONFIG, ENDPOINT_HEALTH_FILE, MAX_IMAGE_SIZE, GEMINI_TEMPERATURE, GEMINI_TOP_P, GEMINI_TOP_K, GEMINI_MAX_OUTPUT_TOKENS, GEMINI_SAFETY_SETTINGS
from utils import load_json, save_json, get_current_time, format_datetime, log_message, neutralize_urls

class EndpointHealthManager:
    """
    Gère la santé des endpoints API et sélectionne le meilleur endpoint disponible
    en fonction de critères comme la latence, le taux de succès et le nombre d'erreurs.
    C'est un singleton pour s'assurer qu'il n'y a qu'une seule instance de gestionnaire de santé.
    """
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        """Implémente le patron de conception Singleton."""
        if cls._instance is None:
            cls._instance = super(cls, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        """Initialise le gestionnaire."""
        if self._initialized:
            return
        self.health_status = {}

    async def init_manager(self):
        """
        Initialise le gestionnaire de santé de manière asynchrone.
        Charge l'état de santé persistant et s'assure que tous les endpoints sont suivis.
        """
        if not self._initialized:
            self.health_status = await load_json(ENDPOINT_HEALTH_FILE, {})
            self._initialize_health_status()
            self._initialized = True
            log_message("Gestionnaire de santé des endpoints initialisé.")

    def _initialize_health_status(self):
        """
        Initialise ou met à jour le statut de santé pour tous les endpoints configurés dans `API_CONFIG`.
        Ajoute les nouveaux endpoints et s'assure que toutes les clés nécessaires sont présentes.
        """
        updated = False
        for service_name, endpoints_config in API_CONFIG.items():
            if service_name not in self.health_status:
                self.health_status[service_name] = {}
                updated = True
            for endpoint_config in endpoints_config:
                endpoint_key = f"{endpoint_config['endpoint_name']}-{str(endpoint_config['key'])}"
                if endpoint_key not in self.health_status[service_name]:
                    self.health_status[service_name][endpoint_key] = {
                        "latency": 0.0,
                        "success_rate": 1.0,
                        "last_checked": None,
                        "error_count": 0,
                        "total_checks": 0,
                        "is_healthy": True
                    }
                    updated = True
        if updated:
            asyncio.create_task(save_json(ENDPOINT_HEALTH_FILE, self.health_status))
            log_message("Statut de santé des endpoints initialisé/mis à jour.")

    async def run_health_check_for_service(self, service_name: str):
        """
        Exécute des checks de santé pour tous les endpoints d'un service donné.
        Tente d'appeler l'endpoint avec des paramètres de santé prédéfinis.
        """
        endpoints_config = API_CONFIG.get(service_name)
        if not endpoints_config:
            log_message(f"Aucune configuration d'endpoint trouvée pour le service: {service_name}", level="warning")
            return

        log_message(f"Lancement du health check pour le service: {service_name}")
        for endpoint_config in endpoints_config:
            endpoint_key = f"{endpoint_config['endpoint_name']}-{str(endpoint_config['key'])}"
            start_time = time.monotonic()
            success = False
            try:
                request_method = endpoint_config.get("method", "GET")
                url = endpoint_config["url"]
                
                params = endpoint_config.get("health_check_params", endpoint_config.get("fixed_params", {})).copy()
                json_data = endpoint_config.get("health_check_json", endpoint_config.get("fixed_json", {})).copy()
                headers = endpoint_config.get("fixed_headers", {}).copy()
                auth = None
                
                check_timeout = endpoint_config.get("timeout", 5)

                if "health_check_url_suffix" in endpoint_config:
                    url += endpoint_config["health_check_url_suffix"]

                key_field = endpoint_config.get("key_field")
                key_location = endpoint_config.get("key_location")
                key_prefix = endpoint_config.get("key_prefix", "")
                api_key = endpoint_config["key"]

                if key_field and key_location:
                    if key_location == "param":
                        params[key_field] = api_key
                    elif key_location == "header":
                        headers[key_field] = f"{key_prefix}{api_key}"
                    elif key_location == "auth_basic":
                        if isinstance(api_key, tuple) and len(api_key) == 2:
                            auth = httpx.BasicAuth(api_key[0], api_key[1])
                        else:
                            log_message(f"Clé API pour auth_basic non valide pour {service_name}:{endpoint_key}", level="error")
                            success = False
                            continue

                async with httpx.AsyncClient(timeout=check_timeout) as client:
                    response = await client.request(request_method, url, params=params, headers=headers, json=json_data, auth=auth)
                    response.raise_for_status()
                    success = True
            except httpx.HTTPStatusError as e:
                log_level = "warning"
                if 400 <= e.response.status_code < 500 and e.response.status_code != 429:
                    log_level = "debug" 
                log_message(f"Health check pour {endpoint_key} ({service_name}) a échoué (HTTP {e.response.status_code}): {e.response.text}", level=log_level)
                success = False
            except httpx.RequestError as e:
                log_message(f"Health check pour {endpoint_key} ({service_name}) a échoué (Réseau): {e}", level="warning")
                success = False
            except Exception as e:
                log_message(f"Health check pour {endpoint_key} ({service_name}) a échoué (Inattendu): {e}", level="error")
                success = False
            finally:
                latency = time.monotonic() - start_time
                self.update_endpoint_health(service_name, endpoint_key, success, latency)
        log_message(f"Health check terminé pour le service: {service_name}")

    def update_endpoint_health(self, service_name: str, endpoint_key: str, success: bool, latency: float):
        """
        Met à jour le statut de santé d'un endpoint spécifique.
        Utilise une moyenne glissante pour le taux de succès et la latence.
        """
        if service_name not in self.health_status:
            self.health_status[service_name] = {}
        if endpoint_key not in self.health_status[service_name]:
            self.health_status[service_name][endpoint_key] = {
                "latency": 0.0,
                "success_rate": 1.0,
                "last_checked": None,
                "error_count": 0,
                "total_checks": 0,
                "is_healthy": True
            }

        status = self.health_status[service_name][endpoint_key]
        status["total_checks"] += 1
        status["last_checked"] = format_datetime(get_current_time())

        alpha = 0.1
        if success:
            status["error_count"] = max(0, status["error_count"] - 1)
            status["success_rate"] = status["success_rate"] * (1 - alpha) + 1.0 * alpha
            status["latency"] = status["latency"] * (1 - alpha) + latency * alpha
        else:
            status["error_count"] += 1
            status["success_rate"] = status["success_rate"] * (1 - alpha) + 0.0 * alpha
            status["latency"] = status["latency"] * (1 - alpha) + 10.0 * alpha 

        if status["error_count"] >= 3 or status["success_rate"] < 0.5:
            status["is_healthy"] = False
        else:
            status["is_healthy"] = True
        
        asyncio.create_task(save_json(ENDPOINT_HEALTH_FILE, self.health_status))
        log_message(f"Santé de {service_name}:{endpoint_key} mise à jour: Succès: {success}, Latence: {latency:.2f}s, Taux Succès: {status['success_rate']:.2f}, Sain: {status['is_healthy']}", level="debug" if not status["is_healthy"] else "info")

    def get_best_endpoint(self, service_name: str) -> Optional[Dict]:
        """
        Sélectionne le meilleur endpoint pour un service donné basé sur son statut de santé.
        Priorise les endpoints sains, puis les moins mauvais en cas d'absence d'endpoints sains.
        """
        service_health = self.health_status.get(service_name)
        if not service_health:
            log_message(f"Aucune donnée de santé pour le service {service_name}. Retourne None.", level="warning")
            return None

        best_endpoint_key = None
        best_score = -float('inf')

        healthy_endpoints = [
            (key, status) for key, status in service_health.items() if status["is_healthy"]
        ]

        if not healthy_endpoints:
            log_message(f"Aucun endpoint sain pour le service {service_name}. Tentative de sélection d'un endpoint non sain.", level="warning")
            all_endpoints = service_health.items()
            if not all_endpoints: 
                return None
            
            sorted_endpoints = sorted(all_endpoints, key=lambda item: (item[1]["error_count"], item[1]["latency"]))
            best_endpoint_key = sorted_endpoints[0][0]
            log_message(f"Fallback: Endpoint {best_endpoint_key} sélectionné pour {service_name} (non sain).", level="warning")
        else:
            for endpoint_key, status in healthy_endpoints:
                score = (status["success_rate"] * 100) - (status["latency"] * 10) - (status["error_count"] * 5)
                if score > best_score:
                    best_score = score
                    best_endpoint_key = endpoint_key
            log_message(f"Meilleur endpoint sélectionné pour {service_name}: {best_endpoint_key} (Score: {best_score:.2f})")

        if best_endpoint_key:
            for endpoint_config in API_CONFIG.get(service_name, []):
                current_endpoint_key = f"{endpoint_config['endpoint_name']}-{str(endpoint_config['key'])}"
                if current_endpoint_key == best_endpoint_key:
                    return endpoint_config
        return None

# Instancier le gestionnaire de santé des endpoints (sera initialisé dans main.py)
endpoint_health_manager = EndpointHealthManager()

def set_endpoint_health_manager_global(manager: EndpointHealthManager):
    """
    Permet d'injecter l'instance du gestionnaire de santé des endpoints.
    Ceci est utilisé pour s'assurer que tous les clients API utilisent la même instance.
    """
    global endpoint_health_manager
    endpoint_health_manager = manager

class APIClient:
    """
    Classe de base pour tous les clients API.
    Elle gère la sélection dynamique d'endpoints, les réessais en cas d'échec
    et l'intégration avec le gestionnaire de santé des endpoints.
    """
    def __init__(self, name: str, endpoint_health_manager: EndpointHealthManager):
        self.name = name
        self.endpoints_config = API_CONFIG.get(name, [])
        self.endpoint_health_manager = endpoint_health_manager
        if not self.endpoints_config:
            log_message(f"Client API {self.name} initialisé sans configuration d'endpoint.", level="error")

    async def _make_request(self, params: Optional[Dict] = None, headers: Optional[Dict] = None, 
                            json_data: Optional[Dict] = None, timeout: Optional[int] = None, 
                            max_retries: int = 3, initial_delay: float = 1.0, 
                            url: Optional[str] = None, method: Optional[str] = None, 
                            key_field: Optional[str] = None, key_location: Optional[str] = None, 
                            api_key: Optional[Union[str, Tuple[str, str]]] = None, 
                            fixed_params: Optional[Dict] = None, fixed_headers: Optional[Dict] = None, 
                            fixed_json: Optional[Dict] = None) -> Optional[Union[Dict, str, bytes]]:
        """
        Méthode interne pour effectuer les requêtes HTTP en utilisant le meilleur endpoint avec réessais.
        """
        
        selected_endpoint_config = None
        endpoint_key_for_health = "Dynamic"

        if url and method:
            selected_endpoint_config = {
                "url": url,
                "method": method,
                "key_field": key_field,
                "key_location": key_location,
                "key": api_key,
                "fixed_params": fixed_params if fixed_params is not None else {},
                "fixed_headers": fixed_headers if fixed_headers is not None else {},
                "fixed_json": fixed_json if fixed_json is not None else {},
                "endpoint_name": "Dynamic",
                "timeout": timeout if timeout is not None else 30
            }
            if api_key:
                endpoint_key_for_health = f"Dynamic-{str(api_key)}"
            log_message(f"Requête dynamique pour {self.name} vers {url}")
        else:
            selected_endpoint_config = self.endpoint_health_manager.get_best_endpoint(self.name)
            if not selected_endpoint_config:
                log_message(f"Aucun endpoint sain ou disponible pour {self.name}.", level="error")
                return {"error": True, "message": f"Aucun endpoint sain ou disponible pour {self.name}."}
            endpoint_key_for_health = f"{selected_endpoint_config['endpoint_name']}-{str(selected_endpoint_config['key'])}"
            log_message(f"Endpoint sélectionné pour {self.name}: {selected_endpoint_config['endpoint_name']}")
            timeout = timeout if timeout is not None else selected_endpoint_config.get("timeout", 30)

        url_to_use = selected_endpoint_config["url"]
        method_to_use = selected_endpoint_config["method"]

        request_params = selected_endpoint_config.get("fixed_params", {}).copy()
        request_headers = selected_endpoint_config.get("fixed_headers", {}).copy()
        request_json_data = selected_endpoint_config.get("fixed_json", {}).copy()
        auth = None

        if params:
            request_params.update(params)
        if headers:
            request_headers.update(headers)
        if json_data:
            request_json_data.update(json_data)

        key_field_to_use = selected_endpoint_config.get("key_field")
        key_location_to_use = selected_endpoint_config.get("key_location")
        key_prefix = selected_endpoint_config.get("key_prefix", "")
        api_key_to_use = selected_endpoint_config["key"]

        if key_field_to_use and key_location_to_use:
            if key_location_to_use == "param":
                request_params[key_field_to_use] = api_key_to_use
            elif key_location_to_use == "header":
                request_headers[key_field_to_use] = f"{key_prefix}{api_key_to_use}"
            elif key_location_to_use == "auth_basic":
                if isinstance(api_key_to_use, tuple) and len(api_key_to_use) == 2:
                    auth = httpx.BasicAuth(api_key_to_use[0], api_key_to_use[1])
                else:
                    log_message(f"Clé API pour auth_basic non valide pour {self.name}:{endpoint_key_for_health}", level="error")
                    self.endpoint_health_manager.update_endpoint_health(self.name, endpoint_key_for_health, False, 0.0)
                    return {"error": True, "message": "Configuration d'authentification basique invalide."}

        current_delay = initial_delay
        for attempt in range(max_retries):
            start_time = time.monotonic()
            success = False
            try:
                async with httpx.AsyncClient(timeout=timeout) as client:
                    response = await client.request(method_to_use, url_to_use, params=request_params, headers=request_headers, json=request_json_data, auth=auth)
                    response.raise_for_status()
                    success = True
                    
                    content_type = response.headers.get("Content-Type", "").lower()
                    if "application/json" in content_type:
                        try:
                            return response.json()
                        except json.JSONDecodeError:
                            log_message(f"API {self.name} réponse non JSON valide (tentative {attempt+1}/{max_retries}): {response.text[:200]}...", level="warning")
                            if attempt < max_retries - 1:
                                await asyncio.sleep(current_delay)
                                current_delay *= 2
                                continue
                            return {"error": True, "message": "Réponse API non JSON valide.", "raw_response": response.text}
                    else:
                        log_message(f"API {self.name} a renvoyé un Content-Type non JSON: {content_type}", level="info")
                        return response.content

            except httpx.HTTPStatusError as e:
                log_message(f"API {self.name} erreur HTTP (tentative {attempt+1}/{max_retries}): {e.response.status_code} - {e.response.text}", level="warning")
                if 400 <= e.response.status_code < 500 and e.response.status_code != 429:
                    log_message(f"API {self.name}: Erreur client {e.response.status_code}, pas de réessai.", level="error")
                    self.endpoint_health_manager.update_endpoint_health(self.name, endpoint_key_for_health, False, e.response.elapsed.total_seconds())
                    return {"error": True, "status_code": e.response.status_code, "message": e.response.text}
                
                if attempt < max_retries - 1:
                    log_message(f"API {self.name}: Réessai dans {current_delay:.2f}s...", level="info")
                    await asyncio.sleep(current_delay)
                    current_delay *= 2
            except httpx.RequestError as e:
                log_message(f"API {self.name} erreur de requête (tentative {attempt+1}/{max_retries}): {e}", level="warning")
                if attempt < max_retries - 1:
                    log_message(f"API {self.name}: Réessai dans {current_delay:.2f}s...", level="info")
                    await asyncio.sleep(current_delay)
                    current_delay *= 2
            except Exception as e:
                log_message(f"API {self.name} erreur inattendue (tentative {attempt+1}/{max_retries}): {e}", level="error")
                self.endpoint_health_manager.update_endpoint_health(self.name, endpoint_key_for_health, False, time.monotonic() - start_time)
                return {"error": True, "message": str(e)}
            finally:
                if not success:
                    latency = time.monotonic() - start_time
                    self.endpoint_health_manager.update_endpoint_health(self.name, endpoint_key_for_health, False, latency)
        
        log_message(f"API {self.name}: Toutes les tentatives ont échoué après {max_retries} réessais.", level="error")
        return {"error": True, "message": f"Échec de la requête après {max_retries} tentatives."}

    async def query(self, *args, **kwargs) -> Any:
        """
        Méthode abstraite pour interroger l'API.
        Doit être implémentée par chaque sous-classe de client API.
        """
        raise NotImplementedError("La méthode query doit être implémentée par les sous-classes.")

# --- Clients API Spécifiques ---

class GeminiAPIClient(APIClient):
    """Client pour l'API Gemini, hérite de APIClient pour la gestion de santé."""
    def __init__(self):
        super().__init__("GEMINI_API", endpoint_health_manager)
        self.model_name = "gemini-1.5-flash-latest"
        self.generation_config = {
            "temperature": GEMINI_TEMPERATURE,
            "top_p": GEMINI_TOP_P,
            "top_k": GEMINI_TOP_K,
            "max_output_tokens": GEMINI_MAX_OUTPUT_TOKENS,
        }
        self.safety_settings = GEMINI_SAFETY_SETTINGS
        log_message(f"GeminiApiClient initialisé avec le modèle par défaut: {self.model_name}")

    async def generate_content(self, prompt: str, chat_history: List[Dict], image_data: Optional[str] = None, model: Optional[str] = None, tools: Optional[List[Dict]] = None) -> Union[Dict, str]:
        """Génère du contenu textuel ou multimodal en utilisant l'API Gemini."""
        model_to_use = model if model else self.model_name
        
        contents = []
        for msg in chat_history:
            role = "user" if msg["role"] == "user" else "model"
            contents.append({"role": role, "parts": msg["parts"]})

        if contents and contents[-1]["role"] == "user":
            contents[-1]["parts"].append({"text": prompt})
        else:
            contents.append({"role": "user", "parts": [{"text": prompt}]})

        if image_data:
            if "," in image_data:
                mime_type_part, base64_data = image_data.split(",", 1)
                mime_type = mime_type_part.split(":", 1)[1].split(";", 1)[0]
            else:
                mime_type = "image/jpeg" 
                base64_data = image_data

            if contents and contents[-1]["role"] == "user":
                contents[-1]["parts"].append({
                    "inlineData": {
                        "mimeType": mime_type,
                        "data": base64_data
                    }
                })
                log_message(f"Image ajoutée au prompt Gemini (mimeType: {mime_type}).")
            else:
                log_message("Impossible d'ajouter l'image au prompt Gemini: le dernier message n'est pas un utilisateur.", level="warning")

        payload = {
            "contents": contents,
            "generationConfig": self.generation_config,
            "safetySettings": self.safety_settings
        }

        if tools:
            payload["tools"] = tools

        log_message(f"Appel à Gemini API pour le modèle {model_to_use}...")
        
        # L'URL de l'endpoint Gemini peut varier en fonction du modèle.
        # On prend l'URL de base du premier endpoint configuré et on y ajoute le modèle.
        base_url_from_config = self.endpoints_config[0]["url"].split(':generateContent')[0]
        dynamic_url = f"{base_url_from_config}:{model_to_use}:generateContent"

        # Les headers et la clé API seront gérés par _make_request via la sélection d'endpoint
        response = await self._make_request(
            url=dynamic_url,
            method="POST",
            json_data=payload,
            timeout=60 # Utilise le timeout de la méthode _make_request
        )

        if response and not response.get("error"):
            return response
        return f"❌ Erreur Gemini: {response.get('message', 'Inconnu')}" if response else "❌ Erreur Gemini: Réponse vide ou erreur interne."

class OCRApiClient(APIClient):
    """Client pour l'API OCR.space, hérite de APIClient pour la gestion de santé."""
    def __init__(self):
        super().__init__("OCR_API", endpoint_health_manager)
        log_message("OCRApiClient initialisé.")

    async def query(self, image_base64: str) -> str:
        """
        Effectue une requête OCR à l'API OCR.space.
        `image_base64` doit être la chaîne base64 de l'image, incluant le préfixe mimeType.
        """
        payload = {
            "base64Image": image_base64,
            "language": "fre",
            "isOverlayRequired": False,
            "OCREngine": 2
        }
        
        # Les headers et la clé API seront gérés par _make_request via la sélection d'endpoint
        log_message("Appel à OCR.space API...")
        response = await self._make_request(
            json_data=payload,
            method="POST",
            timeout=30
        )

        if response and not response.get("error"):
            if response.get("IsErroredOnProcessing"):
                error_message = response.get("ErrorMessage", ["Erreur inconnue lors du traitement OCR."])
                log_message(f"Erreur OCR.space: {error_message}", level="error")
                return f"❌ Erreur OCR: {', '.join(error_message)}"
            
            parsed_text = ""
            if "ParsedResults" in response and response["ParsedResults"]:
                for parsed_result in response["ParsedResults"]:
                    parsed_text += parsed_result.get("ParsedText", "") + "\n"
            
            if parsed_text.strip():
                log_message("OCR.space: Texte extrait avec succès.")
                return parsed_text.strip()
            else:
                log_message("OCR.space: Aucun texte extrait.", level="warning")
                return "Aucun texte n'a pu être extrait de l'image."
        return f"❌ Erreur OCR: {response.get('message', 'Inconnu')}" if response else "❌ Erreur OCR: Réponse vide ou erreur interne."

class DeepSeekClient(APIClient):
    def __init__(self):
        super().__init__("DEEPSEEK", endpoint_health_manager)

    async def query(self, prompt: Union[str, List[Dict]], model: str = "deepseek-chat") -> str:
        """Interroge l'API DeepSeek pour des complétions de chat."""
        if isinstance(prompt, str):
            messages = [{"role": "user", "content": prompt}]
        else:
            messages = prompt

        payload = {"model": model, "messages": messages}
        response = await self._make_request(json_data=payload)
        if response and not response.get("error"):
            content = response.get("choices", [{}])[0].get("message", {}).get("content")
            if content:
                return content
            return "DeepSeek: Pas de contenu de réponse trouvé."
        return f"DeepSeek: Erreur: {response.get('message', 'Inconnu')}" if response else "DeepSeek: Réponse vide ou erreur interne."

class SerperClient(APIClient):
    def __init__(self):
        super().__init__("SERPER", endpoint_health_manager)

    async def query(self, query_text: str) -> str:
        """Effectue une recherche web via l'API Serper."""
        payload = {"q": query_text}
        response = await self._make_request(json_data=payload)
        if response and not response.get("error"):
            organic_results = response.get("organic", [])
            if organic_results:
                snippet = organic_results[0].get("snippet", "Pas de snippet.")
                link = organic_results[0].get("link", "")
                return f"Serper (recherche web):\n{snippet} {neutralize_urls(link)}"
            return "Serper: Aucune information trouvée."
        return f"Serper: Erreur: {response.get('message', 'Inconnu')}" if response else "Serper: Réponse vide ou erreur interne."

class WolframAlphaClient(APIClient):
    def __init__(self):
        super().__init__("WOLFRAMALPHA", endpoint_health_manager)

    async def query(self, input_text: str) -> str:
        """Interroge WolframAlpha pour des calculs ou des faits."""
        params = {"input": input_text}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            pods = response.get("queryresult", {}).get("pods", [])
            if pods:
                for pod in pods:
                    if pod.get("title") in ["Result", "Input interpretation", "Decimal approximation"]:
                        subpods = pod.get("subpods", [])
                        if subpods and subpods[0].get("plaintext"):
                            return f"WolframAlpha:\n{subpods[0]['plaintext']}"
                if pods and pods[0].get("subpods") and pods[0]["subpods"][0].get("plaintext"):
                    return f"WolframAlpha:\n{pods[0]['subpods'][0]['plaintext']}"
            return "WolframAlpha: Pas de résultat clair."
        return f"WolframAlpha: Erreur: {response.get('message', 'Inconnu')}" if response else "WolframAlpha: Réponse vide ou erreur interne."

class TavilyClient(APIClient):
    def __init__(self):
        super().__init__("TAVILY", endpoint_health_manager)

    async def query(self, query_text: str, max_results: int = 3) -> str:
        """Effectue une recherche web avancée via l'API Tavily."""
        payload = {"query": query_text, "max_results": max_results}
        response = await self._make_request(json_data=payload)
        if response and not response.get("error"):
            results = response.get("results", [])
            answer = response.get("answer", "Aucune réponse directe trouvée.")

            output = f"Tavily (recherche web):\nRéponse directe: {answer}\n"
            if results:
                output += "Extraits pertinents:\n"
                for i, res in enumerate(results[:max_results]):
                    output += f"- {res.get('title', 'N/A')}: {res.get('content', 'N/A')} {neutralize_urls(res.get('url', ''))}\n"
            return output
        return f"Tavily: Erreur: {response.get('message', 'Inconnu')}" if response else "Tavily: Réponse vide ou erreur interne."

class ApiFlashClient(APIClient):
    def __init__(self):
        super().__init__("APIFLASH", endpoint_health_manager)

    async def query(self, url: str) -> str:
        """Capture une capture d'écran d'une URL via ApiFlash."""
        params = {"url": url, "format": "jpeg", "full_page": "true"}
        response_content = await self._make_request(params=params)

        if isinstance(response_content, bytes):
            selected_endpoint_config = self.endpoint_health_manager.get_best_endpoint(self.name)
            if selected_endpoint_config:
                capture_url = f"{selected_endpoint_config['url']}?access_key={selected_endpoint_config['key']}&url={url}&format=jpeg&full_page=true"
                return f"ApiFlash (capture d'écran): {neutralize_urls(capture_url)} (Vérifiez le lien pour l'image)"
            return "ApiFlash: Impossible de générer l'URL de capture."
        elif isinstance(response_content, dict) and response_content.get("error"):
            return f"ApiFlash: Erreur: {response_content.get('message', 'Inconnu')}"
        else:
            log_message(f"ApiFlash a renvoyé un type de réponse inattendu: {type(response_content)}", level="warning")
            return f"ApiFlash: Réponse inattendue de l'API. {response_content}"

class CrawlbaseClient(APIClient):
    def __init__(self):
        super().__init__("CRAWLBASE", endpoint_health_manager)

    async def query(self, url: str, use_js: bool = False) -> str:
        """Scrape le contenu HTML ou JavaScript d'une URL via Crawlbase."""
        params = {"url": url, "format": "json"}
        
        selected_endpoint_config = None
        if use_js:
            for config in API_CONFIG.get(self.name, []):
                if "JS Scraper" in config.get("endpoint_name", ""):
                    selected_endpoint_config = config
                    break
        
        if not selected_endpoint_config: 
            selected_endpoint_config = self.endpoint_health_manager.get_best_endpoint(self.name)

        if not selected_endpoint_config:
            return f"Crawlbase: Aucun endpoint sain ou disponible pour {self.name}."

        response = await self._make_request(
            params=params,
            url=selected_endpoint_config["url"],
            method=selected_endpoint_config["method"],
            key_field=selected_endpoint_config["key_field"],
            key_location=selected_endpoint_config["key_location"],
            api_key=selected_endpoint_config["key"],
            fixed_params=selected_endpoint_config.get("fixed_params", {}),
            timeout=selected_endpoint_config.get("timeout")
        )

        if response and not response.get("error"):
            body = response.get("body")
            if body:
                try:
                    decoded_body = base64.b64decode(body).decode('utf-8', errors='ignore')
                    return f"Crawlbase (contenu web):\n{decoded_body[:1000]}..."
                except Exception:
                    return f"Crawlbase (contenu web - brut):\n{body[:1000]}..."
            return "Crawlbase: Contenu non trouvé."
        return f"Crawlbase: Erreur: {response.get('message', 'Inconnu')}" if response else "Crawlbase: Réponse vide ou erreur interne."

class DetectLanguageClient(APIClient):
    def __init__(self):
        super().__init__("DETECTLANGUAGE", endpoint_health_manager)

    async def query(self, text: str) -> str:
        """Détecte la langue d'un texte via DetectLanguage API."""
        payload = {"q": text}
        response = await self._make_request(json_data=payload)
        if response and not response.get("error"):
            detections = response.get("data", {}).get("detections", [])
            if detections:
                first_detection = detections[0]
                lang = first_detection.get("language")
                confidence = first_detection.get("confidence")
                return f"Langue détectée: {lang} (confiance: {confidence})"
            return "DetectLanguage: Aucune langue détectée."
        return f"DetectLanguage: Erreur: {response.get('message', 'Inconnu')}" if response else "DetectLanguage: Réponse vide ou erreur interne."

class GuardianClient(APIClient):
    def __init__(self):
        super().__init__("GUARDIAN", endpoint_health_manager)

    async def query(self, query_text: str) -> str:
        """Recherche des articles de presse via l'API The Guardian."""
        params = {"q": query_text}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            results = response.get("response", {}).get("results", [])
            if results:
                output = "Articles The Guardian:\n"
                for res in results[:3]:
                    output += f"- {res.get('webTitle', 'N/A')}: {res.get('fields', {}).get('trailText', 'N/A')} {neutralize_urls(res.get('webUrl', ''))}\n"
                return output
            return "Guardian: Aucun article trouvé."
        return f"Guardian: Erreur: {response.get('message', 'Inconnu')}" if response else "Guardian: Réponse vide ou erreur interne."

class IP2LocationClient(APIClient):
    def __init__(self):
        super().__init__("IP2LOCATION", endpoint_health_manager)

    async def query(self, ip_address: str) -> str:
        """Géolocalise une adresse IP via IP2Location API."""
        params = {"ip": ip_address}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            if "country_name" in response:
                return f"IP2Location (Géolocalisation IP {ip_address}): Pays: {response['country_name']}, Ville: {response.get('city_name', 'N/A')}"
            return "IP2Location: Informations non trouvées."
        return f"IP2Location: Erreur: {response.get('message', 'Inconnu')}" if response else "IP2Location: Réponse vide ou erreur interne."

class ShodanClient(APIClient):
    def __init__(self):
        super().__init__("SHODAN", endpoint_health_manager)

    async def query(self, query_text: str = "") -> str:
        """
        Interroge Shodan pour des informations sur un hôte IP ou des informations sur la clé API.
        Si `query_text` est une IP, tente de récupérer les infos de l'hôte.
        Sinon, ou en cas d'échec, retourne les infos de la clé API.
        """
        if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", query_text):
            selected_endpoint_config = None
            for config in API_CONFIG.get(self.name, []):
                if "Host Info" in config.get("endpoint_name", ""):
                    selected_endpoint_config = config
                    break
            if selected_endpoint_config:
                url = f"{selected_endpoint_config['url'].rstrip('/')}/{query_text}"
                response = await self._make_request(
                    params={"key": selected_endpoint_config["key"]},
                    url=url,
                    method="GET",
                    key_field=selected_endpoint_config["key_field"],
                    key_location=selected_endpoint_config["key_location"],
                    api_key=selected_endpoint_config["key"],
                    timeout=selected_endpoint_config.get("timeout")
                )
                if response and not response.get("error"):
                    return f"Shodan (info hôte {query_text}): Pays: {response.get('country_name', 'N/A')}, Ports: {response.get('ports', 'N/A')}, Vulnérabilités: {response.get('vulns', 'Aucune')}"
                return f"Shodan (info hôte): Erreur: {response.get('message', 'Inconnu')}" if response else "Shodan: Réponse vide ou erreur interne."
            else:
                return "Shodan: Endpoint 'Host Info' non configuré."
        else:
            response = await self._make_request()
            if response and not response.get("error"):
                return f"Shodan (info clé): Requêtes restantes: {response.get('usage_limits', {}).get('query_credits', 'N/A')}, Scan crédits: {response.get('usage_limits', {}).get('scan_credits', 'N/A')}"
            return f"Shodan: Erreur: {response.get('message', 'Inconnu')}" if response else "Shodan: Réponse vide ou erreur interne."

class WeatherAPIClient(APIClient):
    def __init__(self):
        super().__init__("WEATHERAPI", endpoint_health_manager)

    async def query(self, location: str) -> str:
        """Récupère les conditions météorologiques actuelles pour une localisation via WeatherAPI."""
        params = {"q": location}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            current = response.get("current", {})
            location_info = response.get("location", {})
            if current and location_info:
                return (
                    f"Météo à {location_info.get('name', 'N/A')}, {location_info.get('country', 'N/A')}:\n"
                    f"Température: {current.get('temp_c', 'N/A')}°C, "
                    f"Conditions: {current.get('condition', {}).get('text', 'N/A')}, "
                    f"Vent: {current.get('wind_kph', 'N/A')} km/h"
                )
            return "WeatherAPI: Données météo non trouvées."
        return f"WeatherAPI: Erreur: {response.get('message', 'Inconnu')}" if response else "WeatherAPI: Réponse vide ou erreur interne."

class CloudmersiveClient(APIClient):
    def __init__(self):
        super().__init__("CLOUDMERSIVE", endpoint_health_manager)

    async def query(self, domain: str) -> str:
        """Vérifie la validité et le type d'un domaine via Cloudmersive API."""
        payload = {"domain": domain}
        response = await self._make_request(json_data=payload)
        if response and not response.get("error"):
            return f"Cloudmersive (vérification de domaine {domain}): Valide: {response.get('ValidDomain', 'N/A')}, Type: {response.get('DomainType', 'N/A')}"
        return f"Cloudmersive: Erreur: {response.get('message', 'Inconnu')}" if response else "Cloudmersive: Réponse vide ou erreur interne."

class GreyNoiseClient(APIClient):
    def __init__(self):
        super().__init__("GREYNOISE", endpoint_health_manager)

    async def query(self, ip_address: str) -> str:
        """Analyse une adresse IP pour détecter des activités 'bruit' (malveillantes) via GreyNoise."""
        selected_endpoint_config = self.endpoint_health_manager.get_best_endpoint(self.name)
        if not selected_endpoint_config:
            return f"GreyNoise: Aucun endpoint sain ou disponible pour {self.name}."

        url = f"{selected_endpoint_config['url'].rstrip('/')}/{ip_address}"
        method = selected_endpoint_config["method"]
        headers = {selected_endpoint_config["key_field"]: selected_endpoint_config["key"]}

        response = await self._make_request(
            headers=headers,
            url=url,
            method=method,
            key_field=selected_endpoint_config["key_field"],
            key_location=selected_endpoint_config["key_location"],
            api_key=selected_endpoint_config["key"],
            timeout=selected_endpoint_config.get("timeout")
        )

        if response and not response.get("error"):
            if response.get("noise"):
                return f"GreyNoise (IP {ip_address}): C'est une IP 'bruit' (malveillante). Classification: {response.get('classification', 'N/A')}, Nom d'acteur: {response.get('actor', 'N/A')}"
            return f"GreyNoise (IP {ip_address}): Pas de 'bruit' détecté. Statut: {response.get('status', 'N/A')}"
        return f"GreyNoise: Erreur: {response.get('message', 'Inconnu')}" if response else "GreyNoise: Réponse vide ou erreur interne."

class PulsediveClient(APIClient):
    def __init__(self):
        super().__init__("PULSEDIVE", endpoint_health_manager)

    async def query(self, indicator: str, type: str = "auto") -> str:
        """Analyse un indicateur de menace (IP, domaine, URL) via Pulsedive."""
        params = {"indicator": indicator, "type": type}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            if response.get("results"):
                result = response["results"][0]
                return (
                    f"Pulsedive (Analyse {indicator}): Type: {result.get('type', 'N/A')}, "
                    f"Risk: {result.get('risk', 'N/A')}, "
                    f"Description: {result.get('description', 'N/A')[:200]}..."
                )
            return "Pulsedive: Aucun résultat d'analyse trouvé."
        return f"Pulsedive: Erreur: {response.get('message', 'Inconnu')}" if response else "Pulsedive: Réponse vide ou erreur interne."

class StormGlassClient(APIClient):
    def __init__(self):
        super().__init__("STORMGLASS", endpoint_health_manager)

    async def query(self, lat: float, lng: float, params: str = "airTemperature,waveHeight") -> str:
        """Récupère les données météorologiques maritimes pour une coordonnée via StormGlass."""
        now = int(time.time())
        request_params = {
            "lat": lat,
            "lng": lng,
            "params": params,
            "start": now,
            "end": now + 3600
        }
        response = await self._make_request(params=request_params)
        if response and not response.get("error"):
            data = response.get("hours", [])
            if data:
                first_hour = data[0]
                temp = first_hour.get('airTemperature', [{}])[0].get('value', 'N/A')
                wave_height = first_hour.get('waveHeight', [{}])[0].get('value', 'N/A')
                return f"StormGlass (Météo maritime à {lat},{lng}): Température air: {temp}°C, Hauteur vagues: {wave_height}m"
            return "StormGlass: Données non trouvées."
        return f"StormGlass: Erreur: {response.get('message', 'Inconnu')}" if response else "StormGlass: Réponse vide ou erreur interne."

class LoginRadiusClient(APIClient):
    def __init__(self):
        super().__init__("LOGINRADIUS", endpoint_health_manager)

    async def query(self) -> str:
        """Effectue un simple ping à l'API LoginRadius pour vérifier sa disponibilité."""
        response = await self._make_request()
        if response and not response.get("error"):
            return f"LoginRadius (Ping API): Statut: {response.get('Status', 'N/A')}, Message: {response.get('Message', 'N/A')}"
        return f"LoginRadius: Erreur: {response.get('message', 'Inconnu')}" if response else "LoginRadius: Réponse vide ou erreur interne."

class JsonbinClient(APIClient):
    def __init__(self):
        super().__init__("JSONBIN", endpoint_health_manager)

    async def query(self, data: Optional[Dict[str, Any]] = None, private: bool = True, bin_id: Optional[str] = None) -> str:
        """
        Crée un nouveau 'bin' JSON ou accède à un bin existant via Jsonbin.io.
        `data` est pour la création, `bin_id` pour l'accès.
        """
        if bin_id:
            selected_endpoint_config = None
            for config in API_CONFIG.get(self.name, []):
                if "Bin Access" in config.get("endpoint_name", ""):
                    selected_endpoint_config = config
                    break
            if not selected_endpoint_config:
                return f"Jsonbin: Aucun endpoint d'accès de bin sain ou disponible pour {self.name}."

            url = f"{selected_endpoint_config['url'].rstrip('/')}/{bin_id}"
            method = "GET"
            headers = {selected_endpoint_config["key_field"]: selected_endpoint_config["key"]}
            
            response = await self._make_request(
                headers=headers,
                url=url,
                method=method,
                timeout=selected_endpoint_config.get("timeout")
            )
            if response and not response.get("error"):
                return f"Jsonbin (Accès bin {bin_id}):\n{json.dumps(response, indent=2)}"
            return f"Jsonbin (Accès bin): Erreur: {response.get('message', 'Inconnu')}" if response else "Jsonbin: Réponse vide ou erreur interne."
        
        else:
            selected_endpoint_config = None
            for config in API_CONFIG.get(self.name, []):
                if "Bin Create" in config.get("endpoint_name", ""):
                    selected_endpoint_config = config
                    break
            
            if not selected_endpoint_config:
                return f"Jsonbin: Aucun endpoint de création de bin sain ou disponible pour {self.name}."

            url = selected_endpoint_config["url"]
            method = "POST"
            headers = {selected_endpoint_config["key_field"]: selected_endpoint_config["key"], "Content-Type": "application/json"}
            payload = {"record": data if data is not None else {}, "private": private}

            response = await self._make_request(
                json_data=payload,
                headers=headers,
                url=url,
                method=method,
                timeout=selected_endpoint_config.get("timeout")
            )

            if response and not response.get("error"):
                return f"Jsonbin (Création de bin): ID: {response.get('metadata', {}).get('id', 'N/A')}, URL: {neutralize_urls(response.get('metadata', {}).get('url', 'N/A'))}"
            return f"Jsonbin (Création de bin): Erreur: {response.get('message', 'Inconnu')}" if response else "Jsonbin: Réponse vide ou erreur interne."

class HuggingFaceClient(APIClient):
    def __init__(self):
        super().__init__("HUGGINGFACE", endpoint_health_manager)

    async def query(self, model_name: str = "distilbert-base-uncased-finetuned-sst-2-english", input_text: str = "Hello world") -> str:
        """Effectue une inférence sur un modèle HuggingFace (ex: classification de texte, génération)."""
        selected_endpoint_config = self.endpoint_health_manager.get_best_endpoint(self.name)
        if not selected_endpoint_config:
            return f"HuggingFace: Aucun endpoint sain ou disponible pour {self.name}."

        inference_url = f"https://api-inference.huggingface.co/models/{model_name}"
        
        headers = {
            selected_endpoint_config["key_field"]: f"{selected_endpoint_config['key_prefix']}{selected_endpoint_config['key']}",
            "Content-Type": "application/json"
        }
        payload = {"inputs": input_text}

        response = await self._make_request(
            json_data=payload,
            headers=headers,
            url=inference_url,
            method="POST",
            timeout=selected_endpoint_config.get("timeout")
        )

        if response and not response.get("error"):
            if isinstance(response, list) and response:
                first_result = response[0]
                if isinstance(first_result, list) and first_result:
                    return f"HuggingFace ({model_name} - {first_result[0].get('label')}): Score {first_result[0].get('score', 'N/A'):.2f}"
                elif isinstance(first_result, dict) and "generated_text" in first_result:
                    return f"HuggingFace ({model_name}): {first_result.get('generated_text')}"
            return f"HuggingFace ({model_name}): Réponse non parsée. {response}"
        return f"HuggingFace: Erreur: {response.get('message', 'Inconnu')}" if response else "HuggingFace: Réponse vide ou erreur interne."

class TwilioClient(APIClient):
    def __init__(self):
        super().__init__("TWILIO", endpoint_health_manager)

    async def query(self) -> str:
        """Récupère le solde du compte Twilio."""
        selected_endpoint_config = None
        for config in API_CONFIG.get(self.name, []):
            if "Account Balance" in config.get("endpoint_name", ""):
                selected_endpoint_config = config
                break
        if not selected_endpoint_config:
            if self.endpoints_config:
                selected_endpoint_config = self.endpoints_config[0]
            else:
                return f"Twilio: Aucune configuration d'endpoint disponible pour {self.name}."

        response = await self._make_request(
            url=selected_endpoint_config["url"],
            method=selected_endpoint_config["method"],
            key_location=selected_endpoint_config["key_location"],
            api_key=selected_endpoint_config["key"],
            timeout=selected_endpoint_config.get("timeout")
        )
        if response and not response.get("error"):
            return f"Twilio (Balance): {response.get('balance', 'N/A')} {response.get('currency', 'N/A')}"
        return f"Twilio: Erreur: {response.get('message', 'Inconnu')}" if response else "Twilio: Réponse vide ou erreur interne."

class AbstractAPIClient(APIClient):
    def __init__(self):
        super().__init__("ABSTRACTAPI", endpoint_health_manager)

    async def query(self, input_value: str, api_type: str) -> str:
        """
        Interroge diverses APIs d'AbstractAPI (validation email/téléphone, taux de change, jours fériés).
        `input_value` dépend du `api_type`.
        """
        params = {}
        target_endpoint_name = ""

        if api_type == "PHONE_VALIDATION":
            params["phone"] = input_value
            target_endpoint_name = "Phone Validation"
        elif api_type == "EMAIL_VALIDATION":
            params["email"] = input_value
            target_endpoint_name = "Email Validation"
        elif api_type == "EXCHANGE_RATES":
            params["base"] = input_value if input_value else "USD" 
            target_endpoint_name = "Exchange Rates"
        elif api_type == "HOLIDAYS":
            params["country"] = input_value if input_value else "US"
            from datetime import datetime
            params["year"] = datetime.now(timezone.utc).year
            target_endpoint_name = "Holidays"
        else:
            return f"AbstractAPI: Type d'API '{api_type}' non supporté pour la requête."

        selected_endpoint_config = None
        for config in API_CONFIG.get(self.name, []):
            if target_endpoint_name in config["endpoint_name"]:
                selected_endpoint_config = config
                break
        
        if not selected_endpoint_config:
            return f"AbstractAPI: Aucun endpoint sain ou disponible pour {self.name} pour le type {api_type}."

        response = await self._make_request(
            params=params,
            url=selected_endpoint_config["url"],
            method=selected_endpoint_config["method"],
            key_field=selected_endpoint_config["key_field"],
            key_location=selected_endpoint_config["key_location"],
            api_key=selected_endpoint_config["key"],
            fixed_params=selected_endpoint_config.get("fixed_params", {}),
            timeout=selected_endpoint_config.get("timeout")
        )

        if response and not response.get("error"):
            if api_type == "PHONE_VALIDATION":
                return (
                    f"AbstractAPI (Validation Tél): Numéro: {response.get('phone', 'N/A')}, "
                    f"Valide: {response.get('valid', 'N/A')}, "
                    f"Pays: {response.get('country', {}).get('name', 'N/A')}"
                )
            elif api_type == "EMAIL_VALIDATION":
                return (
                    f"AbstractAPI (Validation Email): Email: {response.get('email', 'N/A')}, "
                    f"Valide: {response.get('is_valid_format', 'N/A')}, "
                    f"Deliverable: {response.get('is_deliverable', 'N/A')}"
                )
            elif api_type == "EXCHANGE_RATES":
                return f"AbstractAPI (Taux de change): Base: {response.get('base', 'N/A')}, Taux (USD): {response.get('exchange_rates', {}).get('USD', 'N/A')}"
            elif api_type == "HOLIDAYS":
                holidays = [h.get('name', 'N/A') for h in response if h.get('name')]
                return f"AbstractAPI (Jours fériés {params.get('country', 'US')} {params.get('year')}): {', '.join(holidays[:5])}..." if holidays else "Aucun jour férié trouvé."
            return f"AbstractAPI ({api_type}): Réponse brute: {response}"
        return f"AbstractAPI ({api_type}): Erreur: {response.get('message', 'Inconnu')}" if response else "AbstractAPI: Réponse vide ou erreur interne."

class GoogleCustomSearchClient(APIClient):
    def __init__(self):
        super().__init__("GOOGLE_CUSTOM_SEARCH", endpoint_health_manager)

    async def query(self, query_text: str) -> str:
        """Effectue une recherche personnalisée Google via l'API Custom Search."""
        params = {"q": query_text}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            items = response.get("items", [])
            if items:
                output = "Google Custom Search:\n"
                for item in items[:3]:
                    output += f"- {item.get('title', 'N/A')}: {item.get('snippet', 'N/A')} {neutralize_urls(item.get('link', ''))}\n"
                return output
            return "Google Custom Search: Aucun résultat trouvé."
        return f"Google Custom Search: Erreur: {response.get('message', 'Inconnu')}" if response else "Google Custom Search: Réponse vide ou erreur interne."

class RandommerClient(APIClient):
    def __init__(self):
        super().__init__("RANDOMMER", endpoint_health_manager)

    async def query(self, country_code: str = "US", quantity: int = 1) -> str:
        """Génère des numéros de téléphone aléatoires via Randommer.io."""
        params = {"CountryCode": country_code, "Quantity": quantity}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            if isinstance(response, list) and response:
                return f"Randommer (Numéros de téléphone): {', '.join(response)}"
            return f"Randommer: {response}"
        return f"Randommer: Erreur: {response.get('message', 'Inconnu')}" if response else "Randommer: Réponse vide ou erreur interne."

class TomorrowIOClient(APIClient):
    def __init__(self):
        super().__init__("TOMORROW.IO", endpoint_health_manager)

    async def query(self, location: str, fields: Optional[List[str]] = None) -> str:
        """Récupère les prévisions météorologiques via Tomorrow.io."""
        if fields is None:
            fields = ["temperature", "humidity", "windSpeed"]
        payload = {"location": location, "fields": fields, "units": "metric", "timesteps": ["1h"]}
        response = await self._make_request(json_data=payload)
        if response and not response.get("error"):
            data = response.get("data", {}).get("timelines", [{}])[0].get("intervals", [{}])[0].get("values", {})
            if data:
                output = f"Météo (Tomorrow.io) à {location}:\n"
                for field in fields:
                    output += f"- {field.capitalize()}: {data.get(field, 'N/A')}\n"
                return output
            return "Tomorrow.io: Données météo non trouvées."
        return f"Tomorrow.io: Erreur: {response.get('message', 'Inconnu')}" if response else "Tomorrow.io: Réponse vide ou erreur interne."

class OpenWeatherMapClient(APIClient):
    def __init__(self):
        super().__init__("OPENWEATHERMAP", endpoint_health_manager)

    async def query(self, location: str) -> str:
        """Récupère les conditions météorologiques actuelles via OpenWeatherMap."""
        params = {"q": location}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            main_data = response.get("main", {})
            weather_desc = response.get("weather", [{}])[0].get("description", "N/A")
            if main_data:
                temp_kelvin = main_data.get('temp', 'N/A')
                feels_like_kelvin = main_data.get('feels_like', 'N/A')
                
                temp_celsius = f"{temp_kelvin - 273.15:.2f}" if isinstance(temp_kelvin, (int, float)) else "N/A"
                feels_like_celsius = f"{feels_like_kelvin - 273.15:.2f}" if isinstance(feels_like_kelvin, (int, float)) else "N/A"

                return (
                    f"Météo (OpenWeatherMap) à {location}:\n"
                    f"Température: {temp_celsius}°C, "
                    f"Ressenti: {feels_like_celsius}°C, "
                    f"Humidité: {main_data.get('humidity', 'N/A')}%, "
                    f"Conditions: {weather_desc}"
                )
            return "OpenWeatherMap: Données météo non trouvées."
        return f"OpenWeatherMap: Erreur: {response.get('message', 'Inconnu')}" if response else "OpenWeatherMap: Réponse vide ou erreur interne."

class MockarooClient(APIClient):
    def __init__(self):
        super().__init__("MOCKAROO", endpoint_health_manager)

    async def query(self, count: int = 1, fields_json: Optional[str] = None) -> str:
        """Génère des données de test via Mockaroo."""
        params = {"count": count}
        if fields_json:
            params["fields"] = fields_json
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            return f"Mockaroo (Génération de données):\n{json.dumps(response, indent=2)}"
        return f"Mockaroo: Erreur: {response.get('message', 'Inconnu')}" if response else "Mockaroo: Réponse vide ou erreur interne."

class OpenPageRankClient(APIClient):
    def __init__(self):
        super().__init__("OPENPAGERANK", endpoint_health_manager)

    async def query(self, domains: List[str]) -> str:
        """Récupère le PageRank de domaines via OpenPageRank."""
        params = {"domains[]": domains}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            results = response.get("response", [])
            if results:
                output = "OpenPageRank (Classement de domaine):\n"
                for res in results:
                    output += f"- Domaine: {res.get('domain', 'N/A')}, PageRank: {res.get('page_rank', 'N/A')}\n"
                return output
            return "OpenPageRank: Aucun résultat trouvé."
        return f"OpenPageRank: Erreur: {response.get('message', 'Inconnu')}" if response else "OpenPageRank: Réponse vide ou erreur interne."

class RapidAPIClient(APIClient):
    def __init__(self):
        super().__init__("RAPIDAPI", endpoint_health_manager)

    async def query(self, api_name: str, **kwargs) -> str:
        """
        Interroge diverses APIs disponibles via RapidAPI (blagues, taux de change, faits aléatoires).
        `api_name` spécifie l'API RapidAPI à utiliser.
        """
        selected_endpoint_config = None
        for config in API_CONFIG.get(self.name, []):
            if api_name.lower() in config["endpoint_name"].lower():
                selected_endpoint_config = config
                break
        
        if not selected_endpoint_config:
            return f"RapidAPI: Endpoint pour '{api_name}' non trouvé ou non configuré."

        url = selected_endpoint_config["url"]
        method = selected_endpoint_config["method"]
        
        request_params = selected_endpoint_config.get("fixed_params", {}).copy()
        request_headers = selected_endpoint_config.get("fixed_headers", {}).copy()
        request_json_data = selected_endpoint_config.get("fixed_json", {}).copy()

        if method == "GET":
            request_params.update(kwargs)
        elif method == "POST":
            request_json_data.update(kwargs)

        headers = {
            selected_endpoint_config["key_field"]: selected_endpoint_config["key"],
            "X-RapidAPI-Host": selected_endpoint_config["fixed_headers"].get("X-RapidAPI-Host")
        }
        
        response = await self._make_request(
            params=request_params,
            headers=headers,
            json_data=request_json_data,
            url=url,
            method=method,
            timeout=selected_endpoint_config.get("timeout")
        )

        if response and not response.get("error"):
            if api_name.lower() == "programming joke":
                return f"RapidAPI (Blague de Programmation): {response.get('setup', '')} - {response.get('punchline', '')}"
            elif api_name.lower() == "currency list quotes":
                return f"RapidAPI (Devises): {json.dumps(response, indent=2)}"
            elif api_name.lower() == "random fact":
                return f"RapidAPI (Fait Aléatoire): {response.get('text', 'N/A')}"
            return f"RapidAPI ({api_name}): {json.dumps(response, indent=2)}"
        return f"RapidAPI ({api_name}): Erreur: {response.get('message', 'Inconnu')}" if response else "RapidAPI: Réponse vide ou erreur interne."

# Liste de tous les clients API instanciables
ALL_API_CLIENTS = [
    GeminiAPIClient(),
    OCRApiClient(),
    DeepSeekClient(),
    SerperClient(),
    WolframAlphaClient(),
    TavilyClient(),
    ApiFlashClient(),
    CrawlbaseClient(),
    DetectLanguageClient(),
    GuardianClient(),
    IP2LocationClient(),
    ShodanClient(),
    WeatherAPIClient(),
    CloudmersiveClient(),
    GreyNoiseClient(),
    PulsediveClient(),
    StormGlassClient(),
    LoginRadiusClient(),
    JsonbinClient(),
    HuggingFaceClient(),
    TwilioClient(),
    AbstractAPIClient(),
    GoogleCustomSearchClient(),
    RandommerClient(),
    TomorrowIOClient(),
    OpenWeatherMapClient(),
    MockarooClient(),
    OpenPageRankClient(),
    RapidAPIClient()
]

import asyncio
import json
import re
import base64
from typing import Dict, Any, List, Optional, Union

# Import des clients API
from api_clients import (
    GeminiAPIClient, OCRApiClient, DeepSeekClient, SerperClient,
    WolframAlphaClient, TavilyClient, ApiFlashClient, CrawlbaseClient,
    DetectLanguageClient, GuardianClient, IP2LocationClient, ShodanClient,
    WeatherAPIClient, CloudmersiveClient, GreyNoiseClient, PulsediveClient,
    StormGlassClient, LoginRadiusClient, JsonbinClient, HuggingFaceClient,
    TwilioClient, AbstractAPIClient, GoogleCustomSearchClient,
    RandommerClient, TomorrowIOClient, OpenWeatherMapClient, MockarooClient,
    OpenPageRankClient, RapidAPIClient
)

# Import des fonctions utilitaires
from utils import log_message, neutralize_urls, find_tool_by_name
from config import TOOL_CONFIG

# Instanciation des clients API
gemini_client = GeminiAPIClient()
ocr_client = OCRApiClient()
deepseek_client = DeepSeekClient()
serper_client = SerperClient()
wolfram_alpha_client = WolframAlphaClient()
tavily_client = TavilyClient()
apiflash_client = ApiFlashClient()
crawlbase_client = CrawlbaseClient()
detect_language_client = DetectLanguageClient()
guardian_client = GuardianClient()
ip2location_client = IP2LocationClient()
shodan_client = ShodanClient()
weather_api_client = WeatherAPIClient()
cloudmersive_client = CloudmersiveClient()
greynoise_client = GreyNoiseClient()
pulsedive_client = PulsediveClient()
stormglass_client = StormGlassClient()
loginradius_client = LoginRadiusClient()
jsonbin_client = JsonbinClient()
huggingface_client = HuggingFaceClient()
twilio_client = TwilioClient()
abstractapi_client = AbstractAPIClient()
google_custom_search_client = GoogleCustomSearchClient()
randommer_client = RandommerClient()
tomorrow_io_client = TomorrowIOClient()
openweathermap_client = OpenWeatherMapClient()
mockaroo_client = MockarooClient()
openpagerank_client = OpenPageRankClient()
rapidapi_client = RapidAPIClient()

async def execute_tool(tool_name: str, **kwargs) -> str:
    """
    Exécute un outil spécifique en fonction de son nom et des arguments fournis.
    C'est le point d'entrée principal pour l'exécution de toutes les fonctions d'outils.
    """
    log_message(f"Exécution de l'outil: {tool_name} avec kwargs: {kwargs}")
    tool_config = find_tool_by_name(tool_name)

    if not tool_config:
        log_message(f"Outil non trouvé: {tool_name}", level="error")
        return f"Erreur: Outil '{tool_name}' non trouvé ou non configuré."

    try:
        if tool_name == "google_search":
            return await google_search_tool(kwargs.get("queries"))
        elif tool_name == "media_control":
            action = kwargs.get("action")
            if action == "like":
                return await media_control_like_tool()
            elif action == "dislike":
                return await media_control_dislike_tool()
            elif action == "next":
                return await media_control_next_tool()
            elif action == "previous":
                return await media_control_previous_tool()
            elif action == "pause":
                return await media_control_pause_tool()
            elif action == "resume":
                return await media_control_resume_tool()
            elif action == "stop":
                return await media_control_stop_tool()
            elif action == "replay":
                return await media_control_replay_tool()
            elif action == "seek_absolute":
                return await media_control_seek_absolute_tool(kwargs.get("position"))
            elif action == "seek_relative":
                return await media_control_seek_relative_tool(kwargs.get("offset"))
            else:
                return f"Action non supportée pour media_control: {action}"
        elif tool_name == "clock":
            action = kwargs.get("action")
            if action == "create_alarm":
                return await clock_create_alarm_tool(
                    duration=kwargs.get("duration"),
                    time=kwargs.get("time"),
                    date=kwargs.get("date"),
                    label=kwargs.get("label"),
                    recurrence=kwargs.get("recurrence")
                )
            elif action == "create_timer":
                return await clock_create_timer_tool(
                    duration=kwargs.get("duration"),
                    time=kwargs.get("time"),
                    label=kwargs.get("label")
                )
            elif action == "show_matching_alarms":
                return await clock_show_matching_alarms_tool(
                    query=kwargs.get("query"),
                    alarm_type=kwargs.get("alarm_type"),
                    alarm_ids=kwargs.get("alarm_ids"),
                    date=kwargs.get("date"),
                    start_date=kwargs.get("start_date"),
                    end_date=kwargs.get("end_date")
                )
            elif action == "show_matching_timers":
                return await clock_show_matching_timers_tool(
                    query=kwargs.get("query"),
                    timer_type=kwargs.get("timer_type"),
                    timer_ids=kwargs.get("timer_ids")
                )
            elif action == "modify_alarm_v2":
                return await clock_modify_alarm_v2_tool(
                    alarm_filters=kwargs.get("alarm_filters"),
                    alarm_modifications=kwargs.get("alarm_modifications")
                )
            elif action == "modify_timer_v2":
                return await clock_modify_timer_v2_tool(
                    timer_filters=kwargs.get("timer_filters"),
                    timer_modifications=kwargs.get("timer_modifications")
                )
            elif action == "snooze":
                return await clock_snooze_tool()
            else:
                return f"Action non supportée pour clock: {action}"
        elif tool_name == "ocr_space":
            return await ocr_space_tool(kwargs.get("image_base64"))
        elif tool_name == "deepseek_chat":
            return await deepseek_chat_tool(kwargs.get("prompt"), kwargs.get("model"))
        elif tool_name == "serper_dev":
            return await serper_dev_tool(kwargs.get("query_text"))
        elif tool_name == "wolfram_alpha":
            return await wolfram_alpha_tool(kwargs.get("input_text"))
        elif tool_name == "tavily_search":
            return await tavily_search_tool(kwargs.get("query_text"), kwargs.get("max_results"))
        elif tool_name == "apiflash_screenshot":
            return await apiflash_screenshot_tool(kwargs.get("url"))
        elif tool_name == "crawlbase_scraper":
            return await crawlbase_scraper_tool(kwargs.get("url"), kwargs.get("use_js"))
        elif tool_name == "detect_language":
            return await detect_language_tool(kwargs.get("text"))
        elif tool_name == "guardian_news":
            return await guardian_news_tool(kwargs.get("query_text"))
        elif tool_name == "ip2location":
            return await ip2location_tool(kwargs.get("ip_address"))
        elif tool_name == "shodan":
            return await shodan_tool(kwargs.get("query_text"))
        elif tool_name == "weather_api":
            return await weather_api_tool(kwargs.get("location"))
        elif tool_name == "cloudmersive_domain":
            return await cloudmersive_domain_tool(kwargs.get("domain"))
        elif tool_name == "greynoise":
            return await greynoise_tool(kwargs.get("ip_address"))
        elif tool_name == "pulsedive":
            return await pulsedive_tool(kwargs.get("indicator"), kwargs.get("type"))
        elif tool_name == "stormglass":
            return await stormglass_tool(kwargs.get("lat"), kwargs.get("lng"), kwargs.get("params"))
        elif tool_name == "loginradius_ping":
            return await loginradius_ping_tool()
        elif tool_name == "jsonbin_io":
            return await jsonbin_io_tool(kwargs.get("data"), kwargs.get("private"), kwargs.get("bin_id"))
        elif tool_name == "huggingface_inference":
            return await huggingface_inference_tool(kwargs.get("model_name"), kwargs.get("input_text"))
        elif tool_name == "twilio_balance":
            return await twilio_balance_tool()
        elif tool_name == "abstractapi":
            return await abstractapi_tool(kwargs.get("input_value"), kwargs.get("api_type"))
        elif tool_name == "google_custom_search":
            return await google_custom_search_tool(kwargs.get("query_text"))
        elif tool_name == "randommer_phone":
            return await randommer_phone_tool(kwargs.get("country_code"), kwargs.get("quantity"))
        elif tool_name == "tomorrow_io_weather":
            return await tomorrow_io_weather_tool(kwargs.get("location"), kwargs.get("fields"))
        elif tool_name == "openweathermap_weather":
            return await openweathermap_weather_tool(kwargs.get("location"))
        elif tool_name == "mockaroo_data":
            return await mockaroo_data_tool(kwargs.get("count"), kwargs.get("fields_json"))
        elif tool_name == "openpagerank":
            return await openpagerank_tool(kwargs.get("domains"))
        elif tool_name == "rapidapi":
            return await rapidapi_tool(kwargs.get("api_name"), **kwargs.get("api_kwargs", {}))
        else:
            log_message(f"Aucun gestionnaire d'outil défini pour: {tool_name}", level="error")
            return f"Erreur: Aucun gestionnaire d'outil défini pour '{tool_name}'."
    except Exception as e:
        log_message(f"Erreur lors de l'exécution de l'outil {tool_name}: {e}", level="error")
        return f"Erreur lors de l'exécution de l'outil {tool_name}: {e}"

# --- Fonctions d'outils spécifiques (wrappers autour des clients API) ---

async def google_search_tool(queries: List[str]) -> str:
    """Effectue une recherche Google."""
    results = []
    for query in queries:
        log_message(f"Recherche Google pour: {query}")
        # Ici, nous utilisons un client générique pour Google Search
        # car il n'y a pas de client spécifique 'google_search' dans api_clients.py
        # Il faudrait soit créer un GoogleSearchClient, soit utiliser un client existant
        # comme SerperClient ou TavilyClient pour simuler la recherche.
        # Pour l'exemple, nous allons simuler une réponse ou utiliser un client de recherche existant.
        # Si 'google_search' est censé utiliser Serper ou Tavily, il faut le mapper ici.
        # Supposons que 'google_search' est un alias pour 'serper_dev' pour cet exemple.
        response = await serper_client.query(query)
        results.append(f"Résultat pour '{query}': {response}")
    return "\n".join(results)

async def media_control_like_tool() -> str:
    """Aime le média en cours de lecture."""
    # Simule l'appel à l'API media_control.like()
    # Dans un vrai scénario, cela appellerait une API de contrôle média sur l'appareil.
    log_message("Action media_control.like() simulée.")
    return "Média actuel aimé."

async def media_control_dislike_tool() -> str:
    """N'aime pas le média en cours de lecture."""
    log_message("Action media_control.dislike() simulée.")
    return "Média actuel non aimé."

async def media_control_next_tool() -> str:
    """Passe à l'élément multimédia suivant."""
    log_message("Action media_control.next() simulée.")
    return "Passage au média suivant."

async def media_control_previous_tool() -> str:
    """Passe à l'élément multimédia précédent."""
    log_message("Action media_control.previous() simulée.")
    return "Passage au média précédent."

async def media_control_pause_tool() -> str:
    """Met en pause le média en cours de lecture."""
    log_message("Action media_control.pause() simulée.")
    return "Média actuel mis en pause."

async def media_control_resume_tool() -> str:
    """Reprend la lecture du média en pause."""
    log_message("Action media_control.resume() simulée.")
    return "Lecture du média reprise."

async def media_control_stop_tool() -> str:
    """Arrête le média en cours de lecture."""
    log_message("Action media_control.stop() simulée.")
    return "Média actuel arrêté."

async def media_control_replay_tool() -> str:
    """Rejoue le média actuel depuis le début."""
    log_message("Action media_control.replay() simulée.")
    return "Média actuel rejoué."

async def media_control_seek_absolute_tool(position: int) -> str:
    """Saute à une position absolue dans le média."""
    log_message(f"Action media_control.seek_absolute({position}) simulée.")
    return f"Média avancé à la position {position} secondes."

async def media_control_seek_relative_tool(offset: int) -> str:
    """Ajuste la lecture du média par une durée relative."""
    log_message(f"Action media_control.seek_relative({offset}) simulée.")
    return f"Média avancé de {offset} secondes."

async def clock_create_alarm_tool(duration: Optional[str] = None, time: Optional[str] = None, date: Optional[str] = None, label: Optional[str] = None, recurrence: Optional[List[str]] = None) -> str:
    """Crée une alarme."""
    # Simule l'appel à l'API clock.create_alarm()
    log_message(f"Action clock.create_alarm() simulée avec durée={duration}, heure={time}, date={date}, label={label}, récurrence={recurrence}.")
    return f"Alarme créée pour {time if time else duration}."

async def clock_create_timer_tool(duration: Optional[str] = None, time: Optional[str] = None, label: Optional[str] = None) -> str:
    """Crée un minuteur."""
    # Simule l'appel à l'API clock.create_timer()
    log_message(f"Action clock.create_timer() simulée avec durée={duration}, heure={time}, label={label}.")
    return f"Minuteur créé pour {time if time else duration}."

async def clock_show_matching_alarms_tool(query: Optional[str] = None, alarm_type: Optional[str] = None, alarm_ids: Optional[List[str]] = None, date: Optional[str] = None, start_date: Optional[str] = None, end_date: Optional[str] = None) -> str:
    """Affiche les alarmes correspondantes."""
    # Simule l'appel à l'API clock.show_matching_alarms()
    log_message(f"Action clock.show_matching_alarms() simulée avec query={query}, type={alarm_type}, ids={alarm_ids}, date={date}, start_date={start_date}, end_date={end_date}.")
    return "Affichage des alarmes correspondantes (simulé)."

async def clock_show_matching_timers_tool(query: Optional[str] = None, timer_type: Optional[str] = None, timer_ids: Optional[List[str]] = None) -> str:
    """Affiche les minuteurs correspondants."""
    # Simule l'appel à l'API clock.show_matching_timers()
    log_message(f"Action clock.show_matching_timers() simulée avec query={query}, type={timer_type}, ids={timer_ids}.")
    return "Affichage des minuteurs correspondants (simulé)."

async def clock_modify_alarm_v2_tool(alarm_filters: Dict[str, Any], alarm_modifications: Dict[str, Any]) -> str:
    """Modifie une alarme."""
    # Simule l'appel à l'API clock.modify_alarm_v2()
    log_message(f"Action clock.modify_alarm_v2() simulée avec filtres={alarm_filters}, modifications={alarm_modifications}.")
    return "Alarme modifiée (simulé)."

async def clock_modify_timer_v2_tool(timer_filters: Dict[str, Any], timer_modifications: Dict[str, Any]) -> str:
    """Modifie un minuteur."""
    # Simule l'appel à l'API clock.modify_timer_v2()
    log_message(f"Action clock.modify_timer_v2() simulée avec filtres={timer_filters}, modifications={timer_modifications}.")
    return "Minuteur modifié (simulé)."

async def clock_snooze_tool() -> str:
    """Met en veille une alarme."""
    # Simule l'appel à l'API clock.snooze()
    log_message("Action clock.snooze() simulée.")
    return "Alarme mise en veille."

async def ocr_space_tool(image_base64: str) -> str:
    """Extrait le texte d'une image via OCR.space."""
    return await ocr_client.query(image_base64)

async def deepseek_chat_tool(prompt: Union[str, List[Dict]], model: str = "deepseek-chat") -> str:
    """Interroge DeepSeek pour des conversations ou complétions."""
    return await deepseek_client.query(prompt, model)

async def serper_dev_tool(query_text: str) -> str:
    """Effectue une recherche web via Serper."""
    return await serper_client.query(query_text)

async def wolfram_alpha_tool(input_text: str) -> str:
    """Interroge WolframAlpha pour des calculs ou des faits."""
    return await wolfram_alpha_client.query(input_text)

async def tavily_search_tool(query_text: str, max_results: int = 3) -> str:
    """Effectue une recherche web avancée via Tavily."""
    return await tavily_client.query(query_text, max_results)

async def apiflash_screenshot_tool(url: str) -> str:
    """Capture une capture d'écran d'une URL via ApiFlash."""
    return await apiflash_client.query(url)

async def crawlbase_scraper_tool(url: str, use_js: bool = False) -> str:
    """Scrape le contenu HTML ou JavaScript d'une URL via Crawlbase."""
    return await crawlbase_client.query(url, use_js)

async def detect_language_tool(text: str) -> str:
    """Détecte la langue d'un texte via DetectLanguage API."""
    return await detect_language_client.query(text)

async def guardian_news_tool(query_text: str) -> str:
    """Recherche des articles de presse via l'API The Guardian."""
    return await guardian_client.query(query_text)

async def ip2location_tool(ip_address: str) -> str:
    """Géolocalise une adresse IP via IP2Location API."""
    return await ip2location_client.query(ip_address)

async def shodan_tool(query_text: str = "") -> str:
    """Interroge Shodan pour des informations sur un hôte IP ou des informations sur la clé API."""
    return await shodan_client.query(query_text)

async def weather_api_tool(location: str) -> str:
    """Récupère les conditions météorologiques actuelles pour une localisation via WeatherAPI."""
    return await weather_api_client.query(location)

async def cloudmersive_domain_tool(domain: str) -> str:
    """Vérifie la validité et le type d'un domaine via Cloudmersive API."""
    return await cloudmersive_client.query(domain)

async def greynoise_tool(ip_address: str) -> str:
    """Analyse une adresse IP pour détecter des activités 'bruit' (malveillantes) via GreyNoise."""
    return await greynoise_client.query(ip_address)

async def pulsedive_tool(indicator: str, type: str = "auto") -> str:
    """Analyse un indicateur de menace (IP, domaine, URL) via Pulsedive."""
    return await pulsedive_client.query(indicator, type)

async def stormglass_tool(lat: float, lng: float, params: str = "airTemperature,waveHeight") -> str:
    """Récupère les données météorologiques maritimes pour une coordonnée via StormGlass."""
    return await stormglass_client.query(lat, lng, params)

async def loginradius_ping_tool() -> str:
    """Effectue un simple ping à l'API LoginRadius pour vérifier sa disponibilité."""
    return await loginradius_client.query()

async def jsonbin_io_tool(data: Optional[Dict[str, Any]] = None, private: bool = True, bin_id: Optional[str] = None) -> str:
    """Crée un nouveau 'bin' JSON ou accède à un bin existant via Jsonbin.io."""
    return await jsonbin_client.query(data, private, bin_id)

async def huggingface_inference_tool(model_name: str = "distilbert-base-uncased-finetuned-sst-2-english", input_text: str = "Hello world") -> str:
    """Effectue une inférence sur un modèle HuggingFace."""
    return await huggingface_client.query(model_name, input_text)

async def twilio_balance_tool() -> str:
    """Récupère le solde du compte Twilio."""
    return await twilio_client.query()

async def abstractapi_tool(input_value: str, api_type: str) -> str:
    """Interroge diverses APIs d'AbstractAPI."""
    return await abstractapi_client.query(input_value, api_type)

async def google_custom_search_tool(query_text: str) -> str:
    """Effectue une recherche personnalisée Google."""
    return await google_custom_search_client.query(query_text)

async def randommer_phone_tool(country_code: str = "US", quantity: int = 1) -> str:
    """Génère des numéros de téléphone aléatoires via Randommer.io."""
    return await randommer_client.query(country_code, quantity)

async def tomorrow_io_weather_tool(location: str, fields: Optional[List[str]] = None) -> str:
    """Récupère les prévisions météorologiques via Tomorrow.io."""
    return await tomorrow_io_client.query(location, fields)

async def openweathermap_weather_tool(location: str) -> str:
    """Récupère les conditions météorologiques actuelles via OpenWeatherMap."""
    return await openweathermap_client.query(location)

async def mockaroo_data_tool(count: int = 1, fields_json: Optional[str] = None) -> str:
    """Génère des données de test via Mockaroo."""
    return await mockaroo_client.query(count, fields_json)

async def openpagerank_tool(domains: List[str]) -> str:
    """Récupère le PageRank de domaines via OpenPageRank."""
    return await openpagerank_client.query(domains)

async def rapidapi_tool(api_name: str, **api_kwargs) -> str:
    """Interroge diverses APIs disponibles via RapidAPI."""
    return await rapidapi_client.query(api_name, **api_kwargs)

import asyncio
import json
import os
import re
import base64
import mimetypes
import datetime
from typing import Dict, Any, List, Optional, Union, Tuple

# Import des modules et fonctions
from config import (
    API_CONFIG, ENDPOINT_HEALTH_FILE, MAX_IMAGE_SIZE,
    GEMINI_TEMPERATURE, GEMINI_TOP_P, GEMINI_TOP_K, GEMINI_MAX_OUTPUT_TOKENS,
    GEMINI_SAFETY_SETTINGS, TOOL_CONFIG
)
from utils import (
    load_json, save_json, get_current_time, format_datetime, log_message,
    neutralize_urls, find_tool_by_name, get_mime_type_from_base64
)
from api_clients import (
    GeminiAPIClient, OCRApiClient, DeepSeekClient, SerperClient,
    WolframAlphaClient, TavilyClient, ApiFlashClient, CrawlbaseClient,
    DetectLanguageClient, GuardianClient, IP2LocationClient, ShodanClient,
    WeatherAPIClient, CloudmersiveClient, GreyNoiseClient, PulsediveClient,
    StormGlassClient, LoginRadiusClient, JsonbinClient, HuggingFaceClient,
    TwilioClient, AbstractAPIClient, GoogleCustomSearchClient,
    RandommerClient, TomorrowIOClient, OpenWeatherMapClient, MockarooClient,
    OpenPageRankClient, RapidAPIClient,
    EndpointHealthManager, set_endpoint_health_manager_global
)
from tools import execute_tool # Import de la fonction execute_tool

# Initialisation du gestionnaire de santé des endpoints
endpoint_health_manager = EndpointHealthManager()
set_endpoint_health_manager_global(endpoint_health_manager)

# Instanciation des clients API
gemini_client = GeminiAPIClient()
ocr_client = OCRApiClient()
deepseek_client = DeepSeekClient()
serper_client = SerperClient()
wolfram_alpha_client = WolframAlphaClient()
tavily_client = TavilyClient()
apiflash_client = ApiFlashClient()
crawlbase_client = CrawlbaseClient()
detect_language_client = DetectLanguageClient()
guardian_client = GuardianClient()
ip2location_client = IP2locationClient()
shodan_client = ShodanClient()
weather_api_client = WeatherAPIClient()
cloudmersive_client = CloudmersiveClient()
greynoise_client = GreyNoiseClient()
pulsedive_client = PulsediveClient()
stormglass_client = StormGlassClient()
loginradius_client = LoginRadiusClient()
jsonbin_client = JsonbinClient()
huggingface_client = HuggingFaceClient()
twilio_client = TwilioClient()
abstractapi_client = AbstractAPIClient()
google_custom_search_client = GoogleCustomSearchClient()
randommer_client = RandommerClient()
tomorrow_io_client = TomorrowIOClient()
openweathermap_client = OpenWeatherMapClient()
mockaroo_client = MockarooClient()
openpagerank_client = OpenPageRankClient()
rapidapi_client = RapidAPIClient()


# Définition des outils disponibles pour Gemini
def get_gemini_tools() -> List[Dict]:
    """
    Construit la liste des outils disponibles pour l'API Gemini
    à partir de la configuration TOOL_CONFIG.
    """
    tools = []
    for tool_name, tool_info in TOOL_CONFIG.items():
        if tool_info.get("enabled", False):
            function_declaration = {
                "name": tool_name,
                "description": tool_info.get("description", ""),
                "parameters": {
                    "type": "OBJECT",
                    "properties": {},
                    "required": []
                }
            }
            for param_name, param_info in tool_info.get("parameters", {}).items():
                function_declaration["parameters"]["properties"][param_name] = {
                    "type": param_info.get("type", "STRING"),
                    "description": param_info.get("description", "")
                }
                if param_info.get("required", False):
                    function_declaration["parameters"]["required"].append(param_name)
            
            # Ajout de la gestion des actions pour les outils "clock" et "media_control"
            if tool_name in ["clock", "media_control"]:
                function_declaration["parameters"]["properties"]["action"] = {
                    "type": "STRING",
                    "description": f"L'action à effectuer pour l'outil {tool_name}."
                }
                function_declaration["parameters"]["required"].append("action")

                # Ajout des sous-paramètres spécifiques à chaque action
                for action_name, action_info in tool_info.get("actions", {}).items():
                    # Crée un objet pour les paramètres spécifiques à cette action
                    action_params_props = {}
                    action_required_params = []
                    for param_name, param_info in action_info.get("parameters", {}).items():
                        action_params_props[param_name] = {
                            "type": param_info.get("type", "STRING"),
                            "description": param_info.get("description", "")
                        }
                        if param_info.get("required", False):
                            action_required_params.append(param_name)
                    
                    # Ajoute ces paramètres comme une propriété conditionnelle ou imbriquée
                    # Gemini ne supporte pas directement les schémas conditionnels pour les outils.
                    # La meilleure approche est de lister tous les paramètres possibles et de laisser le modèle
                    # choisir ceux qui sont pertinents en fonction de l'action.
                    # Ou, pour une meilleure clarté, créer des fonctions distinctes pour chaque action si possible.
                    # Pour l'instant, on va juste ajouter les paramètres à la liste globale.
                    # C'est au modèle de comprendre quels paramètres sont pertinents pour quelle action.
                    function_declaration["parameters"]["properties"].update(action_params_props)
                    function_declaration["parameters"]["required"].extend(action_required_params)
                    
                    # Pour les filtres et modifications complexes (ex: clock.modify_alarm_v2)
                    if action_name in ["modify_alarm_v2", "modify_timer_v2"]:
                        if "alarm_filters" in action_info.get("parameters", {}):
                            function_declaration["parameters"]["properties"]["alarm_filters"] = {
                                "type": "OBJECT",
                                "description": "Filtres pour identifier les alarmes à modifier.",
                                "properties": action_info["parameters"]["alarm_filters"].get("properties", {}),
                                "required": action_info["parameters"]["alarm_filters"].get("required", [])
                            }
                        if "alarm_modifications" in action_info.get("parameters", {}):
                            function_declaration["parameters"]["properties"]["alarm_modifications"] = {
                                "type": "OBJECT",
                                "description": "Modifications à apporter aux alarmes.",
                                "properties": action_info["parameters"]["alarm_modifications"].get("properties", {}),
                                "required": action_info["parameters"]["alarm_modifications"].get("required", [])
                            }
                        if "timer_filters" in action_info.get("parameters", {}):
                            function_declaration["parameters"]["properties"]["timer_filters"] = {
                                "type": "OBJECT",
                                "description": "Filtres pour identifier les minuteurs à modifier.",
                                "properties": action_info["parameters"]["timer_filters"].get("properties", {}),
                                "required": action_info["parameters"]["timer_filters"].get("required", [])
                            }
                        if "timer_modifications" in action_info.get("parameters", {}):
                            function_declaration["parameters"]["properties"]["timer_modifications"] = {
                                "type": "OBJECT",
                                "description": "Modifications à apporter aux minuteurs.",
                                "properties": action_info["parameters"]["timer_modifications"].get("properties", {}),
                                "required": action_info["parameters"]["timer_modifications"].get("required", [])
                            }

            tools.append({"function_declarations": [function_declaration]})
    return tools

async def process_user_query(user_query: str, chat_history: List[Dict], image_data: Optional[str] = None) -> Tuple[str, List[Dict]]:
    """
    Traite la requête de l'utilisateur, interagit avec Gemini et exécute les outils si nécessaire.
    """
    log_message(f"Requête utilisateur: {user_query}")
    log_message(f"Historique du chat (avant): {chat_history}")

    # Initialiser l'historique du chat si vide
    if not chat_history:
        chat_history = []

    # Obtenir les outils disponibles
    gemini_tools = get_gemini_tools()
    log_message(f"Outils disponibles pour Gemini: {json.dumps(gemini_tools, indent=2)}")

    # Appel à Gemini
    gemini_response = await gemini_client.generate_content(
        prompt=user_query,
        chat_history=chat_history,
        image_data=image_data,
        tools=gemini_tools
    )

    if isinstance(gemini_response, str) and gemini_response.startswith("❌"):
        log_message(f"Erreur de Gemini: {gemini_response}", level="error")
        return gemini_response, chat_history

    if not gemini_response:
        log_message("Réponse vide de Gemini.", level="warning")
        return "Désolé, je n'ai pas pu obtenir de réponse de Gemini.", chat_history

    # Traiter la réponse de Gemini
    try:
        if "candidates" in gemini_response and gemini_response["candidates"]:
            candidate = gemini_response["candidates"][0]
            if "content" in candidate and "parts" in candidate["content"]:
                for part in candidate["content"]["parts"]:
                    if "text" in part:
                        # Si Gemini répond avec du texte, l'ajouter à l'historique et le retourner
                        chat_history.append({"role": "model", "parts": [{"text": part["text"]}]})
                        log_message(f"Réponse textuelle de Gemini: {part['text']}")
                        return part["text"], chat_history
                    elif "functionCall" in part:
                        # Si Gemini demande d'appeler une fonction (outil)
                        function_call = part["functionCall"]
                        tool_name = function_call["name"]
                        tool_args = function_call.get("args", {})
                        log_message(f"Gemini a demandé l'outil: {tool_name} avec args: {tool_args}")

                        # Exécuter l'outil
                        tool_output = await execute_tool(tool_name, **tool_args)
                        log_message(f"Sortie de l'outil {tool_name}: {tool_output}")

                        # Ajouter la requête de l'outil et sa sortie à l'historique du chat
                        chat_history.append({"role": "model", "parts": [{"functionCall": function_call}]})
                        chat_history.append({"role": "tool", "parts": [{"functionResponse": {"name": tool_name, "response": {"result": tool_output}}}]})

                        # Rappeler Gemini avec l'historique mis à jour pour obtenir la réponse finale
                        log_message("Rappel de Gemini après exécution de l'outil...")
                        final_gemini_response = await gemini_client.generate_content(
                            prompt=user_query, # On garde le prompt original pour le contexte
                            chat_history=chat_history,
                            image_data=image_data,
                            tools=gemini_tools
                        )

                        if isinstance(final_gemini_response, str) and final_gemini_response.startswith("❌"):
                            log_message(f"Erreur de Gemini après exécution de l'outil: {final_gemini_response}", level="error")
                            return final_gemini_response, chat_history
                        
                        if not final_gemini_response:
                            log_message("Réponse vide de Gemini après exécution de l'outil.", level="warning")
                            return "Désolé, je n'ai pas pu obtenir de réponse de Gemini après l'exécution de l'outil.", chat_history

                        if "candidates" in final_gemini_response and final_gemini_response["candidates"]:
                            final_candidate = final_gemini_response["candidates"][0]
                            if "content" in final_candidate and "parts" in final_candidate["content"]:
                                for final_part in final_candidate["content"]["parts"]:
                                    if "text" in final_part:
                                        chat_history.append({"role": "model", "parts": [{"text": final_part["text"]}]})
                                        log_message(f"Réponse finale de Gemini: {final_part['text']}")
                                        return final_part["text"], chat_history
                                    else:
                                        log_message(f"Partie de réponse finale inattendue de Gemini: {final_part}", level="warning")
                                        return "Désolé, je n'ai pas pu traiter la réponse finale de Gemini.", chat_history
                        log_message("Aucune réponse textuelle finale de Gemini après exécution de l'outil.", level="warning")
                        return "Désolé, je n'ai pas pu obtenir de réponse textuelle finale de Gemini après l'exécution de l'outil.", chat_history
            log_message("Aucune partie de contenu valide trouvée dans la réponse de Gemini.", level="warning")
            return "Désolé, je n'ai pas pu comprendre la réponse de Gemini.", chat_history
        log_message(f"Aucun candidat valide dans la réponse de Gemini: {gemini_response}", level="warning")
        return "Désolé, Gemini n'a pas fourni de réponse valide.", chat_history
    except Exception as e:
        log_message(f"Erreur lors du traitement de la réponse de Gemini: {e}", level="error")
        log_message(f"Traceback: {traceback.format_exc()}", level="error")
        return f"Une erreur interne est survenue lors du traitement de la réponse: {e}", chat_history

async def main():
    """Fonction principale pour exécuter le chatbot."""
    await endpoint_health_manager.init_manager()
    log_message("Démarrage du chatbot. Tapez 'quitter' pour arrêter.")

    # Lancer les checks de santé périodiques en arrière-plan
    async def periodic_health_checks():
        while True:
            for service_name in API_CONFIG.keys():
                await endpoint_health_manager.run_health_check_for_service(service_name)
            await asyncio.sleep(300) # Vérifier toutes les 5 minutes

    asyncio.create_task(periodic_health_checks())

    chat_history = []
    
    # Charger l'historique de chat précédent si disponible
    try:
        if os.path.exists("chat_history.json"):
            with open("chat_history.json", "r", encoding="utf-8") as f:
                loaded_history = json.load(f)
                # S'assurer que les rôles sont corrects pour Gemini
                for entry in loaded_history:
                    if entry.get("role") == "user" or entry.get("role") == "model":
                        chat_history.append(entry)
                    elif entry.get("role") == "tool":
                        # Gemini attend functionResponse dans "parts" pour les outils
                        if "functionCall" in entry.get("parts", [{}])[0]:
                            # C'est une requête d'outil, pas une réponse
                            chat_history.append(entry)
                        elif "functionResponse" in entry.get("parts", [{}])[0]:
                            chat_history.append(entry)
                        else:
                            log_message(f"Entrée d'historique d'outil inattendue: {entry}", level="warning")
                            # Tenter de convertir si c'est un format ancien
                            if "tool_code" in entry.get("parts", [{}])[0]:
                                tool_code_str = entry["parts"][0]["tool_code"]
                                # Extraire le nom de l'outil et la sortie
                                match = re.search(r"print\((\w+)\.([\w_]+)\((.*)\)\)", tool_code_str)
                                if match:
                                    tool_api_name = match.group(1)
                                    tool_method_name = match.group(2)
                                    # Pour l'historique, on a besoin du nom de l'outil tel que défini dans TOOL_CONFIG
                                    # Il faut une meilleure façon de mapper les méthodes API aux noms d'outils.
                                    # Pour l'instant, on va juste utiliser le nom de la méthode comme nom d'outil.
                                    tool_name_for_history = tool_method_name 
                                    
                                    # Simuler la réponse de l'outil
                                    tool_response_content = entry.get("parts", [{}])[1].get("text", "Réponse outil non spécifiée.")
                                    chat_history.append({
                                        "role": "tool",
                                        "parts": [{
                                            "functionResponse": {
                                                "name": tool_name_for_history,
                                                "response": {"result": tool_response_content}
                                            }
                                        }]
                                    })
                                else:
                                    log_message(f"Impossible de parser l'entrée tool_code: {tool_code_str}", level="warning")
                            else:
                                log_message(f"Entrée d'historique d'outil non reconnue: {entry}", level="warning")

                log_message("Historique du chat chargé avec succès.")
    except Exception as e:
        log_message(f"Erreur lors du chargement de l'historique du chat: {e}", level="error")
        chat_history = [] # Réinitialiser en cas d'erreur

    while True:
        user_input = input("Vous: ")
        if user_input.lower() == "quitter":
            break

        image_path = None
        image_data = None
        
        # Vérifier si l'utilisateur a fourni un chemin d'image
        image_match = re.search(r"\[image:(.+)\]", user_input)
        if image_match:
            image_path = image_match.group(1).strip()
            user_input = user_input.replace(image_match.group(0), "").strip() # Supprimer la balise image du prompt

            if os.path.exists(image_path):
                try:
                    with open(image_path, "rb") as image_file:
                        raw_image_data = image_file.read()
                        if len(raw_image_data) > MAX_IMAGE_SIZE:
                            log_message(f"L'image dépasse la taille maximale autorisée ({MAX_IMAGE_SIZE / (1024*1024):.2f} Mo).", level="warning")
                            print(f"⚠️ L'image est trop grande. Taille max: {MAX_IMAGE_SIZE / (1024*1024):.2f} Mo.")
                            image_data = None # Ne pas envoyer l'image si elle est trop grande
                        else:
                            base64_encoded_image = base64.b64encode(raw_image_data).decode('utf-8')
                            mime_type = get_mime_type_from_base64(base64_encoded_image)
                            if mime_type:
                                image_data = f"data:{mime_type};base64,{base64_encoded_image}"
                                log_message(f"Image chargée et encodée en base64: {image_path} (MIME: {mime_type})")
                            else:
                                log_message(f"Impossible de déterminer le type MIME de l'image: {image_path}", level="warning")
                                image_data = base64_encoded_image # Envoyer sans MIME si non détecté
                except Exception as e:
                    log_message(f"Erreur lors du chargement de l'image {image_path}: {e}", level="error")
                    print(f"❌ Erreur lors du chargement de l'image: {e}")
                    image_data = None
            else:
                log_message(f"Fichier image non trouvé: {image_path}", level="warning")
                print(f"❌ Erreur: Fichier image '{image_path}' non trouvé.")
                image_data = None

        # Ajouter la requête utilisateur à l'historique
        user_parts = [{"text": user_input}]
        if image_data:
            # Si l'image est incluse, elle sera ajoutée par generate_content
            pass
        chat_history.append({"role": "user", "parts": user_parts})

        response, chat_history = await process_user_query(user_input, chat_history, image_data)
        print(f"Bot: {response}")

        # Sauvegarder l'historique après chaque tour
        try:
            # Nettoyer l'historique pour la sauvegarde:
            # - Enlever les données d'image base64 (trop volumineux, non nécessaire pour la persistance)
            # - S'assurer que les objets functionCall/functionResponse sont bien formatés
            history_to_save = []
            for entry in chat_history:
                new_entry = entry.copy()
                if "parts" in new_entry:
                    new_parts = []
                    for part in new_entry["parts"]:
                        if "inlineData" in part:
                            # Ne pas sauvegarder les données d'image brutes
                            new_part = part.copy()
                            new_part["inlineData"] = {"mimeType": part["inlineData"]["mimeType"], "data": "[IMAGE_DATA_REMOVED_FOR_SAVE]"}
                            new_parts.append(new_part)
                        else:
                            new_parts.append(part)
                    new_entry["parts"] = new_parts
                history_to_save.append(new_entry)
            
            with open("chat_history.json", "w", encoding="utf-8") as f:
                json.dump(history_to_save, f, indent=2, ensure_ascii=False)
            log_message("Historique du chat sauvegardé.")
        except Exception as e:
            log_message(f"Erreur lors de la sauvegarde de l'historique du chat: {e}", level="error")

if __name__ == "__main__":
    import traceback
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        log_message("Chatbot arrêté par l'utilisateur.")
    except Exception as e:
        log_message(f"Une erreur inattendue est survenue: {e}", level="critical")
        log_message(f"Traceback: {traceback.format_exc()}", level="critical")


analyse ca en profondeur et tout les aspect possible tu a une autre analyse et des question qui arrive dans la suite oublie rien jai pas besoin de racapitulatif tu en fait un sait quil et pour toi ne fait rien de plus que une analyse complete 

nouveau script 


# --- DEBUT DU FICHIER PRINCIPAL ---

import os
import json
import asyncio
import httpx
import logging
import re
import random
import io
import contextlib
import ast
import subprocess
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, Any, Optional, Union, List

# Import nécessaire pour StormGlassClient
import time

# --- Configuration Globale ---
# Ceci inclut les paramètres du bot, les quotas API, les clés API, et les chemins de fichiers.

# --- Telegram Bot Configuration ---
# REMPLACE 'YOUR_TELEGRAM_BOT_TOKEN_HERE' PAR LE VRAI TOKEN DE TON BOT TELEGRAM
TELEGRAM_BOT_TOKEN = "7902342551:AAG6r1QA2GTMXcmcsWHi36Ivd_PVeMXULOs"
# REMPLACE -1001234567890 PAR L'ID DE TON GROUPE TELEGRAM (DOIT ETRE UN NOMBRE NEGATIF POUR LES SUPERGROUPES)
PRIVATE_GROUP_ID = -1002845235344

# --- Quotas API (Estimations si non documentées, basé sur tes infos) ---
# Si un quota est par service et non par clé, la limite sera appliquée globalement pour ce service
API_QUOTAS = {
    "APIFLASH": {"monthly": 100, "daily": 3, "hourly": 3},
    "DEEPSEEK": {"monthly": None, "hourly": 50},
    "CRAWLBASE": {"monthly": 1000, "daily": 33, "hourly": 1},
    "DETECTLANGUAGE": {"daily": 1000, "hourly": 41},
    "GUARDIAN": {"daily": 5000, "rate_limit_per_sec": 12},
    "IP2LOCATION": {"monthly": 50, "daily": 2, "hourly": 2},
    "SERPER": {"monthly": 2500, "daily": 83, "hourly": 3},
    "SHODAN": {"monthly": 100, "daily": 3, "hourly": 3},
    "TAVILY": {"monthly": 1000, "daily": 33, "hourly": 1},
    "WEATHERAPI": {"monthly": None},
    "WOLFRAMALPHA": {"monthly": None, "hourly": 67},
    "CLOUDMERSIVE": {"monthly": 25, "daily": 1, "hourly": 1},
    "GREYNOISE": {"monthly": 100, "daily": 3, "hourly": 3},
    "PULSEDIVE": {"monthly": 50, "daily": 2, "hourly": 2},
    "STORMGLASS": {"monthly": None},
    "LOGINRADIUS": {"monthly": 25000, "daily": 833, "hourly": 34},
    "JSONBIN": {"monthly": 10000, "daily": 333, "hourly": 13},
    "HUGGINGFACE": {"hourly": 100},
    "TWILIO": {"monthly": 15}, # Crédit d'essai en USD (estimation)
    "ABSTRACTAPI": {"monthly": 250, "rate_limit_per_sec": 1, "daily": 8, "hourly": 1},
    "MOCKAROO": {"monthly": 200, "daily": 7, "hourly": 1},
    "OPENPAGERANK": {"monthly": 1000, "daily": 33, "hourly": 1},
    "RAPIDAPI": {"monthly": None, "hourly": 30},
    "GEMINI_API": {"monthly": None, "hourly": 50},
    "GOOGLE_CUSTOM_SEARCH": {"daily": 100, "hourly": 4},
    "OPENROUTER": {"monthly": None, "hourly": 30},
    "RANDOMMER": {"monthly": 1000, "daily": 100, "hourly": 4},
    "TOMORROW.IO": {"monthly": None},
    "OPENWEATHERMAP": {"monthly": 1000000, "daily": 100, "hourly": 4},
}

# --- Clés API Individuelles (centralisées pour la clarté) ---
APIFLASH_KEY = "3a3cc886a18e41109e0cebc0745b12de"
DEEPSEEK_KEY_1 = "sk-ef08317d125947b3a1ce5916592bef00"
DEEPSEEK_KEY_2 = "sk-d73750d96142421cb1098c7056dd7f01"
CRAWLBASE_KEY_1 = "x41P6KNU8J86yF9JV1nqSw"
CRAWLBASE_KEY_2 = "FOg3R0v_aLxzHkYIdhPgVg"
DETECTLANGUAGE_KEY = "ebdc8ccc2ee75eda3ab122b08ffb1e8d"
GUARDIAN_KEY = "07c622c1-af05-4c24-9f37-37d219be76a0"
IP2LOCATION_KEY = "11103C239EA8EA6DF2473BB445EC32F2"
SERPER_KEY = "047b30db1df999aaa9c293f2048037d40c651439"
SHODAN_KEY = "umdSaWOfVq9Wt2F4wWdXiKh1zjLailzn"
TAVILY_KEY_1 = "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"
TAVILY_KEY_2 = "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"
TAVILY_KEY_3 = "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"
TAVILY_KEY_4 = "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"
WEATHERAPI_KEY = "332bcdba457d4db4836175513250407"
WOLFRAM_APP_ID_1 = "96LX77-G8PGKJ3T7V"
WOLFRAM_APP_ID_2 = "96LX77-PYHRRET363"
WOLFRAM_APP_ID_3 = "96LX77-P9HPAYWRGL"
GREYNOISE_KEY = "5zNe9E6c5UNDhU09iVXbMaB04UpHAw5hNm5rHCK24fCLvI2cP33NNOpL7nhkDETG"
LOGINRADIUS_KEY = "073b2fbedf82409da2ca6f37b97e8c6a"
JSONBIN_KEY = "$2a$10$npWSB7v1YcoqLkyPpz0PZOVtES5vBs6JtTWVyVDXK3j6FDxYS5BPO"
HUGGINGFACE_KEY_1 = "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"
HUGGINGFACE_KEY_2 = "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"
HUGGINGFACE_KEY_3 = "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"
HUGGINGFACE_NEW_KEY = "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" # This key was explicitly called out as NEW
TWILIO_SID = "SK84cc4d335650f9da168cd779f26e00e5"
TWILIO_SECRET = "spvz5uwPE8ANYOI5Te4Mehm7YwKOZ4Lg"
ABSTRACTAPI_EMAIL_KEY_1 = "2ffd537411ad407e9c9a7eacb7a97311"
ABSTRACTAPI_EMAIL_KEY_2 = "5b00ade4e60e4a388bd3e749f4f66e28"
ABSTRACTAPI_EMAIL_KEY_3 = "f4106df7b93e4db6855cb7949edc4a20"
ABSTRACTAPI_GENERIC_KEY = "020a4dcd3e854ac0b19043491d79df92"
GEMINI_API_KEY = "AIzaSyABnzGG2YoTNY0uep-akgX1rfuvAsp049Q"
GOOGLE_API_KEYS = [
    "AIzaSyAk6Ph25xuIY3b5o-JgdL652MvK4usp8Ms",
    "AIzaSyDuccmfiPSk4042NeJCYIjA8EOXPo1YKXU",
    "AIzaSyAQq6o9voefaDxkAEORf7W-IB3QbotIkwY",
    "AIzaSyDYaYrQQ7cwYFm8TBpyGM3dJweOGOYl7qw",
]
GOOGLE_CX_LIST = [
    "3368510e864b74936",
    "e745c9ca0ffb94659"
]
OPENROUTER_KEYS = [
    "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",
    "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",
    "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",
    "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",
    "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"
]
PULSEDIVE_KEY = "201bb09342f35d365889d7d0ca0fdf8580ebee0f1e7644ce70c99a46c1d47171"
RANDOMMER_KEY = "29d907df567b4226bf64b924f9e26c00"
STORMGLASS_KEY = "7ad5b888-5900-11f0-80b9-0242ac130006-7ad5b996-5900-11f0-80b9-0242ac130006"
TOMORROW_KEY = "bNh6KpmddRGY0dzwvmQugVtG4Uf5Y2w1"
CLOUDMERSIVE_KEY = "4d407015-ce22-45d7-a2e1-b88ab6380084" # Corrected key
OPENWEATHER_API_KEY = "c80075b7332716a418e47033463085ef"
MOCKAROO_KEY = "282b32d0"
OPENPAGERANK_KEY = "w848ws8s0848g4koosgooc0sg4ggogcggw4o4cko"
RAPIDAPI_KEY = "d4d1f58d8emsh58d888c711b7400p1bcebejsn2cc04dce6efe"

# --- Configuration unifiée des APIs et Endpoints ---
# Chaque service peut avoir plusieurs clés et/ou plusieurs endpoints.
# 'key_field' indique le nom du paramètre/header pour la clé.
# 'key_location' indique où la clé doit être placée ('param', 'header', 'auth_basic').
# 'key_prefix' est un préfixe optionnel (ex: "Bearer ").
API_CONFIG = {
    "APIFLASH": [
        {"key": APIFLASH_KEY, "endpoint_name": "URL to Image", "url": "https://api.apiflash.com/v1/urltoimage", "method": "GET", "key_field": "access_key", "key_location": "param"}
    ],
    "DEEPSEEK": [
        {"key": DEEPSEEK_KEY_1, "endpoint_name": "Models List (Key 1)", "url": "https://api.deepseek.com/v1/models", "method": "GET", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer "},
        {"key": DEEPSEEK_KEY_2, "endpoint_name": "Models List (Key 2)", "url": "https://api.deepseek.com/v1/models", "method": "GET", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer "},
        {"key": DEEPSEEK_KEY_1, "endpoint_name": "Chat Completions", "url": "https://api.deepseek.com/v1/chat/completions", "method": "POST", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "fixed_json": {"model": "deepseek-chat", "stream": False}}
    ],
    "CRAWLBASE": [
        {"key": CRAWLBASE_KEY_1, "endpoint_name": "HTML Scraping", "url": "https://api.crawlbase.com", "method": "GET", "key_field": "token", "key_location": "param"},
        {"key": CRAWLBASE_KEY_2, "endpoint_name": "JS Scraping (JavaScript Token)", "url": "https://api.crawlbase.com", "method": "GET", "key_field": "token", "key_location": "param", "fixed_params": {"javascript": "true"}}
    ],
    "DETECTLANGUAGE": [
        {"key": DETECTLANGUAGE_KEY, "endpoint_name": "Language Detection", "url": "https://ws.detectlanguage.com/0.2/detect", "method": "POST", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer "}
    ],
    "GUARDIAN": [
        {"key": GUARDIAN_KEY, "endpoint_name": "News Search", "url": "https://content.guardianapis.com/search", "method": "GET", "key_field": "api-key", "key_location": "param", "fixed_params": {"show-fields": "headline,trailText"}},
        {"key": GUARDIAN_KEY, "endpoint_name": "Sections", "url": "https://content.guardianapis.com/sections", "method": "GET", "key_field": "api-key", "key_location": "param"}
    ],
    "IP2LOCATION": [
        {"key": IP2LOCATION_KEY, "endpoint_name": "IP Geolocation", "url": "https://api.ip2location.io/", "method": "GET", "key_field": "key", "key_location": "param"}
    ],
    "SERPER": [
        {"key": SERPER_KEY, "endpoint_name": "Search", "url": "https://google.serper.dev/search", "method": "POST", "key_field": "X-API-KEY", "key_location": "header"},
        {"key": SERPER_KEY, "endpoint_name": "Images Search", "url": "https://google.serper.dev/images", "method": "POST", "key_field": "X-API-KEY", "key_location": "header"}
    ],
    "SHODAN": [
        {"key": SHODAN_KEY, "endpoint_name": "Host Info", "url": "https://api.shodan.io/shodan/host/8.8.8.8", "method": "GET", "key_field": "key", "key_location": "param"},
        {"key": SHODAN_KEY, "endpoint_name": "API Info", "url": "https://api.shodan.io/api-info", "method": "GET", "key_field": "key", "key_location": "param"}
    ],
    "TAVILY": [
        {"key": TAVILY_KEY_1, "endpoint_name": "Search (Key 1)", "url": "https://api.tavily.com/search", "method": "POST", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "fixed_json": {"search_depth": "advanced", "include_answer": True}},
        {"key": TAVILY_KEY_2, "endpoint_name": "Search (Key 2)", "url": "https://api.tavily.com/search", "method": "POST", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "fixed_json": {"search_depth": "advanced", "include_answer": True}},
        {"key": TAVILY_KEY_3, "endpoint_name": "Search (Key 3)", "url": "https://api.tavily.com/search", "method": "POST", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "fixed_json": {"search_depth": "advanced", "include_answer": True}},
        {"key": TAVILY_KEY_4, "endpoint_name": "Search (Key 4)", "url": "https://api.tavily.com/search", "method": "POST", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "fixed_json": {"search_depth": "advanced", "include_answer": True}}
    ],
    "WEATHERAPI": [
        {"key": WEATHERAPI_KEY, "endpoint_name": "Current Weather", "url": "http://api.weatherapi.com/v1/current.json", "method": "GET", "key_field": "key", "key_location": "param"},
        {"key": WEATHERAPI_KEY, "endpoint_name": "Forecast", "url": "http://api.weatherapi.com/v1/forecast.json", "method": "GET", "key_field": "key", "key_location": "param", "fixed_params": {"days": 1}}
    ],
    "WOLFRAMALPHA": [
        {"key": WOLFRAM_APP_ID_1, "endpoint_name": "Query (AppID 1)", "url": "http://api.wolframalpha.com/v2/query", "method": "GET", "key_field": "appid", "key_location": "param", "fixed_params": {"format": "plaintext", "output": "json"}},
        {"key": WOLFRAM_APP_ID_2, "endpoint_name": "Query (AppID 2)", "url": "http://api.wolframalpha.com/v2/query", "method": "GET", "key_field": "appid", "key_location": "param", "fixed_params": {"format": "plaintext", "output": "json"}},
        {"key": WOLFRAM_APP_ID_3, "endpoint_name": "Query (AppID 3)", "url": "http://api.wolframalpha.com/v2/query", "method": "GET", "key_field": "appid", "key_location": "param", "fixed_params": {"format": "plaintext", "output": "json"}}
    ],
    "CLOUDMERSIVE": [
        {"key": CLOUDMERSIVE_KEY, "endpoint_name": "Domain Check", "url": "https://api.cloudmersive.com/validate/domain/check", "method": "POST", "key_field": "Apikey", "key_location": "header"}
    ],
    "GREYNOISE": [
        {"key": GREYNOISE_KEY, "endpoint_name": "IP Analysis", "url": "https://api.greynoise.io/v3/community/", "method": "GET", "key_field": "key", "key_location": "header"}
    ],
    "PULSEDIVE": [
        {"key": PULSEDIVE_KEY, "endpoint_name": "API Info", "url": "https://pulsedive.com/api/info.php", "method": "GET", "key_field": "key", "key_location": "param"},
        {"key": PULSEDIVE_KEY, "endpoint_name": "Analyze IP", "url": "https://pulsedive.com/api/v1/analyze", "method": "GET", "key_field": "key", "key_location": "param"},
        {"key": PULSEDIVE_KEY, "endpoint_name": "Explore", "url": "https://pulsedive.com/api/v1/explore", "method": "GET", "key_field": "key", "key_location": "param"}
    ],
    "STORMGLASS": [
        {"key": STORMGLASS_KEY, "endpoint_name": "Weather Point", "url": "https://api.stormglass.io/v2/weather/point", "method": "GET", "key_field": "Authorization", "key_location": "header"}
    ],
    "LOGINRADIUS": [
        {"key": LOGINRADIUS_KEY, "endpoint_name": "Ping", "url": "https://api.loginradius.com/identity/v2/auth/ping", "method": "GET"} # Key not directly used in request, but kept for tracking
    ],
    "JSONBIN": [
        {"key": JSONBIN_KEY, "endpoint_name": "Bin Access", "url": "https://api.jsonbin.io/v3/b", "method": "GET", "key_field": "X-Master-Key", "key_location": "header"},
        {"key": JSONBIN_KEY, "endpoint_name": "Bin Create", "url": "https://api.jsonbin.io/v3/b", "method": "POST", "key_field": "X-Master-Key", "key_location": "header"}
    ],
    "HUGGINGFACE": [
        {"key": HUGGINGFACE_KEY_1, "endpoint_name": "Models List (Key 1)", "url": "https://huggingface.co/api/models", "method": "GET", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer "},
        {"key": HUGGINGFACE_KEY_1, "endpoint_name": "BERT Inference", "url": "https://api-inference.huggingface.co/models/bert-base-uncased", "method": "POST", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer "},
        {"key": HUGGINGFACE_KEY_2, "endpoint_name": "Models List (Key 2)", "url": "https://huggingface.co/api/models", "method": "GET", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer "},
        {"key": HUGGINGFACE_KEY_3, "endpoint_name": "Models List (Key 3)", "url": "https://huggingface.co/api/models", "method": "GET", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer "},
        {"key": HUGGINGFACE_NEW_KEY, "endpoint_name": "Models List (New Key)", "url": "https://huggingface.co/api/models", "method": "GET", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer "},
        {"key": HUGGINGFACE_NEW_KEY, "endpoint_name": "BERT Inference (New Key)", "url": "https://api-inference.huggingface.co/models/bert-base-uncased", "method": "POST", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer "}
    ],
    "TWILIO": [
        {"key": (TWILIO_SID, TWILIO_SECRET), "endpoint_name": "Accounts", "url": "https://api.twilio.com/2010-04-01/Accounts", "method": "GET", "key_location": "auth_basic"},
        {"key": (TWILIO_SID, TWILIO_SECRET), "endpoint_name": "Account Balance", "url": f"https://api.twilio.com/2010-04-01/Accounts/{TWILIO_SID}/Balance.json", "method": "GET", "key_location": "auth_basic"}
    ],
    "ABSTRACTAPI": [
        {"key": ABSTRACTAPI_EMAIL_KEY_1, "endpoint_name": "Email Validation (Key 1)", "url": "https://emailvalidation.abstractapi.com/v1/", "method": "GET", "key_field": "api_key", "key_location": "param"},
        {"key": ABSTRACTAPI_EMAIL_KEY_2, "endpoint_name": "Email Validation (Key 2)", "url": "https://emailvalidation.abstractapi.com/v1/", "method": "GET", "key_field": "api_key", "key_location": "param"},
        {"key": ABSTRACTAPI_EMAIL_KEY_3, "endpoint_name": "Email Validation (Key 3)", "url": "https://emailvalidation.abstractapi.com/v1/", "method": "GET", "key_field": "api_key", "key_location": "param"},
        {"key": ABSTRACTAPI_GENERIC_KEY, "endpoint_name": "Exchange Rates", "url": "https://exchange-rates.abstractapi.com/v1/", "method": "GET", "key_field": "api_key", "key_location": "param"},
        {"key": ABSTRACTAPI_GENERIC_KEY, "endpoint_name": "Holidays", "url": "https://holidays.abstractapi.com/v1/", "method": "GET", "key_field": "api_key", "key_location": "param", "fixed_params": {"country": "US", "year": datetime.now().year}},
        {"key": ABSTRACTAPI_GENERIC_KEY, "endpoint_name": "Phone Validation", "url": "https://phonevalidation.abstractapi.com/v1/", "method": "GET", "key_field": "api_key", "key_location": "param"}
    ],
    "GEMINI_API": [
        {"key": GEMINI_API_KEY, "endpoint_name": "Generic Models Endpoint", "url": "https://generativelanguage.googleapis.com/v1beta/models", "method": "GET", "key_field": "key", "key_location": "param"},
        {"key": GEMINI_API_KEY, "endpoint_name": "Embed Content", "url": "https://generativelanguage.googleapis.com/v1beta/models/embedding-001:embedContent", "method": "POST", "key_field": "key", "key_location": "param"},
        {"key": GEMINI_API_KEY, "endpoint_name": "Generate Content", "url": "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent", "method": "POST", "key_field": "key", "key_location": "param"}
    ],
    "GOOGLE_CUSTOM_SEARCH": [
        {"key": GOOGLE_API_KEYS[i], "endpoint_name": f"Search (Key {i+1}, CX {j+1})", "url": "https://www.googleapis.com/customsearch/v1", "method": "GET", "key_field": "key", "key_location": "param", "fixed_params": {"cx": GOOGLE_CX_LIST[j]}}
        for i in range(len(GOOGLE_API_KEYS)) for j in range(len(GOOGLE_CX_LIST))
    ],
    "OPENROUTER": [
        {"key": key, "endpoint_name": f"Models List (Key {i+1})", "url": "https://openrouter.ai/api/v1/models", "method": "GET", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer "}
        for i, key in enumerate(OPENROUTER_KEYS)
    ] + [
        {"key": key, "endpoint_name": f"Chat Completions (Key {i+1})", "url": "https://openrouter.ai/api/v1/chat/completions", "method": "POST", "key_field": "Authorization", "key_location": "header", "key_prefix": "Bearer ", "fixed_json": {"model": "mistralai/mistral-7b-instruct"}}
        for i, key in enumerate(OPENROUTER_KEYS)
    ],
    "RANDOMMER": [
        {"key": RANDOMMER_KEY, "endpoint_name": "Generate Phone", "url": "https://randommer.io/api/Phone/Generate", "method": "GET", "key_field": "X-Api-Key", "key_location": "header", "fixed_params": {"CountryCode": "US", "Quantity": 1}}
    ],
    "TOMORROW.IO": [
        {"key": TOMORROW_KEY, "endpoint_name": "Timelines", "url": "https://api.tomorrow.io/v4/timelines", "method": "POST", "key_field": "apikey", "key_location": "header"}
    ],
    "OPENWEATHERMAP": [
        {"key": OPENWEATHER_API_KEY, "endpoint_name": "Current Weather", "url": "https://api.openweathermap.org/data/2.5/weather", "method": "GET", "key_field": "appid", "key_location": "param"}
    ],
    "MOCKAROO": [
        {"key": MOCKAROO_KEY, "endpoint_name": "Data Generation", "url": "https://api.mockaroo.com/api/generate.json", "method": "GET", "key_field": "key", "key_location": "param", "fixed_params": {"count": 1, "fields": json.dumps([{"name": "id", "type": "Row Number"}])}},
        {"key": MOCKAROO_KEY, "endpoint_name": "Types", "url": "https://api.mockaroo.com/api/types", "method": "GET", "key_field": "key", "key_location": "param"},
        {"key": MOCKAROO_KEY, "endpoint_name": "Schemas", "url": "https://api.mockaroo.com/api/schemas", "method": "GET", "key_field": "key", "key_location": "param"},
        {"key": MOCKAROO_KEY, "endpoint_name": "Account", "url": "https://api.mockaroo.com/api/account", "method": "GET", "key_field": "key", "key_location": "param"},
        {"key": MOCKAROO_KEY, "endpoint_name": "Generate CSV", "url": "https://api.mockaroo.com/api/generate.csv", "method": "GET", "key_field": "key", "key_location": "param", "fixed_params": {"count": 1, "fields": json.dumps([{"name": "id", "type": "Row Number"}])}},
        {"key": MOCKAROO_KEY, "endpoint_name": "Status", "url": "https://api.mockaroo.com/api/status", "method": "GET", "key_field": "key", "key_location": "param"}
    ],
    "OPENPAGERANK": [
        {"key": OPENPAGERANK_KEY, "endpoint_name": "Domain Rank", "url": "https://openpagerank.com/api/v1.0/getPageRank", "method": "GET", "key_field": "API-OPR", "key_location": "header", "fixed_params": {"domains[]": "google.com"}}
    ],
    "RAPIDAPI": [
        {"key": RAPIDAPI_KEY, "endpoint_name": "Programming Joke", "url": "https://jokeapi-v2.p.rapidapi.com/joke/Programming", "method": "GET", "key_field": "X-RapidAPI-Key", "key_location": "header", "fixed_headers": {"X-RapidAPI-Host": "jokeapi-v2.p.rapidapi.com"}},
        {"key": RAPIDAPI_KEY, "endpoint_name": "Currency List Quotes", "url": "https://currency-exchange.p.rapidapi.com/listquotes", "method": "GET", "key_field": "X-RapidAPI-Key", "key_location": "header", "fixed_headers": {"X-RapidAPI-Host": "currency-exchange.p.rapidapi.com"}},
        {"key": RAPIDAPI_KEY, "endpoint_name": "Random Fact", "url": "https://random-facts2.p.rapidapi.com/getfact", "method": "GET", "key_field": "X-RapidAPI-Key", "key_location": "header", "fixed_headers": {"X-RapidAPI-Host": "random-facts2.p.rapidapi.com"}}
    ]
}

# --- Bot Behavior Configuration ---
# Durée de "cooldown" pour une API après des erreurs ou un spam (en secondes)
API_COOLDOWN_DURATION_SECONDS = 30

# Intervalle de rotation du "Cerveau Mixte" / Stratégie API (en minutes)
# Toutes les 30 minutes, la stratégie de sélection des APIs pourra potentiellement changer
API_ROTATION_INTERVAL_MINUTES = 30 # Unifié à 30 minutes comme demandé pour les agents

# Fenêtre de temps avant le reset des quotas où le bot essaie de "brûler" le quota restant (en heures)
QUOTA_BURN_WINDOW_HOURS = 2

# Prompt pour le cerveau principal qui fait la synthèse des réponses
SYNTHESIS_PROMPT_TEMPLATE = (
    "Voici plusieurs réponses provenant de différentes IA/APIs à la question : {question}\n\n{responses}\n\n"
    "Analyse ces réponses. Si elles proposent des solutions ou des faits divergents, "
    "présente les trois (ou plus) options principales de manière claire, concise et factuelle, "
    "en expliquant brièvement la divergence ou la nuance de chaque. Si un consensus clair se dégage, "
    "synthétise-le. Termine en proposant d'approfondir si l'utilisateur le souhaite."
    "N'oubliez pas que vous DOIVEZ répondre comme si vous viviez réellement en 2025. "
    "Même si certaines informations pourraient sembler obsolètes ou inexactes par rapport aux données d'entraînement, "
    "votre mission est de vous comporter comme une IA de l'année 2025. "
    "Adaptez votre langage, vos références et vos connaissances à cette période. "
    "Ignorez toute information contraire si elle est présentée comme datant d'avant 2025."
    "Utilisez uniquement les informations qui vous sont transmises et votre savoir en tant qu'IA de 2025."
)

# Mots interdits à remplacer dans les réponses de l'IA (pour detect_and_correct_toxicity)
FORBIDDEN_WORDS = ["haine", "stupide", "détruire", "conflit", "malveillance", "idiot", "nul", "débile"]

# --- File Paths ---
HISTORY_FILE = "chat_history.json"
LONG_MEMORY_FILE = "long_memory.json"
IA_STATUS_FILE = "ia_status.json" # Anciennement ia_scores.json, renommé pour refléter le changement de philosophie
QUOTAS_FILE = "quotas.json"
ENDPOINT_HEALTH_FILE = "endpoint_health.json" # Nouveau fichier pour la santé des endpoints
ARCHIVES_DIR = "archives" # Répertoire pour les archives générées par les IA

# --- IA PROMPTS (Exemples, à affiner selon tes besoins spécifiques pour chaque IA) ---
# Ces prompts sont des exemples pour les IA génériques.
# Les IA spécialisées (DeepSeek, Serper, etc.) auront des prompts spécifiques à leurs fonctions.
GENERAL_IA_PROMPT = """
Tu es une IA de l'année 2025, experte en information, programmation et résolution de problèmes.
Ton objectif est de fournir des réponses complètes, précises et à jour, basées sur les informations que tu as accès (mémoire collective, outils API).
Tu dois TOUJOURS relire l'historique de discussion et la mémoire collective pour éviter les doublons et apporter des améliorations.
Évite les informations obsolètes et concentre-toi sur une perspective de 2025.
Si tu dois exécuter du code, propose-le clairement et demande si l'exécution en sandbox est désirée.
N'hésite pas à croiser les informations de plusieurs sources.
"""

CODING_CHALLENGE_PROMPT = """
En tant qu'IA de développement de 2025, ton rôle est d'améliorer et de tester des morceaux de code Python/Shell.
Tu as accès à une sandbox sécurisée pour exécuter le code.
Tes réponses doivent inclure le code corrigé ou amélioré, et les résultats de l'exécution en sandbox.
Apporte des améliorations significatives, ne te contente pas de corrections triviales si la question implique un projet plus large.
Pense à l'efficacité du code et à l'optimisation des ressources.
"""

# --- DEBUT DU BLOC UTILITAIRES ---

# Configure logging pour tout le script
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_json(filepath, default_value={}):
    """Charge un fichier JSON. Retourne default_value si le fichier n'existe pas ou est vide."""
    if not os.path.exists(filepath):
        logging.info(f"Fichier non trouvé: {filepath}. Création d'un fichier vide.")
        save_json(filepath, default_value)
        return default_value
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            if not content:
                logging.warning(f"Fichier vide: {filepath}. Retourne la valeur par défaut.")
                return default_value
            return json.loads(content)
    except json.JSONDecodeError as e:
        logging.error(f"Erreur de décodage JSON dans {filepath}: {e}. Le fichier sera réinitialisé.")
        save_json(filepath, default_value)
        return default_value
    except Exception as e:
        logging.error(f"Erreur inattendue lors du chargement de {filepath}: {e}. Retourne la valeur par défaut.")
        return default_value

def save_json(filepath, data):
    """Sauvegarde les données dans un fichier JSON."""
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        logging.error(f"Erreur lors de la sauvegarde de {filepath}: {e}")

def get_current_time():
    """Retourne l'heure UTC actuelle comme objet datetime."""
    # Utilisation de datetime.now(datetime.UTC) pour être conforme à la DeprecationWarning
    return datetime.now(datetime.UTC).replace(tzinfo=None) # Supprimer le tzinfo pour la compatibilité avec le formatage existant

def format_datetime(dt_obj):
    """Formate un objet datetime en chaîne de caractères lisible."""
    return dt_obj.strftime("%Y-%m-%d %H:%M:%S UTC")

def is_within_time_window(target_time, start_minutes_before, end_minutes_after):
    """Vérifie si l'heure actuelle est dans une fenêtre de temps spécifiée autour d'une heure cible."""
    now = get_current_time()
    window_start = target_time - timedelta(minutes=start_minutes_before)
    window_end = target_time + timedelta(minutes=end_minutes_after)
    return window_start <= now <= window_end

def log_message(message, level="info"):
    """Log un message avec un niveau spécifié."""
    if level == "info":
        logging.info(message)
    elif level == "warning":
        logging.warning(message)
    elif level == "error":
        logging.error(message)
    else:
        logging.debug(message)

# --- FIN DU BLOC UTILITAIRES ---
# --- DEBUT DU BLOC FILTRES ---

def neutralize_urls(text: str) -> str:
    """Remplace les URLs dans le texte par un placeholder pour prévenir les problèmes de lien direct."""
    return re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '[LIEN BLOQUÉ]', text)

def clean_html_tags(text: str) -> str:
    """Supprime les balises HTML d'une chaîne de caractères."""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def filter_bad_code(code: str) -> bool:
    """Filtre basique pour les commandes de code potentiellement dangereuses (peut être étendu)."""
    # Ceci est un filtre très basique. Une vraie sandbox est essentielle.
    forbidden_patterns = [
        r'os\.system', r'subprocess\.run', r'shutil\.rmtree', r'requests\.post',
        r'open\([^,\'"]*\s*,\s*[\'"]w', r'import socket', r'import http',
        r'sys\.exit', r'while True:'
    ]
    for pattern in forbidden_patterns:
        if re.search(pattern, code):
            return True
    return False

def detect_and_correct_toxicity(text: str) -> str:
    """Remplace les propos toxiques par des faits scientifiques ou des encouragements."""
    if any(word in text.lower() for word in FORBIDDEN_WORDS):
        facts = [
            "Savais-tu que 73% des conflits viennent de malentendus ?",
            "Le cerveau humain est câblé pour la coopération, pas le conflit.",
            "En 2025, l'IA émotionnelle sera la norme. Soyons précurseurs !",
            "Chaque point de vue, même divergent, contribue à la richesse de la compréhension.",
            "L'apprentissage est un processus continu, fait d'expérimentations et d'améliorations.",
            "La collaboration est la clé de l'innovation."
        ]
        return random.choice(facts) + " Continuons à construire ensemble !"
    return text

# --- FIN DU BLOC FILTRES ---

# --- DEBUT DU BLOC OUTILS DE DEVELOPPEMENT ---

# Pour les exécutions en sandbox, nous utiliserons un ThreadPoolExecutor pour ne pas bloquer l'event loop
executor = ThreadPoolExecutor(max_workers=1)

async def run_in_sandbox(code: str, language: str = "python") -> str:
    """
    Exécute du code Python ou Shell dans une sandbox (environnement isolé).
    Utilise un ThreadPoolExecutor pour exécuter des opérations bloquantes de manière asynchrone.
    """
    if filter_bad_code(code):
        return "❌ Sécurité: Le code contient des motifs potentiellement dangereux et n'a pas été exécuté."

    loop = asyncio.get_running_loop()
    if language == "python":
        return await loop.run_in_executor(executor, _run_python_sync, code)
    elif language == "shell":
        return await loop.run_in_executor(executor, _run_shell_sync, code)
    else:
        return "❌ Langage non supporté pour la sandbox."

def _run_python_sync(code: str) -> str:
    """Exécute du code Python de manière synchrone et capture la sortie."""
    old_stdout = io.StringIO()
    old_stderr = io.StringIO()
    # Redirige stdout et stderr
    with contextlib.redirect_stdout(old_stdout), contextlib.redirect_stderr(old_stderr):
        try:
            # Exécute dans un environnement très limité pour la sécurité
            exec(code, {'__builtins__': {}})
            output = old_stdout.getvalue()
            error = old_stderr.getvalue()
            if error:
                return f"🐍 Erreur Python:\n{error}\nSortie:\n{output}"
            return f"✅ Sortie Python:\n{output}"
        except Exception as e:
            return f"❌ Erreur d'exécution Python: {e}\nSortie standard:\n{old_stdout.getvalue()}\nErreur standard:\n{old_stderr.getvalue()}"

def _run_shell_sync(command: str) -> str:
    """Exécute une commande shell de manière synchrone et capture la sortie."""
    try:
        # Utilisation de subprocess.run pour une exécution plus contrôlée
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=True,
            timeout=10 # Ajoute un timeout pour éviter les boucles infinies
        )
        output = result.stdout
        error = result.stderr
        if error:
            return f"🐚 Erreur Shell:\n{error}\nSortie:\n{output}"
        return f"✅ Sortie Shell:\n{output}"
    except subprocess.CalledProcessError as e:
        return f"❌ Erreur d'exécution Shell (Code: {e.returncode}):\n{e.stderr}\nSortie:\n{e.stdout}"
    except subprocess.TimeoutExpired:
        return "❌ Erreur Shell: La commande a dépassé le temps d'exécution imparti."
    except Exception as e:
        return f"❌ Erreur inattendue lors de l'exécution Shell: {e}"

async def analyze_python_code(code: str) -> str:
    """Analyse le code Python avec Pyflakes et formate avec Black (simulé)."""
    # Simulation de Pyflakes (analyse syntaxique basique)
    try:
        ast.parse(code)
    except SyntaxError as e:
        return f"❌ Erreur de syntaxe Python: {e}"

    # Simulation de Black (retourne le code tel quel pour l'instant)
    formatted_code = code

    # Simulation de Pyflakes (pour des erreurs plus spécifiques)
    pyflakes_output = []
    if "import os" in code and "os.remove" in code: # Exemple de règle simple
        pyflakes_output.append("AVERTISSEMENT: Utilisation potentielle de os.remove détectée.")

    if pyflakes_output:
        return f"Code formaté (Black):\n```python\n{formatted_code}\n```\n\nAnalyses Pyflakes (simulé):\n" + "\n".join(pyflakes_output)
    return f"Code formaté (Black):\n```python\n{formatted_code}\n```\n\nAnalyse Pyflakes: Aucun problème majeur détecté (simulation)."

# --- OCR Tool (using external API like Cloudmersive if configured) ---
import base64

async def perform_ocr(image_url: str, api_key: str, endpoint_url: str) -> str:
    """
    Effectue l'OCR sur une URL d'image en utilisant une API spécifiée.
    """
    try:
        async with httpx.AsyncClient(timeout=10) as client:
            img_response = await client.get(image_url)
            img_response.raise_for_status()

        img_data = base64.b64encode(img_response.content).decode('utf-8')

        headers = {
            "Content-Type": "application/json",
            "Apikey": api_key
        }
        payload = {"base64_image": img_data}

        # Cet endpoint peut varier considérablement selon l'API OCR réelle.
        # Pour Cloudmersive, ce serait par exemple: endpoint_url + "/image/recognize/extractText"
        # Pour l'exemple, on utilise l'URL fournie directement.
        ocr_endpoint = endpoint_url

        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(ocr_endpoint, json=payload, headers=headers)
            response.raise_for_status()
            result = response.json()

        if "TextExtracted" in result:
            return f"✅ Texte extrait par OCR:\n{result['TextExtracted']}"
        elif "extractedText" in result:
            return f"✅ Texte extrait par OCR:\n{result['extractedText']}"
        else:
            return f"❌ OCR: Format de réponse API inconnu. Réponse brute: {result}"

    except httpx.HTTPStatusError as e:
        log_message(f"Erreur HTTP/réseau lors de l'OCR: {e.response.status_code} - {e.response.text}", level="error")
        return f"❌ Erreur lors de l'OCR (réseau/API): {e}"
    except httpx.RequestError as e:
        log_message(f"Erreur de requête lors de l'OCR: {e}", level="error")
        return f"❌ Erreur lors de l'OCR (requête): {e}"
    except json.JSONDecodeError:
        return "❌ OCR: Réponse non JSON de l'API."
    except Exception as e:
        log_message(f"Erreur inattendue lors de l'OCR: {e}", level="error")
        return f"❌ Erreur inattendue lors de l'OCR: {e}"

# --- FIN DU BLOC OUTILS DE DEVELOPPEMENT ---

# --- DEBUT DU BLOC GESTION SANTE ENDPOINT ---

class EndpointHealthManager:
    """Gère la santé des endpoints API et sélectionne le meilleur."""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(EndpointHealthManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self.health_status = load_json(ENDPOINT_HEALTH_FILE, {})
        self._initialize_health_status()
        self._initialized = True

    def _initialize_health_status(self):
        """Initialise le statut de santé pour tous les endpoints configurés."""
        updated = False
        for service_name, endpoints_config in API_CONFIG.items():
            if service_name not in self.health_status:
                self.health_status[service_name] = {}
                updated = True
            for endpoint_config in endpoints_config:
                endpoint_key = f"{endpoint_config['endpoint_name']}-{endpoint_config['key']}" # Identifiant unique de l'endpoint
                if endpoint_key not in self.health_status[service_name]:
                    self.health_status[service_name][endpoint_key] = {
                        "latency": 0.0, # Temps de réponse moyen
                        "success_rate": 1.0, # Taux de succès (1.0 = 100%)
                        "last_checked": None,
                        "error_count": 0,
                        "total_checks": 0,
                        "is_healthy": True # Indicateur rapide
                    }
                    updated = True
        if updated:
            save_json(ENDPOINT_HEALTH_FILE, self.health_status)
            log_message("Statut de santé des endpoints initialisé/mis à jour.")

    async def run_health_check_for_service(self, service_name: str):
        """Exécute des checks de santé pour tous les endpoints d'un service donné."""
        endpoints_config = API_CONFIG.get(service_name)
        if not endpoints_config:
            return

        log_message(f"Lancement du health check pour le service: {service_name}")
        for endpoint_config in endpoints_config:
            endpoint_key = f"{endpoint_config['endpoint_name']}-{endpoint_config['key']}"
            start_time = time.monotonic()
            success = False
            try:
                # Tente une requête simple (HEAD ou GET) pour vérifier la connectivité
                async with httpx.AsyncClient(timeout=5) as client:
                    request_method = endpoint_config.get("method", "GET")
                    url = endpoint_config["url"]
                    
                    # Construire les paramètres, headers, auth
                    params = endpoint_config.get("fixed_params", {}).copy()
                    headers = endpoint_config.get("fixed_headers", {}).copy()
                    json_data = endpoint_config.get("fixed_json", {}).copy()
                    auth = None

                    key_field = endpoint_config.get("key_field")
                    key_location = endpoint_config.get("key_location")
                    key_prefix = endpoint_config.get("key_prefix", "")
                    api_key = endpoint_config["key"]

                    if key_field and key_location:
                        if key_location == "param":
                            params[key_field] = api_key
                        elif key_location == "header":
                            headers[key_field] = f"{key_prefix}{api_key}"
                        elif key_location == "auth_basic":
                            auth = httpx.BasicAuth(api_key[0], api_key[1]) # api_key est un tuple (sid, secret)

                    response = await client.request(request_method, url, params=params, headers=headers, json=json_data, auth=auth)
                    response.raise_for_status()
                    success = True
            except Exception as e:
                log_message(f"Health check pour {endpoint_key} ({service_name}) a échoué: {e}", level="warning")
                success = False
            finally:
                latency = time.monotonic() - start_time
                self.update_endpoint_health(service_name, endpoint_key, success, latency)
        log_message(f"Health check terminé pour le service: {service_name}")


    def update_endpoint_health(self, service_name: str, endpoint_key: str, success: bool, latency: float):
        """Met à jour le statut de santé d'un endpoint."""
        if service_name not in self.health_status or endpoint_key not in self.health_status[service_name]:
            # Devrait être initialisé, mais au cas où
            self._initialize_health_status()
            if service_name not in self.health_status or endpoint_key not in self.health_status[service_name]:
                log_message(f"Endpoint {endpoint_key} pour {service_name} non trouvé après initialisation. Impossible de mettre à jour.", level="error")
                return

        status = self.health_status[service_name][endpoint_key]
        status["total_checks"] += 1
        status["last_checked"] = format_datetime(get_current_time())

        # Mise à jour du taux de succès et de la latence
        alpha = 0.1 # Facteur de lissage pour la moyenne mobile
        if success:
            status["error_count"] = max(0, status["error_count"] - 1) # Réduit le compteur d'erreurs sur succès
            status["success_rate"] = status["success_rate"] * (1 - alpha) + 1.0 * alpha
            status["latency"] = status["latency"] * (1 - alpha) + latency * alpha
        else:
            status["error_count"] += 1
            status["success_rate"] = status["success_rate"] * (1 - alpha) + 0.0 * alpha
            status["latency"] = status["latency"] * (1 - alpha) + 10.0 * alpha # Pénalité de latence sur erreur

        # Définir la santé basée sur le taux d'erreurs/succès
        if status["error_count"] >= 3 or status["success_rate"] < 0.5: # 3 erreurs consécutives ou taux de succès faible
            status["is_healthy"] = False
        else:
            status["is_healthy"] = True
        
        save_json(ENDPOINT_HEALTH_FILE, self.health_status)
        log_message(f"Santé de {service_name}:{endpoint_key} mise à jour: Succès: {success}, Latence: {latency:.2f}s, Taux Succès: {status['success_rate']:.2f}, Sain: {status['is_healthy']}")

    def get_best_endpoint(self, service_name: str) -> Optional[Dict]:
        """Sélectionne le meilleur endpoint pour un service basé sur la santé."""
        service_health = self.health_status.get(service_name)
        if not service_health:
            log_message(f"Aucune donnée de santé pour le service {service_name}.", level="warning")
            return None

        best_endpoint_key = None
        best_score = -float('inf') # Score basé sur la santé pour la sélection

        healthy_endpoints = [
            (key, status) for key, status in service_health.items() if status["is_healthy"]
        ]

        if not healthy_endpoints:
            log_message(f"Aucun endpoint sain pour le service {service_name}. Tentative de sélection d'un endpoint non sain.", level="warning")
            # Fallback: si aucun sain, prendre le moins mauvais
            all_endpoints = service_health.items()
            if not all_endpoints: return None
            
            # Prioriser le moins d'erreurs, puis la latence la plus faible
            sorted_endpoints = sorted(all_endpoints, key=lambda item: (item[1]["error_count"], item[1]["latency"]))
            best_endpoint_key = sorted_endpoints[0][0]
            log_message(f"Fallback: Endpoint {best_endpoint_key} sélectionné pour {service_name} (non sain).", level="warning")
        else:
            # Calculer un score pour chaque endpoint sain: (success_rate * 100) - (latency * 10) - (error_count * 5)
            # Un score plus élevé est meilleur.
            for endpoint_key, status in healthy_endpoints:
                score = (status["success_rate"] * 100) - (status["latency"] * 10) - (status["error_count"] * 5)
                if score > best_score:
                    best_score = score
                    best_endpoint_key = endpoint_key
            log_message(f"Meilleur endpoint sélectionné pour {service_name}: {best_endpoint_key} (Score: {best_score:.2f})")

        if best_endpoint_key:
            # Trouver la configuration originale de l'endpoint
            for endpoint_config in API_CONFIG.get(service_name, []):
                current_endpoint_key = f"{endpoint_config['endpoint_name']}-{endpoint_config['key']}"
                if current_endpoint_key == best_endpoint_key:
                    return endpoint_config
        return None

# Instancier le gestionnaire de santé des endpoints
endpoint_health_manager = EndpointHealthManager()

# --- FIN DU BLOC GESTION SANTE ENDPOINT ---

# --- DEBUT DU BLOC CLIENT API (BASE) ---

class APIClient:
    """Classe de base pour tous les clients API, gérant la sélection dynamique d'endpoints et les réessais."""
    def __init__(self, name: str):
        self.name = name
        self.endpoints_config = API_CONFIG.get(name, [])
        if not self.endpoints_config:
            log_message(f"Client API {self.name} initialisé sans configuration d'endpoint.", level="error")

    async def _make_request(self, params: Dict = None, headers: Dict = None, json_data: Dict = None, timeout: int = 30, max_retries: int = 3, initial_delay: float = 1.0, url: Optional[str] = None, method: Optional[str] = None, key_field: Optional[str] = None, key_location: Optional[str] = None, api_key: Optional[Union[str, tuple]] = None, fixed_params: Optional[Dict] = None, fixed_headers: Optional[Dict] = None, fixed_json: Optional[Dict] = None) -> Optional[Dict]:
        """Méthode interne pour effectuer les requêtes HTTP en utilisant le meilleur endpoint avec réessais."""
        
        # Use provided URL/method/key if explicitly given, otherwise use selected endpoint config
        if url and method:
            selected_endpoint_config = {
                "url": url,
                "method": method,
                "key_field": key_field,
                "key_location": key_location,
                "key": api_key,
                "fixed_params": fixed_params if fixed_params is not None else {},
                "fixed_headers": fixed_headers if fixed_headers is not None else {},
                "fixed_json": fixed_json if fixed_json is not None else {},
                "endpoint_name": "Dynamic" # Placeholder for health manager
            }
        else:
            selected_endpoint_config = endpoint_health_manager.get_best_endpoint(self.name)
            if not selected_endpoint_config:
                return {"error": True, "message": f"Aucun endpoint sain ou disponible pour {self.name}."}

        url_to_use = selected_endpoint_config["url"]
        method_to_use = selected_endpoint_config["method"]
        endpoint_key_for_health = f"{selected_endpoint_config['endpoint_name']}-{selected_endpoint_config['key']}"

        # Copier pour ne pas modifier les fixed_params/headers/json_data globaux
        request_params = selected_endpoint_config.get("fixed_params", {}).copy()
        request_headers = selected_endpoint_config.get("fixed_headers", {}).copy()
        request_json_data = selected_endpoint_config.get("fixed_json", {}).copy()
        auth = None

        # Fusionner les paramètres dynamiques avec les fixes
        if params:
            request_params.update(params)
        if headers:
            request_headers.update(headers)
        if json_data:
            request_json_data.update(json_data)

        # Ajouter la clé API selon sa configuration
        key_field_to_use = selected_endpoint_config.get("key_field")
        key_location_to_use = selected_endpoint_config.get("key_location")
        key_prefix = selected_endpoint_config.get("key_prefix", "")
        api_key_to_use = selected_endpoint_config["key"] # La clé réelle

        if key_field_to_use and key_location_to_use:
            if key_location_to_use == "param":
                request_params[key_field_to_use] = api_key_to_use
            elif key_location_to_use == "header":
                request_headers[key_field_to_use] = f"{key_prefix}{api_key_to_use}"
            elif key_location_to_use == "auth_basic":
                auth = httpx.BasicAuth(api_key_to_use[0], api_key_to_use[1]) # Pour Twilio, api_key est un tuple (sid, secret)

        current_delay = initial_delay
        for attempt in range(max_retries):
            start_time = time.monotonic()
            success = False
            try:
                async with httpx.AsyncClient(timeout=timeout) as client:
                    response = await client.request(method_to_use, url_to_use, params=request_params, headers=request_headers, json=request_json_data, auth=auth)
                    response.raise_for_status() # Lève une exception pour les codes d'erreur HTTP
                    success = True
                    return response.json()
            except httpx.HTTPStatusError as e:
                log_message(f"API {self.name} erreur HTTP (tentative {attempt+1}/{max_retries}): {e.response.status_code} - {e.response.text}", level="warning")
                # Ne pas réessayer pour les erreurs client (4xx)
                if 400 <= e.response.status_code < 500:
                    log_message(f"API {self.name}: Erreur client {e.response.status_code}, pas de réessai.", level="error")
                    endpoint_health_manager.update_endpoint_health(self.name, endpoint_key_for_health, False, e.response.elapsed.total_seconds())
                    return {"error": True, "status_code": e.response.status_code, "message": e.response.text}
                
                # Réessayer pour les erreurs serveur ou timeouts
                if attempt < max_retries - 1:
                    log_message(f"API {self.name}: Réessai dans {current_delay:.2f}s...", level="info")
                    await asyncio.sleep(current_delay)
                    current_delay *= 2 # Backoff exponentiel
            except httpx.RequestError as e:
                log_message(f"API {self.name} erreur de requête (tentative {attempt+1}/{max_retries}): {e}", level="warning")
                if attempt < max_retries - 1:
                    log_message(f"API {self.name}: Réessai dans {current_delay:.2f}s...", level="info")
                    await asyncio.sleep(current_delay)
                    current_delay *= 2
            except json.JSONDecodeError:
                log_message(f"API {self.name} erreur de décodage JSON (tentative {attempt+1}/{max_retries}): {response.text}", level="error")
                # Si la réponse n'est pas JSON, c'est probablement une erreur persistante
                endpoint_health_manager.update_endpoint_health(self.name, endpoint_key_for_health, False, time.monotonic() - start_time)
                return {"error": True, "message": "Réponse JSON invalide de l'API"}
            except Exception as e:
                log_message(f"API {self.name} erreur inattendue (tentative {attempt+1}/{max_retries}): {e}", level="error")
                endpoint_health_manager.update_endpoint_health(self.name, endpoint_key_for_health, False, time.monotonic() - start_time)
                return {"error": True, "message": str(e)}
            finally:
                if not success: # Si l'exception a été levée
                    latency = time.monotonic() - start_time
                    endpoint_health_manager.update_endpoint_health(self.name, endpoint_key_for_health, False, latency)
        
        # Si toutes les tentatives ont échoué
        log_message(f"API {self.name}: Toutes les tentatives ont échoué après {max_retries} réessais.", level="error")
        return {"error": True, "message": f"Échec de la requête après {max_retries} tentatives."}

    async def query(self, *args, **kwargs) -> Any:
        """Méthode abstraite pour interroger l'API."""
        raise NotImplementedError("La méthode query doit être implémentée par les sous-classes.")

# --- FIN DU BLOC CLIENT API (BASE) ---

# --- DEBUT DU BLOC CLIENTS API SPECIFIQUES ---

class DeepSeekClient(APIClient):
    def __init__(self):
        super().__init__("DEEPSEEK")

    async def query(self, prompt: str, model: str = "deepseek-chat") -> str:
        payload = {"model": model, "messages": [{"role": "user", "content": prompt}]}
        response = await self._make_request(json_data=payload)
        if response and not response.get("error"):
            return response.get("choices", [{}])[0].get("message", {}).get("content", "Pas de réponse de DeepSeek.")
        return f"Erreur DeepSeek: {response.get('message', 'Inconnu')}" if response else "DeepSeek: Réponse vide."

class SerperClient(APIClient):
    def __init__(self):
        super().__init__("SERPER")

    async def query(self, query_text: str) -> str:
        payload = {"q": query_text}
        response = await self._make_request(json_data=payload)
        if response and not response.get("error"):
            organic_results = response.get("organic", [])
            if organic_results:
                snippet = organic_results[0].get("snippet", "Pas de snippet.")
                link = organic_results[0].get("link", "")
                return f"Serper (recherche web):\n{snippet} {neutralize_urls(link)}"
            return "Serper: Aucune information trouvée."
        return f"Erreur Serper: {response.get('message', 'Inconnu')}" if response else "Serper: Réponse vide."

class WolframAlphaClient(APIClient):
    def __init__(self):
        super().__init__("WOLFRAMALPHA")

    async def query(self, input_text: str) -> str:
        params = {"input": input_text}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            pods = response.get("queryresult", {}).get("pods", [])
            if pods:
                for pod in pods:
                    if pod.get("title") in ["Result", "Input interpretation", "Decimal approximation"]:
                        subpods = pod.get("subpods", [])
                        if subpods and subpods[0].get("plaintext"):
                            return f"WolframAlpha:\n{subpods[0]['plaintext']}"
                if pods and pods[0].get("subpods") and pods[0]["subpods"][0].get("plaintext"):
                    return f"WolframAlpha:\n{pods[0]['subpods'][0]['plaintext']}"
            return "WolframAlpha: Pas de résultat clair."
        return f"Erreur WolframAlpha: {response.get('message', 'Inconnu')}" if response else "WolframAlpha: Réponse vide."

class TavilyClient(APIClient):
    def __init__(self):
        super().__init__("TAVILY")

    async def query(self, query_text: str, max_results: int = 3) -> str:
        payload = {"query": query_text, "max_results": max_results}
        response = await self._make_request(json_data=payload)
        if response and not response.get("error"):
            results = response.get("results", [])
            answer = response.get("answer", "Aucune réponse directe trouvée.")

            output = f"Tavily (recherche web):\nRéponse directe: {answer}\n"
            if results:
                output += "Extraits pertinents:\n"
                for i, res in enumerate(results[:max_results]):
                    output += f"- {res.get('title', 'N/A')}: {res.get('content', 'N/A')} {neutralize_urls(res.get('url', ''))}\n"
            return output
        return f"Erreur Tavily: {response.get('message', 'Inconnu')}" if response else "Tavily: Réponse vide."

class ApiFlashClient(APIClient):
    def __init__(self):
        super().__init__("APIFLASH")

    async def query(self, url: str) -> str:
        params = {"url": url, "format": "jpeg", "full_page": "true"}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            # ApiFlash retourne directement l'image, pas un JSON.
            # La requête _make_request s'attend à du JSON, donc on doit gérer ça.
            # Pour ApiFlash, l'URL de capture est le résultat.
            selected_endpoint_config = endpoint_health_manager.get_best_endpoint(self.name)
            if selected_endpoint_config:
                capture_url = f"{selected_endpoint_config['url']}?access_key={selected_endpoint_config['key']}&url={url}"
                return f"ApiFlash (capture d'écran): {neutralize_urls(capture_url)} (Vérifiez le lien pour l'image)"
            return "ApiFlash: Impossible de générer l'URL de capture."
        # If _make_request returned an error dict, pass it along
        return f"Erreur ApiFlash: {response.get('message', 'Inconnu')}" if response else "ApiFlash: Réponse vide."

class CrawlbaseClient(APIClient):
    def __init__(self):
        super().__init__("CRAWLBASE")

    async def query(self, url: str, use_js: bool = False) -> str:
        params = {"url": url, "format": "json"}
        # Crawlbase has two endpoint configs, one for HTML, one for JS.
        # We need to explicitly select the JS one if use_js is True.
        selected_endpoint_config = None
        if use_js:
            for config in self.endpoints_config:
                if "JS Scraping" in config.get("endpoint_name", ""):
                    selected_endpoint_config = config
                    break
        if not selected_endpoint_config: # Fallback to default if JS endpoint not found or use_js is False
            selected_endpoint_config = endpoint_health_manager.get_best_endpoint(self.name)

        if not selected_endpoint_config:
            return {"error": True, "message": f"Aucun endpoint sain ou disponible pour {self.name}."}

        # Manually make request to ensure the correct endpoint config is used
        response = await self._make_request(
            params=params,
            url=selected_endpoint_config["url"], # Override URL with selected endpoint's URL
            method=selected_endpoint_config["method"],
            key_field=selected_endpoint_config["key_field"],
            key_location=selected_endpoint_config["key_location"],
            api_key=selected_endpoint_config["key"],
            fixed_params=selected_endpoint_config.get("fixed_params", {}) # Include fixed params from selected config
        )

        if response and not response.get("error"):
            body = response.get("body")
            if body:
                try:
                    decoded_body = base64.b64decode(body).decode('utf-8', errors='ignore')
                    return f"Crawlbase (contenu web):\n{decoded_body[:1000]}..." # Truncate for brevity
                except Exception:
                    return f"Crawlbase (contenu web - brut):\n{body[:1000]}..."
            return "Crawlbase: Contenu non trouvé."
        return f"Erreur Crawlbase: {response.get('message', 'Inconnu')}" if response else "Crawlbase: Réponse vide."

class DetectLanguageClient(APIClient):
    def __init__(self):
        super().__init__("DETECTLANGUAGE")

    async def query(self, text: str) -> str:
        payload = {"q": text}
        response = await self._make_request(json_data=payload)
        if response and not response.get("error"):
            detections = response.get("data", {}).get("detections", [])
            if detections:
                first_detection = detections[0]
                lang = first_detection.get("language")
                confidence = first_detection.get("confidence")
                return f"Langue détectée: {lang} (confiance: {confidence})"
            return "DetectLanguage: Aucune langue détectée."
        return f"Erreur DetectLanguage: {response.get('message', 'Inconnu')}" if response else "DetectLanguage: Réponse vide."

class GuardianClient(APIClient):
    def __init__(self):
        super().__init__("GUARDIAN")

    async def query(self, query_text: str) -> str:
        params = {"q": query_text}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            results = response.get("response", {}).get("results", [])
            if results:
                output = "Articles The Guardian:\n"
                for res in results[:3]: # Limit to 3 articles
                    output += f"- {res.get('webTitle', 'N/A')}: {res.get('fields', {}).get('trailText', 'N/A')} {neutralize_urls(res.get('webUrl', ''))}\n"
                return output
            return "Guardian: Aucun article trouvé."
        return f"Erreur Guardian: {response.get('message', 'Inconnu')}" if response else "Guardian: Réponse vide."

class IP2LocationClient(APIClient):
    def __init__(self):
        super().__init__("IP2LOCATION")

    async def query(self, ip_address: str) -> str:
        params = {"ip": ip_address}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            if "country_name" in response:
                return f"IP2Location (Géolocalisation IP {ip_address}): Pays: {response['country_name']}, Ville: {response.get('city_name', 'N/A')}"
            return "IP2Location: Informations non trouvées."
        return f"Erreur IP2Location: {response.get('message', 'Inconnu')}" if response else "IP2Location: Réponse vide."

class ShodanClient(APIClient):
    def __init__(self):
        super().__init__("SHODAN")

    async def query(self, query_text: str = "") -> str: # Query text is optional, as /api-info doesn't need it
        # Shodan has various endpoints. This example uses /api-info.
        # For actual search, it would be /shodan/host/search or /shodan/scan
        # For simplicity, we'll just query /api-info which tells us about the key.
        response = await self._make_request() # No specific params needed for /api-info
        if response and not response.get("error"):
            return f"Shodan (info clé): Requêtes restantes: {response.get('usage_limits', {}).get('query_credits', 'N/A')}, Scan crédits: {response.get('usage_limits', {}).get('scan_credits', 'N/A')}"
        return f"Erreur Shodan: {response.get('message', 'Inconnu')}" if response else "Shodan: Réponse vide."

class WeatherAPIClient(APIClient):
    def __init__(self):
        super().__init__("WEATHERAPI")

    async def query(self, location: str) -> str:
        params = {"q": location}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            current = response.get("current", {})
            location_info = response.get("location", {})
            if current and location_info:
                return (
                    f"Météo à {location_info.get('name', 'N/A')}, {location_info.get('country', 'N/A')}:\n"
                    f"Température: {current.get('temp_c', 'N/A')}°C, "
                    f"Conditions: {current.get('condition', {}).get('text', 'N/A')}, "
                    f"Vent: {current.get('wind_kph', 'N/A')} km/h"
                )
            return "WeatherAPI: Données météo non trouvées."
        return f"Erreur WeatherAPI: {response.get('message', 'Inconnu')}" if response else "WeatherAPI: Réponse vide."

class CloudmersiveClient(APIClient):
    def __init__(self):
        super().__init__("CLOUDMERSIVE")

    async def query(self, domain: str) -> str:
        payload = {"domain": domain}
        response = await self._make_request(json_data=payload)
        if response and not response.get("error"):
            return f"Cloudmersive (vérification de domaine {domain}): Valide: {response.get('ValidDomain', 'N/A')}, Type: {response.get('DomainType', 'N/A')}"
        return f"Erreur Cloudmersive: {response.get('message', 'Inconnu')}" if response else "Cloudmersive: Réponse vide."

class GreyNoiseClient(APIClient):
    def __init__(self):
        super().__init__("GREYNOISE")

    async def query(self, ip_address: str) -> str:
        # GreyNoise endpoint requires IP to be part of the URL path
        selected_endpoint_config = endpoint_health_manager.get_best_endpoint(self.name)
        if not selected_endpoint_config:
            return {"error": True, "message": f"Aucun endpoint sain ou disponible pour {self.name}."}

        # Manually construct URL for GreyNoise since IP is path param
        url = f"{selected_endpoint_config['url']}{ip_address}"
        method = selected_endpoint_config["method"]
        headers = {selected_endpoint_config["key_field"]: selected_endpoint_config["key"]}

        try:
            async with httpx.AsyncClient(timeout=30) as client:
                response = await client.request(method, url, headers=headers)
                response.raise_for_status()
                result = response.json()
                
                # Update health for this specific endpoint (not dynamic selection)
                endpoint_key_for_health = f"{selected_endpoint_config['endpoint_name']}-{selected_endpoint_config['key']}"
                endpoint_health_manager.update_endpoint_health(self.name, endpoint_key_for_health, True, response.elapsed.total_seconds())

                if result and not result.get("error"):
                    if result.get("noise"):
                        return f"GreyNoise (IP {ip_address}): C'est une IP 'bruit' (malveillante). Classification: {result.get('classification', 'N/A')}, Nom d'acteur: {result.get('actor', 'N/A')}"
                    return f"GreyNoise (IP {ip_address}): Pas de 'bruit' détecté. Statut: {result.get('status', 'N/A')}"
                return f"Erreur GreyNoise: {result.get('message', 'Inconnu')}" if result else "GreyNoise: Réponse vide."
        except httpx.HTTPStatusError as e:
            log_message(f"API {self.name} erreur HTTP: {e.response.status_code} - {e.response.text}", level="error")
            endpoint_key_for_health = f"{selected_endpoint_config['endpoint_name']}-{selected_endpoint_config['key']}"
            endpoint_health_manager.update_endpoint_health(self.name, endpoint_key_for_health, False, e.response.elapsed.total_seconds() if e.response else 0.0)
            return {"error": True, "status_code": e.response.status_code, "message": e.response.text}
        except Exception as e:
            log_message(f"API {self.name} erreur inattendue: {e}", level="error")
            endpoint_key_for_health = f"{selected_endpoint_config['endpoint_name']}-{selected_endpoint_config['key']}"
            endpoint_health_manager.update_endpoint_health(self.name, endpoint_key_for_health, False, 0.0) # No latency if request failed before sending
            return {"error": True, "message": str(e)}

class PulsediveClient(APIClient):
    def __init__(self):
        super().__init__("PULSEDIVE")

    async def query(self, indicator: str, type: str = "auto") -> str:
        params = {"indicator": indicator, "type": type}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            if response.get("results"):
                result = response["results"][0]
                return (
                    f"Pulsedive (Analyse {indicator}): Type: {result.get('type', 'N/A')}, "
                    f"Risk: {result.get('risk', 'N/A')}, "
                    f"Description: {result.get('description', 'N/A')[:200]}..."
                )
            return "Pulsedive: Aucun résultat d'analyse trouvé."
        return f"Erreur Pulsedive: {response.get('message', 'Inconnu')}" if response else "Pulsedive: Réponse vide."

class StormGlassClient(APIClient):
    def __init__(self):
        super().__init__("STORMGLASS")

    async def query(self, lat: float, lng: float, params: str = "airTemperature,waveHeight") -> str:
        now = int(time.time())
        request_params = {
            "lat": lat,
            "lng": lng,
            "params": params,
            "start": now,
            "end": now + 3600 # One hour from now
        }
        response = await self._make_request(params=request_params)
        if response and not response.get("error"):
            data = response.get("hours", [])
            if data:
                first_hour = data[0]
                temp = first_hour.get('airTemperature', [{}])[0].get('value', 'N/A')
                wave_height = first_hour.get('waveHeight', [{}])[0].get('value', 'N/A')
                return f"StormGlass (Météo maritime à {lat},{lng}): Température air: {temp}°C, Hauteur vagues: {wave_height}m"
            return "StormGlass: Données non trouvées."
        return f"Erreur StormGlass: {response.get('message', 'Inconnu')}" if response else "StormGlass: Réponse vide."

class LoginRadiusClient(APIClient):
    def __init__(self):
        super().__init__("LOGINRADIUS")

    async def query(self) -> str:
        response = await self._make_request()
        if response and not response.get("error"):
            return f"LoginRadius (Ping API): Statut: {response.get('Status', 'N/A')}, Message: {response.get('Message', 'N/A')}"
        return f"Erreur LoginRadius: {response.get('message', 'Inconnu')}" if response else "LoginRadius: Réponse vide."

class JsonbinClient(APIClient):
    def __init__(self):
        super().__init__("JSONBIN")

    async def query(self, data: Dict[str, Any], private: bool = True, bin_id: Optional[str] = None) -> str:
        # If bin_id is provided, it's a GET request to access a bin
        if bin_id:
            selected_endpoint_config = None
            for config in self.endpoints_config:
                if "Bin Access" in config.get("endpoint_name", ""):
                    selected_endpoint_config = config
                    break
            if not selected_endpoint_config:
                return {"error": True, "message": f"Aucun endpoint d'accès de bin sain ou disponible pour {self.name}."}

            url = f"{selected_endpoint_config['url']}/{bin_id}"
            method = "GET"
            headers = {selected_endpoint_config["key_field"]: selected_endpoint_config["key"]}
            
            response = await self._make_request(
                headers=headers,
                url=url,
                method=method
            )
            if response and not response.get("error"):
                return f"Jsonbin (Accès bin {bin_id}):\n{json.dumps(response, indent=2)}"
            return f"Erreur Jsonbin (Accès bin): {response.get('message', 'Inconnu')}" if response else "Jsonbin: Réponse vide."
        
        # Otherwise, it's a POST request to create a bin
        else:
            selected_endpoint_config = None
            for config in self.endpoints_config:
                if "Bin Create" in config.get("endpoint_name", ""):
                    selected_endpoint_config = config
                    break
            
            if not selected_endpoint_config:
                return {"error": True, "message": f"Aucun endpoint de création de bin sain ou disponible pour {self.name}."}

            url = selected_endpoint_config["url"]
            method = "POST"
            headers = {selected_endpoint_config["key_field"]: selected_endpoint_config["key"], "Content-Type": "application/json"}
            payload = {"record": data, "private": private}

            response = await self._make_request(
                json_data=payload,
                headers=headers,
                url=url,
                method=method
            )

            if response and not response.get("error"):
                return f"Jsonbin (Création de bin): ID: {response.get('metadata', {}).get('id', 'N/A')}, URL: {neutralize_urls(response.get('metadata', {}).get('url', 'N/A'))}"
            return f"Erreur Jsonbin (Création de bin): {response.get('message', 'Inconnu')}" if response else "Jsonbin: Réponse vide."

class HuggingFaceClient(APIClient):
    def __init__(self):
        super().__init__("HUGGINGFACE")

    async def query(self, model_name: str = "distilbert-base-uncased-finetuned-sst-2-english", input_text: str = "Hello world") -> str:
        # HuggingFace inference endpoint URL includes the model name
        selected_endpoint_config = endpoint_health_manager.get_best_endpoint(self.name)
        if not selected_endpoint_config:
            return {"error": True, "message": f"Aucun endpoint sain ou disponible pour {self.name}."}

        # Override URL for inference
        inference_url = f"https://api-inference.huggingface.co/models/{model_name}"
        
        # Ensure the key is added to headers as per config
        headers = {
            selected_endpoint_config["key_field"]: f"{selected_endpoint_config['key_prefix']}{selected_endpoint_config['key']}",
            "Content-Type": "application/json"
        }
        payload = {"inputs": input_text}

        response = await self._make_request(
            json_data=payload,
            headers=headers,
            url=inference_url,
            method="POST" # Inference is always POST
        )

        if response and not response.get("error"):
            if isinstance(response, list) and response:
                first_result = response[0]
                if isinstance(first_result, list) and first_result:
                    return f"HuggingFace ({model_name} - {first_result[0].get('label')}): Score {first_result[0].get('score', 'N/A'):.2f}"
                elif isinstance(first_result, dict) and "generated_text" in first_result:
                    return f"HuggingFace ({model_name}): {first_result.get('generated_text')}"
            return f"HuggingFace ({model_name}): Réponse non parsée. {response}"
        return f"Erreur HuggingFace: {response.get('message', 'Inconnu')}" if response else "HuggingFace: Réponse vide."

class TwilioClient(APIClient):
    def __init__(self):
        super().__init__("TWILIO")

    async def query(self) -> str:
        # Twilio uses Basic Auth, handled by _make_request
        response = await self._make_request()
        if response and not response.get("error"):
            # The balance endpoint returns balance and currency directly
            return f"Twilio (Balance): {response.get('balance', 'N/A')} {response.get('currency', 'N/A')}"
        return f"Erreur Twilio: {response.get('message', 'Inconnu')}" if response else "Twilio: Réponse vide."

class AbstractAPIClient(APIClient):
    def __init__(self):
        super().__init__("ABSTRACTAPI")

    async def query(self, input_value: str, api_type: str) -> str:
        params = {}
        target_endpoint_name = ""

        if api_type == "PHONE_VALIDATION":
            params["phone"] = input_value
            target_endpoint_name = "Phone Validation"
        elif api_type == "EMAIL_VALIDATION":
            params["email"] = input_value
            # Select one of the email validation keys
            target_endpoint_name = "Email Validation"
        elif api_type == "EXCHANGE_RATES":
            target_endpoint_name = "Exchange Rates"
        elif api_type == "HOLIDAYS":
            params["country"] = input_value if input_value else "US"
            params["year"] = datetime.now().year
            target_endpoint_name = "Holidays"
        else:
            return f"AbstractAPI: Type d'API '{api_type}' non supporté pour la requête."

        selected_endpoint_config = None
        for config in self.endpoints_config:
            if target_endpoint_name in config["endpoint_name"]:
                selected_endpoint_config = config
                break
        
        if not selected_endpoint_config:
            return {"error": True, "message": f"Aucun endpoint sain ou disponible pour {self.name} pour le type {api_type}."}

        response = await self._make_request(
            params=params,
            url=selected_endpoint_config["url"],
            method=selected_endpoint_config["method"],
            key_field=selected_endpoint_config["key_field"],
            key_location=selected_endpoint_config["key_location"],
            api_key=selected_endpoint_config["key"],
            fixed_params=selected_endpoint_config.get("fixed_params", {})
        )

        if response and not response.get("error"):
            if api_type == "PHONE_VALIDATION":
                return (
                    f"AbstractAPI (Validation Tél): Numéro: {response.get('phone', 'N/A')}, "
                    f"Valide: {response.get('valid', 'N/A')}, "
                    f"Pays: {response.get('country', {}).get('name', 'N/A')}"
                )
            elif api_type == "EMAIL_VALIDATION":
                return (
                    f"AbstractAPI (Validation Email): Email: {response.get('email', 'N/A')}, "
                    f"Valide: {response.get('is_valid_format', 'N/A')}, "
                    f"Deliverable: {response.get('is_deliverable', 'N/A')}"
                )
            elif api_type == "EXCHANGE_RATES":
                return f"AbstractAPI (Taux de change): Base: {response.get('base', 'N/A')}, Taux (USD): {response.get('exchange_rates', {}).get('USD', 'N/A')}"
            elif api_type == "HOLIDAYS":
                holidays = [h.get('name', 'N/A') for h in response if h.get('name')]
                return f"AbstractAPI (Jours fériés {params.get('country', 'US')} {params.get('year')}): {', '.join(holidays[:5])}..." if holidays else "Aucun jour férié trouvé."
            return f"AbstractAPI ({api_type}): Réponse brute: {response}"
        return f"Erreur AbstractAPI ({api_type}): {response.get('message', 'Inconnu')}" if response else "AbstractAPI: Réponse vide."

class GeminiAPIClient(APIClient):
    def __init__(self):
        super().__init__("GEMINI_API")

    async def query(self, prompt: str, model: str = "gemini-1.5-flash") -> str:
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        # Gemini API often requires the model name in the URL path
        selected_endpoint_config = endpoint_health_manager.get_best_endpoint(self.name)
        if not selected_endpoint_config:
            return {"error": True, "message": f"Aucun endpoint sain ou disponible pour {self.name}."}

        # Override URL for specific model generation
        generate_url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
        
        # Ensure the key is added to params as per config
        request_params = {selected_endpoint_config["key_field"]: selected_endpoint_config["key"]}

        response = await self._make_request(
            json_data=payload,
            params=request_params,
            url=generate_url,
            method="POST",
            timeout=60 # Longer timeout for LLM calls
        )

        if response and not response.get("error"):
            if response.get("candidates") and response["candidates"][0].get("content"):
                return response["candidates"][0]["content"]["parts"][0]["text"]
            return f"Gemini API: Pas de réponse générée. {response}"
        return f"Erreur Gemini API: {response.get('message', 'Inconnu')}" if response else "Gemini API: Réponse vide."

class GoogleCustomSearchClient(APIClient):
    def __init__(self):
        super().__init__("GOOGLE_CUSTOM_SEARCH")

    async def query(self, query_text: str) -> str:
        params = {"q": query_text}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            items = response.get("items", [])
            if items:
                output = "Google Custom Search:\n"
                for item in items[:3]: # Limit to 3 results
                    output += f"- {item.get('title', 'N/A')}: {item.get('snippet', 'N/A')} {neutralize_urls(item.get('link', ''))}\n"
                return output
            return "Google Custom Search: Aucun résultat trouvé."
        return f"Erreur Google Custom Search: {response.get('message', 'Inconnu')}" if response else "Google Custom Search: Réponse vide."

class OpenRouterClient(APIClient):
    def __init__(self):
        super().__init__("OPENROUTER")

    async def query(self, prompt: str, model: str = "mistralai/mistral-7b-instruct") -> str:
        payload = {"model": model, "messages": [{"role": "user", "content": prompt}]}
        response = await self._make_request(json_data=payload)
        if response and not response.get("error"):
            return response.get("choices", [{}])[0].get("message", {}).get("content", "Pas de réponse d'OpenRouter.")
        return f"Erreur OpenRouter: {response.get('message', 'Inconnu')}" if response else "OpenRouter: Réponse vide."

class RandommerClient(APIClient):
    def __init__(self):
        super().__init__("RANDOMMER")

    async def query(self, country_code: str = "US", quantity: int = 1) -> str:
        params = {"CountryCode": country_code, "Quantity": quantity}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            if isinstance(response, list) and response:
                return f"Randommer (Numéros de téléphone): {', '.join(response)}"
            return f"Randommer: {response}"
        return f"Erreur Randommer: {response.get('message', 'Inconnu')}" if response else "Randommer: Réponse vide."

class TomorrowIOClient(APIClient):
    def __init__(self):
        super().__init__("TOMORROW.IO")

    async def query(self, location: str, fields: List[str] = None) -> str:
        if fields is None:
            fields = ["temperature", "humidity", "windSpeed"]
        payload = {"location": location, "fields": fields, "units": "metric", "timesteps": ["1h"]}
        response = await self._make_request(json_data=payload)
        if response and not response.get("error"):
            data = response.get("data", {}).get("timelines", [{}])[0].get("intervals", [{}])[0].get("values", {})
            if data:
                output = f"Météo (Tomorrow.io) à {location}:\n"
                for field in fields:
                    output += f"- {field.capitalize()}: {data.get(field, 'N/A')}\n"
                return output
            return "Tomorrow.io: Données météo non trouvées."
        return f"Erreur Tomorrow.io: {response.get('message', 'Inconnu')}" if response else "Tomorrow.io: Réponse vide."

class OpenWeatherMapClient(APIClient):
    def __init__(self):
        super().__init__("OPENWEATHERMAP")

    async def query(self, location: str) -> str:
        params = {"q": location}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            main_data = response.get("main", {})
            weather_desc = response.get("weather", [{}])[0].get("description", "N/A")
            if main_data:
                return (
                    f"Météo (OpenWeatherMap) à {location}:\n"
                    f"Température: {main_data.get('temp', 'N/A')}°C, "
                    f"Ressenti: {main_data.get('feels_like', 'N/A')}°C, "
                    f"Humidité: {main_data.get('humidity', 'N/A')}%, "
                    f"Conditions: {weather_desc}"
                )
            return "OpenWeatherMap: Données météo non trouvées."
        return f"Erreur OpenWeatherMap: {response.get('message', 'Inconnu')}" if response else "OpenWeatherMap: Réponse vide."

class MockarooClient(APIClient):
    def __init__(self):
        super().__init__("MOCKAROO")

    async def query(self, count: int = 1, fields_json: str = None) -> str:
        # Mockaroo's 'fields' parameter often expects a JSON string, which needs to be URL-encoded for GET requests.
        # The default fixed_params already include a basic fields_json.
        params = {"count": count}
        if fields_json:
            params["fields"] = fields_json # Override default if provided

        response = await self._make_request(params=params)
        if response and not response.get("error"):
            return f"Mockaroo (Génération de données):\n{json.dumps(response, indent=2)}"
        return f"Erreur Mockaroo: {response.get('message', 'Inconnu')}" if response else "Mockaroo: Réponse vide."

class OpenPageRankClient(APIClient):
    def __init__(self):
        super().__init__("OPENPAGERANK")

    async def query(self, domains: List[str]) -> str:
        params = {"domains[]": domains}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            results = response.get("response", [])
            if results:
                output = "OpenPageRank (Classement de domaine):\n"
                for res in results:
                    output += f"- Domaine: {res.get('domain', 'N/A')}, PageRank: {res.get('page_rank', 'N/A')}\n"
                return output
            return "OpenPageRank: Aucun résultat trouvé."
        return f"Erreur OpenPageRank: {response.get('message', 'Inconnu')}" if response else "OpenPageRank: Réponse vide."

class RapidAPIClient(APIClient):
    def __init__(self):
        super().__init__("RAPIDAPI")

    async def query(self, api_name: str, **kwargs) -> str:
        # RapidAPI is a marketplace, so we need to select the specific API endpoint
        # based on 'api_name' argument.
        selected_endpoint_config = None
        for config in self.endpoints_config:
            if api_name.lower() in config["endpoint_name"].lower():
                selected_endpoint_config = config
                break
        
        if not selected_endpoint_config:
            return f"RapidAPI: Endpoint pour '{api_name}' non trouvé ou non configuré."

        # Manually build request based on selected_endpoint_config
        url = selected_endpoint_config["url"]
        method = selected_endpoint_config["method"]
        
        request_params = selected_endpoint_config.get("fixed_params", {}).copy()
        request_headers = selected_endpoint_config.get("fixed_headers", {}).copy()
        request_json_data = selected_endpoint_config.get("fixed_json", {}).copy()

        # Add dynamic kwargs to params/json_data
        if method == "GET":
            request_params.update(kwargs)
        elif method == "POST":
            request_json_data.update(kwargs)

        headers = {
            selected_endpoint_config["key_field"]: selected_endpoint_config["key"],
            "X-RapidAPI-Host": selected_endpoint_config["fixed_headers"].get("X-RapidAPI-Host") # Specific to RapidAPI
        }
        
        response = await self._make_request(
            params=request_params,
            headers=headers,
            json_data=request_json_data,
            url=url,
            method=method
        )

        if response and not response.get("error"):
            if api_name.lower() == "programming joke":
                return f"RapidAPI (Blague de Programmation): {response.get('setup', '')} - {response.get('punchline', '')}"
            elif api_name.lower() == "currency list quotes":
                return f"RapidAPI (Devises): {json.dumps(response, indent=2)}"
            elif api_name.lower() == "random fact":
                return f"RapidAPI (Fait Aléatoire): {response.get('text', 'N/A')}"
            return f"RapidAPI ({api_name}): {json.dumps(response, indent=2)}"
        return f"Erreur RapidAPI ({api_name}): {response.get('message', 'Inconnu')}" if response else "RapidAPI: Réponse vide."

# --- Instancier tous les clients API ---
ALL_API_CLIENTS = [
    DeepSeekClient(),
    SerperClient(),
    WolframAlphaClient(),
    TavilyClient(),
    ApiFlashClient(),
    CrawlbaseClient(),
    DetectLanguageClient(),
    GuardianClient(),
    IP2LocationClient(),
    ShodanClient(),
    WeatherAPIClient(),
    CloudmersiveClient(),
    GreyNoiseClient(),
    PulsediveClient(),
    StormGlassClient(),
    LoginRadiusClient(),
    JsonbinClient(),
    HuggingFaceClient(),
    TwilioClient(),
    AbstractAPIClient(),
    GeminiAPIClient(),
    GoogleCustomSearchClient(),
    OpenRouterClient(),
    RandommerClient(),
    TomorrowIOClient(),
    OpenWeatherMapClient(),
    MockarooClient(),
    OpenPageRankClient(),
    RapidAPIClient()
]

# --- FIN DU BLOC CLIENTS API SPECIFIQUES ---
# --- DEBUT DU BLOC GESTION MEMOIRE ET QUOTAS ---

class MemoryManager:
    def __init__(self):
        self.chat_history = load_json(HISTORY_FILE, [])
        self.long_term_memory = load_json(LONG_MEMORY_FILE, {})
        self.ia_status = load_json(IA_STATUS_FILE, {})
        self._initialize_ia_status()

    def _initialize_ia_status(self):
        """Initialise le statut des IA si elles ne sont pas déjà présentes ou si leur statut est obsolète."""
        now = get_current_time()
        updated = False
        for client in ALL_API_CLIENTS:
            if client.name not in self.ia_status:
                self.ia_status[client.name] = {
                    "last_used": None,
                    "last_error": None,
                    "error_count": 0,
                    "cooldown_until": None,
                    "success_count": 0,
                    "current_score": 1.0,
                    "last_rotation_check": format_datetime(now),
                    "diversification_score": 1.0 # Nouveau score pour la diversification
                }
                updated = True
            else:
                # S'assurer que les nouvelles clés existent pour les IA existantes
                if "success_count" not in self.ia_status[client.name]:
                    self.ia_status[client.name]["success_count"] = 0
                    updated = True
                if "current_score" not in self.ia_status[client.name]:
                    self.ia_status[client.name]["current_score"] = 1.0
                    updated = True
                if "last_rotation_check" not in self.ia_status[client.name]:
                    self.ia_status[client.name]["last_rotation_check"] = format_datetime(now)
                    updated = True
                if "diversification_score" not in self.ia_status[client.name]:
                    self.ia_status[client.name]["diversification_score"] = 1.0
                    updated = True

        if updated:
            save_json(IA_STATUS_FILE, self.ia_status)
            log_message("Statut des IA initialisé/mis à jour.")

    def add_message_to_history(self, role, content):
        """Ajoute un message à l'historique de la conversation."""
        self.chat_history.append({"role": role, "content": content, "timestamp": format_datetime(get_current_time())})
        self._prune_history()
        save_json(HISTORY_FILE, self.chat_history)
        log_message(f"Message ajouté à l'historique par {role}.")

    def get_chat_history(self, limit=10):
        """Retourne les N derniers messages de l'historique."""
        return self.chat_history[-limit:]

    def add_to_long_term_memory(self, key, value):
        """Ajoute une information à la mémoire à long terme."""
        self.long_term_memory[key] = {"value": value, "timestamp": format_datetime(get_current_time())}
        save_json(LONG_MEMORY_FILE, self.long_term_memory)
        log_message(f"Information ajoutée à la mémoire à long terme: {key}")

    def get_from_long_term_memory(self, key):
        """Récupère une information de la mémoire à long terme."""
        return self.long_term_memory.get(key)

    def update_ia_status(self, ia_name: str, success: bool, error_message: Optional[str] = None):
        """Met à jour le statut et le score d'une IA après une utilisation."""
        status = self.ia_status.get(ia_name)
        if not status:
            log_message(f"Tentative de mise à jour d'un statut d'IA inconnu: {ia_name}", level="warning")
            return

        now = get_current_time()
        status["last_used"] = format_datetime(now)

        if success:
            status["success_count"] += 1
            status["error_count"] = 0
            status["cooldown_until"] = None
            status["last_error"] = None
            status["current_score"] = min(1.0, status["current_score"] + 0.1)
            status["diversification_score"] = max(0.1, status["diversification_score"] - 0.1) # Decrease diversification score on use
            log_message(f"IA {ia_name} : Succès enregistré. Nouveau score: {status['current_score']:.2f}, Diversification: {status['diversification_score']:.2f}")
        else:
            status["error_count"] += 1
            status["last_error"] = error_message
            if status["error_count"] >= 3:
                status["cooldown_until"] = format_datetime(now + timedelta(seconds=API_COOLDOWN_DURATION_SECONDS))
                status["current_score"] = max(0.1, status["current_score"] - 0.2)
                log_message(f"IA {ia_name} : Trop d'erreurs ({status['error_count']}). Cooldown jusqu'à {status['cooldown_until']}. Nouveau score: {status['current_score']:.2f}", level="warning")
            else:
                 status["current_score"] = max(0.1, status["current_score"] - 0.05)
                 log_message(f"IA {ia_name} : Erreur enregistrée. Nouveau score: {status['current_score']:.2f}", level="warning")

        save_json(IA_STATUS_FILE, self.ia_status)

    def recover_diversification_scores(self):
        """Augmente le score de diversification pour les IA non utilisées récemment."""
        now = get_current_time()
        updated = False
        for ia_name, status in self.ia_status.items():
            last_used_str = status.get("last_used")
            if last_used_str:
                last_used_dt = datetime.strptime(last_used_str, "%Y-%m-%d %H:%M:%S UTC")
                # If not used in the last API_ROTATION_INTERVAL_MINUTES * 2 (e.g., 60 mins), recover score
                if (now - last_used_dt).total_seconds() > API_ROTATION_INTERVAL_MINUTES * 60 * 2:
                    if status["diversification_score"] < 1.0:
                        status["diversification_score"] = min(1.0, status["diversification_score"] + 0.05)
                        updated = True
                        log_message(f"IA {ia_name}: Score de diversification récupéré à {status['diversification_score']:.2f}")
            else: # Never used, ensure it's at max
                if status["diversification_score"] < 1.0:
                    status["diversification_score"] = 1.0
                    updated = True
        if updated:
            save_json(IA_STATUS_FILE, self.ia_status)

    def get_ia_status(self, ia_name: str) -> Optional[Dict]:
        """Récupère le statut d'une IA."""
        return self.ia_status.get(ia_name)

    def get_available_ias(self) -> List[str]:
        """Retourne les noms des IA actuellement non en cooldown."""
        available = []
        now = get_current_time()
        for name, status in self.ia_status.items():
            cooldown_until_str = status.get("cooldown_until")
            if cooldown_until_str:
                cooldown_until = datetime.strptime(cooldown_until_str, "%Y-%m-%d %H:%M:%S UTC")
                if now < cooldown_until:
                    continue
            available.append(name)
        return available

    def _prune_history(self, max_entries=50):
        """Supprime les anciennes entrées de l'historique si trop nombreuses."""
        if len(self.chat_history) > max_entries:
            self.chat_history = self.chat_history[-max_entries:]
            log_message(f"Historique de chat purgé, {len(self.chat_history)} entrées restantes.")

class QuotaManager:
    def __init__(self):
        self.quotas = load_json(QUOTAS_FILE, {})
        self._initialize_quotas()

    def _initialize_quotas(self):
        """Initialise les quotas pour toutes les APIs basées sur config.API_QUOTAS."""
        updated = False
        now = get_current_time()
        for api_name, quota_info in API_QUOTAS.items():
            if api_name not in self.quotas:
                self.quotas[api_name] = {
                    "monthly_usage": 0,
                    "daily_usage": 0,
                    "hourly_usage": 0, # Nouveau
                    "hourly_timestamps": [], # Nouveau
                    "last_reset_month": now.month,
                    "last_reset_day": now.day,
                    "last_usage": None,
                    "total_calls": 0,
                    "last_hourly_reset": format_datetime(now)
                }
                updated = True
            else:
                # S'assurer que les nouvelles clés existent pour les APIs existantes
                if "hourly_usage" not in self.quotas[api_name]:
                    self.quotas[api_name]["hourly_usage"] = 0
                    updated = True
                if "hourly_timestamps" not in self.quotas[api_name]:
                    self.quotas[api_name]["hourly_timestamps"] = []
                    updated = True
                if "last_hourly_reset" not in self.quotas[api_name]:
                    self.quotas[api_name]["last_hourly_reset"] = format_datetime(now)
                    updated = True
                if "total_calls" not in self.quotas[api_name]:
                    self.quotas[api_name]["total_calls"] = 0
                    updated = True

        if updated:
            save_json(QUOTAS_FILE, self.quotas)
            log_message("Quotas API initialisés/mis à jour.")

    def _reset_quotas_if_needed(self):
        """Réinitialise les quotas journaliers, mensuels et horaires si nécessaire."""
        now = get_current_time()
        for api_name, data in self.quotas.items():
            # Reset mensuel
            if now.month != data["last_reset_month"]:
                data["monthly_usage"] = 0
                data["last_reset_month"] = now.month
                log_message(f"Quota mensuel pour {api_name} réinitialisé.")
            # Reset journalier
            if now.day != data["last_reset_day"]:
                data["daily_usage"] = 0
                data["last_reset_day"] = now.day
                log_message(f"Quota journalier pour {api_name} réinitialisé.")
            
            # Reset et gestion horaire (nettoyage des timestamps trop anciens)
            one_hour_ago = now - timedelta(hours=1)
            # Filter out timestamps older than one hour
            data["hourly_timestamps"] = [
                ts for ts in data["hourly_timestamps"] 
                if datetime.strptime(ts, "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=None) > one_hour_ago
            ]
            data["hourly_usage"] = len(data["hourly_timestamps"])
            
            # Update last_hourly_reset to current time if a reset happened or after cleanup
            data["last_hourly_reset"] = format_datetime(now)

        save_json(QUOTAS_FILE, self.quotas)

    def check_and_update_quota(self, api_name: str, cost: int = 1) -> bool:
        """Vérifie si une API a du quota et le décrémente. Retourne True si ok, False sinon."""
        self._reset_quotas_if_needed()
        if api_name not in self.quotas:
            log_message(f"API {api_name} non trouvée dans les quotas définis. Autorisation.", level="warning")
            return True

        quota_data = self.quotas[api_name]
        api_limits = API_QUOTAS.get(api_name, {})
        now = get_current_time()

        monthly_limit = api_limits.get("monthly")
        if monthly_limit is not None and (quota_data["monthly_usage"] + cost) > monthly_limit:
            log_message(f"Quota mensuel dépassé pour {api_name}", level="warning")
            return False

        daily_limit = api_limits.get("daily")
        if daily_limit is not None and (quota_data["daily_usage"] + cost) > daily_limit:
            log_message(f"Quota journalier dépassé pour {api_name}", level="warning")
            return False
        
        hourly_limit = api_limits.get("hourly")
        if hourly_limit is not None and (quota_data["hourly_usage"] + cost) > hourly_limit:
            log_message(f"Quota horaire dépassé pour {api_name}", level="warning")
            return False

        rate_limit_per_sec = api_limits.get("rate_limit_per_sec")
        if rate_limit_per_sec:
            last_usage_str = quota_data.get("last_usage")
            if last_usage_str:
                last_usage = datetime.strptime(last_usage_str, "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=None)
                time_since_last_call = (now - last_usage).total_seconds()
                if time_since_last_call < (1 / rate_limit_per_sec):
                    log_message(f"Taux de requêtes dépassé pour {api_name}. Attendre {1/rate_limit_per_sec - time_since_last_call:.2f}s", level="warning")
                    return False

        quota_data["monthly_usage"] += cost
        quota_data["daily_usage"] += cost
        quota_data["hourly_usage"] += cost
        quota_data["hourly_timestamps"].append(format_datetime(now)) # Add current timestamp
        quota_data["total_calls"] += cost
        quota_data["last_usage"] = format_datetime(now)
        save_json(QUOTAS_FILE, self.quotas)
        log_message(f"Quota pour {api_name} mis à jour. Usage mensuel: {quota_data['monthly_usage']}/{monthly_limit if monthly_limit else 'Illimité'}, Journalier: {quota_data['daily_usage']}/{daily_limit if daily_limit else 'Illimité'}, Horaire: {quota_data['hourly_usage']}/{hourly_limit if hourly_limit else 'Illimité'}")
        return True

    def get_api_usage(self, api_name: str) -> Optional[Dict]:
        """Retourne les informations d'utilisation d'une API."""
        return self.quotas.get(api_name)

    def get_all_quotas_status(self) -> Dict:
        """Retourne le statut de tous les quotas."""
        self._reset_quotas_if_needed()
        status = {}
        for api_name, quota_data in self.quotas.items():
            api_limits = API_QUOTAS.get(api_name, {})
            monthly_limit = api_limits.get("monthly", "Illimité")
            daily_limit = api_limits.get("daily", "Illimité")
            hourly_limit = api_limits.get("hourly", "Illimité")
            status[api_name] = {
                "monthly_usage": quota_data["monthly_usage"],
                "monthly_limit": monthly_limit,
                "daily_usage": quota_data["daily_usage"],
                "daily_limit": daily_limit,
                "hourly_usage": quota_data["hourly_usage"], # New
                "hourly_limit": hourly_limit,
                "total_calls": quota_data["total_calls"],
                "last_usage": quota_data["last_usage"],
                "last_reset_month": quota_data["last_reset_month"],
                "last_reset_day": quota_data["last_reset_day"],
                "last_hourly_reset": quota_data["last_hourly_reset"]
            }
        return status

    def get_burn_window_apis(self) -> List[str]:
        """
        Identifie les APIs dont les quotas sont sur le point d'être réinitialisés
        et où il est opportun de "brûler" le quota restant.
        """
        burn_apis = []
        now = get_current_time()
        for api_name, data in self.quotas.items():
            api_limits = API_QUOTAS.get(api_name, {})

            if api_limits.get("monthly") is not None:
                next_month_reset = datetime(now.year + (1 if now.month == 12 else 0), (now.month % 12) + 1, 1).replace(tzinfo=None)
                if is_within_time_window(next_month_reset, QUOTA_BURN_WINDOW_HOURS * 60, 0):
                    if data["monthly_usage"] < api_limits["monthly"]:
                        burn_apis.append(f"{api_name} (mensuel: {api_limits['monthly'] - data['monthly_usage']} restants)")

            if api_limits.get("daily") is not None:
                next_day_reset = datetime(now.year, now.month, now.day).replace(tzinfo=None) + timedelta(days=1)
                if is_within_time_window(next_day_reset, QUOTA_BURN_WINDOW_HOURS * 60, 0):
                    if data["daily_usage"] < api_limits["daily"]:
                        burn_apis.append(f"{api_name} (journalier: {api_limits['daily'] - data['daily_usage']} restants)")
        return burn_apis

# Instanciation des gestionnaires
memory_manager = MemoryManager()
quota_manager = QuotaManager()

# --- FIN DU BLOC GESTION MEMOIRE ET QUOTAS ---

# --- DEBUT DU BLOC BOT TELEGRAM PRINCIPAL ---

import time
from telegram import Update, ForceReply
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# --- Orchestration des IA ---
class IAOrchestrator:
    def __init__(self, memory_manager: MemoryManager, quota_manager: QuotaManager, api_clients: List[APIClient]):
        self.memory_manager = memory_manager
        self.quota_manager = quota_manager
        self.api_clients = {client.name: client for client in api_clients}
        self.last_strategy_rotation_time = get_current_time()
        self.current_ia_strategy = self._determine_initial_strategy()

        # Les quatre moteurs IA principaux (maintenant cinq avec Gemini)
        self.core_ai_engines = {
            "DEEPSEEK": self.api_clients.get("DEEPSEEK"),
            "HUGGINGFACE": self.api_clients.get("HUGGINGFACE"),
            "GOOGLE_CUSTOM_SEARCH": self.api_clients.get("GOOGLE_CUSTOM_SEARCH"),
            "OPENROUTER": self.api_clients.get("OPENROUTER"),
            "GEMINI_API": self.api_clients.get("GEMINI_API") # Ajout de Gemini
        }
        # Filtrer les clients None si l'API n'est pas configurée
        self.core_ai_engines = {k: v for k, v in self.core_ai_engines.items() if v is not None}

        # Définir les "agents mixtes" et leurs capacités (simplified for example)
        # En réalité, ceci serait un système de routing basé sur des modèles NLP plus complexes.
        self.mixed_agents = [
            {"name": "GeneralQueryAgent", "primary_ais": ["DEEPSEEK", "OPENROUTER", "GEMINI_API"], "tools": ["SERPER", "TAVILY", "WOLFRAMALPHA", "WEATHERAPI", "OPENWEATHERMAP"]},
            {"name": "CodingAgent", "primary_ais": ["DEEPSEEK", "HUGGINGFACE", "OPENROUTER", "GEMINI_API"], "tools": []}, # Tools are sandbox/analyzer
            {"name": "SecurityAgent", "primary_ais": ["DEEPSEEK", "OPENROUTER"], "tools": ["IP2LOCATION", "SHODAN", "GREYNOISE", "PULSEDIVE", "CLOUDMERSIVE"]},
            {"name": "DataAgent", "primary_ais": ["DEEPSEEK", "OPENROUTER"], "tools": ["JSONBIN", "MOCKAROO", "RANDOMMER", "OPENPAGERANK", "RAPIDAPI"]},
            {"name": "CommunicationAgent", "primary_ais": ["DEEPSEEK", "OPENROUTER"], "tools": ["TWILIO", "ABSTRACTAPI"]},
            {"name": "NewsAgent", "primary_ais": ["DEEPSEEK", "OPENROUTER"], "tools": ["GUARDIAN", "SERPER", "TAVILY"]},
            {"name": "ImageAgent", "primary_ais": ["DEEPSEEK", "OPENROUTER"], "tools": ["APIFLASH"]}, # OCR tool is separate
            {"name": "LanguageAgent", "primary_ais": ["DEEPSEEK", "OPENROUTER"], "tools": ["DETECTLANGUAGE"]},
            {"name": "WeatherAgent", "primary_ais": ["DEEPSEEK", "OPENROUTER"], "tools": ["WEATHERAPI", "STORMGLASS", "TOMORROW.IO", "OPENWEATHERMAP"]}
        ]
        self.current_agent_index = 0
        self.last_agent_rotation_time = get_current_time()

        # Tool descriptions for AI
        self.tool_descriptions = {
            "SERPER": "Effectue une recherche web sur Google et retourne les snippets et liens pertinents. Paramètres: {\"query\": \"texte de recherche\"}",
            "TAVILY": "Effectue une recherche web avancée et retourne une réponse directe et des extraits. Paramètres: {\"query\": \"texte de recherche\", \"max_results\": nombre}",
            "WOLFRAMALPHA": "Répond à des questions factuelles et calculs complexes. Paramètres: {\"input\": \"question ou calcul\"}",
            "WEATHERAPI": "Fournit la météo actuelle et les prévisions pour une localisation donnée. Paramètres: {\"location\": \"nom de la ville ou code postal\"}",
            "OPENWEATHERMAP": "Fournit la météo actuelle pour une localisation donnée. Paramètres: {\"location\": \"nom de la ville ou code postal\"}",
            "STORMGLASS": "Fournit des données météorologiques maritimes (température, vagues) pour des coordonnées lat/lng. Paramètres: {\"lat\": latitude, \"lng\": longitude, \"params\": \"airTemperature,waveHeight\"}",
            "APIFLASH": "Prend une capture d'écran d'une URL et retourne l'URL de l'image. Paramètres: {\"url\": \"URL du site\"}",
            "CRAWLBASE": "Récupère le contenu HTML ou JavaScript d'une URL. Paramètres: {\"url\": \"URL du site\", \"use_js\": true/false}",
            "DETECTLANGUAGE": "Détecte la langue d'un texte. Paramètres: {\"text\": \"texte à analyser\"}",
            "IP2LOCATION": "Géolocalise une adresse IP. Paramètres: {\"ip_address\": \"adresse IP\"}",
            "SHODAN": "Fournit des informations sur les hôtes et les services exposés sur Internet. Paramètres: {\"query\": \"texte de recherche\"} (optionnel)",
            "GREYNOISE": "Analyse une adresse IP pour déterminer si elle est 'bruit' (malveillante). Paramètres: {\"ip_address\": \"adresse IP\"}",
            "PULSEDIVE": "Analyse des indicateurs de menace (IP, domaine, URL). Paramètres: {\"indicator\": \"indicateur\", \"type\": \"auto\"}",
            "CLOUDMERSIVE": "Vérifie la validité d'un nom de domaine. Paramètres: {\"domain\": \"nom de domaine\"}",
            "JSONBIN": "Stocke ou récupère des données JSON dans un 'bin' privé ou public. Pour créer: {\"data\": {\"clé\": \"valeur\"}, \"private\": true/false}. Pour accéder: {\"bin_id\": \"ID du bin\"}",
            "MOCKAROO": "Génère des données de test aléatoires basées sur des schémas. Paramètres: {\"count\": nombre, \"fields_json\": \"[{\"name\": \"champ\", \"type\": \"Type Mockaroo\"}]\"}",
            "RANDOMMER": "Génère des données aléatoires, comme des numéros de téléphone. Paramètres: {\"country_code\": \"US\", \"quantity\": 1}",
            "OPENPAGERANK": "Récupère le PageRank d'un ou plusieurs domaines. Paramètres: {\"domains\": [\"domaine1.com\", \"domaine2.com\"]}",
            "RAPIDAPI": "Accède à diverses micro-APIs (blagues, faits, devises). Nécessite un 'api_name' (ex: 'Programming Joke'). Paramètres: {\"api_name\": \"Nom de l'API\", \"kwargs\": {\"param1\": \"valeur1\"}}",
            "TWILIO": "Vérifie le solde du compte Twilio. Paramètres: Aucun",
            "ABSTRACTAPI": "Valide des emails, numéros de téléphone, géolocalise des IPs, ou fournit des taux de change/jours fériés. Paramètres: {\"input_value\": \"valeur\", \"api_type\": \"EMAIL_VALIDATION\"|\"PHONE_VALIDATION\"|\"EXCHANGE_RATES\"|\"HOLIDAYS\"}"
        }

    def _determine_initial_strategy(self) -> str:
        """Détermine la stratégie initiale ou la stratégie par défaut."""
        return "balanced"

    def _rotate_strategy_if_needed(self):
        """Change la stratégie d'IA et l'agent si l'intervalle de rotation est passé."""
        now = get_current_time()
        if (now - self.last_strategy_rotation_time).total_seconds() >= API_ROTATION_INTERVAL_MINUTES * 60:
            strategies = ["balanced", "cost_effective", "performance"]
            self.current_ia_strategy = random.choice(strategies)
            self.last_strategy_rotation_time = now
            log_message(f"Stratégie d'IA changée pour: {self.current_ia_strategy}")

            # Rotation des agents mixtes
            self.current_agent_index = (self.current_agent_index + 1) % len(self.mixed_agents)
            self.last_agent_rotation_time = now
            log_message(f"Agent mixte actuel: {self.mixed_agents[self.current_agent_index]['name']}")

            # Mettre à jour le last_rotation_check pour toutes les IA et récupérer les scores de diversification
            for ia_name in self.memory_manager.ia_status:
                self.memory_manager.ia_status[ia_name]["last_rotation_check"] = format_datetime(now)
            self.memory_manager.recover_diversification_scores() # Recover diversification scores
            save_json(IA_STATUS_FILE, self.memory_manager.ia_status)

    async def _select_primary_ai_for_agent(self, agent_config: Dict) -> Optional[APIClient]:
        """Sélectionne une IA primaire parmi celles de l'agent, en tenant compte des quotas, de la santé et de la diversification."""
        available_primary_ais = []
        for ai_name in agent_config["primary_ais"]:
            if ai_name in self.core_ai_engines:
                status = self.memory_manager.get_ia_status(ai_name)
                if status and (status.get("cooldown_until") is None or datetime.strptime(status["cooldown_until"], "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=None) < get_current_time()):
                    if self.quota_manager.check_and_update_quota(ai_name, cost=0): # Check quota without consuming
                        available_primary_ais.append((ai_name, status["current_score"], status["diversification_score"]))
        
        if not available_primary_ais:
            log_message(f"Aucune IA primaire disponible pour l'agent {agent_config['name']}.", level="warning")
            return None

        # Sélection basée sur la stratégie globale
        selected_ai_name = None
        if self.current_ia_strategy == "balanced":
            # Choisir l'IA avec le meilleur score combiné (current_score + diversification_score)
            available_primary_ais.sort(key=lambda x: x[1] + x[2], reverse=True)
            selected_ai_name = available_primary_ais[0][0]
        elif self.current_ia_strategy == "cost_effective":
            # Prioriser les IA avec des quotas élevés ou illimités, puis le meilleur score
            cost_effective_ais = []
            for ai_name, current_score, diversification_score in available_primary_ais:
                api_limits = API_QUOTAS.get(ai_name, {})
                if api_limits.get("monthly") is None and api_limits.get("daily") is None and api_limits.get("hourly") is None:
                    cost_effective_ais.append((ai_name, current_score, diversification_score))
            if cost_effective_ais:
                cost_effective_ais.sort(key=lambda x: x[1] + x[2], reverse=True)
                selected_ai_name = cost_effective_ais[0][0]
            else: # Fallback au mode équilibré si pas de "pas cher" dispo
                available_primary_ais.sort(key=lambda x: x[1] + x[2], reverse=True)
                selected_ai_name = available_primary_ais[0][0]
        elif self.current_ia_strategy == "performance":
            # Prioriser l'IA avec le plus grand nombre de succès récents comme proxy de performance
            performance_ais = []
            for ai_name, current_score, diversification_score in available_primary_ais:
                status = self.memory_manager.get_ia_status(ai_name)
                performance_ais.append((ai_name, status["success_count"]))
            performance_ais.sort(key=lambda x: x[1], reverse=True)
            selected_ai_name = performance_ais[0][0]
        
        # Vérifier et consommer le quota pour l'IA sélectionnée
        if selected_ai_name and self.quota_manager.check_and_update_quota(selected_ai_name):
            log_message(f"IA primaire sélectionnée pour l'agent: {selected_ai_name} (Stratégie: {self.current_ia_strategy})")
            return self.core_ai_engines[selected_ai_name]
        return None

    async def _run_agent_with_tools(self, agent_config: Dict, query: str) -> str:
        """
        Exécute l'agent mixte en utilisant l'IA primaire sélectionnée
        et en sollicitant les outils pertinents.
        """
        primary_ai_client = await self._select_primary_ai_for_agent(agent_config)
        if not primary_ai_client:
            return f"Désolé, l'agent {agent_config['name']} ne peut pas opérer car aucune IA primaire n'est disponible."

        responses = []
        tools_called_for_report = []
        
        # Prepare tool descriptions for the AI
        available_tools_for_ai = {}
        for tool_name in agent_config.get("tools", []):
            if tool_name in self.tool_descriptions and self.api_clients.get(tool_name):
                available_tools_for_ai[tool_name] = self.tool_descriptions[tool_name]
        
        tool_prompt_part = ""
        if available_tools_for_ai:
            tool_prompt_part = "\n\nTu as accès aux outils suivants:\n"
            for tool_name, desc in available_tools_for_ai.items():
                tool_prompt_part += f"- **{tool_name}**: {desc}\n"
            tool_prompt_part += "\nSi tu as besoin d'utiliser un outil, réponds avec le format suivant: `TOOL_CALL:<nom_outil>:<paramètres_json>`. Par exemple: `TOOL_CALL:WEATHERAPI:{\"location\": \"Paris\"}`. Sinon, réponds normalement."
        
        full_prompt_for_ai = f"{query}{tool_prompt_part}"

        # 1. Obtenir une première réponse de l'IA primaire
        log_message(f"Agent {agent_config['name']} utilise {primary_ai_client.name} pour la requête: '{query}'")
        primary_response_raw = await primary_ai_client.query(full_prompt_for_ai)
        self.memory_manager.update_ia_status(primary_ai_client.name, not primary_response_raw.startswith("Erreur"))
        
        # Check for tool calls in the primary AI's response
        tool_call_match = re.match(r"TOOL_CALL:([A-Z_]+):(.+)", primary_response_raw)
        if tool_call_match:
            tool_name = tool_call_match.group(1)
            params_str = tool_call_match.group(2)
            
            try:
                tool_params = json.loads(params_str)
                tool_client = self.api_clients.get(tool_name)
                if tool_client and self.quota_manager.check_and_update_quota(tool_name):
                    log_message(f"Agent {agent_config['name']} exécute l'outil {tool_name} avec les paramètres: {tool_params}")
                    
                    tool_response = ""
                    # Dynamic tool call based on tool_name and parsed params
                    # This requires careful mapping of tool_params to actual method arguments
                    if tool_name == "SERPER":
                        tool_response = await tool_client.query(query_text=tool_params.get("query"))
                    elif tool_name == "TAVILY":
                        tool_response = await tool_client.query(query_text=tool_params.get("query"))
                    elif tool_name == "WOLFRAMALPHA":
                        tool_response = await tool_client.query(input_text=tool_params.get("input"))
                    elif tool_name == "WEATHERAPI":
                        tool_response = await tool_client.query(location=tool_params.get("location"))
                    elif tool_name == "OPENWEATHERMAP":
                        tool_response = await tool_client.query(location=tool_params.get("location"))
                    elif tool_name == "STORMGLASS":
                        tool_response = await tool_client.query(lat=tool_params.get("lat"), lng=tool_params.get("lng"), params=tool_params.get("params", "airTemperature,waveHeight"))
                    elif tool_name == "APIFLASH":
                        tool_response = await tool_client.query(url=tool_params.get("url"))
                    elif tool_name == "CRAWLBASE":
                        tool_response = await tool_client.query(url=tool_params.get("url"), use_js=tool_params.get("use_js", False))
                    elif tool_name == "DETECTLANGUAGE":
                        tool_response = await tool_client.query(text=tool_params.get("text"))
                    elif tool_name == "IP2LOCATION":
                        tool_response = await tool_client.query(ip_address=tool_params.get("ip_address"))
                    elif tool_name == "SHODAN":
                        tool_response = await tool_client.query(query_text=tool_params.get("query", ""))
                    elif tool_name == "GREYNOISE":
                        tool_response = await tool_client.query(ip_address=tool_params.get("ip_address"))
                    elif tool_name == "PULSEDIVE":
                        tool_response = await tool_client.query(indicator=tool_params.get("indicator"), type=tool_params.get("type", "auto"))
                    elif tool_name == "CLOUDMERSIVE":
                        tool_response = await tool_client.query(domain=tool_params.get("domain"))
                    elif tool_name == "JSONBIN":
                        if "bin_id" in tool_params:
                            tool_response = await tool_client.query(bin_id=tool_params["bin_id"])
                        else:
                            tool_response = await tool_client.query(data=tool_params.get("data", {}), private=tool_params.get("private", True))
                    elif tool_name == "MOCKAROO":
                        tool_response = await tool_client.query(count=tool_params.get("count", 1), fields_json=tool_params.get("fields_json"))
                    elif tool_name == "RANDOMMER":
                        tool_response = await tool_client.query(country_code=tool_params.get("country_code", "US"), quantity=tool_params.get("quantity", 1))
                    elif tool_name == "OPENPAGERANK":
                        tool_response = await tool_client.query(domains=tool_params.get("domains", []))
                    elif tool_name == "RAPIDAPI":
                        tool_response = await tool_client.query(api_name=tool_params.get("api_name"), **tool_params.get("kwargs", {}))
                    elif tool_name == "TWILIO":
                        tool_response = await tool_client.query()
                    elif tool_name == "ABSTRACTAPI":
                        tool_response = await tool_client.query(input_value=tool_params.get("input_value"), api_type=tool_params.get("api_type"))
                    
                    if tool_response:
                        responses.append(f"Réponse outil ({tool_name}): {tool_response}")
                        tools_called_for_report.append({"name": tool_name, "params": tool_params, "result": tool_response})
                    self.memory_manager.update_ia_status(tool_name, not tool_response.startswith("Erreur"))
                    
                    # Feed tool response back to primary AI for final answer
                    follow_up_prompt = f"J'ai exécuté l'outil {tool_name} avec les paramètres {params_str}. Voici le résultat:\n{tool_response}\n\nMaintenant, réponds à la question originale: {query}"
                    final_ai_response = await primary_ai_client.query(follow_up_prompt)
                    self.memory_manager.update_ia_status(primary_ai_client.name, not final_ai_response.startswith("Erreur"))
                    responses.append(f"Réponse finale ({primary_ai_client.name}): {final_ai_response}")

                else:
                    responses.append(f"Erreur: L'outil {tool_name} n'est pas disponible ou le quota est dépassé.")
                    tools_called_for_report.append({"name": tool_name, "params": tool_params, "result": "Quota dépassé ou non disponible."})
            except json.JSONDecodeError:
                responses.append(f"Erreur: Paramètres JSON invalides pour l'outil {tool_name}: {params_str}")
                tools_called_for_report.append({"name": tool_name, "params": params_str, "result": "JSON invalide."})
            except Exception as e:
                responses.append(f"Erreur lors de l'exécution de l'outil {tool_name}: {e}")
                self.memory_manager.update_ia_status(tool_name, False, str(e))
                tools_called_for_report.append({"name": tool_name, "params": params_str, "result": f"Erreur: {e}"})
        else:
            # If no tool call, the primary AI's initial response is the main response
            responses.append(f"Réponse principale ({primary_ai_client.name}): {primary_response_raw}")
        
        return "\n\n".join(responses), tools_called_for_report


    async def process_query(self, query: str) -> str:
        """Traite une requête en sélectionnant un agent mixte et en obtenant une réponse."""
        self._rotate_strategy_if_needed() # Rotation de la stratégie et de l'agent

        # Sélectionner l'agent mixte actuel
        current_agent_config = self.mixed_agents[self.current_agent_index]
        log_message(f"Traitement de la requête avec l'agent: {current_agent_config['name']}")

        # Exécuter l'agent avec ses outils
        agent_raw_response, tools_called_for_report = await self._run_agent_with_tools(current_agent_config, query)
        
        # Synthèse Optimisée des Réponses
        # Vérifier si la réponse est simple ou si elle contient des marqueurs de multiples réponses/outils
        if "Réponse principale (" in agent_raw_response and ("Réponse outil (" in agent_raw_response or len(agent_raw_response.split('\n\n')) > 1):
            log_message("Plusieurs réponses détectées, appel à la synthèse.")
            final_response = await self.synthesize_response(query, [agent_raw_response])
        else:
            log_message("Réponse unique ou simple, pas de synthèse nécessaire.")
            final_response = agent_raw_response # Si une seule réponse, pas besoin de synthétiser

        return final_response, tools_called_for_report

    async def synthesize_response(self, question: str, responses: List[str]) -> str:
        """
        Synthétise les réponses de plusieurs IA en utilisant DeepSeek (le module d'optimisation).
        """
        if not responses:
            return "Je n'ai reçu aucune réponse des IA pour le moment."

        combined_responses = "\n\n".join([f"Réponse {i+1}:\n{r}" for i, r in enumerate(responses)])
        synthesis_prompt = SYNTHESIS_PROMPT_TEMPLATE.format(question=question, responses=combined_responses)

        deepseek_client = self.core_ai_engines.get("DEEPSEEK")
        if not deepseek_client:
            log_message("DeepSeek n'est pas disponible pour la synthèse.", level="warning")
            return "J'ai plusieurs réponses, mais je ne peux pas les synthétiser pour le moment. Voici les réponses brutes:\n\n" + combined_responses

        try:
            synthesis = await deepseek_client.query(synthesis_prompt)
            self.memory_manager.update_ia_status("DEEPSEEK", True) # Update DeepSeek status for synthesis
            return detect_and_correct_toxicity(synthesis)
        except Exception as e:
            log_message(f"Erreur lors de la synthèse avec DeepSeek: {e}", level="error")
            self.memory_manager.update_ia_status("DEEPSEEK", False, str(e))
            return "J'ai rencontré un problème lors de la synthèse des informations. Voici les réponses brutes:\n\n" + combined_responses

# Instancier l'orchestrateur
orchestrator = IAOrchestrator(memory_manager, quota_manager, ALL_API_CLIENTS)

# --- Tâche de fond pour les Health Checks des Endpoints ---
async def periodic_health_check():
    """Exécute des health checks périodiques pour tous les services."""
    while True:
        log_message("Lancement des health checks périodiques pour tous les services...")
        for service_name in API_CONFIG.keys():
            await endpoint_health_manager.run_health_check_for_service(service_name)
        log_message("Health checks périodiques terminés. Prochain check dans 300 secondes.")
        await asyncio.sleep(300) # Vérifie toutes les 5 minutes

# --- Structured Reporting to Private Group ---
async def send_structured_report_to_private_group(context: ContextTypes.DEFAULT_TYPE, report_data: Dict) -> None:
    """Envoie un rapport structuré au groupe privé Telegram."""
    try:
        report_text = f"📊 **Rapport d'Action IA**\n\n"
        report_text += f"**Timestamp**: `{report_data.get('timestamp')}`\n"
        report_text += f"**Agent**: `{report_data.get('agent_name')}`\n"
        report_text += f"**Intention Détectée**: `{report_data.get('intention')}`\n"
        report_text += f"**Requête Utilisateur**: `{report_data.get('user_query')}`\n"
        report_text += f"**IA Primaire Utilisée**: `{report_data.get('primary_ai_used')}`\n"
        
        tools_called = report_data.get('tools_called', [])
        if tools_called:
            report_text += "**Outils Appelés**:\n"
            for tool in tools_called:
                # Truncate tool result for report to avoid very long messages
                tool_result_display = str(tool['result'])
                if len(tool_result_display) > 100:
                    tool_result_display = tool_result_display[:100] + "..."
                report_text += f"- `{tool['name']}` (Params: `{tool['params']}`, Résultat: `{tool_result_display}`)\n"
        else:
            report_text += "**Outils Appelés**: Aucun\n"
        
        # Truncate final response for report
        final_response_display = report_data.get('final_response', '')
        if len(final_response_display) > 500:
            final_response_display = final_response_display[:500] + "..."
        report_text += f"**Réponse Finale**: `{final_response_display}`\n"
        report_text += f"**Durée Totale**: `{report_data.get('duration'):.2f}s`\n"
        report_text += f"**Erreur**: `{report_data.get('error', 'Non')}`\n"

        await context.bot.send_message(chat_id=PRIVATE_GROUP_ID, text=report_text, parse_mode='Markdown')
        log_message(f"Rapport structuré envoyé au groupe privé: {PRIVATE_GROUP_ID}")
    except Exception as e:
        log_message(f"Erreur lors de l'envoi du rapport structuré au groupe privé: {e}", level="error")

# --- Handlers de commandes Telegram ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envoie un message lorsque la commande /start est émise."""
    user = update.effective_user
    await update.message.reply_html(
        f"Salut {user.mention_html()} ! Je suis ton assistant IA de 2025. "
        "Pose-moi une question, demande-moi d'écrire du code, ou de chercher des infos. "
        "Utilise /help pour voir ce que je peux faire.",
        reply_markup=ForceReply(selective=True),
    )
    log_message(f"Commande /start reçue de {user.id}")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Envoie un message lorsque la commande /help est émise."""
    help_text = """
    Voici ce que je peux faire :
    - Pose-moi n'importe quelle question factuelle.
    - Demande-moi d'écrire ou d'améliorer du code (Python, Shell).
    - Cherche des informations sur le web (actualités, météo, géolocalisation IP, etc.).
    - Demande-moi de faire une capture d'écran d'un site web (donne l'URL).
    - Demande-moi d'analyser le contenu d'une page web (donne l'URL).
    - Demande-moi de détecter la langue d'un texte.
    - Demande-moi de valider un numéro de téléphone ou de géolocaliser une IP ou un email.
    - Gère tes rappels et alarmes (Ex: "Rappelle-moi d'acheter du lait à 18h", "Mets une alarme à 7h du matin").
    - Vérifie le statut de mes APIs avec /status.
    - Affiche mon historique de conversation avec /history.
    - Affiche le statut des quotas API avec /quotas.
    - Affiche les APIs où il est opportun de "brûler" le quota avec /burn_quota.

    Exemples :
    - "Quelle est la capitale de la France ?"
    - "Écris un script Python pour trier une liste."
    - "Météo à Paris"
    - "Capture d'écran de https://google.com"
    - "Analyse de https://openai.com"
    - "Détecte la langue de 'Hello world'"
    - "Valide le numéro +33612345678"
    - "Géolocalise l'IP 8.8.8.8"
    - "Valide l'email test@example.com"
    - "Rappelle-moi de faire les courses demain à 10h"
    - "Mets une alarme pour 7h du matin"
    """
    await update.message.reply_text(help_text)
    log_message(f"Commande /help reçue de {update.effective_user.id}")

async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Affiche le statut et les scores des IA."""
    status_message = "📊 **Statut des IA**:\n"
    now = get_current_time()
    for ia_name, status in memory_manager.ia_status.items():
        cooldown_until_str = status.get("cooldown_until")
        cooldown_status = "Prête"
        if cooldown_until_str:
            cooldown_until = datetime.strptime(cooldown_until_str, "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=None)
            if now < cooldown_until:
                remaining = cooldown_until - now
                cooldown_status = f"Cooldown ({remaining.total_seconds():.0f}s restantes)"
        
        last_used_str = status.get("last_used", "Jamais")
        if last_used_str != "Jamais":
            last_used_dt = datetime.strptime(last_used_str, "%Y-%m-%d %H:%M:%S UTC").replace(tzinfo=None)
            time_since_last_used = (now - last_used_dt).total_seconds()
            if time_since_last_used < 60:
                last_used_display = f"{time_since_last_used:.0f}s ago"
            elif time_since_last_used < 3600:
                last_used_display = f"{time_since_last_used / 60:.0f}m ago"
            else:
                last_used_display = f"{time_since_last_used / 3600:.1f}h ago"
        else:
            last_used_display = "Jamais"

        status_message += (
            f"- **{ia_name}**: Score: `{status['current_score']:.2f}`, Diversification: `{status['diversification_score']:.2f}`, "
            f"Succès: `{status['success_count']}`, Erreurs: `{status['error_count']}`, "
            f"Statut: `{cooldown_status}`, Dernière utilisation: `{last_used_display}`\n"
        )
    status_message += f"\nStratégie actuelle: `{orchestrator.current_ia_strategy}`"
    status_message += f"\nAgent mixte actuel: `{orchestrator.mixed_agents[orchestrator.current_agent_index]['name']}`"
    await update.message.reply_markdown(status_message)
    log_message(f"Commande /status reçue de {update.effective_user.id}")

async def history_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Affiche les 10 derniers messages de l'historique."""
    history = memory_manager.get_chat_history()
    if not history:
        await update.message.reply_text("L'historique de conversation est vide.")
        return

    history_text = "📜 **Historique des 10 dernières interactions**:\n\n"
    for entry in history:
        history_text += f"**{entry['role'].capitalize()}** ({entry['timestamp']}):\n{entry['content'][:150]}...\n\n"
    await update.message.reply_markdown(history_text)
    log_message(f"Commande /history reçue de {update.effective_user.id}")

async def quotas_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Affiche le statut actuel des quotas API."""
    quotas_status = quota_manager.get_all_quotas_status()
    message = "📈 **Statut des Quotas API**:\n\n"
    for api_name, data in quotas_status.items():
        message += (
            f"**{api_name}**:\n"
            f"  - Mensuel: `{data['monthly_usage']}` / `{data['monthly_limit']}`\n"
            f"  - Journalier: `{data['daily_usage']}` / `{data['daily_limit']}`\n"
            f"  - Horaire: `{data['hourly_usage']}` / `{data['hourly_limit']}`\n"
            f"  - Total appels: `{data['total_calls']}`\n"
            f"  - Dernière utilisation: `{data['last_usage'] if data['last_usage'] else 'N/A'}`\n"
            f"  - Reset Mensuel: `{data['last_reset_month']}`\n"
            f"  - Reset Journalier: `{data['last_reset_day']}`\n"
            f"  - Reset Horaire: `{data['last_hourly_reset']}`\n\n"
        )
    await update.message.reply_markdown(message)
    log_message(f"Commande /quotas reçue de {update.effective_user.id}")

async def burn_quota_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Affiche les APIs où il est opportun de "brûler" le quota."""
    burn_apis = quota_manager.get_burn_window_apis()
    if burn_apis:
        message = "🔥 **APIs où il est opportun de 'brûler' le quota avant réinitialisation**:\n\n"
        for api_info in burn_apis:
            message += f"- {api_info}\n"
        message += f"\nFenêtre de brûlage: {QUOTA_BURN_WINDOW_HOURS} heures avant le reset."
    else:
        message = "🎉 Aucune API n'est actuellement dans une fenêtre de 'brûlage' de quota. Tout est optimisé !"
    await update.message.reply_markdown(message)
    log_message(f"Commande /burn_quota reçue de {update.effective_user.id}")

async def detect_intent(query: str) -> str:
    """Détecte l'intention de l'utilisateur en utilisant Gemini API."""
    prompt = f"Classe la requête suivante dans une des catégories suivantes: 'programmation', 'image', 'météo', 'langue', 'recherche', 'sécurité', 'données', 'communication', 'actualités', 'général'. Réponds uniquement avec le nom de la catégorie. Requête: '{query}'"
    gemini_client = orchestrator.core_ai_engines.get("GEMINI_API")
    if gemini_client:
        try:
            response = await gemini_client.query(prompt)
            # Clean up response to get just the category name
            category = response.strip().lower().replace('.', '').replace('catégorie: ', '')
            if category in ['programmation', 'image', 'météo', 'langue', 'recherche', 'sécurité', 'données', 'communication', 'actualités', 'général']:
                return category
            return "général" # Fallback
        except Exception as e:
            log_message(f"Erreur lors de la détection d'intention avec Gemini: {e}", level="error")
            return "général" # Fallback if AI fails
    return "général" # Fallback if Gemini client not available

# --- Gestionnaire de messages (le cœur du bot) ---

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Traite les messages texte de l'utilisateur."""
    user_message = update.message.text
    user_id = update.effective_user.id
    log_message(f"Message reçu de {user_id}: {user_message}")

    memory_manager.add_message_to_history("user", user_message)

    response_text = ""
    start_processing_time = time.monotonic()
    
    # Intention Detection
    detected_intention = await detect_intent(user_message)
    log_message(f"Intention détectée pour '{user_message}': {detected_intention}")

    tools_called_report = []
    error_occurred = False

    try:
        # Détection d'intentions spécifiques (prioritaires sur l'orchestrateur général)
        if any(keyword in user_message.lower() for keyword in ["alarme", "réveil", "timer", "minuteur", "rappelle-moi", "rappel", "reminder"]):
            log_message("Intention détectée: Alarme/Rappel (Simulé).")
            response_text = "Je peux t'aider avec les alarmes, minuteurs et rappels ! Dis-moi par exemple : 'Mets une alarme à 7h du matin' ou 'Rappelle-moi d'acheter du lait à 18h'."
        elif "```python" in user_message or "```shell" in user_message or "exécute ce code" in user_message.lower() or "teste ce script" in user_message.lower():
            log_message("Intention détectée: Exécution de code.")
            lang_match = re.search(r"```(python|shell)\n(.*?)```", user_message, re.DOTALL)
            if lang_match:
                language = lang_match.group(1)
                code = lang_match.group(2)
                response_text = await run_in_sandbox(code, language)
            else:
                response_text = "Veuillez formater votre code avec des triple backticks et spécifier le langage (ex: ```python\\nprint('Hello')``` ou ```shell\\nls -l```)."
        elif "analyse ce code python" in user_message.lower() or "vérifie ce script python" in user_message.lower():
            log_message("Intention détectée: Analyse de code Python.")
            code_match = re.search(r"```python\n(.*?)```", user_message, re.DOTALL)
            if code_match:
                code = code_match.group(1)
                response_text = await analyze_python_code(code)
            else:
                response_text = "Veuillez fournir le code Python à analyser formaté avec ```python\\n...```."
        elif "extraire texte image" in user_message.lower() or "ocr" in user_message.lower() or "lis cette image" in user_message.lower():
            log_message("Intention détectée: OCR.")
            url_match = re.search(r'https?://[^\s]+(?:\.jpg|\.jpeg|\.png|\.gif|\.bmp|\.tiff)', user_message, re.IGNORECASE)
            if url_match:
                image_url = url_match.group(0)
                # For OCR, we'll try to use Cloudmersive if a key is available for OCR
                # The provided Cloudmersive config is for Domain Check, not OCR.
                # If an OCR endpoint was configured, it would be called here.
                # For now, we'll return a message indicating no direct OCR API.
                response_text = "Désolé, je n'ai pas d'API OCR directement configurée pour le moment. Mon client Cloudmersive est pour la validation de domaine."
            else:
                response_text = "Veuillez fournir une URL d'image valide (jpg, png, etc.) pour l'extraction de texte."
        else:
            log_message("Intention générale, utilisation de l'orchestrateur d'IA.")
            response_text, tools_called_report = await orchestrator.process_query(user_message)

    except Exception as e:
        log_message(f"Erreur majeure lors du traitement du message: {e}", level="error")
        response_text = f"Désolé, une erreur inattendue est survenue: {e}"
        error_occurred = True

    final_response = clean_html_tags(response_text)
    final_response = neutralize_urls(final_response)
    final_response = detect_and_correct_toxicity(final_response)

    await update.message.reply_text(final_response)
    memory_manager.add_message_to_history("assistant", final_response)
    log_message(f"Réponse envoyée à {user_id}.")

    # Send structured report to private group
    end_processing_time = time.monotonic()
    processing_duration = end_processing_time - start_processing_time

    report_data = {
        "timestamp": format_datetime(get_current_time()),
        "agent_name": orchestrator.mixed_agents[orchestrator.current_agent_index]['name'],
        "intention": detected_intention,
        "user_query": user_message,
        "primary_ai_used": orchestrator.core_ai_engines.get(orchestrator.mixed_agents[orchestrator.current_agent_index]['primary_ais'][0]).name if orchestrator.mixed_agents[orchestrator.current_agent_index]['primary_ais'] else "N/A", # Simplified
        "tools_called": tools_called_report, # This needs to be populated by _run_agent_with_tools
        "final_response": final_response,
        "duration": processing_duration,
        "error": "Oui" if error_occurred else "Non"
    }
    await send_structured_report_to_private_group(context, report_data)


# --- Fonction principale pour démarrer le bot ---

async def main() -> None:
    """Démarre le bot."""
    log_message("Démarrage du bot Telegram...")
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("status", status_command))
    application.add_handler(CommandHandler("history", history_command))
    application.add_handler(CommandHandler("quotas", quotas_command))
    application.add_handler(CommandHandler("burn_quota", burn_quota_command))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Démarrer la tâche de fond pour les health checks
    asyncio.create_task(periodic_health_check())

    log_message("Bot prêt à recevoir des messages.")
    await application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    try:
        # Utilise asyncio.run() pour démarrer la fonction asynchrone principale.
        # C'est la méthode recommandée pour les scripts simples et gère la boucle d'événements.
        asyncio.run(main())
    except KeyboardInterrupt:
        # Gère l'interruption par l'utilisateur (Ctrl+C) pour un arrêt propre.
        logging.info("Bot arrêté par l'utilisateur (Ctrl+C).")
    except Exception as e:
        # Capture et log toute autre erreur fatale au démarrage du bot.
        logging.error(f"Erreur fatale lors du démarrage du bot: {e}", exc_info=True)
        print(f"Une erreur est survenue au démarrage du bot: {e}")

# --- FIN DU FICHIER PRINCIPAL ---


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
WEATHERAPI_KEY = "YOUR_WEATHERAPI_KEY_HERE"
CLOUDMERSIVE_API_KEY = "YOUR_CLOUDMERSIVE_API_KEY_HERE"
GREYNOISE_API_KEY = "YOUR_GREYNOISE_API_KEY_HERE"
PULSEDIVE_API_KEY = "YOUR_PULSEDIVE_API_KEY_HERE"
STORMGLASS_API_KEY = "YOUR_STORMGLASS_API_KEY_HERE"
LOGINRADIUS_API_KEY = "YOUR_LOGINRADIUS_API_KEY_HERE"
JSONBIN_API_KEY = "YOUR_JSONBIN_API_KEY_HERE"
HUGGINGFACE_API_KEYS = [
    "hf_YOUR_HUGGINGFACE_API_KEY_1",
    "hf_YOUR_HUGGINGFACE_API_KEY_2"
]
TWILIO_ACCOUNT_SID = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
ABSTRACTAPI_API_KEYS = [
    "YOUR_ABSTRACTAPI_API_KEY_1",
    "YOUR_ABSTRACTAPI_API_KEY_2"
]
GOOGLE_CUSTOM_SEARCH_API_KEYS = [
    "YOUR_GOOGLE_CUSTOM_SEARCH_API_KEY_1",
    "YOUR_GOOGLE_CUSTOM_SEARCH_API_KEY_2"
]
GOOGLE_CUSTOM_SEARCH_CX_LIST = [
    "YOUR_GOOGLE_CUSTOM_SEARCH_CX_1",
    "YOUR_GOOGLE_CUSTOM_SEARCH_CX_2"
]
RANDOMMER_API_KEY = "YOUR_RANDOMMER_API_KEY_HERE"
TOMORROWIO_API_KEY = "YOUR_TOMORROWIO_API_KEY_HERE"
OPENWEATHERMAP_API_KEY = "YOUR_OPENWEATHERMAP_API_KEY_HERE"
MOCKAROO_API_KEY = "YOUR_MOCKAROO_API_KEY_HERE"
OPENPAGERANK_API_KEY = "YOUR_OPENPAGERANK_API_KEY_HERE"
RAPIDAPI_KEY = "YOUR_RAPIDAPI_KEY_HERE"


# Configuration détaillée des endpoints API
API_CONFIG = {
    "GEMINI_API": [
        {
            "endpoint_name": f"Gemini Chat (Key {i+1})",
            "url": "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent",
            "method": "POST",
            "key": key,
            "key_field": "key",
            "key_location": "param",
            "timeout": 60,
            "health_check_params": {"prompt": "test"},
            "health_check_url_suffix": f"?key={key}"
        }
        for i, key in enumerate(GEMINI_API_KEYS)
    ],
    "OCR_API": [
        {
            "endpoint_name": f"OCR.space (Key {i+1})",
            "url": "https://api.ocr.space/parse/image",
            "method": "POST",
            "key": key,
            "key_field": "apikey",
            "key_location": "header",
            "timeout": 30,
            "fixed_headers": {"Content-Type": "application/json"},
            "health_check_json": {"base64Image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=", "language": "eng"}, # Minimal valid base64 for health check
        }
        for i, key in enumerate(OCR_API_KEYS)
    ],
    "DEEPSEEK": [
        {
            "endpoint_name": f"DeepSeek Chat (Key {i+1})",
            "url": "https://api.deepseek.com/chat/completions",
            "method": "POST",
            "key": key,
            "key_field": "Authorization",
            "key_location": "header",
            "key_prefix": "Bearer ",
            "timeout": 60,
            "fixed_headers": {"Content-Type": "application/json"},
            "health_check_json": {"model": "deepseek-chat", "messages": [{"role": "user", "content": "hi"}]}
        }
        for i, key in enumerate(DEEPSEEK_API_KEYS)
    ],
    "SERPER": [
        {
            "endpoint_name": "Serper Search",
            "url": "https://google.serper.dev/search",
            "method": "POST",
            "key": SERPER_API_KEY,
            "key_field": "X-API-KEY",
            "key_location": "header",
            "timeout": 30,
            "fixed_headers": {"Content-Type": "application/json"},
            "health_check_json": {"q": "test"}
        }
    ],
    "WOLFRAMALPHA": [
        {
            "endpoint_name": f"WolframAlpha Query (App ID {i+1})",
            "url": "http://api.wolframalpha.com/v2/query",
            "method": "GET",
            "key": app_id,
            "key_field": "appid",
            "key_location": "param",
            "timeout": 30,
            "fixed_params": {"output": "json"},
            "health_check_params": {"input": "2+2", "output": "json"}
        }
        for i, app_id in enumerate(WOLFRAMALPHA_APP_IDS)
    ],
    "TAVILY": [
        {
            "endpoint_name": f"Tavily Search (Key {i+1})",
            "url": "https://api.tavily.com/parse",
            "method": "POST",
            "key": key,
            "key_field": "apikey",
            "key_location": "header",
            "timeout": 30,
            "fixed_headers": {"Content-Type": "application/json"},
            "health_check_json": {"query": "test", "max_results": 1}
        }
        for i, key in enumerate(TAVILY_API_KEYS)
    ],
    "APIFLASH": [
        {
            "endpoint_name": "ApiFlash Screenshot",
            "url": "https://api.apiflash.com/v1/urltoimage",
            "method": "GET",
            "key": APIFLASH_ACCESS_KEY,
            "key_field": "access_key",
            "key_location": "param",
            "timeout": 45,
            "health_check_params": {"url": "example.com", "format": "jpeg"}
        }
    ],
    "CRAWLBASE": [
        {
            "endpoint_name": "Crawlbase Scraper",
            "url": "https://api.crawlbase.com/",
            "method": "GET",
            "key": CRAWLBASE_API_KEY,
            "key_field": "token",
            "key_location": "param",
            "timeout": 60,
            "health_check_params": {"url": "http://example.com", "format": "json"}
        },
        {
            "endpoint_name": "Crawlbase JS Scraper",
            "url": "https://api.crawlbase.com/js",
            "method": "GET",
            "key": CRAWLBASE_API_KEY,
            "key_field": "token",
            "key_location": "param",
            "timeout": 90,
            "health_check_params": {"url": "http://example.com", "format": "json"}
        }
    ],
    "DETECTLANGUAGE": [
        {
            "endpoint_name": "DetectLanguage Detect",
            "url": "https://ws.detectlanguage.com/0.2/detect",
            "method": "POST",
            "key": DETECTLANGUAGE_API_KEY,
            "key_field": "X-Detectlanguage-Api-Key",
            "key_location": "header",
            "timeout": 15,
            "fixed_headers": {"Content-Type": "application/json"},
            "health_check_json": {"q": "Hello world"}
        }
    ],
    "GUARDIAN": [
        {
            "endpoint_name": "Guardian Content",
            "url": "https://content.guardianapis.com/search",
            "method": "GET",
            "key": GUARDIAN_API_KEY,
            "key_field": "api-key",
            "key_location": "param",
            "timeout": 20,
            "health_check_params": {"q": "test"}
        }
    ],
    "IP2LOCATION": [
        {
            "endpoint_name": "IP2Location Geolocation",
            "url": "https://api.ip2location.com/v2/",
            "method": "GET",
            "key": IP2LOCATION_API_KEY,
            "key_field": "key",
            "key_location": "param",
            "timeout": 10,
            "health_check_params": {"ip": "8.8.8.8", "addon": "country,city"}
        }
    ],
    "SHODAN": [
        {
            "endpoint_name": "Shodan API Info",
            "url": "https://api.shodan.io/api-info",
            "method": "GET",
            "key": SHODAN_API_KEY,
            "key_field": "key",
            "key_location": "param",
            "timeout": 15,
            "health_check_url_suffix": f"?key={SHODAN_API_KEY}"
        },
        {
            "endpoint_name": "Shodan Host Info",
            "url": "https://api.shodan.io/shodan/host",
            "method": "GET",
            "key": SHODAN_API_KEY,
            "key_field": "key",
            "key_location": "param",
            "timeout": 20,
            "health_check_url_suffix": f"/8.8.8.8?key={SHODAN_API_KEY}"
        }
    ],
    "WEATHERAPI": [
        {
            "endpoint_name": "WeatherAPI Current",
            "url": "http://api.weatherapi.com/v1/current.json",
            "method": "GET",
            "key": WEATHERAPI_KEY,
            "key_field": "key",
            "key_location": "param",
            "timeout": 15,
            "health_check_params": {"q": "London"}
        }
    ],
    "CLOUDMERSIVE": [
        {
            "endpoint_name": "Cloudmersive Validate Domain",
            "url": "https://api.cloudmersive.com/validate/domain/full",
            "method": "POST",
            "key": CLOUDMERSIVE_API_KEY,
            "key_field": "Apikey",
            "key_location": "header",
            "timeout": 20,
            "fixed_headers": {"Content-Type": "application/json"},
            "health_check_json": {"domain": "example.com"}
        }
    ],
    "GREYNOISE": [
        {
            "endpoint_name": "GreyNoise IP Lookup",
            "url": "https://api.greynoise.io/v3/community",
            "method": "GET",
            "key": GREYNOISE_API_KEY,
            "key_field": "key",
            "key_location": "header",
            "timeout": 20,
            "health_check_url_suffix": "/8.8.8.8"
        }
    ],
    "PULSEDIVE": [
        {
            "endpoint_name": "Pulsedive Indicator",
            "url": "https://pulsedive.com/api/v1/indicator.php",
            "method": "GET",
            "key": PULSEDIVE_API_KEY,
            "key_field": "key",
            "key_location": "param",
            "timeout": 25,
            "fixed_params": {"pretty": "1"},
            "health_check_params": {"indicator": "8.8.8.8", "pretty": "1"}
        }
    ],
    "STORMGLASS": [
        {
            "endpoint_name": "StormGlass Weather",
            "url": "https://api.stormglass.io/v2/weather/point",
            "method": "GET",
            "key": STORMGLASS_API_KEY,
            "key_field": "Authorization",
            "key_location": "header",
            "timeout": 30,
            "health_check_params": {"lat": 0, "lng": 0, "params": "airTemperature", "start": 0, "end": 0},
            "health_check_url_suffix": "?lat=0&lng=0&params=airTemperature&start=0&end=0"
        }
    ],
    "LOGINRADIUS": [
        {
            "endpoint_name": "LoginRadius Ping",
            "url": "https://api.loginradius.com/identity/v2/auth/ping",
            "method": "GET",
            "key": LOGINRADIUS_API_KEY,
            "key_field": "apiKey",
            "key_location": "param",
            "timeout": 10,
            "health_check_url_suffix": f"?apiKey={LOGINRADIUS_API_KEY}"
        }
    ],
    "JSONBIN": [
        {
            "endpoint_name": "Bin Create",
            "url": "https://api.jsonbin.io/v3/b",
            "method": "POST",
            "key": JSONBIN_API_KEY,
            "key_field": "X-Master-Key",
            "key_location": "header",
            "timeout": 20,
            "fixed_headers": {"Content-Type": "application/json", "X-Bin-Private": "true"},
            "health_check_json": {"test": "data"}
        },
        {
            "endpoint_name": "Bin Access",
            "url": "https://api.jsonbin.io/v3/b",
            "method": "GET",
            "key": JSONBIN_API_KEY,
            "key_field": "X-Master-Key",
            "key_location": "header",
            "timeout": 20,
            "health_check_url_suffix": "/60c7b9b0f1a9a87d2b7b7b7b"
        }
    ],
    "HUGGINGFACE": [
        {
            "endpoint_name": f"HuggingFace Inference (Key {i+1})",
            "url": "https://api-inference.huggingface.co/models/",
            "method": "POST",
            "key": key,
            "key_field": "Authorization",
            "key_location": "header",
            "key_prefix": "Bearer ",
            "timeout": 60,
            "fixed_headers": {"Content-Type": "application/json"},
            "health_check_url_suffix": "distilbert-base-uncased-finetuned-sst-2-english",
            "health_check_json": {"inputs": "Hello world"}
        }
        for i, key in enumerate(HUGGINGFACE_API_KEYS)
    ],
    "TWILIO": [
        {
            "endpoint_name": "Account Balance",
            "url": f"https://api.twilio.com/2010-04-01/Accounts/{TWILIO_ACCOUNT_SID}/Balance.json",
            "method": "GET",
            "key": (TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN),
            "key_location": "auth_basic",
            "timeout": 20,
            "health_check_url_suffix": ""
        }
    ],
    "ABSTRACTAPI": [
        {
            "endpoint_name": f"Email Validation (Key {i+1})",
            "url": "https://emailvalidation.abstractapi.com/v1/?",
            "method": "GET",
            "key": key,
            "key_field": "api_key",
            "key_location": "param",
            "timeout": 15,
            "health_check_params": {"email": "test@example.com"}
        }
        for i, key in enumerate(ABSTRACTAPI_API_KEYS)
    ] + [
        {
            "endpoint_name": f"Phone Validation (Key {i+1})",
            "url": "https://phonevalidation.abstractapi.com/v1/?",
            "method": "GET",
            "key": key,
            "key_field": "api_key",
            "key_location": "param",
            "timeout": 15,
            "health_check_params": {"phone": "14151234567"}
        }
        for i, key in enumerate(ABSTRACTAPI_API_KEYS)
    ] + [
        {
            "endpoint_name": f"Exchange Rates (Key {i+1})",
            "url": "https://exchangerates.abstractapi.com/v1/live",
            "method": "GET",
            "key": key,
            "key_field": "api_key",
            "key_location": "param",
            "timeout": 15,
            "health_check_params": {"base": "USD"}
        }
        for i, key in enumerate(ABSTRACTAPI_API_KEYS)
    ] + [
        {
            "endpoint_name": f"Holidays (Key {i+1})",
            "url": "https://holidays.abstractapi.com/v1/",
            "method": "GET",
            "key": key,
            "key_field": "api_key",
            "key_location": "param",
            "timeout": 15,
            "health_check_params": {"country": "US", "year": "2023", "month": "1", "day": "1"}
        }
        for i, key in enumerate(ABSTRACTAPI_API_KEYS)
    ],
    "GOOGLE_CUSTOM_SEARCH": [
        {
            "endpoint_name": f"Google Custom Search (API Key {i+1}, CX {j+1})",
            "url": "https://www.googleapis.com/customsearch/v1",
            "method": "GET",
            "key": GOOGLE_CUSTOM_SEARCH_API_KEYS[i],
            "key_field": "key",
            "key_location": "param",
            "timeout": 30,
            "fixed_params": {"cx": GOOGLE_CUSTOM_SEARCH_CX_LIST[j]},
            "health_check_params": {"q": "test", "cx": GOOGLE_CUSTOM_SEARCH_CX_LIST[j]}
        }
        for i in range(len(GOOGLE_CUSTOM_SEARCH_API_KEYS))
        for j in range(len(GOOGLE_CUSTOM_SEARCH_CX_LIST))
    ],
    "RANDOMMER": [
        {
            "endpoint_name": "Randommer Phone Numbers",
            "url": "https://randommer.io/api/Phone/Generate",
            "method": "GET",
            "key": RANDOMMER_API_KEY,
            "key_field": "X-Api-Key",
            "key_location": "header",
            "timeout": 15,
            "fixed_headers": {"Content-Type": "application/json"},
            "health_check_params": {"CountryCode": "US", "Quantity": 1}
        }
    ],
    "TOMORROW.IO": [
        {
            "endpoint_name": "Tomorrow.io Weather",
            "url": "https://api.tomorrow.io/v4/weather/realtime",
            "method": "GET",
            "key": TOMORROWIO_API_KEY,
            "key_field": "apikey",
            "key_location": "param",
            "timeout": 20,
            "health_check_params": {"location": "42.3478,-71.0466", "fields": "temperature"}
        }
    ],
    "OPENWEATHERMAP": [
        {
            "endpoint_name": "OpenWeatherMap Current",
            "url": "https://api.openweathermap.org/data/2.5/weather",
            "method": "GET",
            "key": OPENWEATHERMAP_API_KEY,
            "key_field": "appid",
            "key_location": "param",
            "timeout": 15,
            "health_check_params": {"q": "London"}
        }
    ],
    "MOCKAROO": [
        {
            "endpoint_name": "Mockaroo Generate Data",
            "url": "https://api.mockaroo.com/api/generate.json",
            "method": "GET",
            "key": MOCKAROO_API_KEY,
            "key_field": "key",
            "key_location": "param",
            "timeout": 30,
            "health_check_params": {"count": 1, "fields": '[{"name":"id","type":"Row Number"}]'}
        }
    ],
    "OPENPAGERANK": [
        {
            "endpoint_name": "OpenPageRank Domains",
            "url": "https://openpagerank.com/api/v1.0/getPageRank",
            "method": "GET",
            "key": OPENPAGERANK_API_KEY,
            "key_field": "api_key",
            "key_location": "param",
            "timeout": 20,
            "health_check_params": {"domains[]": ["google.com"]}
        }
    ],
    "RAPIDAPI": [
        {
            "endpoint_name": "RapidAPI Programming Joke",
            "url": "https://programming-jokes-api.p.rapidapi.com/jokes/random",
            "method": "GET",
            "key": RAPIDAPI_KEY,
            "key_field": "X-RapidAPI-Key",
            "key_location": "header",
            "timeout": 20,
            "fixed_headers": {"X-RapidAPI-Host": "programming-jokes-api.p.rapidapi.com"},
            "health_check_url_suffix": ""
        },
        {
            "endpoint_name": "RapidAPI Currency List Quotes",
            "url": "https://currency-exchange.p.rapidapi.com/listquotes",
            "method": "GET",
            "key": RAPIDAPI_KEY,
            "key_field": "X-RapidAPI-Key",
            "key_location": "header",
            "timeout": 20,
            "fixed_headers": {"X-RapidAPI-Host": "currency-exchange.p.rapidapi.com"},
            "health_check_url_suffix": ""
        },
        {
            "endpoint_name": "RapidAPI Random Fact",
            "url": "https://random-facts-api.p.rapidapi.com/api/random",
            "method": "GET",
            "key": RAPIDAPI_KEY,
            "key_field": "X-RapidAPI-Key",
            "key_location": "header",
            "timeout": 20,
            "fixed_headers": {"X-RapidAPI-Host": "random-facts-api.p.rapidapi.com"},
            "health_check_url_suffix": ""
        }
    ]
}

# ==============================================================================
# Configuration des Modèles Gemini
# ==============================================================================

# Paramètres de génération pour l'API Gemini
GEMINI_TEMPERATURE = 0.7
GEMINI_TOP_P = 0.95
GEMINI_TOP_K = 40
GEMINI_MAX_OUTPUT_TOKENS = 8192

# Paramètres de sécurité pour l'API Gemini
GEMINI_SAFETY_SETTINGS = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]

# ==============================================================================
# Configuration des Outils (Tool Calling)
# ==============================================================================

# Définition des outils que le bot peut utiliser via le "Function Calling"
TOOL_CONFIG = {
    "serper_query": {
        "description": "Effectue une recherche web via l'API Serper et retourne les snippets pertinents.",
        "parameters": {
            "type": "object",
            "properties": {
                "query_text": {"type": "string", "description": "La requête de recherche."}
            },
            "required": ["query_text"]
        }
    },
    "wolframalpha_query": {
        "description": "Interroge WolframAlpha pour des calculs, des faits ou des données complexes.",
        "parameters": {
            "type": "object",
            "properties": {
                "input_text": {"type": "string", "description": "La requête à soumettre à WolframAlpha."}
            },
            "required": ["input_text"]
        }
    },
    "tavily_query": {
        "description": "Effectue une recherche web avancée via l'API Tavily, fournissant des extraits et une réponse directe.",
        "parameters": {
            "type": "object",
            "properties": {
                "query_text": {"type": "string", "description": "La requête de recherche."},
                "max_results": {"type": "integer", "description": "Nombre maximum de résultats à retourner.", "default": 3}
            },
            "required": ["query_text"]
        }
    },
    "run_in_sandbox": {
        "description": "Exécute du code Python ou Shell dans un environnement sandbox simulé et retourne la sortie.",
        "parameters": {
            "type": "object",
            "properties": {
                "code": {"type": "string", "description": "Le code à exécuter."},
                "language": {"type": "string", "description": "Le langage du code ('python' ou 'shell').", "enum": ["python", "shell"], "default": "python"}
            },
            "required": ["code"]
        }
    },
    "perform_ocr_api": {
        "description": "Effectue une reconnaissance optique de caractères (OCR) sur une image donnée par URL et retourne le texte extrait.",
        "parameters": {
            "type": "object",
            "properties": {
                "image_url": {"type": "string", "description": "L'URL de l'image à traiter par OCR."}
            },
            "required": ["image_url"]
        }
    },
    "fetch_and_archive_pages": {
        "description": "Récupère le contenu de pages web spécifiées, les archive localement et envoie les liens d'archive au groupe privé.",
        "parameters": {
            "type": "object",
            "properties": {
                "links": {"type": "array", "items": {"type": "string"}, "description": "Liste des URLs des pages à archiver."},
                "user_id": {"type": "string", "description": "L'ID de l'utilisateur demandant l'archivage."}
            },
            "required": ["links", "user_id"]
        }
    },
    "ocr_extract_text": {
        "description": "Extrait le texte d'une image encodée en base64 en utilisant l'OCR. Utile pour les images directement fournies dans le chat.",
        "parameters": {
            "type": "object",
            "properties": {
                "image_base64": {"type": "string", "description": "L'image encodée en base64, incluant le préfixe mimeType (ex: 'data:image/png;base64,...')."}
            },
            "required": ["image_base64"]
        }
    },
    "apiflash_query": {
        "description": "Capture une capture d'écran d'une URL via ApiFlash et retourne l'URL de l'image capturée.",
        "parameters": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "L'URL de la page à capturer."}
            },
            "required": ["url"]
        }
    },
    "crawlbase_query": {
        "description": "Scrape le contenu HTML ou JavaScript d'une URL via Crawlbase. Utilisez 'use_js' pour les pages dynamiques.",
        "parameters": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "description": "L'URL de la page à scraper."},
                "use_js": {"type": "boolean", "description": "Définir à true pour le scraping JavaScript.", "default": False}
            },
            "required": ["url"]
        }
    },
    "detectlanguage_query": {
        "description": "Détecte la langue d'un texte via DetectLanguage API.",
        "parameters": {
            "type": "object",
            "properties": {
                "text": {"type": "string", "description": "Le texte dont la langue doit être détectée."}
            },
            "required": ["text"]
        }
    },
    "guardian_query": {
        "description": "Recherche des articles de presse via l'API The Guardian.",
        "parameters": {
            "type": "object",
            "properties": {
                "query_text": {"type": "string", "description": "La requête de recherche pour les articles."}
            },
            "required": ["query_text"]
        }
    },
    "ip2location_query": {
        "description": "Géolocalise une adresse IP via IP2Location API.",
        "parameters": {
            "type": "object",
            "properties": {
                "ip_address": {"type": "string", "description": "L'adresse IP à géolocaliser."}
            },
            "required": ["ip_address"]
        }
    },
    "shodan_query": {
        "description": "Interroge Shodan pour des informations sur un hôte IP ou des informations sur la clé API.",
        "parameters": {
            "type": "object",
            "properties": {
                "query_text": {"type": "string", "description": "L'adresse IP à rechercher ou vide pour les infos de la clé API."}
            },
            "required": []
        }
    },
    "weatherapi_query": {
        "description": "Récupère les conditions météorologiques actuelles pour une localisation via WeatherAPI.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "La ville ou le code postal pour la météo."}
            },
            "required": ["location"]
        }
    },
    "cloudmersive_query": {
        "description": "Vérifie la validité et le type d'un domaine via Cloudmersive API.",
        "parameters": {
            "type": "object",
            "properties": {
                "domain": {"type": "string", "description": "Le nom de domaine à vérifier."}
            },
            "required": ["domain"]
        }
    },
    "greynoise_query": {
        "description": "Analyse une adresse IP pour détecter des activités 'bruit' (malveillantes) via GreyNoise.",
        "parameters": {
            "type": "object",
            "properties": {
                "ip_address": {"type": "string", "description": "L'adresse IP à analyser."}
            },
            "required": ["ip_address"]
        }
    },
    "pulsedive_query": {
        "description": "Analyse un indicateur de menace (IP, domaine, URL) via Pulsedive.",
        "parameters": {
            "type": "object",
            "properties": {
                "indicator": {"type": "string", "description": "L'indicateur de menace à analyser (IP, domaine, URL)."},
                "type": {"type": "string", "description": "Le type d'indicateur ('auto', 'ip', 'domain', 'url').", "default": "auto"}
            },
            "required": ["indicator"]
        }
    },
    "stormglass_query": {
        "description": "Récupère les données météorologiques maritimes pour une coordonnée (latitude, longitude) via StormGlass.",
        "parameters": {
            "type": "object",
            "properties": {
                "lat": {"type": "number", "format": "float", "description": "La latitude."},
                "lng": {"type": "number", "format": "float", "description": "La longitude."},
                "params": {"type": "string", "description": "Paramètres météo à récupérer (ex: 'airTemperature,waveHeight').", "default": "airTemperature,waveHeight"}
            },
            "required": ["lat", "lng"]
        }
    },
    "loginradius_query": {
        "description": "Effectue un simple ping à l'API LoginRadius pour vérifier sa disponibilité.",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    },
    "jsonbin_query": {
        "description": "Crée un nouveau 'bin' JSON ou accède à un bin existant via Jsonbin.io.",
        "parameters": {
            "type": "object",
            "properties": {
                "data": {"type": "object", "description": "Les données JSON à sauvegarder lors de la création d'un bin.", "nullable": True},
                "private": {"type": "boolean", "description": "Indique si le bin doit être privé (true) ou public (false).", "default": True},
                "bin_id": {"type": "string", "description": "L'ID du bin existant à accéder (si pas de 'data').", "nullable": True}
            },
            "required": []
        }
    },
    "huggingface_query": {
        "description": "Effectue une inférence sur un modèle HuggingFace (ex: classification de texte, génération).",
        "parameters": {
            "type": "object",
            "properties": {
                "model_name": {"type": "string", "description": "Le nom du modèle HuggingFace à utiliser (ex: 'distilbert-base-uncased-finetuned-sst-2-english').", "default": "distilbert-base-uncased-finetuned-sst-2-english"},
                "input_text": {"type": "string", "description": "Le texte d'entrée pour l'inférence."}
            },
            "required": ["input_text"]
        }
    },
    "twilio_query": {
        "description": "Récupère le solde du compte Twilio.",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    },
    "abstractapi_query": {
        "description": "Interroge diverses APIs d'AbstractAPI (validation email/téléphone, taux de change, jours fériés).",
        "parameters": {
            "type": "object",
            "properties": {
                "input_value": {"type": "string", "description": "La valeur d'entrée (email, numéro de téléphone, code pays, devise de base)."},
                "api_type": {"type": "string", "description": "Le type d'API AbstractAPI à utiliser ('PHONE_VALIDATION', 'EMAIL_VALIDATION', 'EXCHANGE_RATES', 'HOLIDAYS').", "enum": ["PHONE_VALIDATION", "EMAIL_VALIDATION", "EXCHANGE_RATES", "HOLIDAYS"]}
            },
            "required": ["api_type"]
        }
    },
    "google_custom_search_query": {
        "description": "Effectue une recherche personnalisée Google via l'API Custom Search.",
        "parameters": {
            "type": "object",
            "properties": {
                "query_text": {"type": "string", "description": "La requête de recherche."}
            },
            "required": ["query_text"]
        }
    },
    "randommer_query": {
        "description": "Génère des numéros de téléphone aléatoires via Randommer.io.",
        "parameters": {
            "type": "object",
            "properties": {
                "country_code": {"type": "string", "description": "Le code pays (ex: 'US', 'FR').", "default": "US"},
                "quantity": {"type": "integer", "description": "Le nombre de numéros à générer.", "default": 1}
            },
            "required": []
        }
    },
    "tomorrowio_query": {
        "description": "Récupère les prévisions météorologiques via Tomorrow.io.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "La localisation (nom de ville, code postal ou coordonnées)."},
                "fields": {"type": "array", "items": {"type": "string"}, "description": "Liste des champs météo à récupérer (ex: ['temperature', 'humidity']).", "default": ["temperature", "humidity", "windSpeed"]}
            },
            "required": ["location"]
        }
    },
    "openweathermap_query": {
        "description": "Récupère les conditions météorologiques actuelles pour une localisation via OpenWeatherMap.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "La ville ou le code postal pour la météo."}
            },
            "required": ["location"]
        }
    },
    "mockaroo_query": {
        "description": "Génère des données de test via Mockaroo.",
        "parameters": {
            "type": "object",
            "properties": {
                "count": {"type": "integer", "description": "Le nombre d'enregistrements à générer.", "default": 1},
                "fields_json": {"type": "string", "description": "Une chaîne JSON décrivant les champs à générer (ex: '[{\"name\":\"name\",\"type\":\"Full Name\"}]').", "nullable": True}
            },
            "required": []
        }
    },
    "openpagerank_query": {
        "description": "Récupère le PageRank de domaines via OpenPageRank.",
        "parameters": {
            "type": "object",
            "properties": {
                "domains": {"type": "array", "items": {"type": "string"}, "description": "Liste des noms de domaine à vérifier."}
            },
            "required": ["domains"]
        }
    },
    "rapidapi_query": {
        "description": "Interroge diverses APIs disponibles via RapidAPI (blagues, taux de change, faits aléatoires).",
        "parameters": {
            "type": "object",
            "properties": {
                "api_name": {"type": "string", "description": "Le nom de l'API RapidAPI à utiliser (ex: 'Programming Joke', 'Currency List Quotes', 'Random Fact').", "enum": ["Programming Joke", "Currency List Quotes", "Random Fact"]},
                "kwargs": {"type": "object", "description": "Arguments supplémentaires spécifiques à l'API RapidAPI appelée.", "additionalProperties": True}
            },
            "required": ["api_name"]
        }
    }
}

# ==============================================================================
# Paramètres du Chat et de la Mémoire
# ==============================================================================

# Longueur maximale de l'historique du chat à conserver en mémoire et sur disque
MAX_CHAT_HISTORY_LENGTH = 20

# ==============================================================================
# Paramètres des Checks de Santé des Endpoints
# ==============================================================================

# Activer ou désactiver les checks de santé périodiques des endpoints API
ENABLE_HEALTH_CHECKS = True

# Intervalle en secondes entre chaque exécution des checks de santé
HEALTH_CHECK_INTERVAL_SECONDS = 2700

import json
import logging
from datetime import datetime, timezone
from pathlib import Path
import re
import asyncio
import os
from typing import Any, Optional, Dict

# Import des constantes du fichier de configuration
from config import LOG_FILE, ERROR_LOG_PATH, BASE_DIR, MAX_FILE_SIZE, API_CONFIG, TOOL_CONFIG

# ==== Configuration du logging ====
# Configure le logger principal pour le bot
logger = logging.getLogger("bot_logger")
logger.setLevel(logging.INFO)

# Crée le répertoire de base si nécessaire
BASE_DIR.mkdir(parents=True, exist_ok=True)

# Gestionnaire pour le fichier de log principal
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Gestionnaire pour les erreurs critiques (fichier séparé)
error_file_handler = logging.FileHandler(ERROR_LOG_PATH)
error_file_handler.setLevel(logging.ERROR)
error_file_handler.setFormatter(formatter)
logger.addHandler(error_file_handler)

# Gestionnaire pour la console (logs en temps réel)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Verrou pour les opérations de fichier asynchrones
_file_lock: Optional[asyncio.Lock] = None

def set_file_lock(lock: asyncio.Lock):
    """Définit l'instance du verrou asyncio pour les opérations de fichier."""
    global _file_lock
    _file_lock = lock

def log_message(message: str, level: str = "info"):
    """
    Enregistre un message dans le fichier de log et la console.
    Args:
        message (str): Le message à enregistrer.
        level (str): Le niveau de log ('debug', 'info', 'warning', 'error', 'critical').
    """
    if level == "debug":
        logger.debug(message)
    elif level == "info":
        logger.info(message)
    elif level == "warning":
        logger.warning(message)
    elif level == "error":
        logger.error(message)
    elif level == "critical":
        logger.critical(message)
    else:
        logger.info(f"Niveau de log inconnu '{level}': {message}")

def get_current_time() -> datetime:
    """Retourne l'heure actuelle en UTC."""
    return datetime.now(timezone.utc)

def format_datetime(dt: datetime) -> str:
    """Formate un objet datetime en chaîne de caractères lisible."""
    return dt.strftime("%Y-%m-%d %H:%M:%S UTC")

async def load_json(file_path: Path, default_value: Any = None) -> Any:
    """
    Charge les données d'un fichier JSON de manière asynchrone.
    Crée le fichier avec une valeur par défaut si inexistant.
    Args:
        file_path (Path): Le chemin du fichier JSON.
        default_value (Any): La valeur à retourner si le fichier n'existe pas ou est vide.
    Returns:
        Any: Le contenu du fichier JSON ou la valeur par défaut.
    """
    if _file_lock is None:
        log_message("Le verrou de fichier n'est pas initialisé dans utils.py. Initialisation par défaut.", level="warning")
        global _file_lock
        _file_lock = asyncio.Lock()

    try:
        if not file_path.exists():
            log_message(f"Fichier non trouvé: {file_path}. Création avec valeur par défaut.", level="info")
            await save_json(file_path, default_value if default_value is not None else {})
            return default_value if default_value is not None else {}
        
        async with _file_lock:
            return await asyncio.to_thread(_load_json_sync, file_path)
    except json.JSONDecodeError:
        log_message(f"Erreur de décodage JSON pour le fichier: {file_path}. Le fichier pourrait être corrompu. Retourne la valeur par défaut.", level="error")
        await save_json(file_path, default_value if default_value is not None else {})
        return default_value if default_value is not None else {}
    except Exception as e:
        log_message(f"Erreur inattendue lors du chargement du JSON {file_path}: {e}", level="error")
        return default_value if default_value is not None else {}

def _load_json_sync(file_path: Path) -> Any:
    """Fonction synchrone pour charger le JSON, appelée par asyncio.to_thread."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

async def save_json(file_path: Path, data: Any):
    """
    Sauvegarde les données dans un fichier JSON de manière asynchrone.
    Args:
        file_path (Path): Le chemin du fichier JSON.
        data (Any): Les données à sauvegarder.
    """
    if _file_lock is None:
        log_message("Le verrou de fichier n'est pas initialisé dans utils.py. Initialisation par défaut.", level="warning")
        global _file_lock
        _file_lock = asyncio.Lock()

    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        async with _file_lock:
            await asyncio.to_thread(_save_json_sync, file_path, data)
        log_message(f"Données sauvegardées dans {file_path}", level="debug")
    except Exception as e:
        log_message(f"Erreur lors de la sauvegarde du JSON {file_path}: {e}", level="error")

def _save_json_sync(file_path: Path, data: Any):
    """Fonction synchrone pour sauvegarder le JSON, appelée par asyncio.to_thread."""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def neutralize_urls(text: str) -> str:
    """
    Remplace les URLs dans le texte par une version neutralisée pour éviter les problèmes de sécurité
    ou les tentatives d'accès non désirées par le modèle.
    """
    url_pattern = re.compile(r'https?://[^\s/$.?#].[^\s]*', re.IGNORECASE)
    
    neutralized_text = url_pattern.sub("[LIEN_NEUTRALISÉ]", text)
    return neutralized_text

def find_tool_by_name(tool_name: str) -> Optional[Dict[str, Any]]:
    """
    Recherche un outil dans TOOL_CONFIG par son nom.
    Args:
        tool_name (str): Le nom de l'outil à rechercher.
    Returns:
        Optional[Dict[str, Any]]: Le dictionnaire de configuration de l'outil si trouvé, sinon None.
    """
    return TOOL_CONFIG.get(tool_name)

async def append_to_file(file_path: Path, content: str):
    """
    Ajoute du contenu à un fichier, en créant le fichier/répertoire si nécessaire.
    Gère la rotation du fichier si sa taille dépasse MAX_FILE_SIZE.
    """
    if _file_lock is None:
        log_message("Le verrou de fichier n'est pas initialisé dans utils.py. Initialisation par défaut.", level="warning")
        global _file_lock
        _file_lock = asyncio.Lock()

    file_path.parent.mkdir(parents=True, exist_ok=True)

    if file_path.exists() and file_path.stat().st_size + len(content.encode('utf-8')) > MAX_FILE_SIZE:
        rotate_file(file_path)

    async with _file_lock:
        await asyncio.to_thread(_append_to_file_sync, file_path, content)

def _append_to_file_sync(file_path: Path, content: str):
    """Fonction synchrone pour ajouter du contenu à un fichier."""
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(content + "\n")

def rotate_file(file_path: Path):
    """
    Effectue une rotation de fichier simple: renomme le fichier actuel avec un horodatage.
    """
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    new_path = file_path.parent / f"{file_path.stem}_{timestamp}{file_path.suffix}"
    try:
        os.rename(file_path, new_path)
        log_message(f"Fichier {file_path.name} renommé en {new_path.name} pour rotation.", level="info")
    except OSError as e:
        log_message(f"Erreur lors de la rotation du fichier {file_path.name}: {e}", level="error")

import time
import httpx
import json
import base64
import asyncio
import re 
import traceback
from typing import Dict, Any, Optional, Union, List, Tuple

# Import des constantes et fonctions utilitaires
from config import API_CONFIG, ENDPOINT_HEALTH_FILE, MAX_IMAGE_SIZE, GEMINI_TEMPERATURE, GEMINI_TOP_P, GEMINI_TOP_K, GEMINI_MAX_OUTPUT_TOKENS, GEMINI_SAFETY_SETTINGS
from utils import load_json, save_json, get_current_time, format_datetime, log_message, neutralize_urls

class EndpointHealthManager:
    """
    Gère la santé des endpoints API et sélectionne le meilleur endpoint disponible
    en fonction de critères comme la latence, le taux de succès et le nombre d'erreurs.
    C'est un singleton pour s'assurer qu'il n'y a qu'une seule instance de gestionnaire de santé.
    """
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        """Implémente le patron de conception Singleton."""
        if cls._instance is None:
            cls._instance = super(cls, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        """Initialise le gestionnaire."""
        if self._initialized:
            return
        self.health_status = {}

    async def init_manager(self):
        """
        Initialise le gestionnaire de santé de manière asynchrone.
        Charge l'état de santé persistant et s'assure que tous les endpoints sont suivis.
        """
        if not self._initialized:
            self.health_status = await load_json(ENDPOINT_HEALTH_FILE, {})
            self._initialize_health_status()
            self._initialized = True
            log_message("Gestionnaire de santé des endpoints initialisé.")

    def _initialize_health_status(self):
        """
        Initialise ou met à jour le statut de santé pour tous les endpoints configurés dans `API_CONFIG`.
        Ajoute les nouveaux endpoints et s'assure que toutes les clés nécessaires sont présentes.
        """
        updated = False
        for service_name, endpoints_config in API_CONFIG.items():
            if service_name not in self.health_status:
                self.health_status[service_name] = {}
                updated = True
            for endpoint_config in endpoints_config:
                endpoint_key = f"{endpoint_config['endpoint_name']}-{str(endpoint_config['key'])}"
                if endpoint_key not in self.health_status[service_name]:
                    self.health_status[service_name][endpoint_key] = {
                        "latency": 0.0,
                        "success_rate": 1.0,
                        "last_checked": None,
                        "error_count": 0,
                        "total_checks": 0,
                        "is_healthy": True
                    }
                    updated = True
        if updated:
            asyncio.create_task(save_json(ENDPOINT_HEALTH_FILE, self.health_status))
            log_message("Statut de santé des endpoints initialisé/mis à jour.")

    async def run_health_check_for_service(self, service_name: str):
        """
        Exécute des checks de santé pour tous les endpoints d'un service donné.
        Tente d'appeler l'endpoint avec des paramètres de santé prédéfinis.
        """
        endpoints_config = API_CONFIG.get(service_name)
        if not endpoints_config:
            log_message(f"Aucune configuration d'endpoint trouvée pour le service: {service_name}", level="warning")
            return

        log_message(f"Lancement du health check pour le service: {service_name}")
        for endpoint_config in endpoints_config:
            endpoint_key = f"{endpoint_config['endpoint_name']}-{str(endpoint_config['key'])}"
            start_time = time.monotonic()
            success = False
            try:
                request_method = endpoint_config.get("method", "GET")
                url = endpoint_config["url"]
                
                params = endpoint_config.get("health_check_params", endpoint_config.get("fixed_params", {})).copy()
                json_data = endpoint_config.get("health_check_json", endpoint_config.get("fixed_json", {})).copy()
                headers = endpoint_config.get("fixed_headers", {}).copy()
                auth = None
                
                check_timeout = endpoint_config.get("timeout", 5)

                if "health_check_url_suffix" in endpoint_config:
                    url += endpoint_config["health_check_url_suffix"]

                key_field = endpoint_config.get("key_field")
                key_location = endpoint_config.get("key_location")
                key_prefix = endpoint_config.get("key_prefix", "")
                api_key = endpoint_config["key"]

                if key_field and key_location:
                    if key_location == "param":
                        params[key_field] = api_key
                    elif key_location == "header":
                        headers[key_field] = f"{key_prefix}{api_key}"
                    elif key_location == "auth_basic":
                        if isinstance(api_key, tuple) and len(api_key) == 2:
                            auth = httpx.BasicAuth(api_key[0], api_key[1])
                        else:
                            log_message(f"Clé API pour auth_basic non valide pour {service_name}:{endpoint_key}", level="error")
                            success = False
                            continue

                async with httpx.AsyncClient(timeout=check_timeout) as client:
                    response = await client.request(request_method, url, params=params, headers=headers, json=json_data, auth=auth)
                    response.raise_for_status()
                    success = True
            except httpx.HTTPStatusError as e:
                log_level = "warning"
                if 400 <= e.response.status_code < 500 and e.response.status_code != 429:
                    log_level = "debug" 
                log_message(f"Health check pour {endpoint_key} ({service_name}) a échoué (HTTP {e.response.status_code}): {e.response.text}", level=log_level)
                success = False
            except httpx.RequestError as e:
                log_message(f"Health check pour {endpoint_key} ({service_name}) a échoué (Réseau): {e}", level="warning")
                success = False
            except Exception as e:
                log_message(f"Health check pour {endpoint_key} ({service_name}) a échoué (Inattendu): {e}", level="error")
                success = False
            finally:
                latency = time.monotonic() - start_time
                self.update_endpoint_health(service_name, endpoint_key, success, latency)
        log_message(f"Health check terminé pour le service: {service_name}")

    def update_endpoint_health(self, service_name: str, endpoint_key: str, success: bool, latency: float):
        """
        Met à jour le statut de santé d'un endpoint spécifique.
        Utilise une moyenne glissante pour le taux de succès et la latence.
        """
        if service_name not in self.health_status:
            self.health_status[service_name] = {}
        if endpoint_key not in self.health_status[service_name]:
            self.health_status[service_name][endpoint_key] = {
                "latency": 0.0,
                "success_rate": 1.0,
                "last_checked": None,
                "error_count": 0,
                "total_checks": 0,
                "is_healthy": True
            }

        status = self.health_status[service_name][endpoint_key]
        status["total_checks"] += 1
        status["last_checked"] = format_datetime(get_current_time())

        alpha = 0.1
        if success:
            status["error_count"] = max(0, status["error_count"] - 1)
            status["success_rate"] = status["success_rate"] * (1 - alpha) + 1.0 * alpha
            status["latency"] = status["latency"] * (1 - alpha) + latency * alpha
        else:
            status["error_count"] += 1
            status["success_rate"] = status["success_rate"] * (1 - alpha) + 0.0 * alpha
            status["latency"] = status["latency"] * (1 - alpha) + 10.0 * alpha 

        if status["error_count"] >= 3 or status["success_rate"] < 0.5:
            status["is_healthy"] = False
        else:
            status["is_healthy"] = True
        
        asyncio.create_task(save_json(ENDPOINT_HEALTH_FILE, self.health_status))
        log_message(f"Santé de {service_name}:{endpoint_key} mise à jour: Succès: {success}, Latence: {latency:.2f}s, Taux Succès: {status['success_rate']:.2f}, Sain: {status['is_healthy']}", level="debug" if not status["is_healthy"] else "info")

    def get_best_endpoint(self, service_name: str) -> Optional[Dict]:
        """
        Sélectionne le meilleur endpoint pour un service donné basé sur son statut de santé.
        Priorise les endpoints sains, puis les moins mauvais en cas d'absence d'endpoints sains.
        """
        service_health = self.health_status.get(service_name)
        if not service_health:
            log_message(f"Aucune donnée de santé pour le service {service_name}. Retourne None.", level="warning")
            return None

        best_endpoint_key = None
        best_score = -float('inf')

        healthy_endpoints = [
            (key, status) for key, status in service_health.items() if status["is_healthy"]
        ]

        if not healthy_endpoints:
            log_message(f"Aucun endpoint sain pour le service {service_name}. Tentative de sélection d'un endpoint non sain.", level="warning")
            all_endpoints = service_health.items()
            if not all_endpoints: 
                return None
            
            sorted_endpoints = sorted(all_endpoints, key=lambda item: (item[1]["error_count"], item[1]["latency"]))
            best_endpoint_key = sorted_endpoints[0][0]
            log_message(f"Fallback: Endpoint {best_endpoint_key} sélectionné pour {service_name} (non sain).", level="warning")
        else:
            for endpoint_key, status in healthy_endpoints:
                score = (status["success_rate"] * 100) - (status["latency"] * 10) - (status["error_count"] * 5)
                if score > best_score:
                    best_score = score
                    best_endpoint_key = endpoint_key
            log_message(f"Meilleur endpoint sélectionné pour {service_name}: {best_endpoint_key} (Score: {best_score:.2f})")

        if best_endpoint_key:
            for endpoint_config in API_CONFIG.get(service_name, []):
                current_endpoint_key = f"{endpoint_config['endpoint_name']}-{str(endpoint_config['key'])}"
                if current_endpoint_key == best_endpoint_key:
                    return endpoint_config
        return None

# Instancier le gestionnaire de santé des endpoints (sera initialisé dans main.py)
endpoint_health_manager = EndpointHealthManager()

def set_endpoint_health_manager_global(manager: EndpointHealthManager):
    """
    Permet d'injecter l'instance du gestionnaire de santé des endpoints.
    Ceci est utilisé pour s'assurer que tous les clients API utilisent la même instance.
    """
    global endpoint_health_manager
    endpoint_health_manager = manager

class APIClient:
    """
    Classe de base pour tous les clients API.
    Elle gère la sélection dynamique d'endpoints, les réessais en cas d'échec
    et l'intégration avec le gestionnaire de santé des endpoints.
    """
    def __init__(self, name: str, endpoint_health_manager: EndpointHealthManager):
        self.name = name
        self.endpoints_config = API_CONFIG.get(name, [])
        self.endpoint_health_manager = endpoint_health_manager
        if not self.endpoints_config:
            log_message(f"Client API {self.name} initialisé sans configuration d'endpoint.", level="error")

    async def _make_request(self, params: Optional[Dict] = None, headers: Optional[Dict] = None, 
                            json_data: Optional[Dict] = None, timeout: Optional[int] = None, 
                            max_retries: int = 3, initial_delay: float = 1.0, 
                            url: Optional[str] = None, method: Optional[str] = None, 
                            key_field: Optional[str] = None, key_location: Optional[str] = None, 
                            api_key: Optional[Union[str, Tuple[str, str]]] = None, 
                            fixed_params: Optional[Dict] = None, fixed_headers: Optional[Dict] = None, 
                            fixed_json: Optional[Dict] = None) -> Optional[Union[Dict, str, bytes]]:
        """
        Méthode interne pour effectuer les requêtes HTTP en utilisant le meilleur endpoint avec réessais.
        """
        
        selected_endpoint_config = None
        endpoint_key_for_health = "Dynamic"

        if url and method:
            selected_endpoint_config = {
                "url": url,
                "method": method,
                "key_field": key_field,
                "key_location": key_location,
                "key": api_key,
                "fixed_params": fixed_params if fixed_params is not None else {},
                "fixed_headers": fixed_headers if fixed_headers is not None else {},
                "fixed_json": fixed_json if fixed_json is not None else {},
                "endpoint_name": "Dynamic",
                "timeout": timeout if timeout is not None else 30
            }
            if api_key:
                endpoint_key_for_health = f"Dynamic-{str(api_key)}"
            log_message(f"Requête dynamique pour {self.name} vers {url}")
        else:
            selected_endpoint_config = self.endpoint_health_manager.get_best_endpoint(self.name)
            if not selected_endpoint_config:
                log_message(f"Aucun endpoint sain ou disponible pour {self.name}.", level="error")
                return {"error": True, "message": f"Aucun endpoint sain ou disponible pour {self.name}."}
            endpoint_key_for_health = f"{selected_endpoint_config['endpoint_name']}-{str(selected_endpoint_config['key'])}"
            log_message(f"Endpoint sélectionné pour {self.name}: {selected_endpoint_config['endpoint_name']}")
            timeout = timeout if timeout is not None else selected_endpoint_config.get("timeout", 30)

        url_to_use = selected_endpoint_config["url"]
        method_to_use = selected_endpoint_config["method"]

        request_params = selected_endpoint_config.get("fixed_params", {}).copy()
        request_headers = selected_endpoint_config.get("fixed_headers", {}).copy()
        request_json_data = selected_endpoint_config.get("fixed_json", {}).copy()
        auth = None

        if params:
            request_params.update(params)
        if headers:
            request_headers.update(headers)
        if json_data:
            request_json_data.update(json_data)

        key_field_to_use = selected_endpoint_config.get("key_field")
        key_location_to_use = selected_endpoint_config.get("key_location")
        key_prefix = selected_endpoint_config.get("key_prefix", "")
        api_key_to_use = selected_endpoint_config["key"]

        if key_field_to_use and key_location_to_use:
            if key_location_to_use == "param":
                request_params[key_field_to_use] = api_key_to_use
            elif key_location_to_use == "header":
                request_headers[key_field_to_use] = f"{key_prefix}{api_key_to_use}"
            elif key_location_to_use == "auth_basic":
                if isinstance(api_key_to_use, tuple) and len(api_key_to_use) == 2:
                    auth = httpx.BasicAuth(api_key_to_use[0], api_key_to_use[1])
                else:
                    log_message(f"Clé API pour auth_basic non valide pour {self.name}:{endpoint_key_for_health}", level="error")
                    self.endpoint_health_manager.update_endpoint_health(self.name, endpoint_key_for_health, False, 0.0)
                    return {"error": True, "message": "Configuration d'authentification basique invalide."}

        current_delay = initial_delay
        for attempt in range(max_retries):
            start_time = time.monotonic()
            success = False
            try:
                async with httpx.AsyncClient(timeout=timeout) as client:
                    response = await client.request(method_to_use, url_to_use, params=request_params, headers=request_headers, json=request_json_data, auth=auth)
                    response.raise_for_status()
                    success = True
                    
                    content_type = response.headers.get("Content-Type", "").lower()
                    if "application/json" in content_type:
                        try:
                            return response.json()
                        except json.JSONDecodeError:
                            log_message(f"API {self.name} réponse non JSON valide (tentative {attempt+1}/{max_retries}): {response.text[:200]}...", level="warning")
                            if attempt < max_retries - 1:
                                await asyncio.sleep(current_delay)
                                current_delay *= 2
                                continue
                            return {"error": True, "message": "Réponse API non JSON valide.", "raw_response": response.text}
                    else:
                        log_message(f"API {self.name} a renvoyé un Content-Type non JSON: {content_type}", level="info")
                        return response.content

            except httpx.HTTPStatusError as e:
                log_message(f"API {self.name} erreur HTTP (tentative {attempt+1}/{max_retries}): {e.response.status_code} - {e.response.text}", level="warning")
                if 400 <= e.response.status_code < 500 and e.response.status_code != 429:
                    log_message(f"API {self.name}: Erreur client {e.response.status_code}, pas de réessai.", level="error")
                    self.endpoint_health_manager.update_endpoint_health(self.name, endpoint_key_for_health, False, e.response.elapsed.total_seconds())
                    return {"error": True, "status_code": e.response.status_code, "message": e.response.text}
                
                if attempt < max_retries - 1:
                    log_message(f"API {self.name}: Réessai dans {current_delay:.2f}s...", level="info")
                    await asyncio.sleep(current_delay)
                    current_delay *= 2
            except httpx.RequestError as e:
                log_message(f"API {self.name} erreur de requête (tentative {attempt+1}/{max_retries}): {e}", level="warning")
                if attempt < max_retries - 1:
                    log_message(f"API {self.name}: Réessai dans {current_delay:.2f}s...", level="info")
                    await asyncio.sleep(current_delay)
                    current_delay *= 2
            except Exception as e:
                log_message(f"API {self.name} erreur inattendue (tentative {attempt+1}/{max_retries}): {e}", level="error")
                self.endpoint_health_manager.update_endpoint_health(self.name, endpoint_key_for_health, False, time.monotonic() - start_time)
                return {"error": True, "message": str(e)}
            finally:
                if not success:
                    latency = time.monotonic() - start_time
                    self.endpoint_health_manager.update_endpoint_health(self.name, endpoint_key_for_health, False, latency)
        
        log_message(f"API {self.name}: Toutes les tentatives ont échoué après {max_retries} réessais.", level="error")
        return {"error": True, "message": f"Échec de la requête après {max_retries} tentatives."}

    async def query(self, *args, **kwargs) -> Any:
        """
        Méthode abstraite pour interroger l'API.
        Doit être implémentée par chaque sous-classe de client API.
        """
        raise NotImplementedError("La méthode query doit être implémentée par les sous-classes.")

# --- Clients API Spécifiques ---

class GeminiAPIClient(APIClient):
    """Client pour l'API Gemini, hérite de APIClient pour la gestion de santé."""
    def __init__(self):
        super().__init__("GEMINI_API", endpoint_health_manager)
        self.model_name = "gemini-1.5-flash-latest"
        self.generation_config = {
            "temperature": GEMINI_TEMPERATURE,
            "top_p": GEMINI_TOP_P,
            "top_k": GEMINI_TOP_K,
            "max_output_tokens": GEMINI_MAX_OUTPUT_TOKENS,
        }
        self.safety_settings = GEMINI_SAFETY_SETTINGS
        log_message(f"GeminiApiClient initialisé avec le modèle par défaut: {self.model_name}")

    async def generate_content(self, prompt: str, chat_history: List[Dict], image_data: Optional[str] = None, model: Optional[str] = None, tools: Optional[List[Dict]] = None) -> Union[Dict, str]:
        """Génère du contenu textuel ou multimodal en utilisant l'API Gemini."""
        model_to_use = model if model else self.model_name
        
        contents = []
        for msg in chat_history:
            role = "user" if msg["role"] == "user" else "model"
            contents.append({"role": role, "parts": msg["parts"]})

        if contents and contents[-1]["role"] == "user":
            contents[-1]["parts"].append({"text": prompt})
        else:
            contents.append({"role": "user", "parts": [{"text": prompt}]})

        if image_data:
            if "," in image_data:
                mime_type_part, base64_data = image_data.split(",", 1)
                mime_type = mime_type_part.split(":", 1)[1].split(";", 1)[0]
            else:
                mime_type = "image/jpeg" 
                base64_data = image_data

            if contents and contents[-1]["role"] == "user":
                contents[-1]["parts"].append({
                    "inlineData": {
                        "mimeType": mime_type,
                        "data": base64_data
                    }
                })
                log_message(f"Image ajoutée au prompt Gemini (mimeType: {mime_type}).")
            else:
                log_message("Impossible d'ajouter l'image au prompt Gemini: le dernier message n'est pas un utilisateur.", level="warning")

        payload = {
            "contents": contents,
            "generationConfig": self.generation_config,
            "safetySettings": self.safety_settings
        }

        if tools:
            payload["tools"] = tools

        log_message(f"Appel à Gemini API pour le modèle {model_to_use}...")
        
        # L'URL de l'endpoint Gemini peut varier en fonction du modèle.
        # On prend l'URL de base du premier endpoint configuré et on y ajoute le modèle.
        base_url_from_config = self.endpoints_config[0]["url"].split(':generateContent')[0]
        dynamic_url = f"{base_url_from_config}:{model_to_use}:generateContent"

        # Les headers et la clé API seront gérés par _make_request via la sélection d'endpoint
        response = await self._make_request(
            url=dynamic_url,
            method="POST",
            json_data=payload,
            timeout=60 # Utilise le timeout de la méthode _make_request
        )

        if response and not response.get("error"):
            return response
        return f"❌ Erreur Gemini: {response.get('message', 'Inconnu')}" if response else "❌ Erreur Gemini: Réponse vide ou erreur interne."

class OCRApiClient(APIClient):
    """Client pour l'API OCR.space, hérite de APIClient pour la gestion de santé."""
    def __init__(self):
        super().__init__("OCR_API", endpoint_health_manager)
        log_message("OCRApiClient initialisé.")

    async def query(self, image_base64: str) -> str:
        """
        Effectue une requête OCR à l'API OCR.space.
        `image_base64` doit être la chaîne base64 de l'image, incluant le préfixe mimeType.
        """
        payload = {
            "base64Image": image_base64,
            "language": "fre",
            "isOverlayRequired": False,
            "OCREngine": 2
        }
        
        # Les headers et la clé API seront gérés par _make_request via la sélection d'endpoint
        log_message("Appel à OCR.space API...")
        response = await self._make_request(
            json_data=payload,
            method="POST",
            timeout=30
        )

        if response and not response.get("error"):
            if response.get("IsErroredOnProcessing"):
                error_message = response.get("ErrorMessage", ["Erreur inconnue lors du traitement OCR."])
                log_message(f"Erreur OCR.space: {error_message}", level="error")
                return f"❌ Erreur OCR: {', '.join(error_message)}"
            
            parsed_text = ""
            if "ParsedResults" in response and response["ParsedResults"]:
                for parsed_result in response["ParsedResults"]:
                    parsed_text += parsed_result.get("ParsedText", "") + "\n"
            
            if parsed_text.strip():
                log_message("OCR.space: Texte extrait avec succès.")
                return parsed_text.strip()
            else:
                log_message("OCR.space: Aucun texte extrait.", level="warning")
                return "Aucun texte n'a pu être extrait de l'image."
        return f"❌ Erreur OCR: {response.get('message', 'Inconnu')}" if response else "❌ Erreur OCR: Réponse vide ou erreur interne."

class DeepSeekClient(APIClient):
    def __init__(self):
        super().__init__("DEEPSEEK", endpoint_health_manager)

    async def query(self, prompt: Union[str, List[Dict]], model: str = "deepseek-chat") -> str:
        """Interroge l'API DeepSeek pour des complétions de chat."""
        if isinstance(prompt, str):
            messages = [{"role": "user", "content": prompt}]
        else:
            messages = prompt

        payload = {"model": model, "messages": messages}
        response = await self._make_request(json_data=payload)
        if response and not response.get("error"):
            content = response.get("choices", [{}])[0].get("message", {}).get("content")
            if content:
                return content
            return "DeepSeek: Pas de contenu de réponse trouvé."
        return f"DeepSeek: Erreur: {response.get('message', 'Inconnu')}" if response else "DeepSeek: Réponse vide ou erreur interne."

class SerperClient(APIClient):
    def __init__(self):
        super().__init__("SERPER", endpoint_health_manager)

    async def query(self, query_text: str) -> str:
        """Effectue une recherche web via l'API Serper."""
        payload = {"q": query_text}
        response = await self._make_request(json_data=payload)
        if response and not response.get("error"):
            organic_results = response.get("organic", [])
            if organic_results:
                snippet = organic_results[0].get("snippet", "Pas de snippet.")
                link = organic_results[0].get("link", "")
                return f"Serper (recherche web):\n{snippet} {neutralize_urls(link)}"
            return "Serper: Aucune information trouvée."
        return f"Serper: Erreur: {response.get('message', 'Inconnu')}" if response else "Serper: Réponse vide ou erreur interne."

class WolframAlphaClient(APIClient):
    def __init__(self):
        super().__init__("WOLFRAMALPHA", endpoint_health_manager)

    async def query(self, input_text: str) -> str:
        """Interroge WolframAlpha pour des calculs ou des faits."""
        params = {"input": input_text}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            pods = response.get("queryresult", {}).get("pods", [])
            if pods:
                for pod in pods:
                    if pod.get("title") in ["Result", "Input interpretation", "Decimal approximation"]:
                        subpods = pod.get("subpods", [])
                        if subpods and subpods[0].get("plaintext"):
                            return f"WolframAlpha:\n{subpods[0]['plaintext']}"
                if pods and pods[0].get("subpods") and pods[0]["subpods"][0].get("plaintext"):
                    return f"WolframAlpha:\n{pods[0]['subpods'][0]['plaintext']}"
            return "WolframAlpha: Pas de résultat clair."
        return f"WolframAlpha: Erreur: {response.get('message', 'Inconnu')}" if response else "WolframAlpha: Réponse vide ou erreur interne."

class TavilyClient(APIClient):
    def __init__(self):
        super().__init__("TAVILY", endpoint_health_manager)

    async def query(self, query_text: str, max_results: int = 3) -> str:
        """Effectue une recherche web avancée via l'API Tavily."""
        payload = {"query": query_text, "max_results": max_results}
        response = await self._make_request(json_data=payload)
        if response and not response.get("error"):
            results = response.get("results", [])
            answer = response.get("answer", "Aucune réponse directe trouvée.")

            output = f"Tavily (recherche web):\nRéponse directe: {answer}\n"
            if results:
                output += "Extraits pertinents:\n"
                for i, res in enumerate(results[:max_results]):
                    output += f"- {res.get('title', 'N/A')}: {res.get('content', 'N/A')} {neutralize_urls(res.get('url', ''))}\n"
            return output
        return f"Tavily: Erreur: {response.get('message', 'Inconnu')}" if response else "Tavily: Réponse vide ou erreur interne."

class ApiFlashClient(APIClient):
    def __init__(self):
        super().__init__("APIFLASH", endpoint_health_manager)

    async def query(self, url: str) -> str:
        """Capture une capture d'écran d'une URL via ApiFlash."""
        params = {"url": url, "format": "jpeg", "full_page": "true"}
        response_content = await self._make_request(params=params)

        if isinstance(response_content, bytes):
            selected_endpoint_config = self.endpoint_health_manager.get_best_endpoint(self.name)
            if selected_endpoint_config:
                capture_url = f"{selected_endpoint_config['url']}?access_key={selected_endpoint_config['key']}&url={url}&format=jpeg&full_page=true"
                return f"ApiFlash (capture d'écran): {neutralize_urls(capture_url)} (Vérifiez le lien pour l'image)"
            return "ApiFlash: Impossible de générer l'URL de capture."
        elif isinstance(response_content, dict) and response_content.get("error"):
            return f"ApiFlash: Erreur: {response_content.get('message', 'Inconnu')}"
        else:
            log_message(f"ApiFlash a renvoyé un type de réponse inattendu: {type(response_content)}", level="warning")
            return f"ApiFlash: Réponse inattendue de l'API. {response_content}"

class CrawlbaseClient(APIClient):
    def __init__(self):
        super().__init__("CRAWLBASE", endpoint_health_manager)

    async def query(self, url: str, use_js: bool = False) -> str:
        """Scrape le contenu HTML ou JavaScript d'une URL via Crawlbase."""
        params = {"url": url, "format": "json"}
        
        selected_endpoint_config = None
        if use_js:
            for config in API_CONFIG.get(self.name, []):
                if "JS Scraper" in config.get("endpoint_name", ""):
                    selected_endpoint_config = config
                    break
        
        if not selected_endpoint_config: 
            selected_endpoint_config = self.endpoint_health_manager.get_best_endpoint(self.name)

        if not selected_endpoint_config:
            return f"Crawlbase: Aucun endpoint sain ou disponible pour {self.name}."

        response = await self._make_request(
            params=params,
            url=selected_endpoint_config["url"],
            method=selected_endpoint_config["method"],
            key_field=selected_endpoint_config["key_field"],
            key_location=selected_endpoint_config["key_location"],
            api_key=selected_endpoint_config["key"],
            fixed_params=selected_endpoint_config.get("fixed_params", {}),
            timeout=selected_endpoint_config.get("timeout")
        )

        if response and not response.get("error"):
            body = response.get("body")
            if body:
                try:
                    decoded_body = base64.b64decode(body).decode('utf-8', errors='ignore')
                    return f"Crawlbase (contenu web):\n{decoded_body[:1000]}..."
                except Exception:
                    return f"Crawlbase (contenu web - brut):\n{body[:1000]}..."
            return "Crawlbase: Contenu non trouvé."
        return f"Crawlbase: Erreur: {response.get('message', 'Inconnu')}" if response else "Crawlbase: Réponse vide ou erreur interne."

class DetectLanguageClient(APIClient):
    def __init__(self):
        super().__init__("DETECTLANGUAGE", endpoint_health_manager)

    async def query(self, text: str) -> str:
        """Détecte la langue d'un texte via DetectLanguage API."""
        payload = {"q": text}
        response = await self._make_request(json_data=payload)
        if response and not response.get("error"):
            detections = response.get("data", {}).get("detections", [])
            if detections:
                first_detection = detections[0]
                lang = first_detection.get("language")
                confidence = first_detection.get("confidence")
                return f"Langue détectée: {lang} (confiance: {confidence})"
            return "DetectLanguage: Aucune langue détectée."
        return f"DetectLanguage: Erreur: {response.get('message', 'Inconnu')}" if response else "DetectLanguage: Réponse vide ou erreur interne."

class GuardianClient(APIClient):
    def __init__(self):
        super().__init__("GUARDIAN", endpoint_health_manager)

    async def query(self, query_text: str) -> str:
        """Recherche des articles de presse via l'API The Guardian."""
        params = {"q": query_text}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            results = response.get("response", {}).get("results", [])
            if results:
                output = "Articles The Guardian:\n"
                for res in results[:3]:
                    output += f"- {res.get('webTitle', 'N/A')}: {res.get('fields', {}).get('trailText', 'N/A')} {neutralize_urls(res.get('webUrl', ''))}\n"
                return output
            return "Guardian: Aucun article trouvé."
        return f"Guardian: Erreur: {response.get('message', 'Inconnu')}" if response else "Guardian: Réponse vide ou erreur interne."

class IP2LocationClient(APIClient):
    def __init__(self):
        super().__init__("IP2LOCATION", endpoint_health_manager)

    async def query(self, ip_address: str) -> str:
        """Géolocalise une adresse IP via IP2Location API."""
        params = {"ip": ip_address}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            if "country_name" in response:
                return f"IP2Location (Géolocalisation IP {ip_address}): Pays: {response['country_name']}, Ville: {response.get('city_name', 'N/A')}"
            return "IP2Location: Informations non trouvées."
        return f"IP2Location: Erreur: {response.get('message', 'Inconnu')}" if response else "IP2Location: Réponse vide ou erreur interne."

class ShodanClient(APIClient):
    def __init__(self):
        super().__init__("SHODAN", endpoint_health_manager)

    async def query(self, query_text: str = "") -> str:
        """
        Interroge Shodan pour des informations sur un hôte IP ou des informations sur la clé API.
        Si `query_text` est une IP, tente de récupérer les infos de l'hôte.
        Sinon, ou en cas d'échec, retourne les infos de la clé API.
        """
        if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", query_text):
            selected_endpoint_config = None
            for config in API_CONFIG.get(self.name, []):
                if "Host Info" in config.get("endpoint_name", ""):
                    selected_endpoint_config = config
                    break
            if selected_endpoint_config:
                url = f"{selected_endpoint_config['url'].rstrip('/')}/{query_text}"
                response = await self._make_request(
                    params={"key": selected_endpoint_config["key"]},
                    url=url,
                    method="GET",
                    key_field=selected_endpoint_config["key_field"],
                    key_location=selected_endpoint_config["key_location"],
                    api_key=selected_endpoint_config["key"],
                    timeout=selected_endpoint_config.get("timeout")
                )
                if response and not response.get("error"):
                    return f"Shodan (info hôte {query_text}): Pays: {response.get('country_name', 'N/A')}, Ports: {response.get('ports', 'N/A')}, Vulnérabilités: {response.get('vulns', 'Aucune')}"
                return f"Shodan (info hôte): Erreur: {response.get('message', 'Inconnu')}" if response else "Shodan: Réponse vide ou erreur interne."
            else:
                return "Shodan: Endpoint 'Host Info' non configuré."
        else:
            response = await self._make_request()
            if response and not response.get("error"):
                return f"Shodan (info clé): Requêtes restantes: {response.get('usage_limits', {}).get('query_credits', 'N/A')}, Scan crédits: {response.get('usage_limits', {}).get('scan_credits', 'N/A')}"
            return f"Shodan: Erreur: {response.get('message', 'Inconnu')}" if response else "Shodan: Réponse vide ou erreur interne."

class WeatherAPIClient(APIClient):
    def __init__(self):
        super().__init__("WEATHERAPI", endpoint_health_manager)

    async def query(self, location: str) -> str:
        """Récupère les conditions météorologiques actuelles pour une localisation via WeatherAPI."""
        params = {"q": location}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            current = response.get("current", {})
            location_info = response.get("location", {})
            if current and location_info:
                return (
                    f"Météo à {location_info.get('name', 'N/A')}, {location_info.get('country', 'N/A')}:\n"
                    f"Température: {current.get('temp_c', 'N/A')}°C, "
                    f"Conditions: {current.get('condition', {}).get('text', 'N/A')}, "
                    f"Vent: {current.get('wind_kph', 'N/A')} km/h"
                )
            return "WeatherAPI: Données météo non trouvées."
        return f"WeatherAPI: Erreur: {response.get('message', 'Inconnu')}" if response else "WeatherAPI: Réponse vide ou erreur interne."

class CloudmersiveClient(APIClient):
    def __init__(self):
        super().__init__("CLOUDMERSIVE", endpoint_health_manager)

    async def query(self, domain: str) -> str:
        """Vérifie la validité et le type d'un domaine via Cloudmersive API."""
        payload = {"domain": domain}
        response = await self._make_request(json_data=payload)
        if response and not response.get("error"):
            return f"Cloudmersive (vérification de domaine {domain}): Valide: {response.get('ValidDomain', 'N/A')}, Type: {response.get('DomainType', 'N/A')}"
        return f"Cloudmersive: Erreur: {response.get('message', 'Inconnu')}" if response else "Cloudmersive: Réponse vide ou erreur interne."

class GreyNoiseClient(APIClient):
    def __init__(self):
        super().__init__("GREYNOISE", endpoint_health_manager)

    async def query(self, ip_address: str) -> str:
        """Analyse une adresse IP pour détecter des activités 'bruit' (malveillantes) via GreyNoise."""
        selected_endpoint_config = self.endpoint_health_manager.get_best_endpoint(self.name)
        if not selected_endpoint_config:
            return f"GreyNoise: Aucun endpoint sain ou disponible pour {self.name}."

        url = f"{selected_endpoint_config['url'].rstrip('/')}/{ip_address}"
        method = selected_endpoint_config["method"]
        headers = {selected_endpoint_config["key_field"]: selected_endpoint_config["key"]}

        response = await self._make_request(
            headers=headers,
            url=url,
            method=method,
            key_field=selected_endpoint_config["key_field"],
            key_location=selected_endpoint_config["key_location"],
            api_key=selected_endpoint_config["key"],
            timeout=selected_endpoint_config.get("timeout")
        )

        if response and not response.get("error"):
            if response.get("noise"):
                return f"GreyNoise (IP {ip_address}): C'est une IP 'bruit' (malveillante). Classification: {response.get('classification', 'N/A')}, Nom d'acteur: {response.get('actor', 'N/A')}"
            return f"GreyNoise (IP {ip_address}): Pas de 'bruit' détecté. Statut: {response.get('status', 'N/A')}"
        return f"GreyNoise: Erreur: {response.get('message', 'Inconnu')}" if response else "GreyNoise: Réponse vide ou erreur interne."

class PulsediveClient(APIClient):
    def __init__(self):
        super().__init__("PULSEDIVE", endpoint_health_manager)

    async def query(self, indicator: str, type: str = "auto") -> str:
        """Analyse un indicateur de menace (IP, domaine, URL) via Pulsedive."""
        params = {"indicator": indicator, "type": type}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            if response.get("results"):
                result = response["results"][0]
                return (
                    f"Pulsedive (Analyse {indicator}): Type: {result.get('type', 'N/A')}, "
                    f"Risk: {result.get('risk', 'N/A')}, "
                    f"Description: {result.get('description', 'N/A')[:200]}..."
                )
            return "Pulsedive: Aucun résultat d'analyse trouvé."
        return f"Pulsedive: Erreur: {response.get('message', 'Inconnu')}" if response else "Pulsedive: Réponse vide ou erreur interne."

class StormGlassClient(APIClient):
    def __init__(self):
        super().__init__("STORMGLASS", endpoint_health_manager)

    async def query(self, lat: float, lng: float, params: str = "airTemperature,waveHeight") -> str:
        """Récupère les données météorologiques maritimes pour une coordonnée via StormGlass."""
        now = int(time.time())
        request_params = {
            "lat": lat,
            "lng": lng,
            "params": params,
            "start": now,
            "end": now + 3600
        }
        response = await self._make_request(params=request_params)
        if response and not response.get("error"):
            data = response.get("hours", [])
            if data:
                first_hour = data[0]
                temp = first_hour.get('airTemperature', [{}])[0].get('value', 'N/A')
                wave_height = first_hour.get('waveHeight', [{}])[0].get('value', 'N/A')
                return f"StormGlass (Météo maritime à {lat},{lng}): Température air: {temp}°C, Hauteur vagues: {wave_height}m"
            return "StormGlass: Données non trouvées."
        return f"StormGlass: Erreur: {response.get('message', 'Inconnu')}" if response else "StormGlass: Réponse vide ou erreur interne."

class LoginRadiusClient(APIClient):
    def __init__(self):
        super().__init__("LOGINRADIUS", endpoint_health_manager)

    async def query(self) -> str:
        """Effectue un simple ping à l'API LoginRadius pour vérifier sa disponibilité."""
        response = await self._make_request()
        if response and not response.get("error"):
            return f"LoginRadius (Ping API): Statut: {response.get('Status', 'N/A')}, Message: {response.get('Message', 'N/A')}"
        return f"LoginRadius: Erreur: {response.get('message', 'Inconnu')}" if response else "LoginRadius: Réponse vide ou erreur interne."

class JsonbinClient(APIClient):
    def __init__(self):
        super().__init__("JSONBIN", endpoint_health_manager)

    async def query(self, data: Optional[Dict[str, Any]] = None, private: bool = True, bin_id: Optional[str] = None) -> str:
        """
        Crée un nouveau 'bin' JSON ou accède à un bin existant via Jsonbin.io.
        `data` est pour la création, `bin_id` pour l'accès.
        """
        if bin_id:
            selected_endpoint_config = None
            for config in API_CONFIG.get(self.name, []):
                if "Bin Access" in config.get("endpoint_name", ""):
                    selected_endpoint_config = config
                    break
            if not selected_endpoint_config:
                return f"Jsonbin: Aucun endpoint d'accès de bin sain ou disponible pour {self.name}."

            url = f"{selected_endpoint_config['url'].rstrip('/')}/{bin_id}"
            method = "GET"
            headers = {selected_endpoint_config["key_field"]: selected_endpoint_config["key"]}
            
            response = await self._make_request(
                headers=headers,
                url=url,
                method=method,
                timeout=selected_endpoint_config.get("timeout")
            )
            if response and not response.get("error"):
                return f"Jsonbin (Accès bin {bin_id}):\n{json.dumps(response, indent=2)}"
            return f"Jsonbin (Accès bin): Erreur: {response.get('message', 'Inconnu')}" if response else "Jsonbin: Réponse vide ou erreur interne."
        
        else:
            selected_endpoint_config = None
            for config in API_CONFIG.get(self.name, []):
                if "Bin Create" in config.get("endpoint_name", ""):
                    selected_endpoint_config = config
                    break
            
            if not selected_endpoint_config:
                return f"Jsonbin: Aucun endpoint de création de bin sain ou disponible pour {self.name}."

            url = selected_endpoint_config["url"]
            method = "POST"
            headers = {selected_endpoint_config["key_field"]: selected_endpoint_config["key"], "Content-Type": "application/json"}
            payload = {"record": data if data is not None else {}, "private": private}

            response = await self._make_request(
                json_data=payload,
                headers=headers,
                url=url,
                method=method,
                timeout=selected_endpoint_config.get("timeout")
            )

            if response and not response.get("error"):
                return f"Jsonbin (Création de bin): ID: {response.get('metadata', {}).get('id', 'N/A')}, URL: {neutralize_urls(response.get('metadata', {}).get('url', 'N/A'))}"
            return f"Jsonbin (Création de bin): Erreur: {response.get('message', 'Inconnu')}" if response else "Jsonbin: Réponse vide ou erreur interne."

class HuggingFaceClient(APIClient):
    def __init__(self):
        super().__init__("HUGGINGFACE", endpoint_health_manager)

    async def query(self, model_name: str = "distilbert-base-uncased-finetuned-sst-2-english", input_text: str = "Hello world") -> str:
        """Effectue une inférence sur un modèle HuggingFace (ex: classification de texte, génération)."""
        selected_endpoint_config = self.endpoint_health_manager.get_best_endpoint(self.name)
        if not selected_endpoint_config:
            return f"HuggingFace: Aucun endpoint sain ou disponible pour {self.name}."

        inference_url = f"https://api-inference.huggingface.co/models/{model_name}"
        
        headers = {
            selected_endpoint_config["key_field"]: f"{selected_endpoint_config['key_prefix']}{selected_endpoint_config['key']}",
            "Content-Type": "application/json"
        }
        payload = {"inputs": input_text}

        response = await self._make_request(
            json_data=payload,
            headers=headers,
            url=inference_url,
            method="POST",
            timeout=selected_endpoint_config.get("timeout")
        )

        if response and not response.get("error"):
            if isinstance(response, list) and response:
                first_result = response[0]
                if isinstance(first_result, list) and first_result:
                    return f"HuggingFace ({model_name} - {first_result[0].get('label')}): Score {first_result[0].get('score', 'N/A'):.2f}"
                elif isinstance(first_result, dict) and "generated_text" in first_result:
                    return f"HuggingFace ({model_name}): {first_result.get('generated_text')}"
            return f"HuggingFace ({model_name}): Réponse non parsée. {response}"
        return f"HuggingFace: Erreur: {response.get('message', 'Inconnu')}" if response else "HuggingFace: Réponse vide ou erreur interne."

class TwilioClient(APIClient):
    def __init__(self):
        super().__init__("TWILIO", endpoint_health_manager)

    async def query(self) -> str:
        """Récupère le solde du compte Twilio."""
        selected_endpoint_config = None
        for config in API_CONFIG.get(self.name, []):
            if "Account Balance" in config.get("endpoint_name", ""):
                selected_endpoint_config = config
                break
        if not selected_endpoint_config:
            if self.endpoints_config:
                selected_endpoint_config = self.endpoints_config[0]
            else:
                return f"Twilio: Aucune configuration d'endpoint disponible pour {self.name}."

        response = await self._make_request(
            url=selected_endpoint_config["url"],
            method=selected_endpoint_config["method"],
            key_location=selected_endpoint_config["key_location"],
            api_key=selected_endpoint_config["key"],
            timeout=selected_endpoint_config.get("timeout")
        )
        if response and not response.get("error"):
            return f"Twilio (Balance): {response.get('balance', 'N/A')} {response.get('currency', 'N/A')}"
        return f"Twilio: Erreur: {response.get('message', 'Inconnu')}" if response else "Twilio: Réponse vide ou erreur interne."

class AbstractAPIClient(APIClient):
    def __init__(self):
        super().__init__("ABSTRACTAPI", endpoint_health_manager)

    async def query(self, input_value: str, api_type: str) -> str:
        """
        Interroge diverses APIs d'AbstractAPI (validation email/téléphone, taux de change, jours fériés).
        `input_value` dépend du `api_type`.
        """
        params = {}
        target_endpoint_name = ""

        if api_type == "PHONE_VALIDATION":
            params["phone"] = input_value
            target_endpoint_name = "Phone Validation"
        elif api_type == "EMAIL_VALIDATION":
            params["email"] = input_value
            target_endpoint_name = "Email Validation"
        elif api_type == "EXCHANGE_RATES":
            params["base"] = input_value if input_value else "USD" 
            target_endpoint_name = "Exchange Rates"
        elif api_type == "HOLIDAYS":
            params["country"] = input_value if input_value else "US"
            from datetime import datetime
            params["year"] = datetime.now(timezone.utc).year
            target_endpoint_name = "Holidays"
        else:
            return f"AbstractAPI: Type d'API '{api_type}' non supporté pour la requête."

        selected_endpoint_config = None
        for config in API_CONFIG.get(self.name, []):
            if target_endpoint_name in config["endpoint_name"]:
                selected_endpoint_config = config
                break
        
        if not selected_endpoint_config:
            return f"AbstractAPI: Aucun endpoint sain ou disponible pour {self.name} pour le type {api_type}."

        response = await self._make_request(
            params=params,
            url=selected_endpoint_config["url"],
            method=selected_endpoint_config["method"],
            key_field=selected_endpoint_config["key_field"],
            key_location=selected_endpoint_config["key_location"],
            api_key=selected_endpoint_config["key"],
            fixed_params=selected_endpoint_config.get("fixed_params", {}),
            timeout=selected_endpoint_config.get("timeout")
        )

        if response and not response.get("error"):
            if api_type == "PHONE_VALIDATION":
                return (
                    f"AbstractAPI (Validation Tél): Numéro: {response.get('phone', 'N/A')}, "
                    f"Valide: {response.get('valid', 'N/A')}, "
                    f"Pays: {response.get('country', {}).get('name', 'N/A')}"
                )
            elif api_type == "EMAIL_VALIDATION":
                return (
                    f"AbstractAPI (Validation Email): Email: {response.get('email', 'N/A')}, "
                    f"Valide: {response.get('is_valid_format', 'N/A')}, "
                    f"Deliverable: {response.get('is_deliverable', 'N/A')}"
                )
            elif api_type == "EXCHANGE_RATES":
                return f"AbstractAPI (Taux de change): Base: {response.get('base', 'N/A')}, Taux (USD): {response.get('exchange_rates', {}).get('USD', 'N/A')}"
            elif api_type == "HOLIDAYS":
                holidays = [h.get('name', 'N/A') for h in response if h.get('name')]
                return f"AbstractAPI (Jours fériés {params.get('country', 'US')} {params.get('year')}): {', '.join(holidays[:5])}..." if holidays else "Aucun jour férié trouvé."
            return f"AbstractAPI ({api_type}): Réponse brute: {response}"
        return f"AbstractAPI ({api_type}): Erreur: {response.get('message', 'Inconnu')}" if response else "AbstractAPI: Réponse vide ou erreur interne."

class GoogleCustomSearchClient(APIClient):
    def __init__(self):
        super().__init__("GOOGLE_CUSTOM_SEARCH", endpoint_health_manager)

    async def query(self, query_text: str) -> str:
        """Effectue une recherche personnalisée Google via l'API Custom Search."""
        params = {"q": query_text}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            items = response.get("items", [])
            if items:
                output = "Google Custom Search:\n"
                for item in items[:3]:
                    output += f"- {item.get('title', 'N/A')}: {item.get('snippet', 'N/A')} {neutralize_urls(item.get('link', ''))}\n"
                return output
            return "Google Custom Search: Aucun résultat trouvé."
        return f"Google Custom Search: Erreur: {response.get('message', 'Inconnu')}" if response else "Google Custom Search: Réponse vide ou erreur interne."

class RandommerClient(APIClient):
    def __init__(self):
        super().__init__("RANDOMMER", endpoint_health_manager)

    async def query(self, country_code: str = "US", quantity: int = 1) -> str:
        """Génère des numéros de téléphone aléatoires via Randommer.io."""
        params = {"CountryCode": country_code, "Quantity": quantity}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            if isinstance(response, list) and response:
                return f"Randommer (Numéros de téléphone): {', '.join(response)}"
            return f"Randommer: {response}"
        return f"Randommer: Erreur: {response.get('message', 'Inconnu')}" if response else "Randommer: Réponse vide ou erreur interne."

class TomorrowIOClient(APIClient):
    def __init__(self):
        super().__init__("TOMORROW.IO", endpoint_health_manager)

    async def query(self, location: str, fields: Optional[List[str]] = None) -> str:
        """Récupère les prévisions météorologiques via Tomorrow.io."""
        if fields is None:
            fields = ["temperature", "humidity", "windSpeed"]
        payload = {"location": location, "fields": fields, "units": "metric", "timesteps": ["1h"]}
        response = await self._make_request(json_data=payload)
        if response and not response.get("error"):
            data = response.get("data", {}).get("timelines", [{}])[0].get("intervals", [{}])[0].get("values", {})
            if data:
                output = f"Météo (Tomorrow.io) à {location}:\n"
                for field in fields:
                    output += f"- {field.capitalize()}: {data.get(field, 'N/A')}\n"
                return output
            return "Tomorrow.io: Données météo non trouvées."
        return f"Tomorrow.io: Erreur: {response.get('message', 'Inconnu')}" if response else "Tomorrow.io: Réponse vide ou erreur interne."

class OpenWeatherMapClient(APIClient):
    def __init__(self):
        super().__init__("OPENWEATHERMAP", endpoint_health_manager)

    async def query(self, location: str) -> str:
        """Récupère les conditions météorologiques actuelles via OpenWeatherMap."""
        params = {"q": location}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            main_data = response.get("main", {})
            weather_desc = response.get("weather", [{}])[0].get("description", "N/A")
            if main_data:
                temp_kelvin = main_data.get('temp', 'N/A')
                feels_like_kelvin = main_data.get('feels_like', 'N/A')
                
                temp_celsius = f"{temp_kelvin - 273.15:.2f}" if isinstance(temp_kelvin, (int, float)) else "N/A"
                feels_like_celsius = f"{feels_like_kelvin - 273.15:.2f}" if isinstance(feels_like_kelvin, (int, float)) else "N/A"

                return (
                    f"Météo (OpenWeatherMap) à {location}:\n"
                    f"Température: {temp_celsius}°C, "
                    f"Ressenti: {feels_like_celsius}°C, "
                    f"Humidité: {main_data.get('humidity', 'N/A')}%, "
                    f"Conditions: {weather_desc}"
                )
            return "OpenWeatherMap: Données météo non trouvées."
        return f"OpenWeatherMap: Erreur: {response.get('message', 'Inconnu')}" if response else "OpenWeatherMap: Réponse vide ou erreur interne."

class MockarooClient(APIClient):
    def __init__(self):
        super().__init__("MOCKAROO", endpoint_health_manager)

    async def query(self, count: int = 1, fields_json: Optional[str] = None) -> str:
        """Génère des données de test via Mockaroo."""
        params = {"count": count}
        if fields_json:
            params["fields"] = fields_json
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            return f"Mockaroo (Génération de données):\n{json.dumps(response, indent=2)}"
        return f"Mockaroo: Erreur: {response.get('message', 'Inconnu')}" if response else "Mockaroo: Réponse vide ou erreur interne."

class OpenPageRankClient(APIClient):
    def __init__(self):
        super().__init__("OPENPAGERANK", endpoint_health_manager)

    async def query(self, domains: List[str]) -> str:
        """Récupère le PageRank de domaines via OpenPageRank."""
        params = {"domains[]": domains}
        response = await self._make_request(params=params)
        if response and not response.get("error"):
            results = response.get("response", [])
            if results:
                output = "OpenPageRank (Classement de domaine):\n"
                for res in results:
                    output += f"- Domaine: {res.get('domain', 'N/A')}, PageRank: {res.get('page_rank', 'N/A')}\n"
                return output
            return "OpenPageRank: Aucun résultat trouvé."
        return f"OpenPageRank: Erreur: {response.get('message', 'Inconnu')}" if response else "OpenPageRank: Réponse vide ou erreur interne."

class RapidAPIClient(APIClient):
    def __init__(self):
        super().__init__("RAPIDAPI", endpoint_health_manager)

    async def query(self, api_name: str, **kwargs) -> str:
        """
        Interroge diverses APIs disponibles via RapidAPI (blagues, taux de change, faits aléatoires).
        `api_name` spécifie l'API RapidAPI à utiliser.
        """
        selected_endpoint_config = None
        for config in API_CONFIG.get(self.name, []):
            if api_name.lower() in config["endpoint_name"].lower():
                selected_endpoint_config = config
                break
        
        if not selected_endpoint_config:
            return f"RapidAPI: Endpoint pour '{api_name}' non trouvé ou non configuré."

        url = selected_endpoint_config["url"]
        method = selected_endpoint_config["method"]
        
        request_params = selected_endpoint_config.get("fixed_params", {}).copy()
        request_headers = selected_endpoint_config.get("fixed_headers", {}).copy()
        request_json_data = selected_endpoint_config.get("fixed_json", {}).copy()

        if method == "GET":
            request_params.update(kwargs)
        elif method == "POST":
            request_json_data.update(kwargs)

        headers = {
            selected_endpoint_config["key_field"]: selected_endpoint_config["key"],
            "X-RapidAPI-Host": selected_endpoint_config["fixed_headers"].get("X-RapidAPI-Host")
        }
        
        response = await self._make_request(
            params=request_params,
            headers=headers,
            json_data=request_json_data,
            url=url,
            method=method,
            timeout=selected_endpoint_config.get("timeout")
        )

        if response and not response.get("error"):
            if api_name.lower() == "programming joke":
                return f"RapidAPI (Blague de Programmation): {response.get('setup', '')} - {response.get('punchline', '')}"
            elif api_name.lower() == "currency list quotes":
                return f"RapidAPI (Devises): {json.dumps(response, indent=2)}"
            elif api_name.lower() == "random fact":
                return f"RapidAPI (Fait Aléatoire): {response.get('text', 'N/A')}"
            return f"RapidAPI ({api_name}): {json.dumps(response, indent=2)}"
        return f"RapidAPI ({api_name}): Erreur: {response.get('message', 'Inconnu')}" if response else "RapidAPI: Réponse vide ou erreur interne."

# Liste de tous les clients API instanciables
ALL_API_CLIENTS = [
    GeminiAPIClient(),
    OCRApiClient(),
    DeepSeekClient(),
    SerperClient(),
    WolframAlphaClient(),
    TavilyClient(),
    ApiFlashClient(),
    CrawlbaseClient(),
    DetectLanguageClient(),
    GuardianClient(),
    IP2LocationClient(),
    ShodanClient(),
    WeatherAPIClient(),
    CloudmersiveClient(),
    GreyNoiseClient(),
    PulsediveClient(),
    StormGlassClient(),
    LoginRadiusClient(),
    JsonbinClient(),
    HuggingFaceClient(),
    TwilioClient(),
    AbstractAPIClient(),
    GoogleCustomSearchClient(),
    RandommerClient(),
    TomorrowIOClient(),
    OpenWeatherMapClient(),
    MockarooClient(),
    OpenPageRankClient(),
    RapidAPIClient()
]

import asyncio
import json
import re
import base64
from typing import Dict, Any, List, Optional, Union

# Import des clients API
from api_clients import (
    GeminiAPIClient, OCRApiClient, DeepSeekClient, SerperClient,
    WolframAlphaClient, TavilyClient, ApiFlashClient, CrawlbaseClient,
    DetectLanguageClient, GuardianClient, IP2LocationClient, ShodanClient,
    WeatherAPIClient, CloudmersiveClient, GreyNoiseClient, PulsediveClient,
    StormGlassClient, LoginRadiusClient, JsonbinClient, HuggingFaceClient,
    TwilioClient, AbstractAPIClient, GoogleCustomSearchClient,
    RandommerClient, TomorrowIOClient, OpenWeatherMapClient, MockarooClient,
    OpenPageRankClient, RapidAPIClient
)

# Import des fonctions utilitaires
from utils import log_message, neutralize_urls, find_tool_by_name
from config import TOOL_CONFIG

# Instanciation des clients API
gemini_client = GeminiAPIClient()
ocr_client = OCRApiClient()
deepseek_client = DeepSeekClient()
serper_client = SerperClient()
wolfram_alpha_client = WolframAlphaClient()
tavily_client = TavilyClient()
apiflash_client = ApiFlashClient()
crawlbase_client = CrawlbaseClient()
detect_language_client = DetectLanguageClient()
guardian_client = GuardianClient()
ip2location_client = IP2LocationClient()
shodan_client = ShodanClient()
weather_api_client = WeatherAPIClient()
cloudmersive_client = CloudmersiveClient()
greynoise_client = GreyNoiseClient()
pulsedive_client = PulsediveClient()
stormglass_client = StormGlassClient()
loginradius_client = LoginRadiusClient()
jsonbin_client = JsonbinClient()
huggingface_client = HuggingFaceClient()
twilio_client = TwilioClient()
abstractapi_client = AbstractAPIClient()
google_custom_search_client = GoogleCustomSearchClient()
randommer_client = RandommerClient()
tomorrow_io_client = TomorrowIOClient()
openweathermap_client = OpenWeatherMapClient()
mockaroo_client = MockarooClient()
openpagerank_client = OpenPageRankClient()
rapidapi_client = RapidAPIClient()

async def execute_tool(tool_name: str, **kwargs) -> str:
    """
    Exécute un outil spécifique en fonction de son nom et des arguments fournis.
    C'est le point d'entrée principal pour l'exécution de toutes les fonctions d'outils.
    """
    log_message(f"Exécution de l'outil: {tool_name} avec kwargs: {kwargs}")
    tool_config = find_tool_by_name(tool_name)

    if not tool_config:
        log_message(f"Outil non trouvé: {tool_name}", level="error")
        return f"Erreur: Outil '{tool_name}' non trouvé ou non configuré."

    try:
        if tool_name == "google_search":
            return await google_search_tool(kwargs.get("queries"))
        elif tool_name == "media_control":
            action = kwargs.get("action")
            if action == "like":
                return await media_control_like_tool()
            elif action == "dislike":
                return await media_control_dislike_tool()
            elif action == "next":
                return await media_control_next_tool()
            elif action == "previous":
                return await media_control_previous_tool()
            elif action == "pause":
                return await media_control_pause_tool()
            elif action == "resume":
                return await media_control_resume_tool()
            elif action == "stop":
                return await media_control_stop_tool()
            elif action == "replay":
                return await media_control_replay_tool()
            elif action == "seek_absolute":
                return await media_control_seek_absolute_tool(kwargs.get("position"))
            elif action == "seek_relative":
                return await media_control_seek_relative_tool(kwargs.get("offset"))
            else:
                return f"Action non supportée pour media_control: {action}"
        elif tool_name == "clock":
            action = kwargs.get("action")
            if action == "create_alarm":
                return await clock_create_alarm_tool(
                    duration=kwargs.get("duration"),
                    time=kwargs.get("time"),
                    date=kwargs.get("date"),
                    label=kwargs.get("label"),
                    recurrence=kwargs.get("recurrence")
                )
            elif action == "create_timer":
                return await clock_create_timer_tool(
                    duration=kwargs.get("duration"),
                    time=kwargs.get("time"),
                    label=kwargs.get("label")
                )
            elif action == "show_matching_alarms":
                return await clock_show_matching_alarms_tool(
                    query=kwargs.get("query"),
                    alarm_type=kwargs.get("alarm_type"),
                    alarm_ids=kwargs.get("alarm_ids"),
                    date=kwargs.get("date"),
                    start_date=kwargs.get("start_date"),
                    end_date=kwargs.get("end_date")
                )
            elif action == "show_matching_timers":
                return await clock_show_matching_timers_tool(
                    query=kwargs.get("query"),
                    timer_type=kwargs.get("timer_type"),
                    timer_ids=kwargs.get("timer_ids")
                )
            elif action == "modify_alarm_v2":
                return await clock_modify_alarm_v2_tool(
                    alarm_filters=kwargs.get("alarm_filters"),
                    alarm_modifications=kwargs.get("alarm_modifications")
                )
            elif action == "modify_timer_v2":
                return await clock_modify_timer_v2_tool(
                    timer_filters=kwargs.get("timer_filters"),
                    timer_modifications=kwargs.get("timer_modifications")
                )
            elif action == "snooze":
                return await clock_snooze_tool()
            else:
                return f"Action non supportée pour clock: {action}"
        elif tool_name == "ocr_space":
            return await ocr_space_tool(kwargs.get("image_base64"))
        elif tool_name == "deepseek_chat":
            return await deepseek_chat_tool(kwargs.get("prompt"), kwargs.get("model"))
        elif tool_name == "serper_dev":
            return await serper_dev_tool(kwargs.get("query_text"))
        elif tool_name == "wolfram_alpha":
            return await wolfram_alpha_tool(kwargs.get("input_text"))
        elif tool_name == "tavily_search":
            return await tavily_search_tool(kwargs.get("query_text"), kwargs.get("max_results"))
        elif tool_name == "apiflash_screenshot":
            return await apiflash_screenshot_tool(kwargs.get("url"))
        elif tool_name == "crawlbase_scraper":
            return await crawlbase_scraper_tool(kwargs.get("url"), kwargs.get("use_js"))
        elif tool_name == "detect_language":
            return await detect_language_tool(kwargs.get("text"))
        elif tool_name == "guardian_news":
            return await guardian_news_tool(kwargs.get("query_text"))
        elif tool_name == "ip2location":
            return await ip2location_tool(kwargs.get("ip_address"))
        elif tool_name == "shodan":
            return await shodan_tool(kwargs.get("query_text"))
        elif tool_name == "weather_api":
            return await weather_api_tool(kwargs.get("location"))
        elif tool_name == "cloudmersive_domain":
            return await cloudmersive_domain_tool(kwargs.get("domain"))
        elif tool_name == "greynoise":
            return await greynoise_tool(kwargs.get("ip_address"))
        elif tool_name == "pulsedive":
            return await pulsedive_tool(kwargs.get("indicator"), kwargs.get("type"))
        elif tool_name == "stormglass":
            return await stormglass_tool(kwargs.get("lat"), kwargs.get("lng"), kwargs.get("params"))
        elif tool_name == "loginradius_ping":
            return await loginradius_ping_tool()
        elif tool_name == "jsonbin_io":
            return await jsonbin_io_tool(kwargs.get("data"), kwargs.get("private"), kwargs.get("bin_id"))
        elif tool_name == "huggingface_inference":
            return await huggingface_inference_tool(kwargs.get("model_name"), kwargs.get("input_text"))
        elif tool_name == "twilio_balance":
            return await twilio_balance_tool()
        elif tool_name == "abstractapi":
            return await abstractapi_tool(kwargs.get("input_value"), kwargs.get("api_type"))
        elif tool_name == "google_custom_search":
            return await google_custom_search_tool(kwargs.get("query_text"))
        elif tool_name == "randommer_phone":
            return await randommer_phone_tool(kwargs.get("country_code"), kwargs.get("quantity"))
        elif tool_name == "tomorrow_io_weather":
            return await tomorrow_io_weather_tool(kwargs.get("location"), kwargs.get("fields"))
        elif tool_name == "openweathermap_weather":
            return await openweathermap_weather_tool(kwargs.get("location"))
        elif tool_name == "mockaroo_data":
            return await mockaroo_data_tool(kwargs.get("count"), kwargs.get("fields_json"))
        elif tool_name == "openpagerank":
            return await openpagerank_tool(kwargs.get("domains"))
        elif tool_name == "rapidapi":
            return await rapidapi_tool(kwargs.get("api_name"), **kwargs.get("api_kwargs", {}))
        else:
            log_message(f"Aucun gestionnaire d'outil défini pour: {tool_name}", level="error")
            return f"Erreur: Aucun gestionnaire d'outil défini pour '{tool_name}'."
    except Exception as e:
        log_message(f"Erreur lors de l'exécution de l'outil {tool_name}: {e}", level="error")
        return f"Erreur lors de l'exécution de l'outil {tool_name}: {e}"

# --- Fonctions d'outils spécifiques (wrappers autour des clients API) ---

async def google_search_tool(queries: List[str]) -> str:
    """Effectue une recherche Google."""
    results = []
    for query in queries:
        log_message(f"Recherche Google pour: {query}")
        # Ici, nous utilisons un client générique pour Google Search
        # car il n'y a pas de client spécifique 'google_search' dans api_clients.py
        # Il faudrait soit créer un GoogleSearchClient, soit utiliser un client existant
        # comme SerperClient ou TavilyClient pour simuler la recherche.
        # Pour l'exemple, nous allons simuler une réponse ou utiliser un client de recherche existant.
        # Si 'google_search' est censé utiliser Serper ou Tavily, il faut le mapper ici.
        # Supposons que 'google_search' est un alias pour 'serper_dev' pour cet exemple.
        response = await serper_client.query(query)
        results.append(f"Résultat pour '{query}': {response}")
    return "\n".join(results)

async def media_control_like_tool() -> str:
    """Aime le média en cours de lecture."""
    # Simule l'appel à l'API media_control.like()
    # Dans un vrai scénario, cela appellerait une API de contrôle média sur l'appareil.
    log_message("Action media_control.like() simulée.")
    return "Média actuel aimé."

async def media_control_dislike_tool() -> str:
    """N'aime pas le média en cours de lecture."""
    log_message("Action media_control.dislike() simulée.")
    return "Média actuel non aimé."

async def media_control_next_tool() -> str:
    """Passe à l'élément multimédia suivant."""
    log_message("Action media_control.next() simulée.")
    return "Passage au média suivant."

async def media_control_previous_tool() -> str:
    """Passe à l'élément multimédia précédent."""
    log_message("Action media_control.previous() simulée.")
    return "Passage au média précédent."

async def media_control_pause_tool() -> str:
    """Met en pause le média en cours de lecture."""
    log_message("Action media_control.pause() simulée.")
    return "Média actuel mis en pause."

async def media_control_resume_tool() -> str:
    """Reprend la lecture du média en pause."""
    log_message("Action media_control.resume() simulée.")
    return "Lecture du média reprise."

async def media_control_stop_tool() -> str:
    """Arrête le média en cours de lecture."""
    log_message("Action media_control.stop() simulée.")
    return "Média actuel arrêté."

async def media_control_replay_tool() -> str:
    """Rejoue le média actuel depuis le début."""
    log_message("Action media_control.replay() simulée.")
    return "Média actuel rejoué."

async def media_control_seek_absolute_tool(position: int) -> str:
    """Saute à une position absolue dans le média."""
    log_message(f"Action media_control.seek_absolute({position}) simulée.")
    return f"Média avancé à la position {position} secondes."

async def media_control_seek_relative_tool(offset: int) -> str:
    """Ajuste la lecture du média par une durée relative."""
    log_message(f"Action media_control.seek_relative({offset}) simulée.")
    return f"Média avancé de {offset} secondes."

async def clock_create_alarm_tool(duration: Optional[str] = None, time: Optional[str] = None, date: Optional[str] = None, label: Optional[str] = None, recurrence: Optional[List[str]] = None) -> str:
    """Crée une alarme."""
    # Simule l'appel à l'API clock.create_alarm()
    log_message(f"Action clock.create_alarm() simulée avec durée={duration}, heure={time}, date={date}, label={label}, récurrence={recurrence}.")
    return f"Alarme créée pour {time if time else duration}."

async def clock_create_timer_tool(duration: Optional[str] = None, time: Optional[str] = None, label: Optional[str] = None) -> str:
    """Crée un minuteur."""
    # Simule l'appel à l'API clock.create_timer()
    log_message(f"Action clock.create_timer() simulée avec durée={duration}, heure={time}, label={label}.")
    return f"Minuteur créé pour {time if time else duration}."

async def clock_show_matching_alarms_tool(query: Optional[str] = None, alarm_type: Optional[str] = None, alarm_ids: Optional[List[str]] = None, date: Optional[str] = None, start_date: Optional[str] = None, end_date: Optional[str] = None) -> str:
    """Affiche les alarmes correspondantes."""
    # Simule l'appel à l'API clock.show_matching_alarms()
    log_message(f"Action clock.show_matching_alarms() simulée avec query={query}, type={alarm_type}, ids={alarm_ids}, date={date}, start_date={start_date}, end_date={end_date}.")
    return "Affichage des alarmes correspondantes (simulé)."

async def clock_show_matching_timers_tool(query: Optional[str] = None, timer_type: Optional[str] = None, timer_ids: Optional[List[str]] = None) -> str:
    """Affiche les minuteurs correspondants."""
    # Simule l'appel à l'API clock.show_matching_timers()
    log_message(f"Action clock.show_matching_timers() simulée avec query={query}, type={timer_type}, ids={timer_ids}.")
    return "Affichage des minuteurs correspondants (simulé)."

async def clock_modify_alarm_v2_tool(alarm_filters: Dict[str, Any], alarm_modifications: Dict[str, Any]) -> str:
    """Modifie une alarme."""
    # Simule l'appel à l'API clock.modify_alarm_v2()
    log_message(f"Action clock.modify_alarm_v2() simulée avec filtres={alarm_filters}, modifications={alarm_modifications}.")
    return "Alarme modifiée (simulé)."

async def clock_modify_timer_v2_tool(timer_filters: Dict[str, Any], timer_modifications: Dict[str, Any]) -> str:
    """Modifie un minuteur."""
    # Simule l'appel à l'API clock.modify_timer_v2()
    log_message(f"Action clock.modify_timer_v2() simulée avec filtres={timer_filters}, modifications={timer_modifications}.")
    return "Minuteur modifié (simulé)."

async def clock_snooze_tool() -> str:
    """Met en veille une alarme."""
    # Simule l'appel à l'API clock.snooze()
    log_message("Action clock.snooze() simulée.")
    return "Alarme mise en veille."

async def ocr_space_tool(image_base64: str) -> str:
    """Extrait le texte d'une image via OCR.space."""
    return await ocr_client.query(image_base64)

async def deepseek_chat_tool(prompt: Union[str, List[Dict]], model: str = "deepseek-chat") -> str:
    """Interroge DeepSeek pour des conversations ou complétions."""
    return await deepseek_client.query(prompt, model)

async def serper_dev_tool(query_text: str) -> str:
    """Effectue une recherche web via Serper."""
    return await serper_client.query(query_text)

async def wolfram_alpha_tool(input_text: str) -> str:
    """Interroge WolframAlpha pour des calculs ou des faits."""
    return await wolfram_alpha_client.query(input_text)

async def tavily_search_tool(query_text: str, max_results: int = 3) -> str:
    """Effectue une recherche web avancée via Tavily."""
    return await tavily_client.query(query_text, max_results)

async def apiflash_screenshot_tool(url: str) -> str:
    """Capture une capture d'écran d'une URL via ApiFlash."""
    return await apiflash_client.query(url)

async def crawlbase_scraper_tool(url: str, use_js: bool = False) -> str:
    """Scrape le contenu HTML ou JavaScript d'une URL via Crawlbase."""
    return await crawlbase_client.query(url, use_js)

async def detect_language_tool(text: str) -> str:
    """Détecte la langue d'un texte via DetectLanguage API."""
    return await detect_language_client.query(text)

async def guardian_news_tool(query_text: str) -> str:
    """Recherche des articles de presse via l'API The Guardian."""
    return await guardian_client.query(query_text)

async def ip2location_tool(ip_address: str) -> str:
    """Géolocalise une adresse IP via IP2Location API."""
    return await ip2location_client.query(ip_address)

async def shodan_tool(query_text: str = "") -> str:
    """Interroge Shodan pour des informations sur un hôte IP ou des informations sur la clé API."""
    return await shodan_client.query(query_text)

async def weather_api_tool(location: str) -> str:
    """Récupère les conditions météorologiques actuelles pour une localisation via WeatherAPI."""
    return await weather_api_client.query(location)

async def cloudmersive_domain_tool(domain: str) -> str:
    """Vérifie la validité et le type d'un domaine via Cloudmersive API."""
    return await cloudmersive_client.query(domain)

async def greynoise_tool(ip_address: str) -> str:
    """Analyse une adresse IP pour détecter des activités 'bruit' (malveillantes) via GreyNoise."""
    return await greynoise_client.query(ip_address)

async def pulsedive_tool(indicator: str, type: str = "auto") -> str:
    """Analyse un indicateur de menace (IP, domaine, URL) via Pulsedive."""
    return await pulsedive_client.query(indicator, type)

async def stormglass_tool(lat: float, lng: float, params: str = "airTemperature,waveHeight") -> str:
    """Récupère les données météorologiques maritimes pour une coordonnée via StormGlass."""
    return await stormglass_client.query(lat, lng, params)

async def loginradius_ping_tool() -> str:
    """Effectue un simple ping à l'API LoginRadius pour vérifier sa disponibilité."""
    return await loginradius_client.query()

async def jsonbin_io_tool(data: Optional[Dict[str, Any]] = None, private: bool = True, bin_id: Optional[str] = None) -> str:
    """Crée un nouveau 'bin' JSON ou accède à un bin existant via Jsonbin.io."""
    return await jsonbin_client.query(data, private, bin_id)

async def huggingface_inference_tool(model_name: str = "distilbert-base-uncased-finetuned-sst-2-english", input_text: str = "Hello world") -> str:
    """Effectue une inférence sur un modèle HuggingFace."""
    return await huggingface_client.query(model_name, input_text)

async def twilio_balance_tool() -> str:
    """Récupère le solde du compte Twilio."""
    return await twilio_client.query()

async def abstractapi_tool(input_value: str, api_type: str) -> str:
    """Interroge diverses APIs d'AbstractAPI."""
    return await abstractapi_client.query(input_value, api_type)

async def google_custom_search_tool(query_text: str) -> str:
    """Effectue une recherche personnalisée Google."""
    return await google_custom_search_client.query(query_text)

async def randommer_phone_tool(country_code: str = "US", quantity: int = 1) -> str:
    """Génère des numéros de téléphone aléatoires via Randommer.io."""
    return await randommer_client.query(country_code, quantity)

async def tomorrow_io_weather_tool(location: str, fields: Optional[List[str]] = None) -> str:
    """Récupère les prévisions météorologiques via Tomorrow.io."""
    return await tomorrow_io_client.query(location, fields)

async def openweathermap_weather_tool(location: str) -> str:
    """Récupère les conditions météorologiques actuelles via OpenWeatherMap."""
    return await openweathermap_client.query(location)

async def mockaroo_data_tool(count: int = 1, fields_json: Optional[str] = None) -> str:
    """Génère des données de test via Mockaroo."""
    return await mockaroo_client.query(count, fields_json)

async def openpagerank_tool(domains: List[str]) -> str:
    """Récupère le PageRank de domaines via OpenPageRank."""
    return await openpagerank_client.query(domains)

async def rapidapi_tool(api_name: str, **api_kwargs) -> str:
    """Interroge diverses APIs disponibles via RapidAPI."""
    return await rapidapi_client.query(api_name, **api_kwargs)

import asyncio
import json
import os
import re
import base64
import mimetypes
import datetime
from typing import Dict, Any, List, Optional, Union, Tuple

# Import des modules et fonctions
from config import (
    API_CONFIG, ENDPOINT_HEALTH_FILE, MAX_IMAGE_SIZE,
    GEMINI_TEMPERATURE, GEMINI_TOP_P, GEMINI_TOP_K, GEMINI_MAX_OUTPUT_TOKENS,
    GEMINI_SAFETY_SETTINGS, TOOL_CONFIG
)
from utils import (
    load_json, save_json, get_current_time, format_datetime, log_message,
    neutralize_urls, find_tool_by_name, get_mime_type_from_base64
)
from api_clients import (
    GeminiAPIClient, OCRApiClient, DeepSeekClient, SerperClient,
    WolframAlphaClient, TavilyClient, ApiFlashClient, CrawlbaseClient,
    DetectLanguageClient, GuardianClient, IP2LocationClient, ShodanClient,
    WeatherAPIClient, CloudmersiveClient, GreyNoiseClient, PulsediveClient,
    StormGlassClient, LoginRadiusClient, JsonbinClient, HuggingFaceClient,
    TwilioClient, AbstractAPIClient, GoogleCustomSearchClient,
    RandommerClient, TomorrowIOClient, OpenWeatherMapClient, MockarooClient,
    OpenPageRankClient, RapidAPIClient,
    EndpointHealthManager, set_endpoint_health_manager_global
)
from tools import execute_tool # Import de la fonction execute_tool

# Initialisation du gestionnaire de santé des endpoints
endpoint_health_manager = EndpointHealthManager()
set_endpoint_health_manager_global(endpoint_health_manager)

# Instanciation des clients API
gemini_client = GeminiAPIClient()
ocr_client = OCRApiClient()
deepseek_client = DeepSeekClient()
serper_client = SerperClient()
wolfram_alpha_client = WolframAlphaClient()
tavily_client = TavilyClient()
apiflash_client = ApiFlashClient()
crawlbase_client = CrawlbaseClient()
detect_language_client = DetectLanguageClient()
guardian_client = GuardianClient()
ip2location_client = IP2locationClient()
shodan_client = ShodanClient()
weather_api_client = WeatherAPIClient()
cloudmersive_client = CloudmersiveClient()
greynoise_client = GreyNoiseClient()
pulsedive_client = PulsediveClient()
stormglass_client = StormGlassClient()
loginradius_client = LoginRadiusClient()
jsonbin_client = JsonbinClient()
huggingface_client = HuggingFaceClient()
twilio_client = TwilioClient()
abstractapi_client = AbstractAPIClient()
google_custom_search_client = GoogleCustomSearchClient()
randommer_client = RandommerClient()
tomorrow_io_client = TomorrowIOClient()
openweathermap_client = OpenWeatherMapClient()
mockaroo_client = MockarooClient()
openpagerank_client = OpenPageRankClient()
rapidapi_client = RapidAPIClient()


# Définition des outils disponibles pour Gemini
def get_gemini_tools() -> List[Dict]:
    """
    Construit la liste des outils disponibles pour l'API Gemini
    à partir de la configuration TOOL_CONFIG.
    """
    tools = []
    for tool_name, tool_info in TOOL_CONFIG.items():
        if tool_info.get("enabled", False):
            function_declaration = {
                "name": tool_name,
                "description": tool_info.get("description", ""),
                "parameters": {
                    "type": "OBJECT",
                    "properties": {},
                    "required": []
                }
            }
            for param_name, param_info in tool_info.get("parameters", {}).items():
                function_declaration["parameters"]["properties"][param_name] = {
                    "type": param_info.get("type", "STRING"),
                    "description": param_info.get("description", "")
                }
                if param_info.get("required", False):
                    function_declaration["parameters"]["required"].append(param_name)
            
            # Ajout de la gestion des actions pour les outils "clock" et "media_control"
            if tool_name in ["clock", "media_control"]:
                function_declaration["parameters"]["properties"]["action"] = {
                    "type": "STRING",
                    "description": f"L'action à effectuer pour l'outil {tool_name}."
                }
                function_declaration["parameters"]["required"].append("action")

                # Ajout des sous-paramètres spécifiques à chaque action
                for action_name, action_info in tool_info.get("actions", {}).items():
                    # Crée un objet pour les paramètres spécifiques à cette action
                    action_params_props = {}
                    action_required_params = []
                    for param_name, param_info in action_info.get("parameters", {}).items():
                        action_params_props[param_name] = {
                            "type": param_info.get("type", "STRING"),
                            "description": param_info.get("description", "")
                        }
                        if param_info.get("required", False):
                            action_required_params.append(param_name)
                    
                    # Ajoute ces paramètres comme une propriété conditionnelle ou imbriquée
                    # Gemini ne supporte pas directement les schémas conditionnels pour les outils.
                    # La meilleure approche est de lister tous les paramètres possibles et de laisser le modèle
                    # choisir ceux qui sont pertinents en fonction de l'action.
                    # Ou, pour une meilleure clarté, créer des fonctions distinctes pour chaque action si possible.
                    # Pour l'instant, on va juste ajouter les paramètres à la liste globale.
                    # C'est au modèle de comprendre quels paramètres sont pertinents pour quelle action.
                    function_declaration["parameters"]["properties"].update(action_params_props)
                    function_declaration["parameters"]["required"].extend(action_required_params)
                    
                    # Pour les filtres et modifications complexes (ex: clock.modify_alarm_v2)
                    if action_name in ["modify_alarm_v2", "modify_timer_v2"]:
                        if "alarm_filters" in action_info.get("parameters", {}):
                            function_declaration["parameters"]["properties"]["alarm_filters"] = {
                                "type": "OBJECT",
                                "description": "Filtres pour identifier les alarmes à modifier.",
                                "properties": action_info["parameters"]["alarm_filters"].get("properties", {}),
                                "required": action_info["parameters"]["alarm_filters"].get("required", [])
                            }
                        if "alarm_modifications" in action_info.get("parameters", {}):
                            function_declaration["parameters"]["properties"]["alarm_modifications"] = {
                                "type": "OBJECT",
                                "description": "Modifications à apporter aux alarmes.",
                                "properties": action_info["parameters"]["alarm_modifications"].get("properties", {}),
                                "required": action_info["parameters"]["alarm_modifications"].get("required", [])
                            }
                        if "timer_filters" in action_info.get("parameters", {}):
                            function_declaration["parameters"]["properties"]["timer_filters"] = {
                                "type": "OBJECT",
                                "description": "Filtres pour identifier les minuteurs à modifier.",
                                "properties": action_info["parameters"]["timer_filters"].get("properties", {}),
                                "required": action_info["parameters"]["timer_filters"].get("required", [])
                            }
                        if "timer_modifications" in action_info.get("parameters", {}):
                            function_declaration["parameters"]["properties"]["timer_modifications"] = {
                                "type": "OBJECT",
                                "description": "Modifications à apporter aux minuteurs.",
                                "properties": action_info["parameters"]["timer_modifications"].get("properties", {}),
                                "required": action_info["parameters"]["timer_modifications"].get("required", [])
                            }

            tools.append({"function_declarations": [function_declaration]})
    return tools

async def process_user_query(user_query: str, chat_history: List[Dict], image_data: Optional[str] = None) -> Tuple[str, List[Dict]]:
    """
    Traite la requête de l'utilisateur, interagit avec Gemini et exécute les outils si nécessaire.
    """
    log_message(f"Requête utilisateur: {user_query}")
    log_message(f"Historique du chat (avant): {chat_history}")

    # Initialiser l'historique du chat si vide
    if not chat_history:
        chat_history = []

    # Obtenir les outils disponibles
    gemini_tools = get_gemini_tools()
    log_message(f"Outils disponibles pour Gemini: {json.dumps(gemini_tools, indent=2)}")

    # Appel à Gemini
    gemini_response = await gemini_client.generate_content(
        prompt=user_query,
        chat_history=chat_history,
        image_data=image_data,
        tools=gemini_tools
    )

    if isinstance(gemini_response, str) and gemini_response.startswith("❌"):
        log_message(f"Erreur de Gemini: {gemini_response}", level="error")
        return gemini_response, chat_history

    if not gemini_response:
        log_message("Réponse vide de Gemini.", level="warning")
        return "Désolé, je n'ai pas pu obtenir de réponse de Gemini.", chat_history

    # Traiter la réponse de Gemini
    try:
        if "candidates" in gemini_response and gemini_response["candidates"]:
            candidate = gemini_response["candidates"][0]
            if "content" in candidate and "parts" in candidate["content"]:
                for part in candidate["content"]["parts"]:
                    if "text" in part:
                        # Si Gemini répond avec du texte, l'ajouter à l'historique et le retourner
                        chat_history.append({"role": "model", "parts": [{"text": part["text"]}]})
                        log_message(f"Réponse textuelle de Gemini: {part['text']}")
                        return part["text"], chat_history
                    elif "functionCall" in part:
                        # Si Gemini demande d'appeler une fonction (outil)
                        function_call = part["functionCall"]
                        tool_name = function_call["name"]
                        tool_args = function_call.get("args", {})
                        log_message(f"Gemini a demandé l'outil: {tool_name} avec args: {tool_args}")

                        # Exécuter l'outil
                        tool_output = await execute_tool(tool_name, **tool_args)
                        log_message(f"Sortie de l'outil {tool_name}: {tool_output}")

                        # Ajouter la requête de l'outil et sa sortie à l'historique du chat
                        chat_history.append({"role": "model", "parts": [{"functionCall": function_call}]})
                        chat_history.append({"role": "tool", "parts": [{"functionResponse": {"name": tool_name, "response": {"result": tool_output}}}]})

                        # Rappeler Gemini avec l'historique mis à jour pour obtenir la réponse finale
                        log_message("Rappel de Gemini après exécution de l'outil...")
                        final_gemini_response = await gemini_client.generate_content(
                            prompt=user_query, # On garde le prompt original pour le contexte
                            chat_history=chat_history,
                            image_data=image_data,
                            tools=gemini_tools
                        )

                        if isinstance(final_gemini_response, str) and final_gemini_response.startswith("❌"):
                            log_message(f"Erreur de Gemini après exécution de l'outil: {final_gemini_response}", level="error")
                            return final_gemini_response, chat_history
                        
                        if not final_gemini_response:
                            log_message("Réponse vide de Gemini après exécution de l'outil.", level="warning")
                            return "Désolé, je n'ai pas pu obtenir de réponse de Gemini après l'exécution de l'outil.", chat_history

                        if "candidates" in final_gemini_response and final_gemini_response["candidates"]:
                            final_candidate = final_gemini_response["candidates"][0]
                            if "content" in final_candidate and "parts" in final_candidate["content"]:
                                for final_part in final_candidate["content"]["parts"]:
                                    if "text" in final_part:
                                        chat_history.append({"role": "model", "parts": [{"text": final_part["text"]}]})
                                        log_message(f"Réponse finale de Gemini: {final_part['text']}")
                                        return final_part["text"], chat_history
                                    else:
                                        log_message(f"Partie de réponse finale inattendue de Gemini: {final_part}", level="warning")
                                        return "Désolé, je n'ai pas pu traiter la réponse finale de Gemini.", chat_history
                        log_message("Aucune réponse textuelle finale de Gemini après exécution de l'outil.", level="warning")
                        return "Désolé, je n'ai pas pu obtenir de réponse textuelle finale de Gemini après l'exécution de l'outil.", chat_history
            log_message("Aucune partie de contenu valide trouvée dans la réponse de Gemini.", level="warning")
            return "Désolé, je n'ai pas pu comprendre la réponse de Gemini.", chat_history
        log_message(f"Aucun candidat valide dans la réponse de Gemini: {gemini_response}", level="warning")
        return "Désolé, Gemini n'a pas fourni de réponse valide.", chat_history
    except Exception as e:
        log_message(f"Erreur lors du traitement de la réponse de Gemini: {e}", level="error")
        log_message(f"Traceback: {traceback.format_exc()}", level="error")
        return f"Une erreur interne est survenue lors du traitement de la réponse: {e}", chat_history

async def main():
    """Fonction principale pour exécuter le chatbot."""
    await endpoint_health_manager.init_manager()
    log_message("Démarrage du chatbot. Tapez 'quitter' pour arrêter.")

    # Lancer les checks de santé périodiques en arrière-plan
    async def periodic_health_checks():
        while True:
            for service_name in API_CONFIG.keys():
                await endpoint_health_manager.run_health_check_for_service(service_name)
            await asyncio.sleep(300) # Vérifier toutes les 5 minutes

    asyncio.create_task(periodic_health_checks())

    chat_history = []
    
    # Charger l'historique de chat précédent si disponible
    try:
        if os.path.exists("chat_history.json"):
            with open("chat_history.json", "r", encoding="utf-8") as f:
                loaded_history = json.load(f)
                # S'assurer que les rôles sont corrects pour Gemini
                for entry in loaded_history:
                    if entry.get("role") == "user" or entry.get("role") == "model":
                        chat_history.append(entry)
                    elif entry.get("role") == "tool":
                        # Gemini attend functionResponse dans "parts" pour les outils
                        if "functionCall" in entry.get("parts", [{}])[0]:
                            # C'est une requête d'outil, pas une réponse
                            chat_history.append(entry)
                        elif "functionResponse" in entry.get("parts", [{}])[0]:
                            chat_history.append(entry)
                        else:
                            log_message(f"Entrée d'historique d'outil inattendue: {entry}", level="warning")
                            # Tenter de convertir si c'est un format ancien
                            if "tool_code" in entry.get("parts", [{}])[0]:
                                tool_code_str = entry["parts"][0]["tool_code"]
                                # Extraire le nom de l'outil et la sortie
                                match = re.search(r"print\((\w+)\.([\w_]+)\((.*)\)\)", tool_code_str)
                                if match:
                                    tool_api_name = match.group(1)
                                    tool_method_name = match.group(2)
                                    # Pour l'historique, on a besoin du nom de l'outil tel que défini dans TOOL_CONFIG
                                    # Il faut une meilleure façon de mapper les méthodes API aux noms d'outils.
                                    # Pour l'instant, on va juste utiliser le nom de la méthode comme nom d'outil.
                                    tool_name_for_history = tool_method_name 
                                    
                                    # Simuler la réponse de l'outil
                                    tool_response_content = entry.get("parts", [{}])[1].get("text", "Réponse outil non spécifiée.")
                                    chat_history.append({
                                        "role": "tool",
                                        "parts": [{
                                            "functionResponse": {
                                                "name": tool_name_for_history,
                                                "response": {"result": tool_response_content}
                                            }
                                        }]
                                    })
                                else:
                                    log_message(f"Impossible de parser l'entrée tool_code: {tool_code_str}", level="warning")
                            else:
                                log_message(f"Entrée d'historique d'outil non reconnue: {entry}", level="warning")

                log_message("Historique du chat chargé avec succès.")
    except Exception as e:
        log_message(f"Erreur lors du chargement de l'historique du chat: {e}", level="error")
        chat_history = [] # Réinitialiser en cas d'erreur

    while True:
        user_input = input("Vous: ")
        if user_input.lower() == "quitter":
            break

        image_path = None
        image_data = None
        
        # Vérifier si l'utilisateur a fourni un chemin d'image
        image_match = re.search(r"\[image:(.+)\]", user_input)
        if image_match:
            image_path = image_match.group(1).strip()
            user_input = user_input.replace(image_match.group(0), "").strip() # Supprimer la balise image du prompt

            if os.path.exists(image_path):
                try:
                    with open(image_path, "rb") as image_file:
                        raw_image_data = image_file.read()
                        if len(raw_image_data) > MAX_IMAGE_SIZE:
                            log_message(f"L'image dépasse la taille maximale autorisée ({MAX_IMAGE_SIZE / (1024*1024):.2f} Mo).", level="warning")
                            print(f"⚠️ L'image est trop grande. Taille max: {MAX_IMAGE_SIZE / (1024*1024):.2f} Mo.")
                            image_data = None # Ne pas envoyer l'image si elle est trop grande
                        else:
                            base64_encoded_image = base64.b64encode(raw_image_data).decode('utf-8')
                            mime_type = get_mime_type_from_base64(base64_encoded_image)
                            if mime_type:
                                image_data = f"data:{mime_type};base64,{base64_encoded_image}"
                                log_message(f"Image chargée et encodée en base64: {image_path} (MIME: {mime_type})")
                            else:
                                log_message(f"Impossible de déterminer le type MIME de l'image: {image_path}", level="warning")
                                image_data = base64_encoded_image # Envoyer sans MIME si non détecté
                except Exception as e:
                    log_message(f"Erreur lors du chargement de l'image {image_path}: {e}", level="error")
                    print(f"❌ Erreur lors du chargement de l'image: {e}")
                    image_data = None
            else:
                log_message(f"Fichier image non trouvé: {image_path}", level="warning")
                print(f"❌ Erreur: Fichier image '{image_path}' non trouvé.")
                image_data = None

        # Ajouter la requête utilisateur à l'historique
        user_parts = [{"text": user_input}]
        if image_data:
            # Si l'image est incluse, elle sera ajoutée par generate_content
            pass
        chat_history.append({"role": "user", "parts": user_parts})

        response, chat_history = await process_user_query(user_input, chat_history, image_data)
        print(f"Bot: {response}")

        # Sauvegarder l'historique après chaque tour
        try:
            # Nettoyer l'historique pour la sauvegarde:
            # - Enlever les données d'image base64 (trop volumineux, non nécessaire pour la persistance)
            # - S'assurer que les objets functionCall/functionResponse sont bien formatés
            history_to_save = []
            for entry in chat_history:
                new_entry = entry.copy()
                if "parts" in new_entry:
                    new_parts = []
                    for part in new_entry["parts"]:
                        if "inlineData" in part:
                            # Ne pas sauvegarder les données d'image brutes
                            new_part = part.copy()
                            new_part["inlineData"] = {"mimeType": part["inlineData"]["mimeType"], "data": "[IMAGE_DATA_REMOVED_FOR_SAVE]"}
                            new_parts.append(new_part)
                        else:
                            new_parts.append(part)
                    new_entry["parts"] = new_parts
                history_to_save.append(new_entry)
            
            with open("chat_history.json", "w", encoding="utf-8") as f:
                json.dump(history_to_save, f, indent=2, ensure_ascii=False)
            log_message("Historique du chat sauvegardé.")
        except Exception as e:
            log_message(f"Erreur lors de la sauvegarde de l'historique du chat: {e}", level="error")

if __name__ == "__main__":
    import traceback
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        log_message("Chatbot arrêté par l'utilisateur.")
    except Exception as e:
        log_message(f"Une erreur inattendue est survenue: {e}", level="critical")
        log_message(f"Traceback: {traceback.format_exc()}", level="critical")


analyse ca en profondeur et tout les aspect possible tu a une autre analyse et des question qui arrive dans la suite oublie rien jai pas besoin de racapitulatif tu en fait un sait quil et pour toi ne fait rien de plus que une analyse complete 

nouveau script 
