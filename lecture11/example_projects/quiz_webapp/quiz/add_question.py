from flask import request, render_template, redirect, url_for, flash
from sqlalchemy.exc import SQLAlchemyError

from quiz import app, db, forms
from quiz.db_tables import Question
from quiz.forms import QuestionForm


@app.route('/add_question', methods=['GET', 'POST'])
def add_question():
    if request.method == 'POST':
        question = Question(question_text=request.form['question'],
                                      option_a=request.form['option_a'],
                                      option_b=request.form['option_b'],
                                      option_c=request.form['option_c'],
                                      option_d=request.form['option_d'],
                                      answer=int(request.form['answer']))
        try:
            db.session.add(question)
            db.session.commit()
            return redirect(url_for('add_question_success'))
        except SQLAlchemyError:
            flash("We couldn't add your question due to a technical issue on "
                  "our side. Please try again later.")
            return _render_form_()
    else:
        return _render_form_()


def _render_form_():
    form = QuestionForm()
    return render_template('add_question.html', form=form)


@app.route('/add_question_success')
def add_question_success():
    return render_template('add_question_success.html')
