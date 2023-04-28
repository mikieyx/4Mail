from flask import render_template, flash, redirect, url_for, request
from .forms import LoginForm, RegistrationForm, ChatForm
from app import myapp_obj

@myapp_obj.route("/")
@myapp_obj.route("/hello")
def hello():
    #return "Hello, welcome to 4Mail! Please log in to start sending chats."
    return render_template('hello.html')

@myapp_obj.route("/index")
def index():
    recipient = 'RecipientName' # assume recipient's username is "RecipientName"
    return render_template('index.html', recipient=recipient)

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # TODO: Add login functionality
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@myapp_obj.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # TODO: Add registration functionality
        flash(f'Account created for {form.username.data}!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

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
