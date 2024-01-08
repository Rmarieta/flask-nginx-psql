from flask_socketio import emit, send
from app import socketio

@socketio.on('message')
def handle_message(message):
    print('Received message:', message)
    emit('response', {'data': 'Server received your message'})

@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received my_event: ' + str(json))