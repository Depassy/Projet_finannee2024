# urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Route pour la page d'accueil des sujets
    path('', views.index, name='index'),
    
    # Route pour afficher un sujet spécifique
    path('sujet/<slug:slug>/', views.sujet_detail, name='sujet_detail'),
    
    # Route pour afficher une réponse spécifique
    path('reponse/<int:id>/', views.reponse_detail, name='reponse_detail'),
]
