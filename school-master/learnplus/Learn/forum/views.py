# views.py

from django.shortcuts import render, get_object_or_404
from .models import Sujet, Reponse

# Vue pour afficher tous les sujets
def index(request):
    sujets = Sujet.objects.all()  # Récupérer tous les sujets
    return render(request, 'forum/index.html', {'sujets': sujets})

# Vue pour afficher un sujet spécifique avec ses réponses
def sujet_detail(request, slug):
    sujet = get_object_or_404(Sujet, slug=slug)  # Récupérer le sujet par slug
    reponses = Reponse.objects.filter(sujet=sujet)  # Récupérer les réponses associées
    return render(request, 'forum/sujet_detail.html', {'sujet': sujet, 'reponses': reponses})

# Vue pour afficher une réponse spécifique
def reponse_detail(request, id):
    reponse = get_object_or_404(Reponse, id=id)  # Récupérer la réponse par ID
    return render(request, 'forum/reponse_detail.html', {'reponse': reponse})
