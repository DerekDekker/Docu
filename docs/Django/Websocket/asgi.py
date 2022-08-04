"""
ASGI config for Websocket project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Websocket.settings')

application = get_asgi_application()


from Websocket.middleware import websockets
application = websockets(application)


# async def application(scope, receive, send):
#     # print(scope)
#     if scope['type'] == 'http':
#         await http_application(scope, receive, send)
#
#     elif scope['type'] == 'websocket':
#         print('websocket方式')
#         await websocket_application(scope, receive, send)