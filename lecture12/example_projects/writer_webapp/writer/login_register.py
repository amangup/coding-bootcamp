from secrets import token_hex

from flask import request, render_template, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.urls import url_parse

from writer import app, db, login_manager
from writer.forms import LoginForm, RegisterForm
from writer.db_tables import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    next_page = request.args.get('next')

    if current_user.is_authenticated:
        return _continue_browsing(next_page)

    form = LoginForm(request.form)

    if request.method == 'POST':
        if form.validate():
            user = User.query.filter_by(email=form.email.data).first()
            if user is not None and user.check_password(form.password.data):
                login_user(user)
                return _continue_browsing(next_page)
            else:
                flash("No user with email-id found, or the password is "
                      "incorrect.")
        else:
            print("Invalid or incomplete input.")

    safe_next_page = _get_safe_url(next_page)
    login_action = (url_for('login') if safe_next_page is None
                    else url_for('login', next=safe_next_page))
    return render_template("login.html", form=form, login_action=login_action)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    next_page = request.args.get('next')
    return _continue_browsing(next_page)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return _continue_browsing()

    form = RegisterForm(request.form)

    if request.method == 'POST':
        if form.validate():
            try:
                return _add_user_to_db(form)
            except SQLAlchemyError:
                flash("We couldn't register you due to a technical issue"
                      " on our side. Please try again later.")
        else:
            flash("The form was not properly completed.")

    return render_template("register.html", form=form)


def _add_user_to_db(form):
    user = User(id=token_hex(32),
                email=form.email.data,
                password_hash=User.hash_password(form.password.data),
                name=form.name.data)
    db.session.add(user)
    db.session.commit()
    login_user(user)
    return _continue_browsing()


def _continue_browsing(next_page=None):
    safe_next_page = _get_safe_url(next_page)
    if safe_next_page:
        return redirect(next_page)
    else:
        return redirect(url_for('all_posts'))


def _get_safe_url(next_page):
    # URL form: scheme://netloc/path;parameters?query#fragment
    # If netloc is empty, it means the URL is relative, which we want to ensure
    # so that we don't send our user to other domains.
    if next_page and not url_parse(next_page).netloc:
        return next_page