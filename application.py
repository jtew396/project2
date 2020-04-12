import os

from flask import Flask, jsonify, render_template, request, session, flash, redirect, url_for
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from helpers import login_required

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)
socketio = SocketIO(app)

users = []
flack_channels = ['Main']

@app.route('/', methods=["GET", "POST"])
@login_required
def index():
    return render_template("index.html", channels=channels)

@app.route('/login', methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("displayname"):
            flash('Must provide display name.')
            print('Must provide display name.')
            return redirect(url_for('login'))
            # return apology("ust provide displayname", 403)

        # Check if the users array already has the displayname
        displayname = request.form.get("displayname")
        if displayname in users:
            flash('That display name is already in use.')
            print('That display name is already in use.')
            print('Users:')
            print(users)
            return redirect(url_for('login'))
        else:
            users.append(displayname)
            # if not users.append(displayname):
            #     flash('Could not save display name.')
            #     print('Could not save display name.')
            #     return redirect(url_for('login'))

        # Remember which user has logged in
        session["user_id"] = displayname

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route('/channels', methods=["GET", "POST"])
@login_required
def channels():
    if request.method == "GET":
        print('Here is the channels array:')
        print(flack_channels)
        return render_template("channels.html", flack_channels=flack_channels)
    else:

        # Check if a channel name was provided
        if not request.form.get("channelname"):
            print('Must provide a channel name.')
            return redirect(url_for('channels'))

        # Add the new channel to the list of channels
        new_channel = request.form.get("channelname")
        if new_channel in flack_channels:
            print('Must provide a novel channel name.')
            return redirect(url_for('channels'))
        else:
            flack_channels.append(new_channel)

        return render_template("channels.html", flack_channels=flack_channels)

@app.route('/channel/<channel_name>')
def channel(channel_name):
    if channel_name not in flack_channels:
        return redirect(url_for('channels'))
    return render_template("channel.html")

# @socketio.on('connect')
# @login_required
# def connect_handler():
#     if session.user_id:
#         emit('my response',
#             {'message': '{0} has joined'.format(session.user_id)},
#             broadcast=True)
#     else:
#         return False

# @socketio.on('message')
# def handleMessage(msg):
#     print('Message: ' + msg)
#     send(msg, broadcast=True)

# @socketio.on('my event')
# def handle_my_custom_event(json):
#     print(json)
#     print('Display Name Created: ' + json["display_name"])
#
#     user_data = {
#         "id": len(users) + 1,
#         "display_name": json["display_name"]
#     }
#
#     # Remember which user id corresponds to their display name
#     session["user_id"] = user_data["id"]
#
#     # Append the user data to the users array
#     users.append(user_data)
#
#     print('User ID: ' + str(session["user_id"]))
#
#     socketio.emit('my response', user_data, broadcoast=True)

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
