# Generated by Django 5.1.3 on 2024-11-28 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='Базовое описание товара', max_length=200),
        ),
    ]
