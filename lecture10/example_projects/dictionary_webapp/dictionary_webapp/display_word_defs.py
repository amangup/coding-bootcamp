from flask import render_template

from dict_service import dictionary
from dictionary_webapp import app

@app.route('/definitions/<word>/<lang>', methods=['GET'])
def display_word_defs(word, lang):
    word_details = dictionary.get_word_details(word, lang)
    if word_details:
        return render_template('definitions.html', word_details=word_details)
    else:
        return (render_template('definitions_error.html', word=word, lang=lang),
                404)

