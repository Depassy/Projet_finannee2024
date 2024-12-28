# chat/tests/test_websockets.py

from channels.testing import WebsocketCommunicator
from chat.routing import application
import json

class WebSocketConnectionTest(TestCase):

    async def test_websocket_connection(self):
        communicator = WebsocketCommunicator(application, path="/ws/chat/")
        connected, subprotocol = await communicator.connect()
        self.assertTrue(connected)
        await communicator.send_json_to({"message": "Hello"})
        response = await communicator.receive_json_from()
        self.assertEqual(response['message'], "Hello")
        await communicator.disconnect()
