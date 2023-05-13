from apps.common.models import Profile
from telegram.ext import  CommandHandler, CallbackContext, ConversationHandler, MessageHandler, Filters
from telegram import Update, ReplyKeyboardMarkup
from apps.bots_config.functions import User_create_or_update,Statistic
button = ReplyKeyboardMarkup([["GetMyID"]], resize_keyboard=True)


def start(update: Update, context: CallbackContext):
    user= update.effective_user
    User_create_or_update(user, Profile)
    update.message.reply_text(f"""

    🖐️Hello {user.username}""")
    return 'bot'
def users_count(update: Update, context: CallbackContext):
    msg=Statistic(Profile)
    update.message.reply_text(msg, reply_markup=button)
    return 'bot'




conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start),
                  ],
    states={
        'bot': [
            MessageHandler(Filters.all, start),
            MessageHandler(Filters.regex('^(' + 'sherzamon_usercount' + ')$'), users_count),
        ],
    },
    fallbacks=[
        CommandHandler('start', start)
    ]

)
