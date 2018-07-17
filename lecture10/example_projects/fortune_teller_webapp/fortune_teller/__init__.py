from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

fortune_list = []

def initialize():
    with open(app.config['FORTUNES_FILEPATH'], encoding='utf-8') as f:
        for fortune in f:
            fortune_list.append(fortune)

from fortune_teller import home, show_fortune

