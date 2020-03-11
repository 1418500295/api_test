import os
from socket import create_connection

from websocket import *
import sys
project_path = os.path.dirname(os.getcwd())
sys.path.append(project_path)

ws = create_connection("ws://127.0.0.1:1347/test/demo/?name=daine")


ws.send("hello daine")
print("接收中")
result = ws.recv()
print(result)
ws.close()