from .forms import LoginForm, RegistrationForm, CheckPasswordForm, ResetPasswordRequestForm, ResetPasswordForm, ChatForm
from app import myapp_obj, db, mail
from flask import render_template, redirect, flash, request, url_for
from flask_login import current_user, login_user, logout_user, login_required
from flask_mail import Message
from .models import User, Email, Task
from datetime import datetime
import time
import http.client
import urllib.parse
import json


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
            flash(
                f'Congratulations, {form.username.data} is an 4Mail user now!')
            return redirect(url_for('login'))
        else:
            flash(f'Sorry, {form.username.data} is already an 4Mail user!')
            return redirect(url_for('login'))

    return render_template('register.html', title='Register 4Mail', form=form)


@myapp_obj.route('/inbox')
def inbox():
    #This filters the emails according to the current user's email address as a recipient
    emails = Email.query.filter_by(recipient=current_user.email).all()
    return render_template('inbox.html', emails=emails)


@myapp_obj.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

def send_reset_email(user):
    token = user.get_reset_password_token()
    msg = Message('Password Reset Request', sender='nguyenhoaianhhsgs@gmail.com', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('reset_password', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)

@myapp_obj.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
        
    form = ResetPasswordRequestForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user: send_reset_email(user)

        flash('In order to see the instructions to reset your password, check your email!')

        return redirect(url_for('login'))
    
    return render_template('reset_password_request.html', title='Reset Password', form=form)

@myapp_obj.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    user = User.verify_reset_password_token(token)

    if not User: return redirect(url_for('home'))

    form = ResetPasswordForm()

    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()

        flash('Congratulations! Your password has already reset!')
        flash('Now you can login to your account through your new password!')

        return redirect(url_for('login'))
    
    return render_template('reset_password.html', form=form)

@myapp_obj.route('/delete/<int:id>')
def delete(id):
    # attempt to get that task by the id and if it doesn't exist -> going to 404
    user = User.query.get_or_404(id)

    try:
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('home'))
    except:
        return 'There was something wrong when deleting your account!'

@myapp_obj.route('/send_email', methods=['GET', 'POST'])
def send_email():
    if request.method == 'POST':
        sender = request.form['sender']
        recipient = request.form['recipient']
        subject = request.form['subject']
        body = request.form['message']

        email = Email(sender=sender, recipient=recipient,
                      subject=subject, body=body)
        db.session.add(email)
        db.session.commit()

        return 'Email sent!'

    return render_template('Email.html')


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


@myapp_obj.route("/todo")
@login_required
def todo():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('todo.html', tasks=tasks)


@myapp_obj.route('/todo/add', methods=['POST'])
@login_required
def add_task():
    name = request.form['name']
    dueDate = request.form['dueDate']
    dueDate = datetime.strptime(dueDate, '%Y-%m-%d').date()
    task = Task(name=name, dueDate=dueDate, user_id=current_user.id)
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('todo'))


@myapp_obj.route('/todo/<int:task_id>', methods=['POST'])
def deleteTask(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('todo'))


class Article:
    def __init__(self, author, title, image, url):
        self.author = author
        self.title = title
        self.image = image
        self.url = url


@myapp_obj.route('/news')
def news():
    conn = http.client.HTTPConnection('api.mediastack.com')
    params = urllib.parse.urlencode({
        'access_key': '3e6930adc8f22818321f218a9aca99ab',
        'countries': "us",
        'sort': 'published_desc',
    })
    conn.request('GET', '/v1/news?{}'.format(params))
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data)
    articles = []
    counter = 0
    while (len(articles) < 4):
        if data["data"][counter]["image"] is not None:
            author = data["data"][counter]["author"]
            title = data["data"][counter]["title"]
            img = data["data"][counter]["image"]
            url = data["data"][counter]["url"]
            article = Article(author, title, img, url)
            articles.append(article)
        counter += 1

    return render_template('news.html', articles=articles)
