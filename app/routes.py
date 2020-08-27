# ...
from flask_login import current_user, login_user
from flask_login import login_required
from app.models import User
from flask_login import logout_user
from app.forms import RegistrationForm
from app import db
from app import app
from flask import render_template, flash, redirect,url_for, session
from app.forms import RegistrationForm, LoginForm
# ...


SECRET_KEY = 'my super secret key'.encode('utf8')

@app.route('/')
@app.route('/index')
@login_required
def index():
    if "USERNAME" in session:
        username = session["USERNAME"]

    return render_template("index.html",user = username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        sess_name = user.username
        # print(form.remember_me.data)
        # input()
        session["USERNAME"] = sess_name
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    print("logging out")
    logout_user()
    return redirect(url_for('index'))



@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)