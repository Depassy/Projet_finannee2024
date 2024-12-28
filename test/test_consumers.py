# chat/tests/test_consumers.py

from django.test import TestCase
from chat.models import Message

class MessageTest(TestCase):
    
    def test_message_to_json(self):
        message = Message.objects.create(text="Hello", user=user, photo=None)
        self.assertIsNone(message.photo)
        # Test de la méthode message_to_json
        try:
            message_json = message.message_to_json()
            self.assertIsInstance(message_json, dict)
        except Exception as e:
            self.fail(f"Error in message_to_json: {e}")
