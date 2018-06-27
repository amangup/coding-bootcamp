from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very-hard-password'
app.config['fortunes_filepath'] = 'fortune_teller_webapp/resources/fortunes.txt'

fortune_list = []
with open(app.config['fortunes_filepath'], encoding='utf-8') as f:
    for fortune in f:
        fortune_list.append(fortune)

from fortune_teller import home, show_fortune

