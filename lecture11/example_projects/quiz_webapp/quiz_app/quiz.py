from flask import render_template, redirect, request

from quiz_app import app, db, db_tables, forms


@app.route('/', methods=['GET', 'POST'])
def quiz():
    questions = db_tables.Question.query.all()
    if request.method == 'GET':
        form = forms.QuizForm()
        for _ in questions:
            form.answers.append_entry()

        return render_template("quiz.html", questions=questions, form=form)
    else:
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
