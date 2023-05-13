from django.core.management.base import BaseCommand
from telegram import Update, Bot
from telegram.ext import Updater
from apps.getmyid.views import conv_handler
class Command(BaseCommand):
    help = 'Says hello to the user'
    def handle(self, *args, **options):
        bot = Bot(token='TOKEN')
        updater = Updater(token='TOKEN', use_context=True)
        updater.dispatcher.add_handler(conv_handler)
        updater.start_polling()
        updater.idle()
