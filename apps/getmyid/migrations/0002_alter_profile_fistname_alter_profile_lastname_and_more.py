# Generated by Django 4.2.1 on 2023-05-13 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getmyid', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fistname',
            field=models.TextField(blank=True, null=True, verbose_name='First_name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lastname',
            field=models.TextField(blank=True, null=True, verbose_name='Lastname'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_id',
            field=models.IntegerField(verbose_name='user id'),
        ),
    ]