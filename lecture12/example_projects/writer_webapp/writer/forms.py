from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length



class LoginForm(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = StringField("Password", validators=[DataRequired()])
    login = SubmitField("Login")


SMALL_PASSWORD_MESSAGE = "A password must have at least 8 characters"

class RegisterForm(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = StringField("Password", validators=[DataRequired(),
                                                   Length(min=8, message=SMALL_PASSWORD_MESSAGE)])
    name = StringField("Name", validators=[DataRequired()])
    register = SubmitField("Register")

