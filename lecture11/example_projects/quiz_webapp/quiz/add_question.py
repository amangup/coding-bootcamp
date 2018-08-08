import bleach

from flask import request, render_template, redirect, url_for, flash
from sqlalchemy.exc import SQLAlchemyError

from quiz import app, db, forms
from quiz.db_tables import Question
from quiz.forms import QuestionForm

ALLOWED_TAGS = ['p', 'br', 'i', 'b', 'sub', 'sup', 'code', 'samp', 'var']


@app.route('/add_question', methods=['GET', 'POST'])
def add_question():
    form = QuestionForm(request.form)
    if request.method == 'POST':
        if form.validate():
            try:
                return _add_question_to_db_(request.form)
            except SQLAlchemyError:
                flash("We couldn't add your question due to a technical issue"
                      " on our side. Please try again later.")
        else:
            flash("Not all required fields were filled.")

    return _render_form_(form)


def _add_question_to_db_(formdata):
    question = Question(question_text=_clean_html_(formdata['question']),
                        option_a=_clean_html_(formdata['option_a']),
                        option_b=_clean_html_(formdata['option_b']),
                        option_c=_clean_html_(formdata['option_c']),
                        option_d=_clean_html_(formdata['option_d']),
                        answer=int(formdata['answer']))

    db.session.add(question)
    db.session.commit()
    return redirect(url_for('add_question_success'))


def _clean_html_(text):
    return bleach.clean(text, tags=ALLOWED_TAGS, attributes=['style'],
                 styles=['color'])


def _render_form_(form):
    return render_template('add_question.html', form=form,
                           allowed_tags=ALLOWED_TAGS)


@app.route('/add_question_success')
def add_question_success():
    return render_template('add_question_success.html')
