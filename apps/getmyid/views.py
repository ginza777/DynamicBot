from apps.getmyid.models import Profile
from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackContext
from telegram import Update, ReplyKeyboardMarkup, ParseMode
from apps.bots_config.functions import User_create_or_update
from apps.bots_config.models import Admin_bots
from apps.bots_config.bot_admin import *

button = ReplyKeyboardMarkup([["GetMyID"]], resize_keyboard=True)


def start(update, context):
    user = update.effective_user
    User_create_or_update(user, Profile)

    id = update.effective_user.id
    if Admin_bots.objects.filter(bot__name='getmyid').filter(telegram_id=id).exists():
        update.message.reply_text(f"""Hello Admin""", reply_markup=admin_buttons)

        return 'adminpanel'
    else:
        update.message.reply_text(f""" 
    🖐️Hello {user.username} 
    ✅ Your id :  {user.id}
    ✅ Current message id :  {update.message.message_id}
    ✅ Update id : {update.update_id}
    ✅ Chat id  : {update.message.chat_id}
    ✅ From user id :  {update.message.from_user.id}
    ✅ https://t.me/{user.username}"
        """, reply_markup=button, parse_mode=ParseMode.HTML)

        return 'bot'


conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start),
                    MessageHandler(Filters.regex('^GetMyID$'), start),

                  ],
    states={

        'adminpanel': list_admin,
        'bot': [

            MessageHandler(Filters.text, start),
        ],

    },
    fallbacks=[

        MessageHandler(Filters.all, start),

    ]
)
