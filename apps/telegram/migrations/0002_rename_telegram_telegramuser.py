# Generated by Django 4.2.3 on 2023-08-07 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Telegram',
            new_name='TelegramUser',
        ),
    ]
