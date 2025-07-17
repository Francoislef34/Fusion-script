# 🤖 Bot IA Telegram Intelligent

Un bot Telegram avancé avec capacités d'IA conversationnelle, recherche web, OCR et gestion de quotas.

## 🚀 Fonctionnalités

### 🤖 IA Conversationnelle
- **Gemini AI** : Modèle principal pour les conversations
- **DeepSeek AI** : Modèle de secours
- **Contexte conversationnel** : Mémorisation des conversations
- **Réponses intelligentes** : Analyse et génération de contenu

### 🔍 Recherche Web
- **Recherche Google** via Serper API
- **Recherche alternative** via Tavily API
- **Résultats formatés** avec titres et extraits
- **Fallback automatique** entre les services

### 📷 Analyse d'Images (OCR)
- **Extraction de texte** depuis les images
- **Support multi-format** : JPG, PNG, GIF, BMP, WebP
- **API OCR.space** avec rotation automatique
- **Détection de langue** : Français et Anglais

### 📊 Gestion des Quotas
- **Limites quotidiennes** et **horaires**
- **Suivi en temps réel** de l'utilisation
- **Cache intelligent** pour les performances
- **Nettoyage automatique** des anciennes données

### 🛡️ Sécurité et Modération
- **Filtrage de contenu** automatique
- **Détection de spam** avancée
- **Liste d'utilisateurs** autorisés/bannis
- **Validation des fichiers** uploadés

## 📁 Structure du Projet

```
bot_telegram/
├── config.py              # Configuration principale
├── utils.py               # Utilitaires et fonctions communes
├── api_clients.py         # Clients API externes
├── memory_and_quotas.py   # Gestion mémoire et quotas
├── filters_and_tools.py   # Filtres et outils de traitement
├── main.py               # Bot principal
├── requirements.txt      # Dépendances Python
├── README_BOT.md        # Documentation
└── bot_data/            # Données du bot (créé automatiquement)
    ├── bot_activity.log
    ├── bot_errors.log
    ├── api_quotas.json
    ├── endpoint_health.json
    ├── ia_status.json
    └── chat_history.json
```

## ⚙️ Installation

### 1. Prérequis
- Python 3.8+
- Compte Telegram avec bot créé via @BotFather
- Clés API pour les services externes

### 2. Installation des dépendances
```bash
pip install -r requirements.txt
```

### 3. Configuration des API Keys

Éditez `config.py` et remplacez les clés API par vos propres clés :

```python
# Clés API à configurer
GEMINI_API_KEYS = [
    "VOTRE_CLE_GEMINI_1",
    "VOTRE_CLE_GEMINI_2"
]

OCR_API_KEYS = [
    "VOTRE_CLE_OCR_1",
    "VOTRE_CLE_OCR_2"
]

DEEPSEEK_API_KEYS = [
    "VOTRE_CLE_DEEPSEEK_1",
    "VOTRE_CLE_DEEPSEEK_2"
]

SERPER_API_KEY = "VOTRE_CLE_SERPER"
TAVILY_API_KEYS = [
    "VOTRE_CLE_TAVILY_1",
    "VOTRE_CLE_TAVILY_2"
]
```

### 4. Configuration du Bot Telegram

1. Créez un bot via @BotFather sur Telegram
2. Récupérez le token du bot
3. Remplacez `BOT_TOKEN` dans `config.py`

### 5. Lancement du Bot

```bash
python main.py
```

## 🎯 Utilisation

### Commandes Disponibles

| Commande | Description |
|----------|-------------|
| `/start` | Démarrer le bot et voir les fonctionnalités |
| `/help` | Afficher l'aide complète |
| `/search [terme]` | Rechercher sur le web |
| `/quota` | Voir vos quotas d'utilisation |
| `/history` | Afficher l'historique des conversations |
| `/clear` | Effacer l'historique |

### Fonctionnalités Interactives

#### 💬 Chat IA
Envoyez simplement un message texte pour discuter avec l'IA :
```
Vous: Qu'est-ce que l'intelligence artificielle ?
Bot: L'intelligence artificielle (IA) est un domaine...
```

#### 🔍 Recherche Web
Utilisez la commande `/search` :
```
/search intelligence artificielle 2024
```

#### 📷 OCR d'Images
Envoyez une image pour extraire le texte :
- Le bot détectera automatiquement qu'il s'agit d'une image
- Le texte extrait sera retourné avec formatage

#### 📄 Documents
Envoyez des documents pour traitement :
- Images : Extraction OCR automatique
- Autres formats : Informations sur le fichier

## ⚙️ Configuration Avancée

### Limites et Quotas

Modifiez les limites dans `config.py` :

```python
DAILY_USER_LIMITS = {
    "messages": 100,      # Messages par jour
    "images": 20,         # Images par jour
    "web_searches": 30,   # Recherches par jour
    "file_uploads": 10    # Fichiers par jour
}

HOURLY_USER_LIMITS = {
    "messages": 20,       # Messages par heure
    "images": 5,          # Images par heure
    "web_searches": 8,    # Recherches par heure
    "file_uploads": 3     # Fichiers par heure
}
```

### Sécurité

Configurez les listes d'utilisateurs dans `config.py` :

```python
# Utilisateurs autorisés (vide = tous autorisés)
AUTHORIZED_USERS = []

# Utilisateurs bannis
BANNED_USERS = []

# Mots-clés interdits
FORBIDDEN_KEYWORDS = [
    "spam", "scam", "malware", "virus", "hack"
]
```

### Modèles IA

Personnalisez les paramètres des modèles :

```python
GEMINI_CONFIG = {
    "model": "gemini-1.5-flash",
    "max_tokens": 4096,
    "temperature": 0.7,
    "top_p": 0.9,
    "top_k": 40
}

DEEPSEEK_CONFIG = {
    "model": "deepseek-chat",
    "max_tokens": 4096,
    "temperature": 0.7,
    "top_p": 0.9
}
```

## 📊 Monitoring et Logs

### Fichiers de Logs

- `bot_activity.log` : Activité générale du bot
- `bot_errors.log` : Erreurs critiques
- `endpoint_health.json` : Santé des APIs
- `api_quotas.json` : Utilisation des quotas
- `ia_status.json` : Performance des IA

### Surveillance des Performances

Le bot inclut un système de monitoring automatique :
- **Suivi des temps de réponse** des APIs
- **Taux de succès** par service
- **Recommandations** automatiques
- **Nettoyage périodique** des données

## 🔧 Maintenance

### Nettoyage Automatique

Le bot effectue automatiquement :
- Nettoyage des quotas anciens (> 7 jours)
- Sauvegarde des données de performance
- Gestion de la mémoire conversationnelle

### Sauvegarde

Les données importantes sont sauvegardées dans `bot_data/` :
- Historique des conversations
- Quotas utilisateurs
- Statistiques de performance

## 🚨 Dépannage

### Erreurs Courantes

1. **Token Bot Invalide**
   - Vérifiez le token dans `config.py`
   - Assurez-vous que le bot est actif

2. **Erreurs API**
   - Vérifiez les clés API dans `config.py`
   - Consultez les logs pour plus de détails

3. **Quotas Dépassés**
   - Utilisez `/quota` pour vérifier l'utilisation
   - Attendez le reset quotidien ou contactez l'admin

4. **Fichiers Trop Volumineux**
   - Limite : 10 MB pour les fichiers
   - Limite : 10 MB pour les images

### Logs et Debug

Activez le debug en modifiant le niveau de log dans `utils.py` :

```python
logging.basicConfig(level=logging.DEBUG)
```

## 🤝 Contribution

Pour contribuer au projet :

1. Fork le repository
2. Créez une branche pour votre fonctionnalité
3. Testez vos modifications
4. Soumettez une pull request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## 🆘 Support

Pour obtenir de l'aide :
- Consultez la documentation
- Vérifiez les logs d'erreur
- Contactez l'administrateur du bot

---

**Version :** 1.0.0  
**Dernière mise à jour :** 2024  
**Auteur :** Assistant IA