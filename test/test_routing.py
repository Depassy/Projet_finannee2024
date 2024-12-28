# chat/tests/test_routing.py

from django.test import TestCase
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.testing import WebsocketCommunicator
from chat.routing import application

class WebSocketRoutingTest(TestCase):
    
    def test_websocket_routes(self):
        # Assurez-vous qu'il n'y a pas de doublons dans les routes WebSocket
        self.assertTrue(URLRouter(application.routing).urlpatterns)
