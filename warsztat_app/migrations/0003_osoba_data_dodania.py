# Generated by Django 5.1.1 on 2024-11-03 15:13

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warsztat_app', '0002_stanowisko_osoba'),
    ]

    operations = [
        migrations.AddField(
            model_name='osoba',
            name='data_dodania',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]