from rest_framework import serializers
from .models import Osoba, Stanowisko, User

class OsobaSerializer(serializers.Serializer):
    imie = serializers.CharField(max_length = 50)# pole tekstowe
    nazwisko = serializers.CharField(max_length = 50)# pole tekstowe 
    stanowisko = serializers.PrimaryKeyRelatedField(queryset = Stanowisko.objects.all(), allow_null=True) 
    data_dodania = serializers.DateField(read_only = True)
    plec = serializers.ChoiceField(choices=Osoba.Plec.choices)

    def create(self, validated_data):
        return Osoba.objects.create(**validated_data) 
    
    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.stanowisko = validated_data.get('stanowisko', instance.stanowisko)
        instance.data_dodania = validated_data.get('data_dodania', instance.data_dodania)
        instance.plec = validated_data.get('plec', instance.plec)
        instance.save()
        return instance
    

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email']

class StanowiskoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stanowisko
        fields = ['nazwa','opis']