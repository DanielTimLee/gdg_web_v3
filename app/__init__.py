from flask import Flask

UPLOAD_FOLDER = '/static/images/coupon'

app = Flask(__name__)

app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

from app.models import *

db.create_all()

from app.routes import *
