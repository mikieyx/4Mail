from app import myapp_obj
from flask import escape, render_template
from .forms import LoginForm


@myapp_obj.route("/")
def home():
    return render_template('sample.html')

@myapp_obj.route("/register")
def register():
    return render_template('register.html')

@myapp_obj.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', form=form)