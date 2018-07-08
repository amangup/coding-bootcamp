from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class NameForm(FlaskForm):
    username = StringField('Name')
    submit = SubmitField('See your fortune!')
