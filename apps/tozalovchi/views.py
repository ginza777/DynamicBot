from apps.bots_config.models import TelegramApi
from apps.tozalovchi.models import Profile
from telegram.ext import CommandHandler, CallbackContext, ConversationHandler
from telegram import Update, ReplyKeyboardMarkup, ParseMode
from apps.bots_config.functions import User_create_or_update
from telegram.ext import Updater, MessageHandler, Filters
from apps.bots_config.models import Admin_bots

# adminpanel
admin_buttons = ReplyKeyboardMarkup([["user_counts", "user_data"], ['bot_admins', 'user_finder'], ['/admin']],
                                    resize_keyboard=True)


def Statistic(Profile):
    count_active = Profile.objects.filter(is_active=True).count()
    count_block = Profile.objects.filter(is_active=False).count()
    count_all = Profile.objects.all().count()
    msg = (f"umumiy hisob : {count_all}\n"
           f"faol foydalanuvchilar soni : {count_active}\n"
           f"nofaol foydalanuvchilar soni : {count_block}\n")
    return msg


def users_count(update: Update, context: CallbackContext):
    msg = Statistic(Profile)
    update.message.reply_text(msg, reply_markup=admin_buttons)
    return 'adminpanel'


def user_data(update, context):
    msg = ''
    num = 1
    for i in Profile.objects.all():
        msg += f"""{num}. {i.user_id} -> {i.username} -> {i.fistname} -> {i.lastname}\n"""
        num += 1
    update.message.reply_text(msg, reply_markup=admin_buttons)

    return 'adminpanel'


def finder_user_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        'username yoki  id ni  yuboring : \n masalan:   @username yoki @1234567890')

    return 'adminpanel'


def finder_user(update: Update, context: CallbackContext):
    msg = update.message.text
    if msg.startswith('@'):
        msg = msg[1:]
        try:
            user = Profile.objects.get(username=msg)
            msg = f"""{user.user_id} - {user.username} - {user.fistname} - {user.lastname}"""
            update.message.reply_text(msg, reply_markup=admin_buttons)
            return 'adminpanel'
        except:
            try:
                user = Profile.objects.get(user_id=msg)
                msg = f"""{user.user_id} - {user.username} - {user.fistname} - {user.lastname}"""
                update.message.reply_text(msg, reply_markup=admin_buttons)
                return 'adminpanel'
            except:
                msg = 'bunday foydalanuvchi mavjud emas'
                update.message.reply_text(msg, reply_markup=admin_buttons)
                return 'adminpanel'


def bot_admins(update: Update, context: CallbackContext):
    msg = ''
    num = 1
    for i in Admin_bots.objects.filter(bot__name='tozalovchi').all():
        bots = ''
        for j in i.bot.all():
            bots += f""" --{j.name}"""
        msg += f"""{num}. {i.telegram_id} ->  name: {i.name} -> status: {i.status} -->  his bots:  {bots}\n"""
        num += 1
    update.message.reply_text(msg, reply_markup=admin_buttons)
    return 'adminpanel'


list_admin = [

    MessageHandler(Filters.regex('^(' + 'user_counts' + ')$'), users_count),
    MessageHandler(Filters.regex('^(' + 'user_data' + ')$'), user_data),
    MessageHandler(Filters.regex('^(' + 'user_finder' + ')$'), finder_user_text),
    MessageHandler(Filters.regex('^(' + 'bot_admins' + ')$'), bot_admins),
    MessageHandler(Filters.regex(r'@[\w]+.*'), finder_user),

]


#############


def start(update: Update, context: CallbackContext):
    user = update.effective_user
    User_create_or_update(user, Profile)
    id = update.effective_user.id
    if Admin_bots.objects.filter(bot__name='tozalovchi').filter(telegram_id=id).exists():
        update.message.reply_text(f"""Hello Admin""")
        update.message.reply_text(f""" ️Hello {user.username}\n✅ Your id :  {user.id}""", reply_markup=admin_buttons,
                                  parse_mode=ParseMode.HTML)
        return 'adminpanel'
    else:
        update.message.reply_text(f""" 
    🖐️Hello {user.username} 
    ✅ Your id :  {user.id}
        """, parse_mode=ParseMode.HTML)
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
        CommandHandler('admin', start),

    ],
    states={
        'bot': [
            CommandHandler('admin', start),
            MessageHandler(Filters.status_update, delete_group_join_messages),

        ],
        'adminpanel': list_admin,
    },
    fallbacks=[
        CommandHandler('admin', start),
        CommandHandler('start', start),
        MessageHandler(Filters.status_update, delete_group_join_messages),
    ]

)
