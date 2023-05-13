from django.core.management.base import BaseCommand
from telegram import Bot
from telegram.ext import Updater
from apps.getmyid.views import conv_handler
class Command(BaseCommand):
    help = 'Says hello to the user'
    def handle(self, *args, **options):
        bot = Bot(token='6274466132:AAF5F7f4suS8tP9kv1Wgy-p90wGude3irGI')
        updater = Updater(token='6274466132:AAF5F7f4suS8tP9kv1Wgy-p90wGude3irGI', use_context=True)
        updater.dispatcher.add_handler(conv_handler)
        updater.start_polling()
        updater.idle()
