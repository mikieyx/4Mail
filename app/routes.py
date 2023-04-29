from .forms import LoginForm, RegistrationForm, CheckPasswordForm, ResetPasswordRequestForm, ResetPasswordForm
from app import myapp_obj, db
from flask import render_template, redirect, flash, request, url_for
from flask_login import current_user, login_user, logout_user, login_required
from .models import User
from .email import send_password_reset_email
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

@myapp_obj.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
        
    form = ResetPasswordRequestForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user: send_password_reset_email(user)

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
    user = User.query.get_or_404(id) #attempt to get that task by the id and if it doesn't exist -> going to 404

    try:
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('home'))
    except:
        return 'There was something wrong when deleting your account!'