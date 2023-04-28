from app import myapp_obj
from .forms import LoginForm
from flask import escape, redirect
from flask import render_template


@myapp_obj.route("/")
def home():
    return render_template('base.html')


@myapp_obj.route("/register")
def register():
    return render_template('register.html')


@myapp_obj.route("/login", methods=['GET', 'POST'])
def logIn():
    form = LoginForm()
    if form.validate_on_submit():
        print('Hi Valid Input')
        return redirect('/')
    return render_template('login.html')
