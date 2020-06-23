import os

from flask import Flask, jsonify, render_template, request, session, flash, redirect, url_for
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from helpers import login_required, create_payload

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
        session["room"] = 'Main'

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
        print(request.form)
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

@app.route('/chat', methods=["GET", "POST"])
def chat():
    if request.method == "GET":
        return render_template("channels.html", flack_channels=flack_channels)
    else:
        # Check if a channel name was provided
        if not request.form.get("channelname"):
            print('Must provide a channel name.')
            return redirect(url_for('channels'))

        channel_name = request.form.get("channelname")

        # Check if the channel exists in the flack channels
        if channel_name not in flack_channels:
            return redirect(url_for('channels'))

        # Make the channel the new room
        session['room'] = request.form.get("channelname")

        return render_template("chat.html", flack_channel=channel_name)

@socketio.on('send_message', namespace='/chat')
def handleMessage(msg):
    # room = session['room']
    payload = create_payload(session['user_id'], msg)
    print(payload)
    print('Message: ' + msg)
    send(payload, json=True, broadcast=True)

@socketio.on('join', namespace='/chat')
def on_join():
    username = session['user_id']
    room = session['room']
    join_room(room)
    msg = username + ' has entered the room.'
    payload = create_payload(username, msg)
    emit('send_message', payload, json=True, room=room)

@socketio.on('leave', namespace='/chat')
def on_leave():
    username = session['user_id']
    room = session['room']
    leave_room(room)
    msg = username + ' has left the room.'
    payload = create_payload(username, msg)
    emit('send_message', payload, json=True, room=room)


if __name__ == '__main__':
    socketio.run(app)
