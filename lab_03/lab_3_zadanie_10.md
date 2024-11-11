
# 1 - wyświetl wszystkie obiekty modelu Osoba
osoba = Osoba.objects.all()

# 2 - wyswietl obiekt modelu Osoba z id = 3
osoba_id_3 = Osoba.objects.get(id=3)

# 3 - wyświetl obiekty modelu Osoba, których nazwa rozpoczyna się na wybraną przez Ciebie literę alfabetu (tak, żeby był co najmniej jeden wynik)
osoby_M = Osoba.objects.filter(imie__startswith='M')

# 4 - wyświetl unikalną listę stanowisk przypisanych dla modeli Osoba
uniq_stanowiska = Osoba.objects.distinct()

# 5 - wyświetl nazwy stanowisk posortowane alfabetycznie malejąco
stanowiska_desc = Stanowisko.objects.order_by('-nazwa')

# 6 - dodaj nową instancję obiektu klasy Osoba i zapisz w bazie
osoba_new = Osoba(imie = "Patryk", nazwisko = "Bochen", stanowisko=Stanowisko.objects.first())
osoba_new.save()