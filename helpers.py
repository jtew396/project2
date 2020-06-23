import json

from flask import redirect, render_template, request, session
from functools import wraps
from datetime import datetime

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

def create_payload(user_id, msg):
    dict = {
        'user_id': user_id,
        'msg': msg,
        'timestamp': datetime.now().strftime("%m/%d/%y %H:%M:%S")
    }
    payload = json.dumps(dict)
    return payload
