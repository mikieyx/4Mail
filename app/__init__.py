from flask import Flask

myapp_obj = Flask(__name__)

myapp_obj.config.from_mapping(
    SECRET_KEY = 'you-will-never-guess'
)

from app import routes

# add the following lines to enable chat functionality
from flask_socketio import SocketIO, emit

# initialize SocketIO
socketio = SocketIO(myapp_obj)

# define event handler for chat messages
@socketio.on('message')
def handle_message(data):
    emit('message', data, broadcast=True)
