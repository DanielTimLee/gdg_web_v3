from flask import Flask

app = Flask(__name__)

app.config.from_object('config')

from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

from app.models import *

db.create_all()

from app.routes import *
