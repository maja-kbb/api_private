# Generated by Django 5.1.1 on 2024-11-03 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warsztat_app', '0004_alter_osoba_plec'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='osoba',
            options={'ordering': ['nazwisko'], 'verbose_name_plural': 'Osoby'},
        ),
    ]