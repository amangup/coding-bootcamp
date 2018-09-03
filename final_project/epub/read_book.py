from flask import render_template, url_for

from epub import app

@app.route('/')
def read_book():
    title = "A Catalogue of Play Equipment"
    author = "Jean Lee Hunt"
    cfi_location = ""
    return render_template("read_book.html", cfi=cfi_location, title=title, author=author,
                           book=url_for('static', filename='test.epub'))
