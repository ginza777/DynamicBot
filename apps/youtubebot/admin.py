from django.contrib import admin
from apps.youtubebot.models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'username', 'fistname', 'lastname', 'is_active', 'is_bot','language_code']
    list_editable = ['is_active']
