import os

from flask import Flask, jsonify, render_template, request, session
from flask_session import Session
from flask_socketio import SocketIO, send, emit
from tempfile import mkdtemp

# Configure application
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Universal variables
user = []
users = []

@socketio.on('message')

@app.route("/", methods=["GET", "POST"])
def index():

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure that a display name was submitted
        # Need to write this condition

        # Gather the display_name string from the JS AJAX POST request
        display_name = request.form['display_name']

        # Create a user data dict to save to the users array
        user_data = {
            "id": users.length + 1,
            "display_name": display_name
        }

        # Remember which user id corresponds to their display name
        session["user_id"] = user_data["id"]

        # Append the user data to the users array
        users.append(user_data)

    else:

        print("We made it to index.")
        return render_template("index.html", user=user)

@socketio.on("message")
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Create a Display Name for the user"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("display_name"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

# @app.route("/register", methods=["POST"])
# def register():
#     print("We made it to register...")
#     # Query for the username
#     username = request.form.get("username-create")
#     print(username)
#
#     # Make sure the username was successfully passed
#     if not username:
#         return jsonify({"success": False})
#
#     return jsonify({"success": True, "username": username})
#
# @socketio.on("send message")
# def message(data)
#     selection = data["selection"]
#     emit("message", {"message": message}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
