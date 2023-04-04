import flask, os, random, json
from flask_sock import Sock
from middleware import pin_protected
from dotenv import load_dotenv

load_dotenv()

clients = []

app = flask.Flask(__name__, static_folder='public', template_folder='templates')
app.config['SECRET_KEY'] = os.urandom(24).hex()
sock = Sock(app)   

import websocket

@pin_protected
@app.get('/')
def index():
    return flask.render_template('index.html')

@app.get('/login')
def login():
    return flask.render_template('login.html')

@app.post('/login') 
def login_post():
    pin = flask.request.form.get('pin')
    if pin == os.getenv('PIN'):
        flask.session['authenticated'] = True
        return flask.redirect('/')
    return flask.redirect('/login')

app.run(host='0.0.0.0', port=5000, debug=True)

