# chat/tests/test_routing.py

from django.test import TestCase
from chat.routing import application

class RoutingTest(TestCase):

    def test_duplicate_routes(self):
        # Vérifiez qu'il n'y a pas de doublons dans les routes définies
        routes = application.routing
        self.assertEqual(len(routes), len(set(routes)))  # Vérifie qu'il n'y a pas de doublons
