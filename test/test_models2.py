# chat/tests/test_models.py

from django.core.exceptions import ValidationError
from django.test import TestCase
from chat.models import Message

class MessageTest(TestCase):

    def test_message_length_validation(self):
        long_message = "a" * 1001  # Dépasse la longueur maximale
        with self.assertRaises(ValidationError):
            message = Message.objects.create(text=long_message)
