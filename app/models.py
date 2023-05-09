from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import myapp_obj, login, db
from time import time
import jwt
import base64


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            myapp_obj.config['SECRET_KEY'], algorithm='HS256')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, myapp_obj.config['SECRET_KEY'], algorithms=[
                            'HS256'])['reset_password']
        except:
            return
        return User.query.get(id)

    def __repr__(self):
        return f'<User {self.id}: {self.username}>'

# TODO Delete this
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Post {self.id}: {self.body}>'


class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(120), nullable=False)
    recipient = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(120), nullable=False)
    body = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Task user {self.id}: {self.name}>'

# Adds a one to many relationship with the user
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    dueDate = db.Column(db.DATE())

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Task user {self.id}: {self.name}>'


with myapp_obj.app_context():
    db.create_all()


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
