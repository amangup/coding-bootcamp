from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField


class WordForm(FlaskForm):
    word = StringField('Word')
    language = SelectField(u'Language', choices=[('en', 'English (US)'),
                                                 ('es', 'Spanish')])
    submit = SubmitField('See Word Definitions')
