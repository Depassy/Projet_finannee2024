# chat/tests/test_consumers.py

from django.test import TestCase
from chat.consumers import ChatConsumer

class ChatConsumerTest(TestCase):

    def test_receive_invalid_command(self):
        consumer = ChatConsumer()
        invalid_message = {"invalid_command": "data"}
        with self.assertRaises(KeyError):  # En cas de commande inconnue
            consumer.receive(invalid_message)
