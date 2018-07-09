from flask import Flask

app = Flask(__name__)

fortune_list = []

def initialize(config):
    app.config.from_object(config)

    with open(app.config['FORTUNES_FILEPATH'], encoding='utf-8') as f:
        for fortune in f:
            fortune_list.append(fortune)

from fortune_teller import home, show_fortune

