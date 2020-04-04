import os

from flask import Flask, jsonify, render_template, request, session
from flask_login import login_user, current_user, LoginManager, UserMixin
# from flask_session import Session
from flask_socketio import SocketIO, send, emit, join_room, leave_room
# from tempfile import mkdtemp

# Configure application
app = Flask(__name__)
# Set the Secret Key
app.config["SECRET_KEY"] = os.urandom(24)
# app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')
# Initialize SocketIO
socketio = SocketIO(app)
# Initialize Flask Login Manager
# login_manager = LoginManager()
# login_manager.init_app(app)

# Configure session to use filesystem (instead of signed cookies)
# app.config["SESSION_FILE_DIR"] = mkdtemp()
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

# Flask Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

# Flask Login User Model
class User(UserMixin):
    number_of_users = 0
    # user_database = {}

    def __init__(self, id):
        self.id = id
        self.name = "user" + str(id)
        self.display_name = self.name
        # user_database[self.id] = {
        #     'name': self.name,
        #     'display_name': self.display_name
        # }
        # self.password = self.name + "_secret"
        User.number_of_users += 1

    def __repr__(self):
        return "%d/%s" % (self.id, self.name)
        # return "%d/%s/%s" % (self.id, self.name, self.password)

    @classmethod
    def get(cls, id):
        return cls.user_database.get(id)

# Universal variables
# user = []
# users = []

@app.route("/", methods=["GET", "POST"])
def index():
    if current_user.is_authenticated:
        return render_template("index.html")
    else:
        user = User(User.number_of_users + 1)
        login_user(user)
        return render_template("index.html")

    # print("We made it to index.")
    # if session:
    #     if session["user_id"]:
    #         print("We have logged in as ID: " + str(session.user_id))
    # return render_template("index.html", user=user)

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# Implmenting auto-login so I don't need a login route
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     # Here we use a class of some kind to represent and validate our
#     # client-side form data. For example, WTForms is a library that will
#     # handle this for us, and we use a custom LoginForm to validate.
#     form = LoginForm()
#     if form.validate_on_submit():
#         # Login and validate the user.
#         # user should be an instance of your `User` class
#         login_user(user)
#
#         flask.flash('Logged in successfully.')
#
#         next = flask.request.args.get('next')
#         # is_safe_url should check if the url is safe for redirects.
#         # See http://flask.pocoo.org/snippets/62/ for an example.
#         if not is_safe_url(next):
#             return flask.abort(400)
#
#         return flask.redirect(next or flask.url_for('index'))
#     return flask.render_template('login.html', form=form)

# @app.route("/logout")
# @login_required           # <- not defined
# def logout():
#     logout_user()
#     return redirect(somewhere)
#
# @socketio.on('connect')
# def connect_handler():
#     if current_user.is_authenticated:
#         emit('my response',
#              {'message': '{0} has joined'.format(current_user.name)},
#              broadcast=True)
#     else:
#         return False  # not allowed here

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
