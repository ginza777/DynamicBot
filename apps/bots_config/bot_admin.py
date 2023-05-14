from django.db.models import Q
from apps.getmyid.views import *

# ##########################buttons---------------------------

admin_buttons = ReplyKeyboardMarkup([["user_counts", "user_data"], ['bot_admins','user_finder'],['GetMyID']],
                                    resize_keyboard=True)


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
                user=Profile.objects.get(user_id=msg)
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
    for i in Admin_bots.objects.filter(bot__name='getmyid').all():
        bots = ''
        for j in i.bot.all():
            bots += f""" --{j.name}"""
        msg += f"""{num}. {i.telegram_id} ->  name: {i.name} -> status: {i.status} -->  his bots:  {bots}\n"""
        num += 1
    update.message.reply_text(msg, reply_markup=admin_buttons)
    return 'adminpanel'


def Statistic(Model):
    count_active = Model.objects.filter(is_active=True).count()
    count_block = Model.objects.filter(is_active=False).count()
    count_all = Model.objects.all().count()
    msg = (f"umumiy hisob : {count_all}\n"
           f"faol foydalanuvchilar soni : {count_active}\n"
           f"nofaol foydalanuvchilar soni : {count_block}\n")
    return msg


list_admin = [


    MessageHandler(Filters.regex('^(' + 'user_counts' + ')$'), users_count),
    MessageHandler(Filters.regex('^(' + 'user_data' + ')$'), user_data),
    MessageHandler(Filters.regex('^(' + 'user_finder' + ')$'), finder_user_text),
    MessageHandler(Filters.regex('^(' + 'bot_admins' + ')$'), bot_admins),
    MessageHandler(Filters.regex(r'@[\w]+.*'), finder_user),



]
