from django.db import models

# Create your models here.

class Bot_Token(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    token=models.CharField(max_length=200,null=True,blank=True)
    extra_field=models.CharField(max_length=200,null=True,blank=True)
    phone_number=models.CharField(max_length=200,null=True,blank=True)
    bot_username=models.CharField(max_length=200,null=True,blank=True)


    class Meta:
        verbose_name='Bot Token'
        verbose_name_plural='Bot Tokens'
        db_table='bot_token'


    def __str__(self):
        return self.name

class Admin_bots(models.Model):
    telegram_id=models.CharField(max_length=200,null=True,blank=True)
    name=models.CharField(max_length=200,null=True,blank=True)
    bot=models.ForeignKey(Bot_Token,on_delete=models.SET_NULL,null=True,blank=True)
    is_active=models.BooleanField(default=True)


    class Meta:
        verbose_name='Admin_bots'
        verbose_name_plural='Admin_bots'
        db_table='admin_bots'


    def __str__(self):
        return self.name