from django.urls import re_path
from chat import consumers

# Like urls.py such as (urlpatterns) with (websocket_urlpatterns) and (path) with (re_path)
# as_asgi() has performance like as_view()
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]