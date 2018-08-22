from flask import request, render_template, redirect, url_for
from flask_login import login_user, current_user, logout_user

from writer import app, db, login_manager
from writer.forms import LoginForm, RegisterForm
from writer.db_tables import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return _home_page()

    form = LoginForm(request.form)

    if request.method == 'POST':
        if form.validate():
            user = User.query.filter_by(email=form.email.data).first()
            if user is not None and user.check_password(form.password.data):
                login_user(user)
                return _home_page()

    render_template("login.html")

@app.route('/logout')
def logout():
    logout_user()
    return _home_page()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return _home_page()

    form = RegisterForm(request.form)

    if request.method == 'POST':
        if form.validate():
            user = User(email=form.email.data,
                        password_hash=User.hash_password(form.password.data),
                        name=form.name.data)
            db.session.add(user)
            db.session.commit()
            return _home_page()

    render_template("register.html")


def _home_page():
    return redirect(url_for('all_posts'))
