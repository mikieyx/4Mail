from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_mail import Mail
from config import Config
import os

myapp_obj = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

myapp_obj.config.from_mapping(
    SECRET_KEY = '4mail',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)

myapp_obj.config['MAIL_SERVER'] = 'smtp.gmail.com'
myapp_obj.config['MAIL_PORT'] = 587
myapp_obj.config['MAIL_USE_TLS'] = True
myapp_obj.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
myapp_obj.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')

db = SQLAlchemy(myapp_obj)

migrate = Migrate(myapp_obj, db)

login = LoginManager(myapp_obj)
login.login_view = 'login'

login.init_app(myapp_obj)

bootstrap = Bootstrap(myapp_obj)

mail = Mail(myapp_obj)

from app import routes, models