import smtplib

from datetime import datetime, timezone, timedelta
from email.mime.text import MIMEText
from flask import request, flash, redirect, render_template, url_for
from flask_login import current_user, login_user
from hashlib import blake2b
from secrets import token_urlsafe
from sqlalchemy.exc import SQLAlchemyError

from writer import app, db
from writer.db_tables import User, PasswordResetToken
from writer.forms import ResetPasswordEmailForm, PasswordUpdateForm

RESET_TOKEN_LENGTH = 32
EMAIL_SUBJECT = "Password Reset link"
EMAIL_TEMPLATE = "Please use the link below to reset your password.\n{0}"
EMAIL_SENDER_ADDRESS = 'noreply@mywriter.web'


@app.route('/password_reset_email', methods=['GET', 'POST'])
def password_reset_email():
    if request.method == 'POST':
        form = ResetPasswordEmailForm(request.form)
        if form.validate():
            return _generate_token_and_send_email(form)
        else:
            flash("Provided email is not valid.")

    email = None
    if current_user.is_authenticated:
        email = current_user.email

    return _confirm_reset_link(email)


@app.route('/update_password', methods=['GET', 'POST'])
def update_password():
    if current_user.is_authenticated:
        redirect(url_for('all_posts'))

    token_id = request.args.get('token')

    if not token_id:
        return redirect(url_for('all_posts'))

    if request.method == 'POST':
        form = PasswordUpdateForm(request.form)
        if form.validate():
            try:
                _reset_password(token_id, form)
                return redirect(url_for('all_posts'))
            except SQLAlchemyError:
                flash("Couldn't reset the password due to a technical issue."
                      "Please try again later.")
        else:
            flash("Correct the password field errors.")

    return _show_reset_password_form(token_id)


def _generate_token_and_send_email(form):
    email = form.email.data
    user = _get_user(email)
    if user:
        try:
            reset_token_id = _add_reset_token_to_db(user)
            _send_email(email, reset_token_id)
            return _show_reset_email_confirmation(email)
        except (SQLAlchemyError, smtplib.SMTPConnectError):
            flash("Couldn't send the reset email due to a technical issue."
                  "Please try again later.")
    else:
        flash("No user found with given email address.")

    return _confirm_reset_link()


def _get_user(email):
    user = None
    if email:
        user = User.query.filter(User.email == email).first()

    return user


def _add_reset_token_to_db(user):
    reset_token_id = token_urlsafe(RESET_TOKEN_LENGTH)
    token_hash = blake2b(reset_token_id.encode()).hexdigest()
    token_expiration = datetime.now(timezone.utc) + timedelta(hours=1)

    token = PasswordResetToken(user_id=user.id,
                               token_hash=token_hash,
                               token_expiration=token_expiration,
                               token_used=False)
    db.session.add(token)
    db.session.commit()

    return reset_token_id


def _send_email(email, reset_token_id):
    password_reset_url = url_for('update_password', _external=True,
                                 token=reset_token_id)
    email_text = EMAIL_TEMPLATE.format(password_reset_url)

    email_message = MIMEText(email_text)
    email_message['Subject'] = EMAIL_SUBJECT
    email_message['From'] = EMAIL_SENDER_ADDRESS
    email_message['To'] = email

    with smtplib.SMTP('localhost') as smtp:
        smtp.send_message(email_message)


def _show_reset_email_confirmation(email):
    return render_template("reset_email_confirm.html", email=email)


def _confirm_reset_link(email=None):
    form = ResetPasswordEmailForm()
    form.email.data = email
    return render_template("reset_email.html", form=form)


def _reset_password(token_id, form):
    token = _get_token(token_id)
    user = token.user
    user.password_hash = User.password_hash(form.password.data)
    token.token_used = True

    db.session.commit()

    login_user(user)


def _show_reset_password_form(token_id):
    token = _get_token(token_id)
    if not token:
        return "The password reset token is not valid."

    current_time = datetime.now(timezone.utc)
    if current_time > token.expiration:
        return "The password reset token has expired."

    form = ResetPasswordEmailForm()
    return render_template("update_password.html", form=form)


def _get_token(token_id):
    token_hash = blake2b(token_id.encode()).hexdigest()
    return PasswordResetToken.query.get(token_hash)
