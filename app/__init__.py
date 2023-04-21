from app import routes, models
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

myapp_obj = Flask(__name__)
# myapp_obj.config.from_mapping(..)

db = SQLAlchemy(myapp_obj)
