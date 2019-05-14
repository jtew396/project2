import os

from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit

# Configure application
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():

    # Query for the username
    username = request.form.get("username-create")
    print(username)

    # Make sure the username was successfully passed
    if not username:
        return jsonify({"success": False})



# @app.route("/login", methods=["POST"])
# def register():

#    return jsonify({"success": True, "username": username})




if __name__ == '__main__':
    socketio.run(app)
