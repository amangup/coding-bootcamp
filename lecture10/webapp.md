# Web Applications using Flask

- In this lecture, we are going to build our first web app! This lecture is designed to be a tutorial which you should follow along in practice. Our first web app is the **fortune teller**. It asks for the user's name, and shows them their fortune!

## Web App Development Frameworks

- There are many web app development frameworks one can use in Python. 
- We are going to use one of the most popular ones - it is called [Flask](http://flask.pocoo.org/)
- It is used for production websites by many companies. 
- It's easy to get started and start building apps. 
- Flask is a python library which has implemented a lot of what is required to build a web server. It exposes an API designed to make it easy to build new web servers by allowing users to focus only on the components that makes their web app unique, while hiding the unnecessary complexity. 
- As a developer, it's important to be aware of what it is hiding. As we build our web app, we will peek behind the curtains at times.

## Python packages

- In python, you can package many modules together into one _namespace_. This makes it easy to refer to all the modules which are semantically related.
- To create a package, you put all your modules (.py files) into one directory. 
- For python to recognize it as a package, though, you need to create a special file called `__init__.py` in your directory. This file can even be empty. It can also be used for creating some global definitions, as we will see later in this tutorial.

Here is an example of a directory structure (example taken from python docs):

```
movie_filter.py
effects/
        __init__.py
        echo.py
        surround.py
        reverse.py
```

- In the listing above, we have a directory called `effects`. Thus, we are creating a package called `effects`.
- Inside the directory, we have three different modules, called `echo`, `surround` and `reverse`.
- We also have a file called `__init__.py`, which is a mandatory requirement.

The file `movie_filter.py` is the code where we actually use the modules in the package. Python has an alternate syntax to import modules (as compared to what we learnt before), and that is convenient in this setting, as shown below.


```python
from effects import echo, surround
```

- The import statement is self-explanatory. It introduces a new keyword `from`.
- When you run `movie_filter.py`, it looks for the package `effects` in its own directory and all subdirectories.

Understanding packages is essential for working on projects in Python. Each web app will be structured as a collection of packages. 

## Preliminary structure for our app

In the beginning we will need to create the following file and directory structure for our app.

```
requirements.txt
webapp/
       test_server.py
       fortune_teller/
                      __init__.py
                      home.py
```

Through the course of this tutorial, we will expand this structure.

In `requirements.txt` file, add the following two lines:

```
Flask==1.0.2
Flask-WTF==0.14.2
```

These are the Flask libraries we will use today.

## Hello, World app

- As is customary, we start by creating a simple web app which just displays 'Hello, world!' to the user.
 
### Creating the Flask object

To get started, we have to create an object of type `Flask`. This is an object that will get used repeatedly throughout our code.

We add the following code to `__init__.py`:

```python
from flask import Flask

app = Flask(__name__)

from fortune_teller import home
```

- The first line is used to import the `Flask` class.
- In the second line, we create an object called `app`. Every Flask app must have a name, and in this case the variable `__name__` will default to the name of the package, which is `fortune_teller`.
- In the third line, are importing yet another module. This has no effect until we add something to the `home` module. We will understand why it is required in the next section.
  - Note that we are referring to the package `fortune_teller` from the code that is _inside_ that package.
 
### Creating a view
- In Flask, the URL paths are mapped to functions.
- Such a function is called a **view function**.
- Let's write a view function which returns "Hello, World" whenever someone visits our home page.

In `home.py`, write the following code:

```python
from fortune_teller import app


@app.route('/')
def hello():
    return 'Hello, World!'
```

- In the first line, we are importing the object `app`. This is required as we are going to _register_ the mapping from path to the view function onto this app.
- We create a simple function which just returns the string "Hello, World!".
- The magic happens in the line `@app.route('/')`.
  - This Python syntax is called a **decorator**. The decorator usage is similar to a method call: It's similar to calling the method `route` in the object `app`, with the argument `'/'`.
  - The decorator allows the Flask code to make entry into its own data structures which says that whenever the user requests for the path `'/'` (called the _root_  path), it should use the function `hello()` to respond.

- This mapping only registered if the module `home` is imported. 
  - Remember the last line we wrote in `__init__.py`? That is where we are importing this module, and the decorator runs (even though the function is not called). Internally, the decorator adds an **url rule** to create the mapping between the path and the function.
  
### Running the server

- To test our app, we need to run a web server.
- The following method of running the server is typically used only during development, and not in production environment.

In `test_server.py`, we write the following code.

```python
from fortune_teller import app


def main():
    app.run(host='127.0.0.1', port=8080)
    

if __name__ == '__main__':
    main()
```

- In the first line, we are importing the `app` object from the `fortune_teller` package.
  - Note that we are now _outside_ the package.
- The method `run()` in the object `app` starts a web server. We provide the method with two arguments, which is the address of where we are running the web server.
  - `host` is used to refer to the IP address. In networking, the address **127.0.0.1** always means the **localhost**, i.e., the device on which you are running this code.
  - `port` is the port on which this web server will listen. We can choose any value which is not already being used. Typically, no production code uses 8080, and it's commonly used for development.
  
Your Hello World webapp is ready! You can run the file `test_server.py`, go to your browser and type the address `http://localhost:8080/` and you will see the result. Try changing the return value of the `hello()` function and see the browser output change.

### Understanding more
We will use this app to understand a bit more about how Flask works.

1. When the page opens in your browser, right click on the page and select "View Source". You will see that there is just one line there, and it is exactly equal to your return value from the function.
    * This means that Flask uses the string you return as the HTML response. If you use your web browser's inspector (press Ctrl/Cmd + Shift + C, and choose the "Network" tab), you will see that among the response params, the content type is `text/html; charset=utf-8`.
    * Change the `hello()` function to return this string `<html><body><h1>Hello, World!</h1></body></html>` so that your response string actually is in HTML. You will see that the size of text becomes larger. This is because the tag `h1` formats the text to look like a heading.
    * In general, the HTTP response contains a number of parameters. Flask generates all of them for you.
    
2. Enter the address `http://localhost:8080/nowhere`, while having the network inspector running. You will notice that the response status is now 404.
    * Flask automatically returns an appropriate response when someone goes to a path that doesn't exist.
    
3. Let's try to break the code. In the `hello()` function, change the code to `return str(2/0)`. This will raise an Exception when you load the page. Do that, with the network inspector running. You will see the message "Internal Server Error", and the response code is 500.
    * This is another situation that Flask handles automatically.
    * If, in `test_server.py`, you add the argument `debug=True` in the method call `app.run()`, you will see that Flask gives you the details of the Exception that is raised (in this case, the `ZeroDivisionError`).
    * There is a second benefit of `debug=True`: it reloads the web server automatically when you change the code - so we will keep it this way for future.

## Using templates

- A web server responds to HTTP requests with HTML content. 
- This HTML content is dynamically generated based on what the user needs. For example, in our fortune teller app, we will create a fortune page which will greet the user by name, and then display a random fortune which will be different each time the user loads the page.
- But some parts of the HTML remain the same - the structure, the look of different parts, etc.
- To take care of these requirements, web developers use **templates**. Understanding a templating system well is _essential_ for web development.

### What is a template
- A template is an HTML page where some of its parts are replaced by placeholders which can be filled by code.
- Flask comes bundled with a templating system called `jinja2`. It is designed for python.
- In this system, we can pass objects to the template, and inside the template, the placeholders can use those objects to complete the HTML.

Let's use a simple template to change our Hello World app to say "Hello, World!" in one of many languages chosen at random.

### Creating a template

In Flask, there is a convention to store templates in the `/templates` directory. We will create that directory and create a template called `hello_world.html` inside it. Our directory structure looks like this now:

```
requirements.txt
webapp/
       test_server.py
       fortune_teller/
                      templates/
                                hello_world.html
                      __init__.py
                      home.py
```

Here is what the file `hello_world.html` will contain:

```html
<!doctype html>
<html>
    <head>
        <title>Hello</title>
    </head>
    <body>
        <h1>{{ hello_world }}</h1>
    </body>
</html>
```

- This is a very simple html page
- It sets the title to "Hello" (this shows up on the Titlebar of the browser window).
- It has a body, in which we have a placeholder inside the `h1` tag (that will display the text as big and bold.)
- The placeholder uses double curly braces in the start and the end, and expects the object `hello_world` - which it uses to replace the placeholder with.

### Rendering a template
- The act of replacing placeholders with concrete data in a template is called **rendering a template**.

To use the template, we will need to modify the code in `home.py` as follows:

```python
import random

from flask import render_template
from fortune_teller import app

hello_world_list = [
    "Hello, World!",
    "Hola, Mundo!",
    "Salut, Lume",
    "你好, 世界",
    "안녕하세요, 세계",
    "Bonjour, le monde",
    "Salve, orbis terrarum",
    "こんにちは, 世界",
    "नमस्ते, दुनिया"
]

@app.route('/')
def hello():
    greeting = hello_world_list[random.randint(0, len(hello_world_list) - 1)]
    return render_template("hello_world.html", hello_world=greeting)
```

If you start your server after making the changes, and keep refreshing the address we've been using, you will see a greeting in different language every time.

There are two new elements you need to understand how this works:
- Firstly, we need to import the `render_template` function for this work. It's part of the `flask` module.
- In the function `hello()`, we call the function `render_template` with the name of the template we are using (Flask knows which directory to look for to find this file), and then you have to use keyword arguments to give values for all objects the template is expecting you to provide.
- The `render_template` function returns a string which is the _rendered html_, and that is returned as the value of the function.

The template systems are sophisticated languages of their own, containing things like if conditions and loops. We will learn this language for the `jinja2` template system as we build more web servers.

## Fortune Teller App

### Creating web forms
- To build our Fortune Teller app, we need to create a web form which asks the user for their name. In this section, we will learn how to create a web form, and then how to use the data collected in the form.
- We will expand our app to two pages. 
  - The home page will now ask the user for their name.
  - The "fortune" page will greet the user by their name. We will add a fortune to this page in the next section.
  
- To create forms we need to use a package called `Flask-WTF` (which is already present in our `requirements.txt`). The first step is to create a new class for which we will create a new file called `forms.py` inside our `fortune_teller` package. Here are its contents:

```python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class NameForm(FlaskForm):
    username = StringField('Name')
    submit = SubmitField('See your fortune!')
```

- An object of `NameForm` will be passed to the template, which is then used by template to render the page. There is a lot of functionality that is also contained in the NameForm class:
    - It knows how to generate the HTML for each form field.
    - On the web, forms can be used to _attack_ a website. This class helps us protect from that.
    - Even though we are not using it right now, it allows us to validate the data entered in the form.

- To get all that functionality, we inherit from the class `FlaskForm`.
- In our class, we create class variables which define what each field in the form is
  - The `username` is a field where one can enter a string. It should be presented to the user with the label "Name".
  - The `submit` field represents the form submit button. The button should say "See your fortune!".
- Since we are creating class variables, it looks like that the data for `username` and `submit` will be the same for all objects. But that is not the case: Internally, FlaskForm creates a copy of `username` and `submit` for each instance and uses the class variables for the definition of field only.

#### Creating a form template
 
- We will create a new template which uses an object of type `NameForm` to render. 
- We will call it `home.html`, since it will be shown as the home page of our web app. Here is what it looks like:

```html
<!doctype html>
<html>
    <head>
        <title>Fortune Teller</title>
    </head>
    <body>
        <h2>Please enter your name</h2>
        <form action="{{ url_for('show_fortune') }}" method="POST">
            {{ form.hidden_tag() }}
            <p>
                {{ form.username.label }}<br>
                {{ form.username(size=32) }}
            </p>
            <p>{{ form.submit() }}</p>
        </form>
    </body>
</html>
```

- Let's focus on the section which begins with `<form>` and ends with `</form>`
- HTML defines the `<form>` tag that browsers understand and render as a form.

- A form must define the `action` and the `method`:
  - `action` is the URL path that the user to go to when the form is submitted. The data entered in the form is part of that request. We will understand what the function `url_for()` does shortly.
  - `method` is the HTTP method to use when making that request. HTTP recommends that we use `POST` method when we are sending data to the web server.

- Inside the form, we need to render two fields - `form.username` and `form.submit`.
  - When we call the method `form.username()`, FlaskForm generates the HTML for that field. Same is true for the method `form.submit()`. These methods are created by FlaskForm internally.
  - Note that the template can call a method (or function) to replace the placeholder with a string.
  - We can access the label that we gave to a field using the `label` data attribute.

- We have a field called `form.hidden_tag()` because it helps prevent a type of online attack called `CSRF attack`. For now, we will just follow this convention and not worry about security in this lecture.

- The function `url_for()` is a helper function to generate a URL, in this case, using the _name_ of the view function. 
- We will create a new view for showing the fortune, and name the corresponding view function `show_fortune`. `url_for()` will automatically check what URL path is that view mapped to, and use it to create the URL.
- We will use this function in another context later.

#### Rendering the form template

Let's modify the `home.py` to render this template, as follows:

```python
from flask import render_template
from fortune_teller import app, forms

@app.route('/')
def home():
    form = forms.NameForm()

    # The following two lines are for understanding forms, and are not used
    # for the web app.
    print(form.username())
    print(form.submit())

    return render_template('home.html', form=form)
``` 
 
- We create the `form` object using the `NameForm` class.
- When we call `render_template`, we pass the form object to the template as expected.

- I added two (temporary) print statements which show that exactly happens when the `username()` and `submit()` methods are called. If you see the output of your program, you will find the HTML for the form fields (`<input>` tags).

#### The Fortune page
- We now have to create a page which reads the data from this form and creates an appropriate greeting. To do that, we need a template and a view function. Let's begin with the template file `fortune.html`:

```html
<!doctype html>
<html>
    <head>
        <title>Fortune Teller</title>
    </head>
    <body>
        <h2>Hello, {{ username }}!</h2>
    </body>
</html>
``` 

- In the view function we need to access the data that was entered into the form. To do that, we can use the `request` object that Flask provides.

Here is how the code file `show_fortune.py` looks like:

```python
from flask import render_template, request
from fortune_teller import app

@app.route('/fortune', methods=['POST'])
def show_fortune():
    name = request.form['username']
    return render_template('fortune.html', username=name)
```

- The `request` object has a dictionary attribute called `form`, which contains the data for the form fields. We are accessing the data for the field `username`.
- Another thing to note is the `methods` argument to the `@app.route` decorator. By default, `app.route` assumes this method accepts a `GET` request only. But, in our case, we send a `POST` request to this URL from the form, so we must tell Flask that this view accepts `POST` requests.

We are almost done. We only need to take care of a formality for form security purposes - add the following line in `__init__.py`. This creates a sort of password for your app.

```python
app.config['SECRET_KEY'] = 'very-hard-password'
```

You should also update the next import line to the following (include `show_fortune`):
```python
from fortune_teller import home, show_fortune
```

Time to run it! Run the test server and see how it works.

#### More about /fortune view

1. The way we have created the `/fortune` view, we can only go to that URL via the form. If you enter `http://localhost:8080/fortune` in your browser, you will get a Bad Request response (status=400).

2. The form data is sent as part of the request when we submit the form. It can be seen in the Request Params section of the network inspector in your browser.

3. When you submit the form and see the `/fortune` page, try refreshing it. The browser will ask you if you want to resend the data you sent earlier. This is because of what we saw in point 1 above - the request which is used to render this page (`POST` request, form data is included) is different from the request that is created when you simply enter `http://localhost:8080/fortune` in your browser (`GET` request, no form data).

### Displaying a random fortune on the fortune page

- I have created a file called [fortunes.txt](https://github.com/amangup/coding-bootcamp/blob/master/lecture10/fortunes.txt) which contains a list of many fortunes, one per line.
- **This part is left as an exercise**: Use this file and display a random fortune to the user.

### Static files

Let's spruce up our web app a bit. First, let's display an image on the home page.

To do that, we need to understand how does a web server serve static files.
- The browser makes a `GET` request for a static file like any other `GET` request.
- The web server should understand that this request is for a file, and it has to send back that file in response.
- Flask supports this behaviour.
    - Though Flask supports this, it is not used in production servers. Production websites use CDNs (Content Delivery Network) to store and serve static files. Doing that is out of the scope of this lecture.

#### Showing images

- First we need an image. I found this image called `cookie_rich.jpg` using Google Search, which I am going to use:

![Fortune Cookie](https://raw.githubusercontent.com/amangup/coding-bootcamp/master/lecture10/examples/fortune_teller_webapp/fortune_teller/static/cookie_rich.jpg)

- We need to copy this file in a folder called `static`. Here is how the directory structure looks now:

```
requirements.txt
webapp/
       test_server.py
       fortune_teller/
                      templates/
                                hello_world.html
                                fortune.html
                      static/
                                cookie_rich.jpg
                      __init__.py
                      home.py
                      show_fortune.py
                      forms.py
```

To display the image, we just need to add the following line inside `home.html` template:

```html
<img src="{{ url_for('static', filename='cookie_rich.jpg') }}" width="300"/>
```

- The HTML `img` tag is used to display images.
- The `src` field in the `img` tag contains the URL at which image can be found.
- We use the `url_for()` function to create that URL.
  - Flask has a convention where the directory named `static` can be used to serve static files. It will not work if you rename the directory to something else.
  - If you call the function `url_for` as shown above, it creates the appropriate url for the image.

- The width tag is just to make the size of the image a bit smaller.

You can now see the image (whatever you chose) on the home page of your web app.

#### Showing the fortune in style

We are going to use CSS (Cascading Style Sheets) to beautify the look of how the fortune is displayed. This is how it looks:

 ![Fortune](https://raw.githubusercontent.com/amangup/coding-bootcamp/master/lecture10/fortune_css.png)

For that, we need appropriate CSS code. I found the following code online, put this into a file called `quote.css`, and copied it into the `static` directory. I have almost no idea how this CSS works!

```
/* From https://www.kirstencassidy.com/css-fancy-quotes/ */

.quotation{
  font-size: 30px;
  //margin: 0 auto;
  quotes: "\201C""\201D""\2018""\2019";
  padding: 10px 20px;
  line-height: 1.4;
}

.quotation:before {
  content: open-quote;
  display: inline;
  height: 0;
  line-height: 0;
  left: -10px;
  position: relative;
  top: 30px;
  color: #ccc;
  font-size: 3em;
}
.quotation::after {
  content: close-quote;
  display: inline;
  height: 0;
  line-height: 0;
  left: 10px;
  position: relative;
  top: 35px;
  color: #ccc;
  font-size: 3em;
}
```

Again, we only need to change the template (this time, `fortune.html`). Here is how my `fortune.html` template looks like:

```html
<!doctype html>
<html>
    <head>
        <title>Fortune Teller</title>
        <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='quote.css') }}">
    </head>
    <body>
        <h2>Hello, {{ username }}!</h2>
        <br>
         <div class="quotation">
             {{ fortune_text }}
         </div>
    </body>
</html>
```

- To link CSS to your HTML file, we use the `link` HTML tag. 
- We need to tell the `link` tag where to find the file containing the CSS code. We use the `url_for()` function in exactly the same way we used it to display the image above.
- To the tag in which we put the fortune (I use `div` by default), we add `class="quotation"` to refer to the CSS class `quotation` that is created in the CSS code.

## Deploying your app on pythonanywhere.com

- We have created a fun website, and we obviously want to share it with our friends!
- To do that, we need to host our web app on a hosting platform.
- We are going to use [pythonanywhere.com](https://www.pythonanywhere.com/) to host our web app.
  - It has a free level of service which is good enough for our this purpose.
  - It is compatible with Flask apps, and thus it's pretty easy to get our app running there.
  
Here is the list of instructions to deploy your fortune teller website there:

1. Create a Beginner account at pythonanywhere.com, and log in.
2. On your computer, create a zip file which contains the directory `fortune_teller`. Do not include `test_server.py`.
3. On pythonanywhere.com, go to your Dashboard -> Files -> Browse Files. You should see that you are in the directory `/home/<your username>`.
4. Using `Upload a file`, upload the zip archive that you just created. You should see that file in the list of files.
5. On top of the listings, there is a link called "Open Bash console here". It opens a terminal.
6. Once the terminal is running (you should see a `$` prompt), run the command `unzip fortune_teller.zip`. That will unzip the files for your web app.
7. On the top right, click on the tribar icon, and select "Web".
8. Click on `Add a new web app`. Click next until you reach "Select a Python Web framework".
9. Select "Flask", and then select Python 3.6. When it asks you the path where to create the flask app, just choose the default (we will not use that).
10. Eventually, you should see the "configuration" page for your web app. Click on Code -> WSGI configuration file: (starts with `/var/www`).
11. You are now editing a python file. Change `project_home` path to `u/home/<your username>/fortune_teller`
12. In the last line, change `flask_app` to `fortune_teller`.

That's it! You now have a fortune teller website running at `<your username>.pythonanywhere.com` (might need a refresh or two to show your web app). 

### WSGI

You might be curious on how the website is running even though we didn't upload `test_server.py` and call `app.run()`. Python anywhere runs its own web server. To communicate with your app, it uses a Python interface called WSGI (Web Server Gateway Interface). Flask complies with this specification. Thus, python anywhere's server can interact with our Flask app and make the website run.


