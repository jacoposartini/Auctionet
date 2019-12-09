from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from auctions.models import Auction
from datetime import datetime

class OffersConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['auction_id']
        self.room_group_name = 'chat_%s' % self.room_name

        if Auction.objects.filter(id=self.room_name,
            expiration_date__gte=datetime.now()).exists():
            async_to_sync(self.channel_layer.group_add)(
                self.room_group_name,
                self.channel_name
            )
            self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        offer = int(text_data)
        auction = Auction.objects.get(id=self.room_name)
        if offer > auction.current_price:
            auction.current_price = offer
            auction.winner = self.scope['user']
            auction.save()
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'broadcast_message',
                    'offer': offer,
                    'sender': self.scope['user'].username
                }
            )

    def broadcast_message(self, event):
        offer = event['offer']
        sender = event['sender']
        self.send(text_data=json.dumps({
            'offer': offer,
            'sender': sender
        }))







#
