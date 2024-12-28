# chat/tests/test_admin.py

from django.contrib.admin.sites import site
from django.test import TestCase
from chat.admin import SalonAdmin, MessageAdmin

class AdminTest(TestCase):
    
    def test_search_field(self):
        # Assurez-vous que search_fields est bien utilisé
        admin_site = site
        admin_model = admin_site._registry[SalonAdmin]
        self.assertTrue('search_fields' in admin_model.__dict__)
