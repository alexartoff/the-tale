# Generated by Django 3.2.9 on 2021-11-11 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobs', '0007_fill_mobs_properties'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobrecord',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
