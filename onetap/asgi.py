"""
ASGI config for onetap project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/

"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onetap.settings')

django.setup()




from beacon.routing import websocket_urlpatterns
from channels.security.websocket import AllowedHostsOriginValidator
from beacon.middleware import JwtAuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
django_asgi_app = get_asgi_application()



application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            JwtAuthMiddlewareStack(
                URLRouter(
                    websocket_urlpatterns
                )
            ),
        ),
    }
)
