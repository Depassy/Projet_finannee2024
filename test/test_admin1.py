# chat/tests/test_admin.py

from django.contrib.admin.sites import site
from django.test import TestCase
from chat.admin import SalonAdmin, MessageAdmin

class AdminTest(TestCase):

    def test_list_filter(self):
        admin_site = site
        admin_model = admin_site._registry[SalonAdmin]
        self.assertEqual(admin_model.list_filter.count('status'), 1)
