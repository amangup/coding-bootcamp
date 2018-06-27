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
  - `port` is the port on which this web server will listen. We can choose any value which is not already being used. Typically, no production code uses 8080, and its commonly used for development.
  
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
- This placeholder uses double curly braces in the start and the end, and expects the object `hello_world` - which it use to replace the placeholder with.

### Rendering a template
- The act of replacing placeholders with concrete data in a template is called **rendering a template**.

To use the template, we will need to modify the code in `home.py`

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
- The render_template returns a string which is the _rendered html_, which is the return value of the function.

The template systems are sophisticated languages of their own, containing things like if conditions and loops. We will learn this language for the `jinja2` template system as we build more web servers.

### Creating web forms


  