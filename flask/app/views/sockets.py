from flask_socketio import emit, send, join_room, leave_room
from app import socketio
import os

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

@socketio.on('chat')
def chat(data):    
    print("chat "+str(data))
    emit('chat', "From hostname " + os.uname().nodename + " : " + data['message'], broadcast=True, to=data['room'])

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send("From hostname " + os.uname().nodename + " : " + username + ' has entered the room.', to=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send("From hostname " + os.uname().nodename + " : " + username + ' has left the room.', to=room)