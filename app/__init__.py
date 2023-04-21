from app import routes, models
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
<<<<<<< HEAD
from flask_login import LoginManager
=======
>>>>>>> 8d085a97572d23837dbfeb16d1d0beb4b48677be

myapp_obj = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

myapp_obj.config.from_mapping(
<<<<<<< HEAD
    SECRET_KEY = 'you-are-the-users',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)

db = SQLAlchemy(myapp_obj)

login = LoginManager(myapp_obj)

login.login_view = 'login'

from app import routes, models
=======
    SECRET_KEY='4mail',
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(myapp_obj)
>>>>>>> 8d085a97572d23837dbfeb16d1d0beb4b48677be
