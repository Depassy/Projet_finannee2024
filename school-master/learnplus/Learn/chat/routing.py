from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/instructor/messages/(?P<classe>\w+)/$', consumers.ChatConsumer),
    re_path(r'ws/student/messages/(?P<classe>\w+)/$', consumers.ChatConsumer),
]
