from flask_socketio import emit, send, join_room, leave_room
from app import socketio, redis_client
import os
from flask import request

@socketio.on('connect')
def handle_connect():
    con_type = request.args.get('conType')  # Assuming students are identified by 'student' conType
    user_id = request.args.get('userId')

    print('\nCONNECT:\n',{ con_type, user_id },'\n')

    if con_type == 'STUDENT':
        print('\nADDING TO REDIS CLIENT\n')
        redis_client.sadd('connected_users', user_id)

@socketio.on('disconnect')
def handle_disconnect():
    con_type = request.args.get('conType')
    user_id = request.args.get('userId')

    if con_type == 'STUDENT':
        redis_client.srem('connected_users', user_id)

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