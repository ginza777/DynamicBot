from django.contrib import admin
from .models import Bot_Token,Admin_bots,TelegramApi

@admin.register(Bot_Token)
class Bot_TokenAdmin(admin.ModelAdmin):
    list_display=['id','name','token','extra_field']


# Register your models here.

@admin.register(Admin_bots)
class Admin_botsAdmin(admin.ModelAdmin):
    list_display=['id','name','telegram_id','status','is_active']
    list_filter=['id','name','telegram_id','status','is_active']

@admin.register(TelegramApi)
class TelegramApiAdmin(admin.ModelAdmin):
    list_display=['id','name','token','api_id','api_hash','channel','group','phone_number']
    list_filter=['id','name','token','api_id','api_hash','channel','group','phone_number']