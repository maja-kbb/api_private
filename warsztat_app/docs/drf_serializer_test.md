from warsztat_app.models import Osoba, Stanowisko
from warsztat_app.serializers import OsobaSerializer, StanowiskoModelSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io


# serializer stanowisko
stanowisko = Stanowisko(nazwa="projektant", opis="Projektuje rzeczy")
stanowisko.save()
stanowisko_serializer = StanowiskoModelSerializer(stanowisko)
print("Zserializowane dane stanowiska:", stanowisko_serializer.data)


# serializer osoba
osoba = Osoba(imie="Julia", nazwisko="Magowska", stanowisko=stanowisko, data_dodania="2024-11-10", plec = 1)
osoba.save()
osoba_serializer = OsobaSerializer(osoba)
print("Zserializowane dane osoby:", osoba_serializer.data)

# serializacja osoba do formatu JSON
content = JSONRenderer().render(osoba_serializer.data)
print(content)

# deserializacja JSON
stream = io.BytesIO(content)
data = JSONParser().parse(stream)
deserializer = OsobaSerializer(data=data)
deserializer.is_valid()
print(deserializer.validated_data)
deserializer.save()
print(deserializer.data)