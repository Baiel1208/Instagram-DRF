# Generated by Django 4.2.3 on 2023-07-06 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True, verbose_name='Дата создания')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_images/', verbose_name='Фотогария')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]