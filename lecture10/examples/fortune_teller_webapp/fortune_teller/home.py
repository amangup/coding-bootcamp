from flask import render_template, url_for, redirect
from fortune_teller import app
from fortune_teller import forms

@app.route('/')
def hello():
    form = forms.NameForm()
    return render_template('home.html',
                           form=form)

