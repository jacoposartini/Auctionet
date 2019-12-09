from channels.routing import ProtocolTypeRouter, URLRouter
from .wsgi import *
from .token_auth import TokenAuthMiddleware

import auctions.routing
application = ProtocolTypeRouter({
    'websocket': TokenAuthMiddleware(
        URLRouter(
            auctions.routing.websocket_urlpatterns
        )
    ),
})










#
