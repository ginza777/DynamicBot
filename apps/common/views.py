from apps.common.models import Profile
from telegram.ext import CommandHandler, CallbackContext, ConversationHandler, MessageHandler, Filters
from telegram import Update, ReplyKeyboardMarkup, ParseMode
from apps.bots_config.functions import User_create_or_update,Statistic
button = ReplyKeyboardMarkup([["GetMyID"]], resize_keyboard=True)


def start(update, context):
    user = update.effective_user
    User_create_or_update(user, Profile)
    update.message.reply_text(f""" 
🖐️Hello {user.username} 
✅ Your id :  {user.id}
✅ Current message id :  {update.message.message_id}
✅ Update id : {update.update_id}
✅ Chat id  : {update.message.chat_id}
✅ From user id :  {update.message.from_user.id}
✅ https://t.me/{user.username}"
    """, reply_markup=button,parse_mode=ParseMode.HTML)

    return 'bot'

def users_count(update: Update, context: CallbackContext):
    msg=Statistic(Profile)
    update.message.reply_text(msg, reply_markup=button)
    return 'bot'


conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start),
                  MessageHandler(Filters.all, start),
                  ],
    states={
        'bot': [
            MessageHandler(Filters.regex('^(' + 'sherzamon_usercount' + ')$'), users_count),

        ],
    },
    fallbacks=[
        MessageHandler(Filters.all, start),
        CommandHandler('start', start)
    ]
)
