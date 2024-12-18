from django.db import models
from django.core.exceptions import ValidationError
from django.utils.timezone import now  
import datetime
import re

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)




class Stanowisko(models.Model):
    nazwa = models.CharField(max_length = 100)
    opis = models.TextField(blank = True)
    def __str__(self):
        return self.nazwa


class Osoba(models.Model):
    imie = models.CharField(max_length = 50)  # pole tekstowe
    nazwisko = models.CharField(max_length = 50)# pole tekstowe 
    stanowisko = models.ForeignKey(Stanowisko, on_delete = models.SET_NULL, null=True) 
    data_dodania = models.DateField(default = datetime.date.today)

    class Plec(models.IntegerChoices):
        KOBIETA = 1
        MEZCZYZNA = 2
        INNA = 3
    plec = models.IntegerField(choices = Plec.choices)



    def __str__(self):
        return f"{self.imie} {self.nazwisko}"




    class Meta:
        ordering = ["nazwisko"]
        verbose_name_plural = "Osoby"
    def __str__(self):
        return f"{self.imie} {self.nazwisko}"
