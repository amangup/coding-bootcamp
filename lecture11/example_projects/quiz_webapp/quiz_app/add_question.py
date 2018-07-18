from flask import request, render_template, redirect, url_for
from quiz_app import app, db, forms
from quiz_app import db_tables


@app.route('/add_question', methods=['GET', 'POST'])
def add_question():
    if request.method == 'POST':
        question = db_tables.Question(question_text=request.form['question'],
                                      option_a=request.form['option_a'],
                                      option_b=request.form['option_b'],
                                      option_c=request.form['option_c'],
                                      option_d=request.form['option_d'],
                                      answer=int(request.form['answer']))
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('add_question_success'))
    else:
        form = forms.QuestionForm()
        return render_template('add_question.html', form=form)


@app.route('/add_question_success')
def add_question_success():
    return render_template('add_question_success.html')
