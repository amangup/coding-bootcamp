from flask import render_template, request, redirect, url_for
from dictionary_webapp import app, forms

@app.route('/', methods=['GET', 'POST'])
def dictionary_home():
    if request.method == 'POST':
        word = request.form['word'].lower()
        language = request.form['language']
        return redirect(url_for('display_word_defs', word=word, lang=language))
    else:
        form = forms.WordForm()
        return render_template('dictionary_home.html', form=form)