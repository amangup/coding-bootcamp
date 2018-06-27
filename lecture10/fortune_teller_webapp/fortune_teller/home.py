from flask import render_template, url_for, redirect
from fortune_teller import app
from fortune_teller import forms

@app.route('/')
@app.route('/index')
def hello():
    form = forms.NameForm()
    return render_template('home.html',
                           image_path=url_for('static', filename='cookie_rich.jpg'),
                           form=form)

