import flask, os, random, json
from flask_sock import Sock
from middleware import pin_protected
from dotenv import load_dotenv

load_dotenv()

app = flask.Flask(__name__)
sock = Sock(app)   