from channels.auth import AuthMiddlewareStack
from django.contrib.auth.models import AnonymousUser
from users.models import CustomUser

class TokenAuthMiddleware:
    def __init__(self, inner):
        self.inner = inner

    def __call__(self, scope):
        token_name, token_key = (scope['subprotocols'][0],
                                    scope['subprotocols'][1])

        try:
            if token_name == 'Token':
                user = CustomUser.objects.get(token=token_key)
                scope['user'] = user
        except CustomUser.DoesNotExist:
            scope['user'] = AnonymousUser()
        return self.inner(scope)

TokenAuthMiddlewareStack = lambda inner: TokenAuthMiddleware(
                                            AuthMiddlewareStack(inner))























#
