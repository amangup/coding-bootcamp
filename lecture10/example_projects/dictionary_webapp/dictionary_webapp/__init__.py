from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very-hard-password'

from dictionary_webapp import dictionary_home, display_word_defs
