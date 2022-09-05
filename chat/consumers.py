import json

from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # Accepts an incoming socket
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        # Change type from json to python object ...
        text_data_dict = json.loads(text_data)
        # Get value of python object from key message ...
        message = text_data_dict['message']
        # Reply message by type json
        self.send(text_data=json.dumps({
            'message':message
        }))
