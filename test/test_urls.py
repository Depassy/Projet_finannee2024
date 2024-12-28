# chat/tests/test_urls.py

from django.urls import reverse
from django.test import TestCase

class URLTest(TestCase):

    def test_urls(self):
        response = self.client.get(reverse('forum:index'))  # Remplacer par la route appropriée
        self.assertEqual(response.status_code, 200)  # Test pour vérifier que l'URL existe
