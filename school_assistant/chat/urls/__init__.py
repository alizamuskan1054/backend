from django.urls import path, include

urlpatterns = [
    path("", include("chat.urls.admin")),
    # WebSocket routing (ws://.../ws/chat/{session_id}) is NOT here --
    # that's registered separately in config/asgi.py once consumers.py exists.
]