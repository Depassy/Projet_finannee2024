from django.test import TestCase
from .models import Salon, Message
from school.models import Classe
from django.contrib.auth.models import User

class SalonTestCase(TestCase):
    def test_create_salon(self):
        classe = Classe.objects.create(name="Classe Test")
        salon = Salon.objects.create(classe=classe, nom="Salon Test")
        self.assertEqual(salon.nom, "Salon Test")
