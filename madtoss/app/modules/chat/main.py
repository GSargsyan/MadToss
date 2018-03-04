import jinja2
import os
from collections import deque
from flask import session
from flask_uwsgi_websocket import GeventWebSocket

from app import app, db

"""
template_dir = os.path.dirname(os.path.abspath(__file__)) +  '/templates'
loader = jinja2.FileSystemLoader(template_dir)
environment = jinja2.Environment(loader=loader)
"""

websocket = GeventWebSocket(app)

backlog = deque()
users = {}

def init_chat():
    pass

@websocket.route('/chat')
def chat(ws):
    users[ws.id] = ws
    #for msg in backlog:
    #    ws.send(msg)

    while True:
        msg = ws.receive()
        ws.send("Got " + msg.decode())
        if msg is not None:
            backlog.append(msg)
            for id in users:
                if id != ws.id:
                    users[id].send(msg)
        else:
            break

    del users[ws.id]
