from django.urls import path
from . import views

urlpatterns = [
    # Пустой путь '' будет открывать список
    path('', views.aquarium_list, name='aquarium_list_url'),
    
    # Путь 'create/' будет открывать форму
    path('create/', views.create_aquarium, name='create_aquarium_url'),
]