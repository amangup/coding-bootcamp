# Testing

In this lecture we will learn how to write tests for our code. The goal of testing is to make sure our code works as intended, and it ensures that incremental changes to break existing functionality (especially, when that incremental change is being written by someone other than the original author).

## Code defects

We've spent a lot of time to learn to write code. We've also realized that it is not always easy to get the code work correctly all the time. This realization is formalized by the term _code defect_, which means that for some input case, the code doesn't function as intended.

Code defects are commonly measured as the number of defects in 1000 lines of code. According to some online sources, the typical defect rate in the industry is 10-30 defects per 1000 lines of code. Obviously, everyone would want to have 0 defects in their code, but in reality the effort and time required to write such code is just not practical. Also, it depends on what the code is intended to do - for some data analysis code used internally in a team to get a rough idea how well a product is working, maybe some code defects are fine. But, if the code is controlling the NASA space shuttle, we would prefer to have no defects at all.

Given that it's almost impossible to have no code defects, should we just assume that defects are OK and put no effort in containing them? Again, it's obvious that a large number of code defects is not OK. If we were building a website and the user got a 500 Internal Server Error every two minutes, we would eventually lose all users.

There are some practices we can follow which can help reduce code defects. The most important of these is **testing**, and we will focus on how to write tests in this lecture.

## How to minimize code defects

Here are some general practices that software companies do to reduce code defects. 
.
- **KISS** (short for _Keep it Simple, Stupid_). One of the most important ways to reduce code defects is keeping your code as simple as possible. Finding simple solutions to problems is worth any extra effort as it helps to reduce the number of mistakes in the implementation.
- **Write less code**. If there is no code, there are no defects :-). In my experience, programmers tend write more code than necessary - sometimes to solve for use cases that don't exist in reality, or in their attempt to make the program _future-proof_, introduce code that never actually gets used. Such practices will likely add more defects even in the functionality that is needed right now.
- **Write good code**. _Good_ code is easily understandable, and follows principles that, when followed, reduce the chance of introducing an error. Many books are written to help programmers learn "good coding".
- **Understand requirements and have good product documentation**. In many companies, the programmers are treated as just _coders_ who write code to execute someone else's will. In my experience, that frequently results in wrong implementations because the programmers are not clear on the purpose of the code they're writing. Having good documentation and spreading awareness of why we're doing the things the way we are doing helps immensely in reducing defects. I have seen companies lose millions of dollars and reputation due to bugs in code caused due to this reason.
- **Write tests**. A _test_ is a program that checks whether your main code is running correctly. By writing tests, you can ensure that your code handles the use cases correctly. Even more importantly, tests ensure that when changes are made to the main code, the original functionality remains correctly implemented (otherwise, the tests would fail). In my work, the amount of time that goes into implementation of functionality is about _half_ the time I spend in writing tests for that implementation (and usually the lines of test code is more than the lines of code in the implementation as well).

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

This is an example from the **Series** assignment in the `Classes` set. On repl.it, the automatic testing uses unit tests to check if your code is correct.

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
   
If we change the value of EPSILON to `1E-10`, then the test fails (why?):

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

- If you've spent enough time thinking, there is no easy way to test this because the hour of day is different depending on when the test is run (and you don't want your test to pass only when run at certain times of the day!).
- This is an example of hard-to-test code. It has meaningful functionality but we can't test that functionality easily.
  - Part of the set of paradigms for good coding is to write testable code. Untestable code should be an extreme exception.

Essentially, A test provides an input to your code and checks if the output matches an expectation. Our current implementation of the function takes no input from the caller.

To make our code more easily testable, we can change the function `day_period()` to take the hour as input:

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

Since we've spent written a lot of flask apps, we should discuss how to write unit tests for that.

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

- Our main aim is to implement a function that can take `request` as an argument, and respond with the _details_ we need to check for correctness, not the exact HTML or HTTP response.
- For the first aspect, we create a new function called `dictionary_home_impl()` which has the actual logic for the view function, and takes `request` as an argument. **This is the function we will unit test.**
- For the second aspect, we have created a new class `ViewFunctionResponse` which captures possible responses from the view function. The new function that we have written - `dictionary_home_impl()` - returns an object of this class.
- The main view function `dictionary_home()` (which we have registered with Flask) just calls the `dictionary_home_impl()` with `request`. 
- Since `dictionary_home_impl()` responds with an object `ViewFunctionResponse` and the Flask view function needs to return an HTML response, we've written a helper function called `get_http_response()`. 
   - The view function `dictionary_home()` uses that get to the HTTP response. 
- We can leave this function untested. As practically all of the logic is outside this function, this is not a major problem.

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
   - Note that Python doesn't need `request` to be of specific type. It just needs the attributes that you access from the object to exist.
- In each test case, we create a Mock Request with an appropriate values for its parameters and call the function we are testing with that request (`dictionary_home_impl()`).
- Since this function returns an object of type `ViewFunctionResponse`, we can assert the values of it's data attributes to check if the response is correct.


This example can be used as a pattern to write unit tests for Flask apps (in fact, I haven't found any good solution on the internet for unit-testing Flask apps). But there are a few more reasons why I wanted to show you this method:

- It is another way to make the point about what is testable code. Having easy ways to set input and fetch the output are important.
- If I were on the team writing Flask, I would not have chosen their approach to writing view functions. They clearly overlooked testability, or assumed people will find round-about ways for it.
- It's not always the case that the platforms you're using are designed to make your app easily testable. But, you can find ways to make _your_ code testable, as shown in this section.

## Test Coverage

Let's say you've learnt about testing and have spent some time writing tests. How can you be sure that your code is well tested?

There are metrics to indicate how well tested your code is, and the most important one is called **Coverage**. It's very commonly used in programming teams. But, as we will learn below, there is no single metric that you can rely on to say that your code is well tested, and this holds true for coverage as well. 

I will focus on explaining what coverage is, but not on how to actually run coverage analysis for your code. It's quite easy to do yourself, and you can read about it here: https://coverage.readthedocs.io/en/coverage-4.5.1x/.

### Definition of coverage

Let's go back to our first example on testing, and modify the test a bit:

```python
1: def abs_diff(a, b):
2:    diff = a - b
3:    if diff < 0:
4:        diff = -1 * diff
6:    return diff
```

```python
from important_code import abs_diff


class TestAbsDiff:
    def test_positive(self):
        assert 1 == abs_diff(2, 1)
```

- In the test, I've removed the test case `test_negative()`. Thus, we are not validating if the function `abs_diff()` runs correctly when `a < b`.
- If we run our sole test, the `if` clause on line 3 is always `False`. Thus, line 4 is never executed.
- In the example above, only 4 of the 5 lines of the main code is executed during test runs. We can say that the **test coverage is 80%**.

**Test Coverage** is the metric measuring how much of your code is executed when you run your tests. 0% coverage means you have no tests, and 100% coverage means that your tests are written so that all code paths in your program are invoked by tests.

### Is 100% coverage sufficient

Let's look at another example, and in this case, our main code is clearly wrong:

```python
1: def abs_value(a):
2:     return a
```

```python
from important_code import abs_value


class TestAbs:
    def test_positive(self):
        assert 1 == abs_value(1)
```

Let's ask the two important questions:

1. Do the tests pass? **Yes**
2. What is the test coverage? **100%**

But, your implementation of `abs_value()` is clearly wrong!

This is a good time to remind you that the coverage metric only checks if code is executed. But, the same line of code can be executed with many values of variables, and coverage doesn't take that into account. So, even if your tests _cover_ each line of your code, your tests may not have invoked each of those lines with a good enough variety of values.

As we mentioned earlier in the section about Coverage, it's not a metric that you can completely rely on. The way to interpret Test Coverage is this: **High coverage is necessary, but not sufficient, to say that your code is well tested.**

