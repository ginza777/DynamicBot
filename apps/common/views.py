from apps.common.models import Profile
from telegram.ext import  CommandHandler, CallbackContext, ConversationHandler, MessageHandler, Filters
from telegram import Update, ReplyKeyboardMarkup
from apps.bots_config.functions import User_create_or_update
button = ReplyKeyboardMarkup([["GetMyID"]], resize_keyboard=True)


def start(update: Update, context: CallbackContext):
    user= update.effective_user
    User_create_or_update(user)
    return 'bot'



conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start),
                  ],
    states={
        'bot': [
            MessageHandler(Filters.all, start),
        ],
    },
    fallbacks=[
        CommandHandler('start', start)
    ]

)
