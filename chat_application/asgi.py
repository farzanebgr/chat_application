import os
import chat.routing

# Reference to the currently authenticated user
from channels.auth import AuthMiddlewareStack

# For routing according to type
from channels.routing import ProtocolTypeRouter, URLRouter

# Factory function which returns an OriginValidator configured to use
from channels.security.websocket import AllowedHostsOriginValidator

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chat_application.settings")
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    # Protocol for http request!
    "http": get_asgi_application(),
    #Protocol for websocket request!!
    "websocket": AllowedHostsOriginValidator(
        # Authenticated user in scope
        AuthMiddlewareStack(
            # Routing url
            URLRouter(
                # Read urls from this file
                chat.routing.websocket_urlpatterns
            )
        )
    ),
})