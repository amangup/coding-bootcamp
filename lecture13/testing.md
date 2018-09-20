# Testing

In this lecture we will learn how to write tests for our code. The goal of testing is to make sure our code works as intended, and when working as part of a team, it ensures that incremental changes to break existing functionality.

## Code defects

We've spent a lot of time to learn to write code. But, we've also realized that it is not always easy to get the code work correctly all the time. This realization is formalized by the term _code defect_, which means that for some input case, the code doesn't function as intended.

Code defects are measured as the count of of _defects_ per 1000 lines. According to some online sources, the typical defect rate in the industry is 10-30 defects per 1000 lines of code. Obviously, everyone would want to have 0 defects in their code, but in reality the effort and time required to write such code is simply not practical. Also, it depends on what the code is intended to do - for an internal data analysis code which is used to get a rough idea how well a product is working, maybe some code defects are fine. But, if the code is controlling the NASA space shuttle, we would prefer to have no defects at all.

Given that it's almost impossible to have no code defects, should we just assume that defects are OK and put no effort in containing them? Again, it's obvious that a large number of code defects is not OK. If we were building a website and the user got a 500 Internal Server Error every two minutes, we would eventually lose all users.

There are some practices we can follow which can help reduce code defects. The most important of these is **testing**, and we will focus on how to write tests in this lecture.

## How to minimize code defects

Here are some general practices that software companies do to reduce code defects. 
.
- **KISS** (short for _Keep it Simple, Stupid_). One of the most important ways to reduce code defects is keeping your code as simple as possible. Finding simple solutions to problems is worth the extra effort to reduce mistakes in implementation.
- **Write less code**. If there is no code, there are no defects :-). In my experience, programmers tend to solve for use cases that don't exist in reality, or in their attempt to make the program _future-proof_, introduce code that never actually gets used. Such practices makes the code have more defects even in the functionality that is needed right now.
- **Write good code**. _Good_ code is easily understandable, and follows principles that, when followed, reduce the chance of introducing an error.
- **Have good documentation**. In many companies, the programmers are treated as just _coders_ who write code to execute someone else's will. In my experience, that frequently results in wrong implementations because the programmers are not clear on the purpose of the code they're writing. Having good documentation and spreading awareness of why we're doing the things the way we are doing helps immensely in reducing defects. I have seen companies lose millions of dollars and reputation due to bugs in code caused due to this reason.
- **Write tests**. A test is code that checks whether your main code is running correctly. By writing tests, you can ensure that your code handles the use cases correctly. Even more importantly, tests ensure that when changes are made to the main code, the original functionality remains correctly implemented (otherwise, the tests would fail). In my work, the amount of time that goes into implementation of functionality is about _half_ the time I spend in writing tests for that implementation (and usually the lines of test code is more than the lines of code in the implementation as well).

## A unit test

Testing has various forms, and in this lecture, we will focus on the type of testing called **unit testing**. A unit test checks a _unit_ of code, which can be thought of as one function or one class designed to do one thing. The goal is that all individual parts of the _machine_ are working as intended. Obviously, this doesn't ensure that the machine will also work correctly, but, in my experience, this goes a _long long_ way towards that goal.

Time to see some code. Here is a function that calculates the absolute difference of two numbers (in file `important_code.py`).

```python
def abs_diff(a, b):
    diff = a - b
    if diff < 0:
        diff = -1 * diff
        
    return diff
```

Here is a simple unit test for this code (in file `test_important_code.py`).

```python
from important_code import abs_diff


class TestAbsDiff:
    def test_positive(self):
        assert 1 == abs_diff(2, 1)

    def test_negative(self):
        assert 1 == abs_diff(1, 2)
```

- Essentially, each test does this: The test code imports the function (or class) to test, runs it with some values, and then _asserts_ that the output of the function should match our expectation.
  - The `assert` keyword checks if the expression that is written next to it is `True` of not. If it is `False`, it makes the program fail.
- You can see that we've created a class `TestAbsDiff` to club all tests which check the function `abs_diff`. This is always a good idea, as it's common to have multiple test cases for even the simplest of functions.
- We have created two methods `test_positive()` and `test_negative()` in the class `TestAbsDiff` to contain the test for different use cases.
- The naming conventions we've used as follows:
  - The name of the test file is `test_<name_of_code_file>.py`. This is a commonly used convention and makes it easy to organize test code and know which code is main implementation and which code is for testing.
  - The class name is `Test<FunctionName>`, but it uses camel case notation instead of underscores (as is the convention for class names). There should ideally be one Test class for one function or one class which is being tested.
  - The method names for individual test are of the form `test_<test_case>`, where the test_case part of the name is used to indicate what functionality this test case is testing.
  
  
To run this test, we use a python library called `pytest`. This library automatically detects which code is test code using the naming conventions we've used, and runs all the tests.

In PyCharm, to enable testing, you need to do two things:
1. Go to Settings --> Tools --> Python Integrated Tools, and in the testing section, change the default test runner to `pytest`.
2. In Run --> Edit Configurations and add a new configuration of type Python tests --> pytest. I named it `Test`, and made the target `custom`.

Now I can choose `Test` in the dropdown in the top right, and then click on Run, which runs all the tests in my current project.

Here is the output of the test code written above:

```
============================= test session starts ==============================
platform linux -- Python 3.6.6, pytest-3.8.0, py-1.6.0, pluggy-0.7.1
rootdir: /home/aman/aman_code/coding-bootcamp, inifile:collected 2 items

lecture13/test_important_code.py ..                                      [100%]

=========================== 2 passed in 0.11 seconds ===========================

```

- It lists the files which contain the test code.
- It shows that there are two test cases, and mentions that they both passed.

Now let's see what happens if our code is wrong. We change the implementation of the function `abs_diff()` to this:


```python
def abs_diff(a, b):
    return a - b
```

Now if I run the test, I get the following output:

```
============================= test session starts ==============================
platform linux -- Python 3.6.6, pytest-3.8.0, py-1.6.0, pluggy-0.7.1
rootdir: /home/aman/aman_code/coding-bootcamp, inifile:collected 2 items

lecture13/test_important_code.py .F
lecture13/test_important_code.py:7 (TestAbsDiff.test_negative)
-1 != 1

Expected :1
Actual   :-1
 <Click to see difference>

self = <test_important_code.TestAbsDiff object at 0x7f9f29341f60>

    def test_negative(self):
>       assert 1 == abs_diff(1, 2)
E       assert 1 == -1
E        +  where -1 = abs_diff(1, 2)

lecture13/test_important_code.py:9: AssertionError
                                      [100%]

=================================== FAILURES ===================================
__________________________ TestAbsDiff.test_negative ___________________________

self = <test_important_code.TestAbsDiff object at 0x7f9f29341f60>

    def test_negative(self):
>       assert 1 == abs_diff(1, 2)
E       assert 1 == -1
E        +  where -1 = abs_diff(1, 2)

lecture13/test_important_code.py:9: AssertionError
====================== 1 failed, 1 passed in 0.14 seconds ======================
```

- In the end, it gives a summary that 1 test passed, and 1 test failed.
- For each failure, it gives you the details on where that failure occurred what was the difference between the expected and actual values.
   - Note that pycharm considers the value on the left of `==` in the assertion as the _expected_ value.

A test failure shows that something is wrong. 
- In most cases, one would fix the main code so that the tests pass.
- In some cases, though, the tests fail because the intended outcome itself changes (say the code calculated federal taxes, and the tax rates changed).


## Test Example Two: Test a class

This is an example from the **Series** assignment in the `Classes` set. On repl, the automatic testing uses unit tests to check if your code is correct.

```python
import math

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
```

- In this code, the `Series` class sums the numbers from 1 to n.
- The class `PiSeries` overrides the `transform()` method of `Series` class so that the sum of the series is close to the value of Pi / 4.

Here is the test code for this class:

```python
import math
from important_code import Series, PiSeries


EPSILON = 1E-4


class TestSeries:
    def test_100_terms(self):
        series = Series()
        assert 5050 == series.series_sum(100)


class TestPiSeries:
    def test_20000_terms(self):
        series = PiSeries()
        assert math.isclose(math.pi / 4, series.series_sum(200000), abs_tol=EPSILON)
```

- We have two test classes for the two classes in the main code.
- Each class has one test case to check the correctness.
- For the case of `TestPiSeries`, our assertion looks different. This is because the output of our series will not be exactly equal Pi / 4, but be close to it.
   - The value of `abs_tol` is set to 0.0001 (= `1E-4`, which is _1 raised to power -4_). The function `math.isclose()` function checks if the difference of two values is less than `abs_tol`.
   
If we change the value of EPSILON to `1E-10`, then the test fails:

```
=================================== FAILURES ===================================
________________________ TestPiSeries.test_20000_terms _________________________

self = <test_important_code.TestPiSeries object at 0x7fecfe1583c8>

    def test_20000_terms(self):
        series = PiSeries()
>       assert math.isclose(math.pi / 4, series.series_sum(200000), abs_tol=EPSILON)
E       assert False
E        +  where False = <built-in function isclose>((3.141592653589793 / 4), 0.7853969133974404, abs_tol=1e-10)
E        +    where <built-in function isclose> = math.isclose
E        +    and   3.141592653589793 = math.pi
E        +    and   0.7853969133974404 = <bound method Series.series_sum of <important_code.PiSeries object at 0x7fecfe158438>>(200000)
E        +      where <bound method Series.series_sum of <important_code.PiSeries object at 0x7fecfe158438>> = <important_code.PiSeries object at 0x7fecfe158438>.series_sum

lecture13/test_important_code.py:25: AssertionError
```

## Writing testable code

Let's define a function which tells us if it's morning (6am to 12pm), afternoon (12pm to 4pm), evening (4pm to 10pm) or night (10pm to 6am).

```python
from datetime import datetime

def day_period():
    hour = datetime.now().hour
    if hour >= 6 and hour < 12:
        return "morning"
    elif hour >= 12 and hour < 16:
        return "afternoon"
    elif hour >= 16 and hour < 22:
        return "evening"
    else:
        return "night"
        
## Example use of this function
print ("Good %s, senorita!" % day_period())
```

How will you write an unittest for this?
```








Don't scroll down










```

- If you've spent enough time thinking, there is no easy way to test this (because the hour of day is different depending on when the test is run). The only real option is to duplicate the whole functionality in the test as well, and see if the output matches. There is no point in testing some code if the test code itself has to duplicate the main code.
- This is an example of non-testable code. It has meaningful functionality but we can't test that functionality.
  - Part of paradigms for good coding is to write testable code. Untestable code should be an extreme exception.

A test has to provide an input and check if the output matches an expectation. Our current implentation of the function takes no input from the caller.
We can change the function above to take the hour as input:

```python
from datetime import datetime

def day_period(hour):
    if hour >= 6 and hour < 12:
        return "morning"
    elif hour >= 12 and hour < 16:
        return "afternoon"
    elif hour >= 16 and hour < 22:
        return "evening"
    else:
        return "night"
        
## Example use of this function
current_hour = datetime.now().hour
print ("Good %s, senorita!" % day_period(current_hour))
```

- We've moved the part where we find what hour of the day is it currently outside the function `day_period()`.
- Now we can easily test the function `day_period()`.
- The user can provide the value for current hour, instead of the function find that out. We assume that finding the current hour is easy enough that we can leave that part untested.

## Testing Flask apps

Since we've spent written a lot of flask apps, we should discuss how to unit tests for that.

- The unit for testing in this case would be the view function.
  - The input to a view function is the `request`. 
  - The output of the view function is either a combination of template name and parameters to the template, or a redirect with the redirect url.
  - Note that we don't really want to test the exact HTML in case the view function is supposed to render a template - that would be testing the template. We only want to test that the right template is invoked, with correct values of template variables. 
- Flask view functions have the same problem as our `day_period()` function that all the input parameters to the view function (like the object `request`) is not provided as an argument, but rather it's value is "magically" set. 
- We can use some tricks, though, to modify our view function implementation so that we can write unittests.


```python
from flask import render_template, request, redirect, url_for
from dictionary_webapp import app, forms

@app.route('/', methods=['GET', 'POST'])
def dictionary_home():
    if request.method == 'POST':
        word = request.form['word'].lower()
        language = request.form['language']
        return redirect(url_for('display_word_defs', word=word, lang=language))
    else:
        form = forms.WordForm()
        return render_template('dictionary_home.html', form=form)
```

This is an example of a view function that I wrote in my implementation for the dictionary assignment (in lecture 10). As mentioned before, we can't really call the `dictionary_home()` function directly because there is no easy way to set the value of `request`.

Instead, we modify the code as follows:

```python
from flask import render_template, request, redirect, url_for
from dictionary_webapp import app, forms


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
         
    def get_http_response(self):
        if self.render_response:
            return render_template(self.render_template, **self.kwargs)
        elif self.redirect_response:
            return redirect(url_for(self.redirect_view, **self.kwargs))
        else:
            return "Not Found", 404


@app.route('/', methods=['GET', 'POST'])
def dictionary_home():
    view_response = dictionary_home_impl(request)
    return view_response.get_http_response()    

def dictionary_home_impl(request):
    view_response = ViewFunctionResponse()
    if request.method == 'POST':
        word = request.form['word'].lower()
        language = request.form['language']
        kwargs = {'word': word, 'lang': language}
        view_response.create_redirect_response('display_word_defs', kwargs)
    else:
        form = forms.WordForm()
        kwargs = {'form': form}
        view_response.create_render_response('dictionary_home.html', kwargs)
        
    return view_response        
```

This looks like a lot of code, but the new code can be shared across all view functions, so it needs to be written only once.

- Our main aim is to implement a function that can take `request` as an argument, and respond with the details we need to check for correctness and not the exact HTML or HTTP response.
- For the first aspect, we create a new function called `dictionary_home_impl()` which has the real logic for the view function, and takes request as an argument. **This is the function we will unit test.**
- For the second aspect, we have created a new class `ViewFunctionResponse` which captures possible responses from the view function. The new function we have written `dictionary_home_impl()` returns an object of this class we can test.
- The main view function `dictionary_home()` (which we have registered with Flask) just calls the `dictionary_home_impl()` and uses the helper function in the class `ViewFunctionResponse` to get the HTTP response to return to Flask. We can leave this untested, and practically all of the logic is outside this function, this is not a major problem.

Now, we can write the test as follows:

```python
from important_code import ViewFunctionResponse, dictionary_home_impl


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
        assert isinstance(view_response.kwargs['form'], WordForm)

    def test_post_request(self):
        request = MockRequest('POST', {'word': 'ace', 'language': 'en'})
        view_response = dictionary_home_impl(request)
        assert True == view_response.redirect_response
        assert 'display_word_defs' == view_response.redirect_view
        assert 'ace' == view_response.kwargs['word']
        assert 'en' == view_response.kwargs['lang']
```

- We have created a new class called `MockRequest`, which contains the parameters for request method and the data gathered from the form (in case of POST request).
- In each test case, we create a Mock Request with an appropriate values for its parameters and call the function we are testing with that request (`dictionary_home_impl()`).
- Since this function returns an object of type `ViewFunctionResponse`, we can assert the values of it's data attributes to check if the response is correct.



  