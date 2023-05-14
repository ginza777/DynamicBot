from django.db import models

# Create your models here.


class TelegramApi(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    token=models.CharField(max_length=200,null=True,blank=True)
    api_id=models.CharField(max_length=200,null=True,blank=True)
    api_hash=models.CharField(max_length=200,null=True,blank=True)
    channel=models.CharField(max_length=200,null=True,blank=True)
    group=models.CharField(max_length=200,null=True,blank=True)
    phone_number=models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.api_id

    class Meta:
        verbose_name='Telegram Api'
        verbose_name_plural='Telegram Apis'
        db_table='telegram_api'


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
    bot=models.ManyToManyField('Bot_Token',related_name='bot_token')
    is_active=models.BooleanField(default=True)
    status=models.CharField(max_length=50,null=True,blank=True ,choices=(('admin','admin'),('partner','partner'),('block','block')),default='partner')


    class Meta:
        verbose_name='Admin_bots'
        verbose_name_plural='Admin_bots'
        db_table='admin_bots'


    def __str__(self):
        return self.name