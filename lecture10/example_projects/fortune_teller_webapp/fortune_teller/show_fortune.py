import random

from flask import render_template, request
from fortune_teller import app, fortune_list, forms

@app.route('/fortune', methods=['GET', 'POST'])
def show_fortune():
    name = request.form['username']
    fortune = fortune_list[random.randint(0, len(fortune_list) - 1)]
    return render_template('fortune.html', username=name, fortune_text=fortune)
