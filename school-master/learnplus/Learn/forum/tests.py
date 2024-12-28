# tests.py

from django.test import TestCase
from .models import Sujet
from django.contrib.auth.models import User

class SujetModelTest(TestCase):
    
    def test_sujet_creation(self):
        # Création d'un utilisateur pour associer au sujet
        user = User.objects.create_user(username='testuser', password='password')
        
        # Création d'un sujet
        sujet = Sujet.objects.create(
            titre="Test Sujet", 
            question="Quelle est la question?",
            user=user  # Associer l'utilisateur
        )
        
        # Vérification du titre et du slug du sujet
        self.assertEqual(sujet.titre, "Test Sujet")
        self.assertTrue(sujet.slug)  # Vérifier que le slug a bien été généré
