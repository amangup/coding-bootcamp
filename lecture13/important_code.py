import math
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField


def abs_diff(a, b):
    diff = a - b
    if diff < 0:
        diff = -1 * diff

    return diff


class Series:
    def transform(self, k):
        return k

    def series_sum(self, n):
        total = 0
        for i in range(n):
            total += self.transform(i + 1)

        return total


class PiSeries(Series):
    def transform(self, k):
        return math.pow(-1, k - 1) * (1 / (2 * k - 1))


class ViewFunctionResponse:
    def __init__(self):
        self.render_response = False
        self.redirect_response = False

    def create_render_response(self, template_name, kwargs):
        self.render_response = True
        self.redirect_response = False
        self.render_template = template_name
        self.kwargs = kwargs

    def create_redirect_response(self, view_function, kwargs):
        self.redirect_response = True
        self.render_response = False
        self.redirect_view = view_function
        self.kwargs = kwargs


class WordForm(FlaskForm):
    word = StringField('Word')
    language = SelectField(u'Language', choices=[('en', 'English (US)'),
                                                 ('es', 'Spanish')])
    submit = SubmitField('See Word Definitions')


def dictionary_home_impl(request):
    view_response = ViewFunctionResponse()
    if request.method == 'POST':
        word = request.form['word'].lower()
        language = request.form['language']
        kwargs = {'word': word, 'lang': language}
        view_response.create_redirect_response('display_word_defs', kwargs)
    else:
        #form = WordForm()
        kwargs = {'form': None}
        view_response.create_render_response('dictionary_home.html', kwargs)

    return view_response