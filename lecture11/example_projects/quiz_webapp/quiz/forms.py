from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField, \
    FieldList
from wtforms.validators import DataRequired


CHOICES = [('1', 'Option A'),
           ('2', 'Option B'),
           ('3', 'Option C'),
           ('4', 'Option D')]


class QuestionForm(FlaskForm):
    question = TextAreaField('Question', validators=[DataRequired()])
    option_a = StringField('Option A', validators=[DataRequired()])
    option_b = StringField('Option B', validators=[DataRequired()])
    option_c = StringField('Option C', validators=[DataRequired()])
    option_d = StringField('Option D', validators=[DataRequired()])
    answer = RadioField('Correct Answer',
                        choices=CHOICES, validators=[DataRequired()])
    submit = SubmitField('Add the Question')


class QuizForm(FlaskForm):
    answers = FieldList(RadioField('Correct Answer', choices=CHOICES),
                        min_entries=0)
    submit = SubmitField('Submit your answers')
