# Generated by Django 3.2.9 on 2021-11-11 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emissaries', '0003_auto_20211109_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emissary',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
