from django.urls import path
from . import views

urlpatterns = [
    
    path('osoby/', views.OsobaList.as_view(), name='osoba-list'),
    path('osoby/<int:pk>/', views.OsobaDetail.as_view(), name='osoba-detail'),
    path('osoby/filtrowane/<str:substring>/', views.osoba_filter, name='osoba-filter'),
    path('stanowiska/', views.stanowisko_list, name='stanowisko-list'),
    path('stanowiska/<int:pk>/', views.stanowisko_detail, name='stanowisko-detail'),
]
