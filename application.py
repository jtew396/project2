import os

from flask import Flask, jsonify, render_template, request, session
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from helpers import login_required

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)
socketio = SocketIO(app)

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():


@socketio.on('connect')a
def connect_handler():
    if current_user.is_authenticated:
        emit('my response',
            {'message': '{0} has joined'.format(current_user.name)},
            broadcast=True)
    else:
        return False

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)

@socketio.on('my event')
def handle_my_custom_event(json):
    print(json)
    print('Display Name Created: ' + json["display_name"])

    user_data = {
        "id": len(users) + 1,
        "display_name": json["display_name"]
    }

    # Remember which user id corresponds to their display name
    session["user_id"] = user_data["id"]

    # Append the user data to the users array
    users.append(user_data)

    print('User ID: ' + str(session["user_id"]))

    socketio.emit('my response', user_data, broadcoast=True)

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(username + ' has entered the room.', room=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', room=room)


if __name__ == '__main__':
    socketio.run(app)
