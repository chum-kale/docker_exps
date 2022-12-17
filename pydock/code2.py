import time
import redis
from flask import Flask

app = Flask(__name__)

@app.route('/')
def count():
    return '<h2>Count stuff</h2>'