from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import myapp_obj, login, db
from time import time
import jwt
import base64

# Set up the table User with different columns in Database:
class User(db.Model, UserMixin):
    # User's ID:
    id = db.Column(db.Integer, primary_key=True)
    # Username:
    username = db.Column(db.String(32), nullable=False)
    # User's password:
    password = db.Column(db.String(32), nullable=False)
    # User's email:
    email = db.Column(db.String(100), nullable=False, unique=True)

    # Set up relationship with class Post:
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    # Function which generates password hash for user's password --> more protected!
    def set_password(self, password):
        self.password = generate_password_hash(password)

    # Function which checks the hash of password given by user and the password in Database:
    def check_password(self, password):
        return check_password_hash(self.password, password)

    # Function which generates a reset password token for the user:
    # The token will expire after 600 seconds (10 mins)
    def get_reset_password_token(self, expires_in=600):
        # Generates token by using the encode() method of PyJWT package: 
        return jwt.encode(
            # The dictionary below contains the data which will be encoded
            # with our Flask app's secret key to sign the token
            # and hashing algorithm 'HS256' for that token signature:
            {'reset_password': self.id, 'exp': time() + expires_in},
            myapp_obj.config['SECRET_KEY'], algorithm='HS256')

    # This static method verifies 1 reset password token then returns corresponding user:
    @staticmethod
    def verify_reset_password_token(token):
        try:
            # Decoding token by decode() method in PyJWT package:
            id = jwt.decode(token, myapp_obj.config['SECRET_KEY'], algorithms=['HS256'])['reset_password']
        except:
            # If the token is invalid (or has been already expired) --> None:
            return
        # If the token is valid --> the user object corresponding to the user id in the token.
        return User.query.get(id)

    # Function that returns 1 string every time creating 1 new row (user): 
    def __repr__(self):
        return f'<User {self.id}: {self.username}>'

# Set up the table Post with different columns in Database:
class Post(db.Model):
    # Post ID:
    id = db.Column(db.Integer, primary_key=True)
    # Post Body:
    body = db.Column(db.String(256))
    # Post timestamp:
    timestamp = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)

    # Set up relationship with class User:
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # Function that returns 1 string every time creating 1 new Post element in Database:
    def __repr__(self):
        return f'<Post {self.id}: {self.body}>'

# Set up the table Email with different columns in Database:
class Email(db.Model):
    # Email's ID:
    id = db.Column(db.Integer, primary_key=True)
    # Email's Sender:
    sender = db.Column(db.String(120), nullable=False)
    # Email's Recipient:
    recipient = db.Column(db.String(120), nullable=False)
    # Email's Subject:
    subject = db.Column(db.String(120), nullable=False)
    # Email's Body:
    body = db.Column(db.Text, nullable=False)

    # Function that returns 1 string every time creating 1 new Email element in Database:
    def __repr__(self):
        return f'<Email {self.id}: {self.name}>'

# Set up the table Task with different columns in Database:
class Task(db.Model):
    # Task's ID:
    id = db.Column(db.Integer, primary_key=True)
    # Task's Name:
    name = db.Column(db.String(256))
    # Task's dueDate:
    dueDate = db.Column(db.DATE())

    # Set up relationship with class User:
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Task user {self.id}: {self.name}>'

# Create all the tables by calling create_all() method of the db object 
# within the application context to ensure that the app's database connection is available:
with myapp_obj.app_context():
    db.create_all()

# This is a callback function used by Flask-Login to load a user from a user ID.
# The 'id' argument is the user ID as a string, 
# which we convert to an integer before querying the database for the user:
@login.user_loader
# The function returns a User object or None if no user is found with the given ID.
def load_user(id):
    return User.query.get(int(id))
