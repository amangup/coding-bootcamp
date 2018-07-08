## Assignment: Dictionary website

In this assignment, you are going to create a website which asks user for a word and shows all the definitions of that word. To get the definitions, we are going to use a service created by the Oxford Dictionaries team.

On top of lecture 10, you will need to learn a few more things to be able to finish this assignment:
- Using a Oxford Dictionaries RESTful API service
- Understand what JSON it and parse it
- Learn how to do URL redirection
- `if` statements and `for` loops in HTML templates

Let's get started.

### REST API

When we learned about HTTP servers, we learned that an HTTP response body doesn't have to be HTML. HTTP servers can be used to implement any kind of service. There are many such services which provide information relevant to the query asked by the user of the service. These services are commonly called REST API services (the precise definition of REST API is somewhat more complicated).

The Oxford dictionaries provides a REST API to provide dictionary definitions. The user can call the service with a specific URL (which includes the word, language, etc.), and the HTTP response is a JSON object containing a bunch of information including it's definitions, different parts of speech it can be used as, and more.

The Oxford Dictionaries REST API details are here: [https://developer.oxforddictionaries.com/](https://developer.oxforddictionaries.com/).

First, register on the website and get the API key. You will need that key to access their API.

You can read the documentation on its documentation page. The relevant section is **Dictionary entries**. You can even try it right there - it shows you how to construct the relevant URL and how does the response looks like. It even has the following snippet to show you how to use it using Python:

```python
import requests
import json

# TODO: replace with your own app_id and app_key
# for more information on how to install requests
# http://docs.python-requests.org/en/master/user/install/#install
import requests
import json

# TODO: replace with your own app_id and app_key
app_id = '<my app_id>'
app_key = '<my app_key>'

language = 'en'
word_id = 'Ace'

url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

print("code {}\n".format(r.status_code))
print("text \n" + r.text)
print("json \n" + json.dumps(r.json()))
```

- This code uses the `requests` module to make an HTTP GET request to the Oxford API's URL and capture the response. In your assignment, you will do something very similar to get the word definitions.

### JSON

JSON stands for **JavaScript Object Notation** and it's a string data format. It's commonly used to transfer _structured data_ (like lists and dictionaries in Python) over the internet. To transfer data over the internet, you have to be able to format the data as a string. Structured data, like a dictionary, has a very complicated representation in the memory (different elements of dictionary are at discontiguous memory locations) and that memory structure can't be transferred as it is. This is why we need formats like JSON. 

For this assignment, you will need to understand JSON well.

- Here is an article which explains what JSON is: [Working with JSON](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON). You don't need to do the "Active Learning" section, as it uses Javascript.
- A great reference: [https://www.json.org/](https://www.json.org/)

In Python, the `json` module is used to parse a JSON string, and returns an object representing the JSON data (if the JSON string represents a list, you will get a list, if it's an key:value object, you will get a dictionary, etc). Note that for this exercise, you don't really have to parse JSON - the return value of `r.json()` (see snippet in the previous section) is a dictionary object which you can use straightaway (`r.json()['results']` gives you value for the key `results`, which is a list of dictionaries itself.)

You will have to spend some time and effort to figure out how to extract what you need from the Oxford API's response. A good dictionary website should show the part of speech, the definition and example sentences (all of which are included in the response).

### URL redirection

URL redirection means that when you go to an URL on your browser, that URL automatically redirects you to another one without your input. This can be useful to make your dictionary website better, but it's optional.

In a dictionary website, it would be desirable to allow users to go to an URL like: `www.mydictionary.com/definitions/mushroom` and get the definition of the word mushroom. This allows users to bookmark pages, share URLs, and the output is the same for all users at any time. Note that our fortune teller website doesn't support that - in fact, if the user went to the `/fortune` path without using the form on the home page, it would give an error.

To do that, we need to do two things:

1. Show the word definitions if someone navigates to `www.mydictionary.com/definitions/mushroom` in their browser. To do that, your code needs to be able to access the word `mushroom`, so that you can show it's definitions.

The URL rules in Flask can have variable names. [This link](http://flask.pocoo.org/docs/1.0/quickstart/#variable-rules) shows how they work (you will do something similar to the username example shown at the link).

2. When the user types a word and submits the form (on your website's home page), you will have to read the word user entered, and then _redirect_ to the link as shown above.

Let's say, you implemented `definitions` URL handler as follows:

```python
@app.route('/definitions/<word>')
def show_definitions(word):
    # respond with an HTML which contains the word's definitions
    pass
``` 

Then you can write your home page like this:

```python
from flask import redirect, render_template, url_for, request

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # get 'word' from the form
        return redirect(url_for('show_definitions', word=word))
    else:
        # create a 'form' object
        return render_template('home.html', form=form)
```

You will also need to make sure that the form's submit url is the home page of your website:

```html
<form action="{{ url_for('home') }}" method="POST">
```

### `if` and `for` statements in HTML templates

The `jinja2` template system allows you to use to use `for` and `if` control statements inside HTML templates. This is useful for this assignment 

- a word can have many definitions, and you need for loops inside the template to create an HTML for all of those.
- Some word definitions have example sentences, others not. You will need `if` statements do check if they are present, and show them if they are.

They are implemented in a very convenient manner. For example, this is how `for` statement works, when you pass `alist` to the template:

```html
{% for item in alist %}
<b>item</b>
<% endfor %}
```

- Note that the for condition is written exactly as you would in Python. The tag `<b>` makes the text bold.

Here is how the `if` statement works:

```html
{% if definitions %}
<!-- Use definitions variable here -->
{% endif %}
```

The detailed documentation is [here](http://jinja.pocoo.org/docs/2.10/templates/#list-of-control-structures).