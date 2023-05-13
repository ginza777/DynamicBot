from django.contrib import admin
from .models import Bot_Token,Admin_bots

@admin.register(Bot_Token)
class Bot_TokenAdmin(admin.ModelAdmin):
    list_display=['name','token','extra_field']


# Register your models here.

@admin.register(Admin_bots)
class Admin_botsAdmin(admin.ModelAdmin):
    list_display=['telegram_id','name','bot','is_active']
    list_filter=['telegram_id','name','bot','is_active']
