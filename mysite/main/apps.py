import threading
from django.apps import AppConfig
import asyncio
import websockets


class MainConfig(AppConfig):
    name = 'main'

    # def ready(self):
    #     print(True)
    #     a = test()
    #     b = threading.Thread(target=a.run())
    #     b.start()
    #     print("server run")

# class test():
#     async def echo(self,websocket, path):
        
#         print('echo')
#         async for message in websocket:
#             print(message,'received from client')
#             greeting = f"Hello {message}!"
#             await websocket.send(greeting)
#             print(f"> {greeting}")
    
#     def run(self):
#         try:
#             print("123")
#             asyncio.get_event_loop().run_until_complete(websockets.serve(self.echo, 'localhost', 8765))
#             print("456")
#             asyncio.get_event_loop().run_forever()
#             print("789")
#         except Exception as e:
#             print(e)
#             print("server close")