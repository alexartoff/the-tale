# Generated by Django 3.1.13 on 2021-11-09 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tt_events_log', '0004_auto_20211018_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='data',
            field=models.JSONField(default=dict),
        ),
    ]
