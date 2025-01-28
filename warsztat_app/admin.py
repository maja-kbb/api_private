from django.contrib import admin

# Register your models here.
from .models import Osoba, Stanowisko




class OsobaAdmin(admin.ModelAdmin):
    readonly_fields = ['data_dodania']
    list_display = ('imie', 'nazwisko', 'stanowisko_display', 'data_dodania')
    list_filter = ('stanowisko', 'data_dodania')

    def stanowisko_display(self, obj):
        # Sprawdza, czy stanowisko nie jest None, i zwraca odpowiedni tekst
        if obj.stanowisko:
            return f"{obj.stanowisko.nazwa} ({obj.stanowisko.id})"
        return "Brak"
    

class StanowiskoAdmin(admin.ModelAdmin):
  
    list_display = ('nazwa', 'opis')
    
    list_filter = ('nazwa',) 

admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Stanowisko)