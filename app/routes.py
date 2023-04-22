from .forms import LoginForm
from app import myapp_obj
from flask import render_template, redirect, flash
from flask_login import current_user, login_user, logout_user, login_required


@myapp_obj.route("/")
def home():
    return render_template('sample.html')

@myapp_obj.route("/register")
def register():
    return render_template('register.html')

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    # create form
    form = LoginForm()
    # if form inputs are valid
    if form.validate_on_submit():
        # search database for username
        # user = User.query.filter_by(...)
        # check the password
        # if password matches
        # login_user(user)
        flash(f'Here are the input {form.username.data} and {form.password.data}')
        return redirect('/')
    return render_template('login.html', form=form)