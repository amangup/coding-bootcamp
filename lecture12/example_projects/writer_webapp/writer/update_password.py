import smtplib

from datetime import datetime, timezone, timedelta
from email.mime.text import MIMEText
from flask import request, flash, redirect, render_template, url_for
from hashlib import blake2b
from secrets import token_urlsafe

from writer import app, db
from writer.db_tables import User, PasswordResetToken

RESET_TOKEN_LENGTH = 32
EMAIL_SUBJECT = "Password Reset link"
EMAIL_TEMPLATE = ("Please use the link below to reset your password.\n{0}")
EMAIL_SENDER_ADDRESS = 'noreply@mywriter.web'


@app.route('/updatepassword')
def update_password():
    token = request.args.get('token')

    if request.method == 'POST':
        email, user = _check_email_and_get_user()
        if user:
            reset_token_id = _add_reset_token_to_db(user)
            _send_email(email, reset_token_id)
            return _show_reset_email_confirmation()
        else:
            flash("No user found with given email address.")
            return _confirm_reset_link()
    else:
        if token:
            return _reset_password()
        else:
            return _confirm_reset_link()


def _check_email_and_get_user():
    email = request.form['email']
    user = None
    if email:
        user = User.query.filter(User.email == email).first()

    return email, user


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

    s = smtplib.SMTP('localhost')
    s.send_message(email_message)
    s.quit()

