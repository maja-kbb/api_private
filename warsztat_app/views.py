from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Osoba, Stanowisko
from .serializers import OsobaSerializer, StanowiskoModelSerializer

# Wyświetlenie listy obiektów Osoba
@api_view(['GET', 'POST'])
def osoba_list(request):
    if request.method == 'GET':
        osoby = Osoba.objects.all()
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = OsobaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



# Wyświetlenie, dodanie i usunięcie pojedynczego obiektu Osoba
@api_view(['GET', 'DELETE'])
def osoba_detail(request, pk=None):
    if request.method == 'GET':
        osoba = get_object_or_404(Osoba, pk=pk)
        serializer = OsobaSerializer(osoba)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        osoba = get_object_or_404(Osoba, pk=pk)
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Wyświetlenie listy Osób zawierających zadany ciąg znaków w polu nazwa
@api_view(['GET'])
def osoba_filter(request, substring):
    osoby = Osoba.objects.filter(imie__icontains=substring) | Osoba.objects.filter(nazwisko__icontains=substring)
    serializer = OsobaSerializer(osoby, many=True)
    return Response(serializer.data)

# Wyświetlenie listy obiektów Stanowisko
@api_view(['GET', 'POST'])
def stanowisko_list(request):
    if request.method == 'GET':
        stanowiska = Stanowisko.objects.all()
        serializer = StanowiskoModelSerializer(stanowiska, many=True)
        return Response(serializer.data)
 
    elif request.method == 'POST':
        serializer = StanowiskoModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Wyświetlenie, dodanie i usunięcie pojedynczego obiektu Stanowisko
@api_view(['GET','DELETE'])
def stanowisko_detail(request, pk=None):
    if request.method == 'GET':
        stanowisko = get_object_or_404(Stanowisko, pk=pk)
        serializer = StanowiskoModelSerializer(stanowisko)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        stanowisko = get_object_or_404(Stanowisko, pk=pk)
        stanowisko.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OsobaList(APIView):
    def get(self, request):
        osoby = Osoba.objects.all()
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = OsobaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class OsobaDetail(APIView):
    def get(self, request, pk = None):
        if request.method == 'GET':
            osoba = get_object_or_404(Osoba, pk=pk)
            serializer = OsobaSerializer(osoba)
            return Response(serializer.data)
    
    def delete(self, request, pk = None):
        osoba = get_object_or_404(Osoba, pk=pk)
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


