import functools
from flask import request
from flask_login import current_user
from flask_socketio import disconnect, emit

def authenticated_only(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        if not current_user.is_authenticated:
            disconnect()
        else:
            return f(*args, **kwargs)
    return wrapped

# @socketio.on('my event')
# @authenticated_only
# def handle_my_custom_event(data):
#     emit('my response', {'message': '{0} has joined'.format(current_user.name)},
#          broadcast=True)
