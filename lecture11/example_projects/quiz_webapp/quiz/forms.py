from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField, \
    FieldList
from wtforms.validators import DataRequired


CHOICES = [('1', 'Option A'),
           ('2', 'Option B'),
           ('3', 'Option C'),
           ('4', 'Option D')]


class QuestionForm(FlaskForm):
    question = TextAreaField('Question')
    option_a = StringField('Option A')
    option_b = StringField('Option B')
    option_c = StringField('Option C')
    option_d = StringField('Option D')
    answer = RadioField('Correct Answer',
                        choices=CHOICES)
    submit = SubmitField('Add the Question')


class QuizForm(FlaskForm):
    answers = FieldList(RadioField('Correct Answer', choices=CHOICES,
                                   validators=[DataRequired()]),
                        min_entries=0)
    submit = SubmitField('Submit your answers')
