import os
import chat.routing

# Reference to the currently authenticated user
from channels.auth import AuthMiddlewareStack

# For routing according to type
from channels.routing import ProtocolTypeRouter, URLRouter

# Factory function which returns an OriginValidator configured to use
from channels.security.websocket import AllowedHostsOriginValidator

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_application.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    )
})