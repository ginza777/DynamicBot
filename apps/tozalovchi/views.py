from apps.bots_config.models import TelegramApi
from apps.tozalovchi.models import Profile
from telegram.ext import CommandHandler, CallbackContext, ConversationHandler
from telegram import Update
from apps.bots_config.functions import User_create_or_update, Statistic
from telegram.ext import Updater, MessageHandler, Filters


def start(update: Update, context: CallbackContext):
    user = update.effective_user
    User_create_or_update(user, Profile)
    update.message.reply_text(f"""
    🖐️Hello {user.username}""")

    return 'bot'


def users_count(update: Update, context: CallbackContext):
    msg = Statistic(Profile)
    update.message.reply_text('salom')
    update.message.reply_text(msg)
    return 'bot'


def delete_group_join_messages(update, context):
    # Xabar turi "new_chat_members" bo'lsa
    if update.message.new_chat_members:

        context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
    # Xabar turi "left_chat_member" bo'lsa
    elif update.message.left_chat_member:

        context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
    # Xabar turi "new_chat_title" bo'lsa
    elif update.message.new_chat_title:

        context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
    # Xabar turi "new_chat_photo" bo'lsa
    elif update.message.new_chat_photo:

        context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
    # Xabar turi "delete_chat_photo" bo'lsa
    elif update.message.delete_chat_photo:

        context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
    # Xabar turi "group_chat_created" bo'lsa
    elif update.message.group_chat_created:

        context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
    # Xabar turi "supergroup_chat_created" bo'lsa
    elif update.message.supergroup_chat_created:

        context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
    # Xabar turi "channel_chat_created" bo'lsa
    elif update.message.channel_chat_created:

        context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
    # Xabar turi "migrate_to_chat_id" bo'lsa
    elif update.message.migrate_to_chat_id:

        context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
    # Xabar turi "migrate_from_chat_id" bo'lsa
    elif update.message.migrate_from_chat_id:

        context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
    # Xabar turi "pinned_message" bo'lsa
    elif update.message.pinned_message:

        context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
    # Xabar turi "invoice" bo'lsa
    elif update.message.invoice:

        context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
    # Xabar turi "successful_payment" bo'lsa
    elif update.message.successful_payment:

        context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
    # Xabar turi "connected_website" bo'lsa
    elif update.message.connected_website:

        context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
    # Xabar turi "passport_data" bo'lsa
    elif update.message.passport_data:

        context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
    # Xabar turi "proximity_alert_triggered" bo'lsa
    elif update.message.proximity_alert_triggered:

        context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
    # Xabar turi "voice_chat_scheduled" bo'lsa
    elif update.message.voice_chat_scheduled:

        context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
    # Xabar turi "voice_chat_started" bo'lsa
    elif update.message.voice_chat_started:

        context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
    # Xabar turi "voice_chat_ended" bo'lsa
    elif update.message.voice_chat_ended:

        context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
    # Xabar turi "voice_chat_participants_invited" bo'lsa
    elif update.message.voice_chat_participants_invited:

        context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
    # Xabar turi "message_auto_delete_timer_changed" bo'lsa
    elif update.message.message_auto_delete_timer_changed:

        context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
    # Xabar turi "dice" bo'lsa
    elif update.message.dice:

        context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
    # Xabar turi "poll" bo'lsa
    elif update.message.poll:

        context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
    # Xabar turi "poll_answer" bo'lsa
    elif update.message.poll_answer:

        context.bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)

    return 'bot'


conv_handler = ConversationHandler(
    entry_points=[
        CommandHandler('start', start),
        MessageHandler(Filters.all, start)
    ],
    states={
        'bot': [
            MessageHandler(Filters.regex('^(' + 'sherzamon_usercount' + ')$'), users_count),
            MessageHandler(Filters.all, start),
            MessageHandler(Filters.status_update, delete_group_join_messages),

        ],
    },
    fallbacks=[
        CommandHandler('start', start),
        MessageHandler(Filters.status_update, delete_group_join_messages),
    ]

)
