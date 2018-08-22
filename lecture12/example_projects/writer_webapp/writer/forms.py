from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo

SMALL_PASSWORD_MESSAGE = "A password must have at least 8 characters"


class LoginForm(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    login = SubmitField("Login")


class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(),
                                                     Length(min=8,
                                                            message=SMALL_PASSWORD_MESSAGE)])
    repeat_password = PasswordField('Repeat Password',
                                    validators=[DataRequired(), EqualTo('password')])

    register = SubmitField("Register")


class CreatePostForm(FlaskForm):
    title = StringField("Article Title", validators=[DataRequired()])
    text = TextAreaField("Article Text", validators=[DataRequired()])
    publish = SubmitField('Publish the article')
    save = SubmitField('Save the article')
