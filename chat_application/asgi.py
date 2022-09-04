import os
#For routing according to type
from channels.routing import ProtocolTypeRouter

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_application.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # Just HTTP for now. (We can add other protocols later.)
})