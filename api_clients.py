import aiohttp
import asyncio
import json
import logging
from typing import Dict, Any, Optional, List
from datetime import datetime, timedelta
import config
import utils

# Variables globales
endpoint_health_manager = None
current_api_index = 0

class EndpointHealthManager:
    """Gestionnaire de santé des endpoints API"""
    
    def __init__(self):
        self.health_data = {}
        self.load_health_data()
    
    def load_health_data(self):
        """Charge les données de santé depuis le fichier"""
        try:
            with open(config.ENDPOINT_HEALTH_FILE, 'r') as f:
                self.health_data = json.load(f)
        except FileNotFoundError:
            self.health_data = {}
    
    def save_health_data(self):
        """Sauvegarde les données de santé"""
        try:
            with open(config.ENDPOINT_HEALTH_FILE, 'w') as f:
                json.dump(self.health_data, f, indent=2)
        except Exception as e:
            logging.error(f"Erreur sauvegarde santé endpoints: {e}")
    
    def record_success(self, endpoint: str):
        """Enregistre un succès pour un endpoint"""
        if endpoint not in self.health_data:
            self.health_data[endpoint] = {"success": 0, "failure": 0, "last_success": None, "last_failure": None}
        
        self.health_data[endpoint]["success"] += 1
        self.health_data[endpoint]["last_success"] = datetime.now().isoformat()
        self.save_health_data()
    
    def record_failure(self, endpoint: str, error: str = ""):
        """Enregistre un échec pour un endpoint"""
        if endpoint not in self.health_data:
            self.health_data[endpoint] = {"success": 0, "failure": 0, "last_success": None, "last_failure": None}
        
        self.health_data[endpoint]["failure"] += 1
        self.health_data[endpoint]["last_failure"] = datetime.now().isoformat()
        self.save_health_data()
    
    def get_endpoint_health(self, endpoint: str) -> Dict:
        """Récupère la santé d'un endpoint"""
        return self.health_data.get(endpoint, {"success": 0, "failure": 0, "last_success": None, "last_failure": None})

class GeminiClient:
    """Client pour l'API Gemini"""
    
    def __init__(self):
        self.api_keys = config.GEMINI_API_KEYS
        self.current_key_index = 0
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models"
    
    def get_next_api_key(self) -> str:
        """Récupère la prochaine clé API disponible"""
        key = self.api_keys[self.current_key_index]
        self.current_key_index = (self.current_key_index + 1) % len(self.api_keys)
        return key
    
    async def generate_response(self, prompt: str, context: str = "") -> Optional[str]:
        """Génère une réponse avec Gemini"""
        api_key = self.get_next_api_key()
        model = config.GEMINI_CONFIG["model"]
        
        url = f"{self.base_url}/{model}:generateContent?key={api_key}"
        
        payload = {
            "contents": [{
                "parts": [{"text": f"{context}\n\n{prompt}" if context else prompt}]
            }],
            "generationConfig": {
                "maxOutputTokens": config.GEMINI_CONFIG["max_tokens"],
                "temperature": config.GEMINI_CONFIG["temperature"],
                "topP": config.GEMINI_CONFIG["top_p"],
                "topK": config.GEMINI_CONFIG["top_k"]
            }
        }
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=payload, timeout=config.TIMEOUTS["api_request"]) as response:
                    if response.status == 200:
                        data = await response.json()
                        if "candidates" in data and data["candidates"]:
                            content = data["candidates"][0]["content"]["parts"][0]["text"]
                            if endpoint_health_manager:
                                endpoint_health_manager.record_success("gemini")
                            return content
                        else:
                            logging.error("Réponse Gemini invalide")
                            if endpoint_health_manager:
                                endpoint_health_manager.record_failure("gemini", "Réponse invalide")
                    else:
                        logging.error(f"Erreur Gemini API: {response.status}")
                        if endpoint_health_manager:
                            endpoint_health_manager.record_failure("gemini", f"Status {response.status}")
        except Exception as e:
            logging.error(f"Erreur Gemini: {e}")
            if endpoint_health_manager:
                endpoint_health_manager.record_failure("gemini", str(e))
        
        return None

class DeepSeekClient:
    """Client pour l'API DeepSeek"""
    
    def __init__(self):
        self.api_keys = config.DEEPSEEK_API_KEYS
        self.current_key_index = 0
        self.base_url = "https://api.deepseek.com/v1/chat/completions"
    
    def get_next_api_key(self) -> str:
        """Récupère la prochaine clé API disponible"""
        key = self.api_keys[self.current_key_index]
        self.current_key_index = (self.current_key_index + 1) % len(self.api_keys)
        return key
    
    async def generate_response(self, prompt: str, context: str = "") -> Optional[str]:
        """Génère une réponse avec DeepSeek"""
        api_key = self.get_next_api_key()
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": config.DEEPSEEK_CONFIG["model"],
            "messages": [
                {"role": "system", "content": context} if context else {"role": "user", "content": prompt}
            ],
            "max_tokens": config.DEEPSEEK_CONFIG["max_tokens"],
            "temperature": config.DEEPSEEK_CONFIG["temperature"],
            "top_p": config.DEEPSEEK_CONFIG["top_p"]
        }
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(self.base_url, json=payload, headers=headers, timeout=config.TIMEOUTS["api_request"]) as response:
                    if response.status == 200:
                        data = await response.json()
                        if "choices" in data and data["choices"]:
                            content = data["choices"][0]["message"]["content"]
                            if endpoint_health_manager:
                                endpoint_health_manager.record_success("deepseek")
                            return content
                        else:
                            logging.error("Réponse DeepSeek invalide")
                            if endpoint_health_manager:
                                endpoint_health_manager.record_failure("deepseek", "Réponse invalide")
                    else:
                        logging.error(f"Erreur DeepSeek API: {response.status}")
                        if endpoint_health_manager:
                            endpoint_health_manager.record_failure("deepseek", f"Status {response.status}")
        except Exception as e:
            logging.error(f"Erreur DeepSeek: {e}")
            if endpoint_health_manager:
                endpoint_health_manager.record_failure("deepseek", str(e))
        
        return None

class OCRClient:
    """Client pour l'API OCR"""
    
    def __init__(self):
        self.api_keys = config.OCR_API_KEYS
        self.current_key_index = 0
        self.base_url = "https://api.ocr.space/parse/image"
    
    def get_next_api_key(self) -> str:
        """Récupère la prochaine clé API disponible"""
        key = self.api_keys[self.current_key_index]
        self.current_key_index = (self.current_key_index + 1) % len(self.api_keys)
        return key
    
    async def extract_text_from_image(self, image_path: str) -> Optional[str]:
        """Extrait le texte d'une image"""
        api_key = self.get_next_api_key()
        
        try:
            with open(image_path, 'rb') as image_file:
                files = {'image': image_file}
                data = {
                    'apikey': api_key,
                    'language': 'eng,fra',
                    'isOverlayRequired': False,
                    'filetype': 'png,jpg,jpeg',
                    'detectOrientation': True
                }
                
                async with aiohttp.ClientSession() as session:
                    async with session.post(self.base_url, data=data, files=files, timeout=config.TIMEOUTS["image_processing"]) as response:
                        if response.status == 200:
                            result = await response.json()
                            if result.get('IsErroredOnProcessing', False):
                                logging.error(f"Erreur OCR: {result.get('ErrorMessage', 'Erreur inconnue')}")
                                if endpoint_health_manager:
                                    endpoint_health_manager.record_failure("ocr", result.get('ErrorMessage', 'Erreur inconnue'))
                                return None
                            
                            extracted_text = ""
                            for parsed_result in result.get('ParsedResults', []):
                                extracted_text += parsed_result.get('ParsedText', '')
                            
                            if endpoint_health_manager:
                                endpoint_health_manager.record_success("ocr")
                            return extracted_text.strip()
                        else:
                            logging.error(f"Erreur OCR API: {response.status}")
                            if endpoint_health_manager:
                                endpoint_health_manager.record_failure("ocr", f"Status {response.status}")
        except Exception as e:
            logging.error(f"Erreur OCR: {e}")
            if endpoint_health_manager:
                endpoint_health_manager.record_failure("ocr", str(e))
        
        return None

class WebSearchClient:
    """Client pour la recherche web"""
    
    def __init__(self):
        self.serper_api_key = config.SERPER_API_KEY
        self.tavily_api_keys = config.TAVILY_API_KEYS
        self.current_tavily_index = 0
        self.serper_url = "https://google.serper.dev/search"
        self.tavily_url = "https://api.tavily.com/search"
    
    def get_next_tavily_key(self) -> str:
        """Récupère la prochaine clé Tavily disponible"""
        key = self.tavily_api_keys[self.current_tavily_index]
        self.current_tavily_index = (self.current_tavily_index + 1) % len(self.tavily_api_keys)
        return key
    
    async def search_web(self, query: str, max_results: int = 5) -> List[Dict]:
        """Effectue une recherche web"""
        # Essayer d'abord Serper, puis Tavily en fallback
        results = await self._search_with_serper(query, max_results)
        if not results:
            results = await self._search_with_tavily(query, max_results)
        
        return results
    
    async def _search_with_serper(self, query: str, max_results: int) -> List[Dict]:
        """Recherche avec Serper API"""
        if self.serper_api_key == "YOUR_SERPER_API_KEY_HERE":
            return []
        
        headers = {"X-API-KEY": self.serper_api_key}
        payload = {"q": query, "num": max_results}
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(self.serper_url, json=payload, headers=headers, timeout=config.TIMEOUTS["web_search"]) as response:
                    if response.status == 200:
                        data = await response.json()
                        results = []
                        for result in data.get('organic', [])[:max_results]:
                            results.append({
                                'title': result.get('title', ''),
                                'snippet': result.get('snippet', ''),
                                'link': result.get('link', '')
                            })
                        if endpoint_health_manager:
                            endpoint_health_manager.record_success("serper")
                        return results
                    else:
                        logging.error(f"Erreur Serper API: {response.status}")
                        if endpoint_health_manager:
                            endpoint_health_manager.record_failure("serper", f"Status {response.status}")
        except Exception as e:
            logging.error(f"Erreur Serper: {e}")
            if endpoint_health_manager:
                endpoint_health_manager.record_failure("serper", str(e))
        
        return []
    
    async def _search_with_tavily(self, query: str, max_results: int) -> List[Dict]:
        """Recherche avec Tavily API"""
        api_key = self.get_next_tavily_key()
        if api_key == "YOUR_TAVILY_API_KEY_1":
            return []
        
        headers = {"api-key": api_key}
        params = {"query": query, "max_results": max_results}
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.tavily_url, params=params, headers=headers, timeout=config.TIMEOUTS["web_search"]) as response:
                    if response.status == 200:
                        data = await response.json()
                        results = []
                        for result in data.get('results', [])[:max_results]:
                            results.append({
                                'title': result.get('title', ''),
                                'snippet': result.get('content', ''),
                                'link': result.get('url', '')
                            })
                        if endpoint_health_manager:
                            endpoint_health_manager.record_success("tavily")
                        return results
                    else:
                        logging.error(f"Erreur Tavily API: {response.status}")
                        if endpoint_health_manager:
                            endpoint_health_manager.record_failure("tavily", f"Status {response.status}")
        except Exception as e:
            logging.error(f"Erreur Tavily: {e}")
            if endpoint_health_manager:
                endpoint_health_manager.record_failure("tavily", str(e))
        
        return []

# Instances globales
gemini_client = GeminiClient()
deepseek_client = DeepSeekClient()
ocr_client = OCRClient()
web_search_client = WebSearchClient()

def set_endpoint_health_manager_global(manager):
    """Définit le gestionnaire de santé des endpoints global"""
    global endpoint_health_manager
    endpoint_health_manager = manager