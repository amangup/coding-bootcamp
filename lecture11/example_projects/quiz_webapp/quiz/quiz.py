from flask import render_template, redirect, request

from quiz import app, db, db_tables, forms


@app.route('/')
def quiz():
    questions = db_tables.Question.query.all()
    form = forms.QuizForm()
    for i, question in enumerate(questions):
        form.answers.append_entry()
        choices = []
        choices.append(('1', question.option_a))
        choices.append(('2', question.option_b))
        choices.append(('3', question.option_c))
        choices.append(('4', question.option_d))
        form.answers.entries[i].choices = choices

    return render_template("quiz.html", questions=questions, form=form)


@app.route('/score', methods=['POST'])
def score():
    questions = db_tables.Question.query.all()
    answers = []
    score = 0
    for i, question in enumerate(questions):
        user_answer = int(request.form['answers-' + str(i)])
        user_answer_letter = _get_answer_letter_(user_answer)
        if user_answer == question.answer:
            score += 1
            answers.append('{0} is correct'.format(user_answer_letter))
        else:
            correct_answer_letter = _get_answer_letter_(question.answer)
            answers.append('{0} is incorrect. Correct answer is {1}'
                           .format(user_answer_letter, correct_answer_letter))

    return render_template('quiz_answers.html', questions=questions,
                           answers=answers, score=score)


def _get_answer_letter_(user_answer):
    return chr(ord('A') + user_answer - 1)
