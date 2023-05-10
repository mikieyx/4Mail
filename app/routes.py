from .forms import LoginForm, RegistrationForm, CheckPasswordForm, ResetPasswordRequestForm, ResetPasswordForm, ChatForm
from app import myapp_obj, db, mail
from flask import render_template, redirect, flash, request, url_for
from flask_mail import Message
from flask_login import current_user, login_user, logout_user, login_required
from .models import User, Email, Task
from datetime import datetime
import time
import http.client
import urllib.parse
import json


@myapp_obj.route('/', methods=['GET', 'POST'])
def home():
    # Renders the home.html template when the user navigates to the root URL:
    return render_template('home.html')


@myapp_obj.route('/login', methods=['GET', 'POST'])
def login():
    # If the user is already logged in (authenticated), redirect the user to the home page:
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    # Create an instance of the LoginForm:
    form = LoginForm()

    # If the form has been submitted and all fields are valid, attempt to log the user in:
    if form.validate_on_submit():
        # Query the User table for a user with the specified username:
        user = User.query.filter_by(username=form.username.data).first()

        # If the user doesn't exist, flash an error message and redirect to the login page:
        if user is None:
            flash('Invalid Username')
            return redirect(url_for('login'))
        # If the entered password is incorrect, flash an error message and redirect to the login page:
        if not user.check_password(form.password.data):
            flash('Invalid Password')
            return redirect(url_for('login'))

        # If the user exists and the entered password is correct, log the user in and redirect the user to the home page:
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('home'))

    # Render the login.html template with the LoginForm instance:
    return render_template('login.html', title='Sign In for 4Mail', form=form)


@myapp_obj.route('/register', methods=['GET', 'POST'])
def register():
    # If the user is already authenticated (logged in), redirect the user to the home page:
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    # Create an instance of the RegistrationForm:
    form = RegistrationForm()

    # If the form has been submitted and all fields are valid, attempt to create 1 new user:
    if form.validate_on_submit():
        # Check if 1 user with the same username already exists in the database:
        if db.session.query(User).filter_by(username=form.username.data).count() < 1:
            # Create 1 new User object with the form data and add it to the database:
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            # Flash a success message and redirect to the login page:
            flash(f'Congratulations, {form.username.data} is an 4Mail user now!')
            return redirect(url_for('login'))
        else:
            # If 1 user with the same username already exists, flash an error message and redirect to the login page:
            flash(f'Sorry, {form.username.data} is already an 4Mail user!')
            return redirect(url_for('login'))

    # Render the register.html template with the RegistrationForm instance:
    return render_template('register.html', title='Register 4Mail', form=form)


@myapp_obj.route('/inbox')
def inbox():
    # This filters the emails according to the current user's email address as a recipient:
    emails = Email.query.filter_by(recipient=current_user.email).all()
    # Render the inbox.html template with the list of emails:
    return render_template('inbox.html', emails=emails)


@myapp_obj.route('/logout')
def logout():
    #  Log the user out and redirect to the login page:
    logout_user()
    return redirect(url_for('login'))

# Function sends 1 email with 1 password reset link to the user:
def send_reset_email(user):
    # Generate a reset password token for the user:
    token = user.get_reset_password_token()

    # Construct the message object with the recipient email, sender email, and subject:
    msg = Message('Password Reset Request', sender='nguyenhoaianhhsgs@gmail.com', recipients=[user.email])
    
    # Set the email body with the password reset link and 1 message:
    msg.body = f'''To reset your password, visit the following link:
{url_for('reset_password', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    
    # Send the email to the user:
    mail.send(msg)

# This route handles the password reset request form:
@myapp_obj.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    # If the user is already logged in (authenticated), redirect the user to the home page:
    if current_user.is_authenticated:
        return redirect(url_for('home'))
        
    # Create an instance of the reset password request form:
    form = ResetPasswordRequestForm()

    # If the form has been submitted and is valid:
    if form.validate_on_submit():
        # Finds the user by user's email address:
        user = User.query.filter_by(email=form.email.data).first()

        # If the user exists, send the reset password email:
        if user: send_reset_email(user)

        # Flash a message to the user to check their email for password reset instructions:
        flash('In order to see the instructions to reset your password, check your email!')

        # Redirect the user to the login page:
        return redirect(url_for('login'))
    
    # Render the reset password request page:
    return render_template('reset_password_request.html', title='Reset Password', form=form)

# This route handles the reset password form:
@myapp_obj.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    # If the user is already logged in (authenticated), redirect them to the home page:
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    # Verifies the reset password token and get the user from database:
    user = User.verify_reset_password_token(token)

    # If the user doesn't exist, redirect to the home page: 
    if not User: return redirect(url_for('home'))

    # Creates 1 instance of the reset password form:
    form = ResetPasswordForm()

    # If the form has been submitted and is valid:
    if form.validate_on_submit():
        # Sets the user's new password and Commits this change to the database:
        user.set_password(form.password.data)
        db.session.commit()

        # Flash 1 message to the user that the user's password has been reset successfully:
        flash('Congratulations! Your password has already reset!')
        flash('Now you can login to your account through your new password!')

        # Redirect the user to the login page:
        return redirect(url_for('login'))
    
    # Render the reset password page:
    return render_template('reset_password.html', form=form)

# This route handles the user account deletion:
@myapp_obj.route('/delete/<int:id>')
def delete(id):
    # attempt to get the user by provided id, and if it doesn't exist -> return 404 error
    user = User.query.get_or_404(id)

    try:
        # Delete the user from the database:
        db.session.delete(user)
        db.session.commit()

        # Redirect the user to the home page:
        return redirect(url_for('home'))
    except:
        # If there was 1 error while deleting the user's account, display 1 error message:
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

# Todo page needs to gather all the tasks that were created by the current user
# from the data base and pass it into the html
@myapp_obj.route("/todo")
@login_required
def todo():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('todo.html', tasks=tasks)


# The route to add a task to the database. Gather the necessary information from filling out the form
# and add it to the database. After adding it to the database we redirect to the todo page so that
# it will show the updated task list
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

# The route to delete the task. After deleting, we redirect to the todo page to
# reflect the updated todo list
@myapp_obj.route('/todo/<int:task_id>', methods=['POST'])
def deleteTask(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('todo'))


# Create a quick article object to better store the articles.
class Article:
    def __init__(self, author, title, image, url):
        self.author = author
        self.title = title
        self.image = image
        self.url = url


@myapp_obj.route('/news')
def news():
    # To display news, the application needs to make an api request to mediastack api
    # I have to establish an http connection and get the correct parameters
    # Then I will make the get request to the api
    conn = http.client.HTTPConnection('api.mediastack.com')
    params = urllib.parse.urlencode({
        'access_key': '3e6930adc8f22818321f218a9aca99ab',
        'countries': "us",
        'sort': 'published_desc',
    })
    conn.request('GET', '/v1/news?{}'.format(params))

    # After making the request, I format the response in a more manageable way
    res = conn.getresponse()
    data = res.read()
    data = json.loads(data)

    # Now that I have a json format of the response, I will parse through the json
    # object and gather all the articles that have an image  and store it in the arrray
    # I have initiated a counter so that we only get 4 articles max
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

    # After getting the articles, I pass in the list of articles to the html file
    return render_template('news.html', articles=articles)
