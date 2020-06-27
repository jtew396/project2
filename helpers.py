import json

from flask import redirect, render_template, request, session
from functools import wraps
from datetime import datetime
from time import mktime

def login_required(f):
    """
    Decorate routes to require login.
    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def create_payload(user_id, data):
    timestamp = datetime.now()
    payload = {

        # 'socket_id': data['socket_id'],
        'message_id': user_id + str(int(mktime(timestamp.timetuple()))),
        'user_id': user_id,
        'msg': data['msg'],
        'timestamp': timestamp.strftime("%m/%d/%y %H:%M:%S")
    }
    return payload
