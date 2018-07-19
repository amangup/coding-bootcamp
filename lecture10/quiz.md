# Quiz

**Question 1**  
What is the output of the following program?

```python
class A:
    value = 1

class B:
    value = 2
    def __init__(self):
        self.value = 3

a_instance = A()
b_instance = B()
print(A.value, a_instance.value, B.value, b_instance.value)
```

Options:  
a: 1, 0, 2, 3  
b: 1, 1, 2, 2  
c: 1, 1, 2, 3  
d: raises an error

**Question 2**  
What is the output of the following program?

```python
class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def sum(self):
        return self.a + self.b
        
class Multiply(Sum):
    def __init__(self, a, b):
        self.c = a
        self.d = b
    
    def multiply(self):
        return self.c * self.d
        
m = Multiply(2, 3)
print(m.multiply())
print(m.sum())    
```

Options:  
a: 6, then raises an error  
b: 6, 0  
c: raises an error  
d: 6, 5  


**Question 3**  
Let's we have built a functional flask app called `my_webapp`, and we add the following view function to it. We then run the website at `www.mywebsite.com`.

```python
from flask import request

from my_webapp import app

@app.route("/tester")
def tester():
    if request.method == 'POST':
        return "Got a post request!"
    else:
        return "Not a post request"
```

What will happen when send the following HTTP request to it?

```
POST /tester HTTP/1.1
Host: www.mywebsite.com
```

Options:  
a: We'll see "Got a post request!" in the response  
b: We'll see "Not a post request" in the response  
c: We'll see an HTTP error saying "Page not Found" (404)  
d: We'll see an HTTP error saying "Method not allowed" (405)  

**Question 4**  
Launch your browser, go to the address URL, type "en.wikipedia.org" and press enter. Now launch your browser's network inspector (Ctrl/Cmd + Shift + C, then network tab) and do that again.

Among all the `GET` requests, find the one with Request URL = `https://en.wikipedia.org/wiki/Main_Page`. 

What is the HTTP response status code for that request?

Options:  
a: 30x  
b: 20x  
c: 40x  
d: 50x  

**Question 5**  
We send an HTTP GET request to an HTTP server. Which of the HTTP response content types listed below are valid (i.e., what kind of data can a HTTP server respond with)?

Options:  
a: text/html  
b: image/jpg  
c: application/json  
d: All of the above

**Question 6**  
In a functional flask app, let's say we have a page with the following template called `message.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>A message</title>
</head>
<body>
    <h1>{{ data.message() }}</h1>
</body>
</html>
```

And we implement the following view function in our app:

```python
from flask import render_template

from my_webapp import app

class Data:
    def message(self):
        return ("What we think, we become. -- Buddha")

@app.route("/message")
def test():
    return render_template("message.html", data=Data())
```

What will happen when go to the path `/message` on your webserver?

Options:  
a: There will be an error saying that you can't call methods in a template  
b: There will be an error saying that object `data` has no attribute `message`  
c: We will see a web page with the Buddha's quote.  
d: None of the above   

**Question 7**  
In a functional flask app, let's say we have a page with the following template called `home.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Classifieds Home</title>
</head>
<body>
    <!-- 'a' tag creates a hypertext link to the URL specified in the
    href property -->
    <a href="{{ url_for('listing') }}">See the listings</a>
</body>
</html>
```

And we implement the following two view functions in our app:

```python
from flask import render_template

from my_webapp import app

@app.route("/")
def home():
    return render_template("home.html")
```

```python
from my_webapp import app

@app.route("/listing")
def show_classifieds():
    # returns the page with all the listings
```

What will happen when go to the path `/` on your webserver?

Options:  
a: We will see the home page with the link to the 'listing' page.    
b: There will be a page not found error (404).   
c: There will be an error saying that it can't find the endpoint 'listing'    
d: None of the above      

**Question 8**  
Let's we create a form class as follows, and put it in `forms.py`:
```python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class NameForm(FlaskForm):
    username = StringField('Name')
    submit = SubmitField('Submit')
```

And we implement the following view function:

```python
from my_webapp import app, forms

@app.route("/")
def home():
    form = forms.NameForm()
    print(form.submit())
    # returns the rendered html page
```

What does the print statement in above code output when we go to the path `/`?

Options:  
a: `<label for="submit">Submit</label><br>`  
b: `<input id="submit" name="submit" type="submit" value="Submit">`  
c: `Submit`  
d: None of the above  
