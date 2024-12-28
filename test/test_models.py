# chat/tests/test_models.py

from django.test import TestCase
from chat.models import Salon

class SalonTest(TestCase):
    
    def test_default_name(self):
        salon = Salon.objects.create()  # Nom par défaut
        self.assertIsNotNone(salon.nom)  # Le nom doit être généré
