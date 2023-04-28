from flask import render_template, flash, redirect, url_for, request
from .forms import LoginForm, RegistrationForm, ChatForm
from app import myapp_obj, db
from flask_login import current_user, login_user, logout_user, login_required
from .models import User
import time

@myapp_obj.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@myapp_obj.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
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
        return redirect(url_for('home'))
    
    return render_template('login.html', title='Sign In for 4Mail', form=form)

@myapp_obj.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = RegistrationForm()

    if form.validate_on_submit():
        if db.session.query(User).filter_by(username=form.username.data).count() < 1:
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash(f'Congratulations, {form.username.data} is an 4Mail user now!')
            return redirect(url_for('login'))
        else:
            flash(f'Sorry, {form.username.data} is already an 4Mail user!')
            return redirect(url_for('login'))
    
    return render_template('register.html', title='Register 4Mail', form=form)

@myapp_obj.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@myapp_obj.route("/chat", methods=['GET', 'POST'])
def chat():
    form = ChatForm()
    if form.validate_on_submit():
        recipient = form.recipient.data
        message = form.message.data
        # TODO: Send the chat message to the recipient
        flash(f'Message sent to {recipient}: {message}')
        return redirect(url_for('chat'))
    return render_template('chat.html', form=form)