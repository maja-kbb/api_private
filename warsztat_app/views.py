from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.decorators import permission_required, login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404
import datetime
from .models import Osoba, Stanowisko
from .permissions import CustomDjangoModelPermissions
from .serializers import OsobaSerializer, StanowiskoModelSerializer
from django.contrib.auth import logout


class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": "Wylogowano pomyślnie"})

# Wyświetlenie listy obiektów Osoba
@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def osoba_list(request):
    if request.method == 'GET':
        if not request.user.has_perm('warsztat_app.view_other_person'):
            osoby = Osoba.objects.filter(wlasciciel=request.user)
        else:
            osoby = Osoba.objects.all()
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = OsobaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(wlasciciel=request.user)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



# Wyświetlenie, dodanie i usunięcie pojedynczego obiektu Osoba
@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated, CustomDjangoModelPermissions])
@permission_required('warsztat_app.view_osoba')
def osoba_detail(request, pk):
    #if not request.user.has_perm('warsztat_app.view_person'):
        #raise PermissionDenied()
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def osoba_update(request, pk):

    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Osoba
    :return: Response (with status and/or object/s data)
    """
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = OsobaSerializer(osoba, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   
@api_view(['DELETE'])    
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def osoba_delete(request, pk):
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
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





def welcome_view(request):
    now = datetime.datetime.now()
    html = f"""
        <html><body>
        Witaj użytkowniku! </br>
        Wygrałeś nowy iPhone 6S! </br>
        Aktualna data i czas na serwerze: {now}.
        </body></html>"""
    return HttpResponse(html)


@login_required
@permission_required('warsztat_app.view_osoba')
def osoba_list_html(request):
    # pobieramy wszystkie obiekty Person z bazy poprzez QuerySet
    osoby = Osoba.objects.all()
    return render(request,
                  "warsztat_app/osoba/list.html",
                  {'osoby': osoby})


def osoba_detail_html(request, id):
    # pobieramy konkretny obiekt Person
    try:
        osoba = Osoba.objects.get(id=id)
    except Osoba.DoesNotExist:
        raise Http404("Obiekt Person o podanym id nie istnieje")

    return render(request,
                  "warsztat_app/osoba/detail.html",
                  {'osoba': osoba})


class StanowiskoMemberView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            stanowisko = Stanowisko.objects.get(pk=pk)
        except Stanowisko.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        
        osoby = Osoba.objects.filter(stanowisko = stanowisko)
        serializer = OsobaSerializer(osoby, many = True)
        return Response(serializer.data)