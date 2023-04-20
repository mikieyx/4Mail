from app import myapp_obj
from flask import escape
from flask import render_template


@myapp_obj.route("/")
def home():
    return render_template('sample.html')

@myapp_obj.route("/register")
def register():
    return render_template('register.html')

@myapp_obj.route("/login")
def logIn():
    return render_template('login.html')
