# Generated by Django 3.1.13 on 2021-11-09 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistics', '0002_fullstatistics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fullstatistics',
            name='data',
            field=models.JSONField(),
        ),
    ]
