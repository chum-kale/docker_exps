import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = flask(__name__)

@app.route('/')
