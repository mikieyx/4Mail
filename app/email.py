from threading import Thread
from flask_mail import Message
from app import mail, myapp_obj
from flask import render_template

# Function sends 1 email using the flask-mail extension:
# Parameters: a subject line, sender address, recipient addresses, a plain-text message body, and 1 HTML message body
def send_email(subject, sender, recipients, text_body, html_body):
    # Creates 1 new message object with the given subject, sender, and recipients:
    msg = Message(subject, sender=sender, recipients=recipients)
    # Set the plain-text message body:
    msg.body = text_body
    # Set the HTML message body:
    msg.html = html_body
    # Creates 1 new thread to send the email asynchronously:
    Thread(target=send_async_email, args=(myapp_obj, msg)).start()

# Function sends an email asynchronously using the flask-mail extension:
# Parameters: a Flask app object and a message object
def send_async_email(app, msg):
    # Create 1 app context for the Flask app:
    with myapp_obj.app_context():
        # Use the Flask-Mail extension to send the message:
        mail.send(msg)
