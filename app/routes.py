from app import myapp_obj
from flask import escape
from flask import render_template


@myapp_obj.route("/")
def home():
    return render_template('sample.html')
