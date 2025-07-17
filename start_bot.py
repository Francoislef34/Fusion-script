#!/usr/bin/env python3
"""
Script de démarrage du Bot IA Telegram
Vérifie les dépendances et lance le bot avec gestion d'erreurs
"""

import sys
import subprocess
import importlib.util
from pathlib import Path

def check_python_version():
    """Vérifie la version de Python"""
    if sys.version_info < (3, 8):
        print("❌ Erreur: Python 3.8+ requis")
        print(f"Version actuelle: {sys.version}")
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} détecté")
    return True

def check_dependencies():
    """Vérifie les dépendances requises"""
    required_packages = [
        'telegram',
        'aiohttp',
        'aiofiles',
        'asyncio'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            importlib.import_module(package)
            print(f"✅ {package} installé")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package} manquant")
    
    if missing_packages:
        print(f"\n📦 Installation des dépendances manquantes...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
            print("✅ Dépendances installées avec succès")
            return True
        except subprocess.CalledProcessError:
            print("❌ Erreur lors de l'installation des dépendances")
            print("Exécutez manuellement: pip install -r requirements.txt")
            return False
    
    return True

def check_config():
    """Vérifie la configuration du bot"""
    try:
        import config
        
        # Vérifier le token du bot
        if config.BOT_TOKEN == "7902342551:AAG6r1QA2GTMZcmcsWHi36Ivd_PVeMXULOs":
            print("⚠️  Attention: Token bot par défaut détecté")
            print("   Veuillez configurer votre propre token dans config.py")
        
        # Vérifier les clés API
        if "YOUR_GEMINI_API_KEY_1" in config.GEMINI_API_KEYS:
            print("⚠️  Attention: Clés API Gemini non configurées")
            print("   Le bot fonctionnera avec des capacités limitées")
        
        if "YOUR_SERPER_API_KEY_HERE" in config.SERPER_API_KEY:
            print("⚠️  Attention: Clé API Serper non configurée")
            print("   La recherche web sera limitée")
        
        print("✅ Configuration vérifiée")
        return True
        
    except ImportError as e:
        print(f"❌ Erreur import config: {e}")
        return False
    except Exception as e:
        print(f"❌ Erreur vérification config: {e}")
        return False

def create_directories():
    """Crée les répertoires nécessaires"""
    try:
        # Créer le répertoire bot_data
        bot_data_dir = Path("bot_data")
        bot_data_dir.mkdir(exist_ok=True)
        print("✅ Répertoires créés")
        return True
    except Exception as e:
        print(f"❌ Erreur création répertoires: {e}")
        return False

def main():
    """Fonction principale"""
    print("🚀 Démarrage du Bot IA Telegram")
    print("=" * 50)
    
    # Vérifications préliminaires
    if not check_python_version():
        sys.exit(1)
    
    if not check_dependencies():
        sys.exit(1)
    
    if not check_config():
        sys.exit(1)
    
    if not create_directories():
        sys.exit(1)
    
    print("\n✅ Toutes les vérifications sont passées")
    print("🤖 Lancement du bot...")
    print("=" * 50)
    
    try:
        # Importer et lancer le bot
        from main import main as bot_main
        import asyncio
        
        asyncio.run(bot_main())
        
    except KeyboardInterrupt:
        print("\n🛑 Arrêt du bot demandé par l'utilisateur")
    except Exception as e:
        print(f"\n❌ Erreur fatale: {e}")
        print("Consultez les logs pour plus de détails")
        sys.exit(1)

if __name__ == "__main__":
    main()