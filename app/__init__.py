# Import all the modules that we need to initialize in this project:
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_mail import Mail
import os

# Initialize our Flask app:
myapp_obj = Flask(__name__)

# Telling our Flask app where our database is located:
basedir = os.path.abspath(os.path.dirname(__file__))

myapp_obj.config.from_mapping(
    SECRET_KEY = '4mail',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)

# Configure things we need to let 1 gmail account automatically send password reset link to users:
myapp_obj.config['MAIL_SERVER'] = 'smtp.gmail.com'
myapp_obj.config['MAIL_PORT'] = 587
myapp_obj.config['MAIL_USE_TLS'] = True
myapp_obj.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
myapp_obj.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')

# Database is initialized with the settings from our app:
db = SQLAlchemy(myapp_obj)

# Initializes a Migrate object that is bound to the Flask application and its database to execute DB migrations:
migrate = Migrate(myapp_obj, db)

# Initializes LoginManager to manage lots of functionalities of login and logout for users:
login = LoginManager(myapp_obj)
login.login_view = 'login'

login.init_app(myapp_obj)

# Initializes Bootstrap for our Flask app:
bootstrap = Bootstrap(myapp_obj)

# Initializes Mail for our Flask app to let it send and receive emails:
mail = Mail(myapp_obj)

# add the following lines to enable chat functionality
from flask_socketio import SocketIO, emit

# initialize SocketIO
socketio = SocketIO(myapp_obj)

# define event handler for chat messages
@socketio.on('message')
def handle_message(data):
    emit('message', data, broadcast=True)

from app import routes, models
