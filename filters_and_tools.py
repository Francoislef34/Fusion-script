import re
import asyncio
import aiohttp
import logging
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime
import config
import utils
import api_clients

# Imports des constantes depuis config.py
from config import (
    FORBIDDEN_KEYWORDS, AUTHORIZED_USERS, BANNED_USERS,
    MAX_FILE_SIZE, MAX_IMAGE_SIZE, MESSAGES
)

# Imports depuis utils.py
from utils import (
    is_file_size_valid, sanitize_filename, format_file_size
)

# Variable globale pour l'instance OCR
ocr_api_client_instance = None # Sera assigné par main.py

def set_ocr_api_client_instance(instance):
    """Définit l'instance OCR globale"""
    global ocr_api_client_instance
    ocr_api_client_instance = instance

class ContentFilter:
    """Filtre de contenu pour la modération"""
    
    def __init__(self):
        self.forbidden_keywords = set(FORBIDDEN_KEYWORDS)
        self.spam_patterns = [
            r'(?i)(buy\s+now|limited\s+time|act\s+fast|click\s+here)',
            r'(?i)(free\s+offer|money\s+back|guaranteed)',
            r'(?i)(earn\s+money|work\s+from\s+home|get\s+rich)',
            r'(?i)(viagra|cialis|weight\s+loss)',
            r'(?i)(lottery|winner|prize|claim)'
        ]
        self.compiled_patterns = [re.compile(pattern) for pattern in self.spam_patterns]
    
    def check_message(self, message: str) -> Tuple[bool, str]:
        """Vérifie si un message est approprié"""
        message_lower = message.lower()
        
        # Vérifier les mots-clés interdits
        for keyword in self.forbidden_keywords:
            if keyword.lower() in message_lower:
                return False, f"Message contient un mot-clé interdit: {keyword}"
        
        # Vérifier les patterns de spam
        for pattern in self.compiled_patterns:
            if pattern.search(message):
                return False, "Message détecté comme spam"
        
        # Vérifier la longueur excessive
        if len(message) > 4000:
            return False, "Message trop long (limite: 4000 caractères)"
        
        return True, "OK"
    
    def check_user_authorization(self, user_id: int) -> bool:
        """Vérifie si un utilisateur est autorisé"""
        if AUTHORIZED_USERS and user_id not in AUTHORIZED_USERS:
            return False
        if user_id in BANNED_USERS:
            return False
        return True

class MessageProcessor:
    """Processeur de messages avec analyse et classification"""
    
    def __init__(self):
        self.command_patterns = {
            'help': r'^/help|^aide|^help',
            'search': r'^/search|^recherche|^cherche',
            'ocr': r'^/ocr|^texte|^extract',
            'quota': r'^/quota|^limite|^usage',
            'history': r'^/history|^historique',
            'clear': r'^/clear|^effacer|^reset',
            'admin': r'^/admin|^admin'
        }
        self.compiled_patterns = {k: re.compile(v, re.IGNORECASE) for k, v in self.command_patterns.items()}
    
    def classify_message(self, message: str) -> Dict[str, Any]:
        """Classifie un message selon son type"""
        classification = {
            'type': 'text',
            'command': None,
            'has_url': False,
            'has_image': False,
            'language': 'unknown',
            'sentiment': 'neutral'
        }
        
        # Détecter les commandes
        for command, pattern in self.compiled_patterns.items():
            if pattern.search(message):
                classification['command'] = command
                classification['type'] = 'command'
                break
        
        # Détecter les URLs
        url_pattern = r'https?://[^\s]+'
        if re.search(url_pattern, message):
            classification['has_url'] = True
        
        # Détecter la langue (simple détection)
        if re.search(r'[àâäéèêëïîôöùûüÿç]', message, re.IGNORECASE):
            classification['language'] = 'french'
        elif re.search(r'[a-z]', message, re.IGNORECASE):
            classification['language'] = 'english'
        
        return classification
    
    def extract_urls(self, message: str) -> List[str]:
        """Extrait les URLs d'un message"""
        url_pattern = r'https?://[^\s]+'
        return re.findall(url_pattern, message)
    
    def clean_message(self, message: str) -> str:
        """Nettoie un message"""
        # Supprimer les caractères de contrôle
        message = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', message)
        # Normaliser les espaces
        message = re.sub(r'\s+', ' ', message).strip()
        return message

class FileProcessor:
    """Processeur de fichiers (images, documents)"""
    
    def __init__(self):
        self.supported_image_formats = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'}
        self.supported_document_formats = {'.pdf', '.txt', '.doc', '.docx'}
        self.max_file_size = MAX_FILE_SIZE
        self.max_image_size = MAX_IMAGE_SIZE
    
    def is_supported_image(self, filename: str) -> bool:
        """Vérifie si le fichier est une image supportée"""
        return any(filename.lower().endswith(ext) for ext in self.supported_image_formats)
    
    def is_supported_document(self, filename: str) -> bool:
        """Vérifie si le fichier est un document supporté"""
        return any(filename.lower().endswith(ext) for ext in self.supported_document_formats)
    
    def validate_file(self, filename: str, file_size: int) -> Tuple[bool, str]:
        """Valide un fichier"""
        if not filename:
            return False, "Nom de fichier manquant"
        
        if file_size > self.max_file_size:
            return False, f"Fichier trop volumineux ({format_file_size(file_size)})"
        
        if self.is_supported_image(filename):
            if file_size > self.max_image_size:
                return False, f"Image trop volumineuse ({format_file_size(file_size)})"
        
        return True, "OK"
    
    async def process_image_for_ocr(self, image_path: str) -> Optional[str]:
        """Traite une image pour l'extraction de texte"""
        if not ocr_api_client_instance:
            logging.error("Instance OCR non disponible")
            return None
        
        try:
            text = await ocr_api_client_instance.extract_text_from_image(image_path)
            return text
        except Exception as e:
            logging.error(f"Erreur traitement OCR: {e}")
            return None

class WebTools:
    """Outils pour la manipulation web"""
    
    def __init__(self):
        self.session = None
    
    async def get_session(self) -> aiohttp.ClientSession:
        """Récupère ou crée une session HTTP"""
        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession()
        return self.session
    
    async def fetch_url_content(self, url: str) -> Optional[str]:
        """Récupère le contenu d'une URL"""
        try:
            session = await self.get_session()
            async with session.get(url, timeout=config.TIMEOUTS["file_download"]) as response:
                if response.status == 200:
                    content_type = response.headers.get('content-type', '')
                    if 'text' in content_type:
                        return await response.text()
                    else:
                        logging.warning(f"Contenu non textuel: {content_type}")
                        return None
                else:
                    logging.error(f"Erreur HTTP {response.status} pour {url}")
                    return None
        except Exception as e:
            logging.error(f"Erreur récupération URL {url}: {e}")
            return None
    
    async def download_file(self, url: str, save_path: str) -> bool:
        """Télécharge un fichier depuis une URL"""
        try:
            session = await self.get_session()
            async with session.get(url, timeout=config.TIMEOUTS["file_download"]) as response:
                if response.status == 200:
                    with open(save_path, 'wb') as f:
                        async for chunk in response.content.iter_chunked(8192):
                            f.write(chunk)
                    return True
                else:
                    logging.error(f"Erreur téléchargement {url}: {response.status}")
                    return False
        except Exception as e:
            logging.error(f"Erreur téléchargement fichier {url}: {e}")
            return False
    
    async def check_url_status(self, url: str) -> Dict[str, Any]:
        """Vérifie le statut d'une URL"""
        try:
            session = await self.get_session()
            async with session.head(url, timeout=10) as response:
                return {
                    'status': response.status,
                    'content_type': response.headers.get('content-type', ''),
                    'content_length': response.headers.get('content-length', ''),
                    'accessible': response.status < 400
                }
        except Exception as e:
            return {
                'status': 0,
                'error': str(e),
                'accessible': False
            }

class TextTools:
    """Outils de traitement de texte"""
    
    @staticmethod
    def summarize_text(text: str, max_length: int = 500) -> str:
        """Résume un texte"""
        if len(text) <= max_length:
            return text
        
        # Simple résumé par phrases
        sentences = re.split(r'[.!?]+', text)
        summary = ""
        
        for sentence in sentences:
            if len(summary + sentence) <= max_length:
                summary += sentence + ". "
            else:
                break
        
        return summary.strip()
    
    @staticmethod
    def extract_keywords(text: str, max_keywords: int = 10) -> List[str]:
        """Extrait les mots-clés d'un texte"""
        # Supprimer la ponctuation et convertir en minuscules
        text = re.sub(r'[^\w\s]', '', text.lower())
        words = text.split()
        
        # Filtrer les mots courts et les mots vides
        stop_words = {'le', 'la', 'les', 'un', 'une', 'des', 'et', 'ou', 'mais', 'de', 'du', 'a', 'au', 'avec', 'pour', 'dans', 'sur', 'par', 'sans', 'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}
        
        word_freq = {}
        for word in words:
            if len(word) > 2 and word not in stop_words:
                word_freq[word] = word_freq.get(word, 0) + 1
        
        # Trier par fréquence et retourner les plus fréquents
        sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        return [word for word, freq in sorted_words[:max_keywords]]

# Instances globales
content_filter = ContentFilter()
message_processor = MessageProcessor()
file_processor = FileProcessor()
web_tools = WebTools()
text_tools = TextTools()

async def cleanup_resources():
    """Nettoie les ressources"""
    if web_tools.session and not web_tools.session.closed:
        await web_tools.session.close()