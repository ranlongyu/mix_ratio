from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create flask app
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from main_app import model, routes
