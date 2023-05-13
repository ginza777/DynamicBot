from django.core.management.base import BaseCommand
from telegram import Bot
from telegram.ext import Updater, MessageHandler, Filters
from apps.tozalovchi.views import *
from apps.bots_config.models import Bot_Token
TOKEN=Bot_Token.objects.get(name='tozalovchi').token

class Command(BaseCommand):
    help = 'Says hello to the user'
    def handle(self, *args, **options):
        bot = Bot(token=TOKEN)
        updater = Updater(token=TOKEN, use_context=True)

        updater.dispatcher.add_handler(MessageHandler(Filters.status_update, delete_group_join_messages)),

        updater.dispatcher.add_handler(conv_handler)
        updater.start_polling()
        updater.idle()

