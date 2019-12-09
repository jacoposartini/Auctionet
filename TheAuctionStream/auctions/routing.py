from django.urls import include, path
from auctions import consumers

websocket_urlpatterns = [
    path('ws/<int:auction_id>/', consumers.OffersConsumer),
]
















#
