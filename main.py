import asyncio
import logging
import os
from datetime import datetime
from pathlib import Path
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes
import config
import utils
import api_clients
import memory_and_quotas
import filters_and_tools

# Configuration du logging
logger, error_logger = utils.setup_logging()

# Variables globales
bot = None
endpoint_health_manager = None

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /start"""
    user_id = update.effective_user.id
    user_name = update.effective_user.first_name
    
    welcome_message = f"""
👋 Bonjour {user_name} !

Je suis votre assistant IA intelligent. Voici ce que je peux faire pour vous :

🤖 **IA Conversationnelle**
• Répondre à vos questions
• Analyser des textes
• Aider avec des tâches créatives

🔍 **Recherche Web**
• Rechercher des informations en ligne
• Analyser des pages web
• Extraire des données

📷 **Analyse d'Images**
• Extraire du texte des images (OCR)
• Analyser le contenu visuel
• Traiter des documents

📊 **Gestion des Quotas**
• Suivi de votre utilisation
• Limites quotidiennes et horaires
• Statistiques d'usage

**Commandes disponibles :**
/help - Aide et commandes
/search [terme] - Recherche web
/quota - Voir vos quotas
/history - Historique des conversations
/clear - Effacer l'historique

Envoyez-moi un message pour commencer !
    """
    
    await update.message.reply_text(welcome_message)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /help"""
    help_text = """
🤖 **Guide d'utilisation du Bot IA**

**Commandes principales :**
• `/start` - Démarrer le bot
• `/help` - Afficher cette aide
• `/search [terme]` - Recherche web
• `/quota` - Voir vos quotas d'utilisation
• `/history` - Historique des conversations
• `/clear` - Effacer l'historique

**Fonctionnalités :**
• **Chat IA** : Posez des questions, demandez de l'aide
• **Recherche web** : Utilisez `/search` suivi de votre recherche
• **OCR** : Envoyez une image pour extraire le texte
• **Analyse de liens** : Envoyez des URLs pour les analyser

**Limites d'utilisation :**
• Messages : 100/jour, 20/heure
• Images : 20/jour, 5/heure
• Recherches web : 30/jour, 8/heure
• Fichiers : 10/jour, 3/heure

**Support :**
Pour toute question ou problème, contactez l'administrateur.
    """
    
    await update.message.reply_text(help_text)

async def search_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /search pour la recherche web"""
    user_id = update.effective_user.id
    
    # Vérifier les quotas
    if not await memory_and_quotas.quota_manager.check_quota(user_id, "web_searches"):
        await update.message.reply_text(config.MESSAGES["quota_exceeded"])
        return
    
    # Extraire la requête de recherche
    if not context.args:
        await update.message.reply_text("❌ Veuillez spécifier un terme de recherche.\nExemple: `/search intelligence artificielle`")
        return
    
    query = " ".join(context.args)
    
    # Message de traitement
    processing_msg = await update.message.reply_text("🔍 Recherche en cours...")
    
    try:
        # Effectuer la recherche
        results = await api_clients.web_search_client.search_web(query, max_results=5)
        
        if results:
            # Incrémenter le quota
            await memory_and_quotas.quota_manager.increment_quota(user_id, "web_searches")
            
            # Formater les résultats
            response = f"🔍 **Résultats pour :** {query}\n\n"
            for i, result in enumerate(results, 1):
                response += f"{i}. **{result['title']}**\n"
                response += f"   {result['snippet'][:200]}...\n"
                response += f"   🔗 {result['link']}\n\n"
            
            # Diviser si trop long
            if len(response) > 4096:
                response = response[:4093] + "..."
            
            await processing_msg.edit_text(response)
        else:
            await processing_msg.edit_text("❌ Aucun résultat trouvé pour cette recherche.")
    
    except Exception as e:
        logger.error(f"Erreur recherche web: {e}")
        await processing_msg.edit_text("❌ Erreur lors de la recherche. Veuillez réessayer.")

async def quota_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /quota pour voir les quotas"""
    user_id = update.effective_user.id
    
    try:
        quota_status = await memory_and_quotas.quota_manager.get_user_quota_status(user_id)
        
        response = "📊 **Vos quotas d'utilisation :**\n\n"
        
        for quota_type, limits in quota_status.items():
            daily = limits["daily"]
            hourly = limits["hourly"]
            
            response += f"**{quota_type.upper()}**\n"
            response += f"  📅 Quotidien: {daily['used']}/{daily['limit']} ({daily['remaining']} restants)\n"
            response += f"  ⏰ Horaire: {hourly['used']}/{hourly['limit']} ({hourly['remaining']} restants)\n\n"
        
        await update.message.reply_text(response)
    
    except Exception as e:
        logger.error(f"Erreur affichage quotas: {e}")
        await update.message.reply_text("❌ Erreur lors de la récupération des quotas.")

async def history_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /history pour voir l'historique"""
    user_id = update.effective_user.id
    
    try:
        history = await memory_and_quotas.memory_manager.get_full_history(user_id, limit=10)
        
        if history:
            response = "📚 **Vos 10 derniers messages :**\n\n"
            for i, entry in enumerate(reversed(history), 1):
                timestamp = datetime.fromisoformat(entry['timestamp']).strftime("%d/%m %H:%M")
                message_preview = entry['message'][:50] + "..." if len(entry['message']) > 50 else entry['message']
                response += f"{i}. **{timestamp}** - {message_preview}\n"
        else:
            response = "📚 Aucun historique disponible."
        
        await update.message.reply_text(response)
    
    except Exception as e:
        logger.error(f"Erreur affichage historique: {e}")
        await update.message.reply_text("❌ Erreur lors de la récupération de l'historique.")

async def clear_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /clear pour effacer l'historique"""
    user_id = update.effective_user.id
    
    try:
        memory_and_quotas.memory_manager.clear_user_memory(user_id)
        await update.message.reply_text("🗑️ Votre historique a été effacé.")
    except Exception as e:
        logger.error(f"Erreur effacement historique: {e}")
        await update.message.reply_text("❌ Erreur lors de l'effacement de l'historique.")

async def handle_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Gestionnaire des messages texte"""
    user_id = update.effective_user.id
    message_text = update.message.text
    
    # Vérifier l'autorisation
    if not filters_and_tools.content_filter.check_user_authorization(user_id):
        await update.message.reply_text("❌ Vous n'êtes pas autorisé à utiliser ce bot.")
        return
    
    # Vérifier le contenu
    is_valid, reason = filters_and_tools.content_filter.check_message(message_text)
    if not is_valid:
        await update.message.reply_text(f"❌ Message rejeté: {reason}")
        return
    
    # Vérifier les quotas
    if not await memory_and_quotas.quota_manager.check_quota(user_id, "messages"):
        await update.message.reply_text(config.MESSAGES["quota_exceeded"])
        return
    
    # Classifier le message
    classification = filters_and_tools.message_processor.classify_message(message_text)
    
    # Message de traitement
    processing_msg = await update.message.reply_text("🤖 Traitement en cours...")
    
    try:
        # Récupérer le contexte de conversation
        context_text = memory_and_quotas.memory_manager.get_conversation_context(user_id)
        
        # Générer la réponse avec l'IA
        start_time = datetime.now()
        
        # Essayer d'abord Gemini, puis DeepSeek en fallback
        response = await api_clients.gemini_client.generate_response(message_text, context_text)
        ia_used = "gemini"
        
        if not response:
            response = await api_clients.deepseek_client.generate_response(message_text, context_text)
            ia_used = "deepseek"
        
        end_time = datetime.now()
        response_time = (end_time - start_time).total_seconds()
        
        if response:
            # Enregistrer l'utilisation
            await memory_and_quotas.performance_tracker.record_ia_usage(ia_used, True, response_time)
            
            # Ajouter à la mémoire
            await memory_and_quotas.memory_manager.add_to_memory(user_id, message_text, response)
            
            # Incrémenter le quota
            await memory_and_quotas.quota_manager.increment_quota(user_id, "messages")
            
            # Envoyer la réponse
            await processing_msg.edit_text(response)
        else:
            await memory_and_quotas.performance_tracker.record_ia_usage(ia_used, False, response_time)
            await processing_msg.edit_text("❌ Désolé, je n'ai pas pu générer une réponse. Veuillez réessayer.")
    
    except Exception as e:
        logger.error(f"Erreur traitement message: {e}")
        await processing_msg.edit_text("❌ Une erreur s'est produite. Veuillez réessayer.")

async def handle_photo_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Gestionnaire des messages photo"""
    user_id = update.effective_user.id
    
    # Vérifier les quotas
    if not await memory_and_quotas.quota_manager.check_quota(user_id, "images"):
        await update.message.reply_text(config.MESSAGES["quota_exceeded"])
        return
    
    # Message de traitement
    processing_msg = await update.message.reply_text("📷 Traitement de l'image...")
    
    try:
        # Récupérer la photo
        photo = update.message.photo[-1]  # Plus grande taille
        file = await context.bot.get_file(photo.file_id)
        
        # Vérifier la taille
        if photo.file_size > config.MAX_IMAGE_SIZE:
            await processing_msg.edit_text(f"❌ Image trop volumineuse ({utils.format_file_size(photo.file_size)})")
            return
        
        # Télécharger l'image
        image_path = f"temp_image_{user_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        await file.download_to_drive(image_path)
        
        # Extraire le texte avec OCR
        extracted_text = await api_clients.ocr_client.extract_text_from_image(image_path)
        
        # Nettoyer le fichier temporaire
        try:
            os.remove(image_path)
        except:
            pass
        
        if extracted_text:
            # Incrémenter le quota
            await memory_and_quotas.quota_manager.increment_quota(user_id, "images")
            
            response = f"📷 **Texte extrait de l'image :**\n\n{extracted_text}"
            
            # Limiter la longueur
            if len(response) > 4096:
                response = response[:4093] + "..."
            
            await processing_msg.edit_text(response)
        else:
            await processing_msg.edit_text("❌ Aucun texte n'a pu être extrait de cette image.")
    
    except Exception as e:
        logger.error(f"Erreur traitement image: {e}")
        await processing_msg.edit_text("❌ Erreur lors du traitement de l'image.")

async def handle_document_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Gestionnaire des messages document"""
    user_id = update.effective_user.id
    document = update.message.document
    
    # Vérifier les quotas
    if not await memory_and_quotas.quota_manager.check_quota(user_id, "file_uploads"):
        await update.message.reply_text(config.MESSAGES["quota_exceeded"])
        return
    
    # Vérifier le fichier
    is_valid, reason = filters_and_tools.file_processor.validate_file(document.file_name, document.file_size)
    if not is_valid:
        await update.message.reply_text(f"❌ Fichier rejeté: {reason}")
        return
    
    # Message de traitement
    processing_msg = await update.message.reply_text("📄 Traitement du document...")
    
    try:
        # Télécharger le document
        file = await context.bot.get_file(document.file_id)
        doc_path = f"temp_doc_{user_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{document.file_name}"
        await file.download_to_drive(doc_path)
        
        # Traiter selon le type
        if filters_and_tools.file_processor.is_supported_image(document.file_name):
            # Traitement OCR pour les images
            extracted_text = await api_clients.ocr_client.extract_text_from_image(doc_path)
            if extracted_text:
                response = f"📄 **Texte extrait du document :**\n\n{extracted_text}"
            else:
                response = "❌ Aucun texte n'a pu être extrait de ce document."
        else:
            response = f"📄 Document reçu: {document.file_name}\nTaille: {utils.format_file_size(document.file_size)}"
        
        # Nettoyer le fichier temporaire
        try:
            os.remove(doc_path)
        except:
            pass
        
        # Incrémenter le quota
        await memory_and_quotas.quota_manager.increment_quota(user_id, "file_uploads")
        
        # Limiter la longueur
        if len(response) > 4096:
            response = response[:4093] + "..."
        
        await processing_msg.edit_text(response)
    
    except Exception as e:
        logger.error(f"Erreur traitement document: {e}")
        await processing_msg.edit_text("❌ Erreur lors du traitement du document.")

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Gestionnaire d'erreurs"""
    logger.error(f"Erreur non gérée: {context.error}")
    error_logger.error(f"Erreur dans update {update}: {context.error}")

async def periodic_cleanup():
    """Nettoyage périodique"""
    while True:
        try:
            await asyncio.sleep(3600)  # Toutes les heures
            await memory_and_quotas.cleanup_old_data()
            await memory_and_quotas.performance_tracker.save_performance_data()
            logger.info("Nettoyage périodique effectué")
        except Exception as e:
            logger.error(f"Erreur nettoyage périodique: {e}")

async def main():
    """Fonction principale"""
    global bot, endpoint_health_manager
    
    # Afficher le message de démarrage
    print(config.STARTUP_MESSAGE)
    
    # Initialiser les composants
    endpoint_health_manager = api_clients.EndpointHealthManager()
    
    # Configurer les variables globales
    utils.set_file_lock(asyncio.Lock())
    utils.set_endpoint_health_manager_global(endpoint_health_manager)
    api_clients.set_endpoint_health_manager_global(endpoint_health_manager)
    filters_and_tools.set_ocr_api_client_instance(api_clients.ocr_client)
    
    # Initialiser le système de mémoire
    await memory_and_quotas.initialize_memory_system()
    
    # Créer l'application bot
    bot = Application.builder().token(config.BOT_TOKEN).build()
    
    # Ajouter les gestionnaires
    bot.add_handler(CommandHandler("start", start_command))
    bot.add_handler(CommandHandler("help", help_command))
    bot.add_handler(CommandHandler("search", search_command))
    bot.add_handler(CommandHandler("quota", quota_command))
    bot.add_handler(CommandHandler("history", history_command))
    bot.add_handler(CommandHandler("clear", clear_command))
    
    # Gestionnaires de messages
    bot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_message))
    bot.add_handler(MessageHandler(filters.PHOTO, handle_photo_message))
    bot.add_handler(MessageHandler(filters.Document.ALL, handle_document_message))
    
    # Gestionnaire d'erreurs
    bot.add_error_handler(error_handler)
    
    # Démarrer le nettoyage périodique
    asyncio.create_task(periodic_cleanup())
    
    # Démarrer le bot
    logger.info("Bot démarré avec succès")
    await bot.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Arrêt du bot demandé par l'utilisateur")
    except Exception as e:
        logger.error(f"Erreur fatale: {e}")
        error_logger.error(f"Erreur fatale: {e}")
    finally:
        # Nettoyage final
        asyncio.run(filters_and_tools.cleanup_resources())
        logger.info("Bot arrêté")