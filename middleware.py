import flask
from functools import wraps

def pin_protected(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not flask.session:
            return flask.redirect('/login')
        return f(*args, **kwargs)
    return decorated_function