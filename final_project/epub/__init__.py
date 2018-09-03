from flask import Flask

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from epub import read_book, location_sync