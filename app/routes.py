from .forms import LoginForm, RegistrationForm
from app import myapp_obj, db
from flask import render_template, flash, redirect, request, url_for
from flask_login import current_user, login_user, logout_user, login_required
from .models import User
import time

@myapp_obj.route('/', methods=['GET', 'POST'])
def home():
    return render_template('sample.html')

@myapp_obj.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('sample'))
    
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        
        if user is None:
            flash('Invalid Username')
            return redirect(url_for('login'))
        if not user.check_password(form.password.data):
            flash('Invalid Password')
            return redirect(url_for('login'))
        
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('sample'))
    
    return render_template('login.html', title='Sign In for 4Mail', form=form)

@myapp_obj.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('sample'))
    
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()
        flash(f'Congratulations, {form.username.data} is an 4Mail user now!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
