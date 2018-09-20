import math
from important_code import abs_diff, Series, PiSeries, ViewFunctionResponse, dictionary_home_impl


EPSILON = 1E-4


class TestAbsDiff:
    def test_positive(self):
        assert 1 == abs_diff(2, 1)

    def test_negative(self):
        assert 1 == abs_diff(1, 2)


class TestSeries:
    def test_100_terms(self):
        series = Series()
        assert 5050 == series.series_sum(100)


class TestPiSeries:
    def test_20000_terms(self):
        series = PiSeries()
        assert math.isclose(math.pi / 4, series.series_sum(200000), abs_tol=EPSILON)


class MockRequest:
    def __init__(self, method, form_dict):
        self.method = method
        self.form = form_dict


class TestDictionaryHome:
    def test_get_request(self):
        request = MockRequest('GET', {})
        view_response = dictionary_home_impl(request)
        assert True == view_response.render_response
        assert 'dictionary_home.html' == view_response.render_template
#        assert isinstance(view_response.kwargs['form'], WordForm)

    def test_post_request(self):
        request = MockRequest('POST', {'word': 'ace', 'language': 'en'})
        view_response = dictionary_home_impl(request)
        assert True == view_response.redirect_response
        assert 'display_word_defs' == view_response.redirect_view
        assert 'ace' == view_response.kwargs['word']
        assert 'en' == view_response.kwargs['lang']