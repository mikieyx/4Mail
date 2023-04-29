from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import myapp_obj, login, db
import jwt


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

    posts = db.relationship('Post', backref='author', lazy='dynamic')
    task = db.relationship('Task', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        return f'<User {self.id}: {self.username}>'

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
    important = db.Column(db.Boolean, default=False)  # new field for important emails

    def __repr__(self):
        return f'<Email {self.id}: {self.subject}>'

    def star_email(self):
        self.important = True
        db.session.commit()


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
