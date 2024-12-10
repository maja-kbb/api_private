from django.urls import path, include 
from . import views

urlpatterns = [
    
    path('osoby/', views.osoba_list, name='osoba-list'),
    path('osoby/<int:pk>/', views.osoba_detail, name='osoba-detail'),
    path('osoby/filtrowane/<str:substring>/', views.osoba_filter, name='osoba-filter'),
    path('stanowiska/', views.stanowisko_list, name='stanowisko-list'),
    path('stanowiska/<int:pk>/', views.stanowisko_detail, name='stanowisko-detail'),
    path('osoby/update/<int:pk>/', views.osoba_update_delete, name='osoba-update'),
    path('osoby/delete/<int:pk>/', views.osoba_update_delete, name='osoba-delete'),
    path('welcome/', views.welcome_view, name = 'welcome-view'),
    path('osoby_html/', views.osoba_list_html, name = 'osoba-list-html'),
    path('osoby_html/<int:id>/', views.osoba_detail_html, name = 'osoba-detail-html'),
]
