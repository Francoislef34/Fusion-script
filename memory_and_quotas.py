import json
import asyncio
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional
import logging
import config
import utils

# Imports des constantes depuis config.py
from config import (
    DAILY_USER_LIMITS, HOURLY_USER_LIMITS, 
    QUOTAS_FILE, USER_CHAT_HISTORY_FILE,
    MESSAGES
)

# Imports depuis utils.py
from utils import (
    safe_json_read, safe_json_write, 
    get_user_quota_key, get_hourly_quota_key,
    check_user_quota, increment_user_quota
)

class QuotaManager:
    """Gestionnaire des quotas utilisateur"""
    
    def __init__(self):
        self.quotas_cache = {}
        self.cache_expiry = {}
        self.cache_duration = timedelta(minutes=5)
    
    async def check_quota(self, user_id: int, quota_type: str) -> bool:
        """Vérifie si l'utilisateur a encore des quotas disponibles"""
        cache_key = f"{user_id}_{quota_type}"
        current_time = datetime.now()
        
        # Vérifier le cache
        if cache_key in self.quotas_cache and current_time < self.cache_expiry.get(cache_key, datetime.min):
            return self.quotas_cache[cache_key]
        
        # Vérifier les quotas réels
        has_quota = await check_user_quota(user_id, quota_type)
        
        # Mettre en cache
        self.quotas_cache[cache_key] = has_quota
        self.cache_expiry[cache_key] = current_time + self.cache_duration
        
        return has_quota
    
    async def increment_quota(self, user_id: int, quota_type: str):
        """Incrémente le quota utilisateur"""
        await increment_user_quota(user_id, quota_type)
        
        # Invalider le cache
        cache_key = f"{user_id}_{quota_type}"
        if cache_key in self.quotas_cache:
            del self.quotas_cache[cache_key]
    
    async def get_user_quota_status(self, user_id: int) -> Dict[str, Dict]:
        """Récupère le statut complet des quotas d'un utilisateur"""
        quotas = await safe_json_read(config.QUOTAS_FILE, {})
        
        status = {}
        for quota_type in DAILY_USER_LIMITS.keys():
            daily_key = get_user_quota_key(user_id, quota_type)
            hourly_key = get_hourly_quota_key(user_id, quota_type)
            
            daily_usage = quotas.get(daily_key, 0)
            hourly_usage = quotas.get(hourly_key, 0)
            
            status[quota_type] = {
                "daily": {
                    "used": daily_usage,
                    "limit": DAILY_USER_LIMITS[quota_type],
                    "remaining": max(0, DAILY_USER_LIMITS[quota_type] - daily_usage)
                },
                "hourly": {
                    "used": hourly_usage,
                    "limit": HOURLY_USER_LIMITS[quota_type],
                    "remaining": max(0, HOURLY_USER_LIMITS[quota_type] - hourly_usage)
                }
            }
        
        return status
    
    async def reset_user_quotas(self, user_id: int):
        """Réinitialise tous les quotas d'un utilisateur (admin seulement)"""
        quotas = await safe_json_read(config.QUOTAS_FILE, {})
        
        keys_to_remove = []
        for key in quotas.keys():
            if key.startswith(f"{user_id}_"):
                keys_to_remove.append(key)
        
        for key in keys_to_remove:
            del quotas[key]
        
        await safe_json_write(config.QUOTAS_FILE, quotas)
        
        # Vider le cache
        self.quotas_cache.clear()
        self.cache_expiry.clear()

class MemoryManager:
    """Gestionnaire de la mémoire et de l'historique des conversations"""
    
    def __init__(self):
        self.conversation_memory = {}
        self.max_memory_size = 1000  # Nombre maximum de messages en mémoire
        self.max_conversation_length = 50  # Longueur maximale d'une conversation
    
    async def add_to_memory(self, user_id: int, message: str, response: str, context: str = ""):
        """Ajoute une interaction à la mémoire"""
        if user_id not in self.conversation_memory:
            self.conversation_memory[user_id] = []
        
        interaction = {
            "timestamp": datetime.now().isoformat(),
            "message": message,
            "response": response,
            "context": context
        }
        
        self.conversation_memory[user_id].append(interaction)
        
        # Limiter la taille de la conversation
        if len(self.conversation_memory[user_id]) > self.max_conversation_length:
            self.conversation_memory[user_id] = self.conversation_memory[user_id][-self.max_conversation_length:]
        
        # Sauvegarder dans le fichier
        await utils.save_chat_history(user_id, message, response)
    
    def get_conversation_context(self, user_id: int, max_messages: int = 10) -> str:
        """Récupère le contexte de conversation récent"""
        if user_id not in self.conversation_memory:
            return ""
        
        recent_messages = self.conversation_memory[user_id][-max_messages:]
        context_parts = []
        
        for interaction in recent_messages:
            context_parts.append(f"Utilisateur: {interaction['message']}")
            context_parts.append(f"Assistant: {interaction['response']}")
        
        return "\n".join(context_parts)
    
    async def get_full_history(self, user_id: int, limit: int = 20) -> List[Dict]:
        """Récupère l'historique complet depuis le fichier"""
        return await utils.get_chat_history(user_id, limit)
    
    def clear_user_memory(self, user_id: int):
        """Efface la mémoire d'un utilisateur"""
        if user_id in self.conversation_memory:
            del self.conversation_memory[user_id]
    
    def get_memory_stats(self) -> Dict:
        """Récupère les statistiques de mémoire"""
        total_users = len(self.conversation_memory)
        total_messages = sum(len(conv) for conv in self.conversation_memory.values())
        
        return {
            "total_users": total_users,
            "total_messages": total_messages,
            "average_messages_per_user": total_messages / total_users if total_users > 0 else 0
        }

class PerformanceTracker:
    """Suivi des performances et de la diversification des IA"""
    
    def __init__(self):
        self.performance_data = {}
        self.ia_usage_stats = {}
    
    async def record_ia_usage(self, ia_type: str, success: bool, response_time: float):
        """Enregistre l'utilisation d'une IA"""
        if ia_type not in self.ia_usage_stats:
            self.ia_usage_stats[ia_type] = {
                "total_requests": 0,
                "successful_requests": 0,
                "failed_requests": 0,
                "total_response_time": 0,
                "average_response_time": 0
            }
        
        stats = self.ia_usage_stats[ia_type]
        stats["total_requests"] += 1
        stats["total_response_time"] += response_time
        
        if success:
            stats["successful_requests"] += 1
        else:
            stats["failed_requests"] += 1
        
        stats["average_response_time"] = stats["total_response_time"] / stats["total_requests"]
    
    async def get_ia_performance_report(self) -> Dict:
        """Génère un rapport de performance des IA"""
        report = {
            "timestamp": datetime.now().isoformat(),
            "ia_stats": self.ia_usage_stats,
            "recommendations": []
        }
        
        # Analyser les performances et générer des recommandations
        for ia_type, stats in self.ia_usage_stats.items():
            success_rate = stats["successful_requests"] / stats["total_requests"] if stats["total_requests"] > 0 else 0
            
            if success_rate < 0.8:
                report["recommendations"].append(f"IA {ia_type}: Taux de succès faible ({success_rate:.2%})")
            
            if stats["average_response_time"] > 10:
                report["recommendations"].append(f"IA {ia_type}: Temps de réponse élevé ({stats['average_response_time']:.2f}s)")
        
        return report
    
    async def save_performance_data(self):
        """Sauvegarde les données de performance"""
        data = {
            "ia_usage_stats": self.ia_usage_stats,
            "last_updated": datetime.now().isoformat()
        }
        await safe_json_write(config.IA_STATUS_FILE, data)
    
    async def load_performance_data(self):
        """Charge les données de performance"""
        data = await safe_json_read(config.IA_STATUS_FILE, {})
        self.ia_usage_stats = data.get("ia_usage_stats", {})

# Instances globales
quota_manager = QuotaManager()
memory_manager = MemoryManager()
performance_tracker = PerformanceTracker()

async def initialize_memory_system():
    """Initialise le système de mémoire et de quotas"""
    await performance_tracker.load_performance_data()
    logging.info("Système de mémoire et quotas initialisé")

async def cleanup_old_data():
    """Nettoie les anciennes données"""
    utils.clean_old_quotas()
    logging.info("Nettoyage des anciennes données terminé")