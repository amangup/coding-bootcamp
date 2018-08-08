# Web Applications using Databases

In the last lecture, we built websites that have no _state_. Irrespective of user and time, they provide the same functionality.

Most websites do have a state, though. The state changes over time, like the list of articles on the home page of a blog (global state), or the user's profile on a social network (user specific state).

The state is represented by data, which is stored in a database (DB). In this lecture, we will learn what databases are and how to build web applications using a database. We will build a quiz app, in which the users can answer quiz questions and know their score. You can also add new questions to the database (which then the users will be asked in the quiz).

This is a lot to learn. Let's start with the first item - What are Databases?

## What is a database?

A database is an organized collection of data. The data is organized into **tables**, and from a practical perspective, a database can be thought of as a collection of tables. Each table contains data that logically belongs together, however different tables can be related to each other.

A database allows you to 
- create the **schema** for your data
- add, update or remove data from the tables
- run a **query** to get the information you need.

To understand things better, let's take a specific use case. Let's say we have two tables:
- A table called `car_purchases` containing a list of car purchases in a country.
- A table called `car_models` containing basic information about all car models.

### Tables and Columns
- A table is defined by a schema, which is the list of all **columns** that the table can contain. Each column has a name, and a type (for the kind of data it stores, like number, string, etc.). This type is specific to the DB (SQL DBs define a common set of types), and is not the type defined in Python or any other programming language (this distinction is important to remember).

    For the table `car_purchases`, we can consider following columns:
    - Date of purchase (type Date)
    - Name of buyer (type String)
    - City of purchase (type String)
    - Amount paid for purchase (type Number)
    - Make of the car (type String)
    - Model of the car (type String)
    
    For the table `car_models`, we can consider the following columns:
    - Make (type String)
    - Model (type String)
    - Body Type (type String)
    - Engine Type (type List)

- Data is stored in multiple rows, where each row contains a value for each column in the table schema.

    Here are examples of how our two tables might look like:
    
    **car_purchases**
    
    | Date | Name of buyer | City | Amount | Make | Model |
    | --- | --- | --- | --- | --- | --- |
    | 1-Apr-2018 | Grace | Monterey | 27,000 | Mazda | Miata |
    | 4-Apr-2018 | Graham | Greenwich | 300,000 | Ferrari | 458 |
    
    **car_models**
    
    | Make | Model | Body Type | Engine Type |
    | --- | --- | --- | --- |
    | Mazda | Miata | Roadster | [S4] |
    | Audi | A6 | Saloon | [S4, V6] |
    | Ferrari | 458 | Coupe | [V8] |


- There are some special column types.
- The most important one is called a **primary key**. This is a column (or a combination of columns) which uniquely identify a row. In some DBs, such a column must always exist. 
    * For the table `car_models`, we can consider the combination of Make and Model as the key, as no two cars have the same make and the model.
    * For the table `car_purchases`, we currently don't have a primary key. Frequently, the primary key is just an integer ID. The database itself can maintain that integer ID, by using the next integer every time a new row is added. If we use that, our `car_purchases` will table will look like this:
    
    | id | Date | Name of buyer | City | Amount | Make | Model |
    | --- | --- | --- | --- | --- | --- | --- |
    | 1 | 1-Apr-2018 | Grace | Monterey | 27,000 | Mazda | Miata |
    | 2 | 4-Apr-2018 | Graham | Greenwich | 300,000 | Ferrari | 458 |
    
- A table can contain a **foreign key**. Foreign key is a column (or a combination of columns) which uniquely identifies a row in _another table_. In our tables, the Make and Model columns in the table `car_purchases` serve as the foreign key, to the `car_models` table.

- Some columns can be marked as **indexed**. Marking a column as indexed increases the speed of queries which use that column _in a condition_ (we will learn exactly what this means a little later). This speed improvement comes at the cost of more memory and disk space usage.

## Actions

Now that we understand how data is stored in a DB, let's understand what kind of actions we can take.

### Schema changes

The specifications of tables and columns is called a **schema**. The actions you can take are:
- create new databases
- create new tables
- add new columns to the tables
- very rarely, remove or change the type of existing columns.

These actions are one time changes. Some of them need to be done before you can build your web app (create new databases, tables), while the others are somethings that you as you implement new features or modify your web app.

The problem of schema _design_ (or _data design_) is usually a tough one to solve well. Good data design makes it easy to do actions on the tables. There is a whole [set of principles](https://en.wikipedia.org/wiki/Database_normalization) that are designed to aid data design.

### Write actions

All actions which modify the contents of the tables are called write actions. You can

- add new row(s) of data to a table
- modify or remove an existing from the table

These actions are very frequent and usually done every time an user does some action on your web app (e.g. on a social network, every time you post something new, a new row is created in a table).

### Read actions

You can query the database for some information you need. This could be
- A single row for one user
- All rows in a table
- All rows, where the contents of the table meet some criteria. For e.g., in our data about car purchases, we might want to know the number of purchases where the buyer spent more than $100,000. For this query, you apply a _condition_ on the Amount column.
- information that needs to use multiple tables. For e.g., if we want to know how many SUVs were purchased in April, our first condition is applied to the column Body Type in `car_models` and the second one is applied to the column Date in `car_purchases`. These types of queries need to **join** two or more tables.

This is just a small set of examples. The queries can become arbitrarily complicated.

### SQL

For all the actions listed above, we need a way to tell the DB to execute those actions. There is a language called **Structured Query Language (SQL)** which is most common way to do that. Practically all the DBs in the world understand SQL.

An example query (for one of the items listed above in Read actions section) is: `SELECT * FROM car_purchases WHERE Amount > 100000`.

We will not use SQL in our tutorial and projects. But familiarity with SQL is expected from developers, and thus it's a good idea to learn it.

### Database solutions
There are many database _solutions_ in the market, essentially software that implements the concepts we discussed above. MySQL and PostgreSQL are two very famous DBs that many companies use. These databases run as _servers_ where users and applications can log in and execute queries.

For our work, we will use a simpler DB called [SQLite](https://www.sqlite.org/about.html). SQLLite doesn't use a server based design, instead it stores the data in disk files. This helps us avoid setting up a DB server before we can get started (and is used by many developers for this reason). The database interaction code we will write is agnostic to the database solution (i.e., the same code supports many solutions, including SQLite, MySQL and PSQL), thanks to a library called **SQLAlchemy**.

## Modeling websites visually 

In this tutorial, we are going to build a website which let's users take a quiz. As we've already seen, a single website can contain can contain many views, templates, forms, etc. and it can be difficult to remember how each of those are connected. To help create a mental picture, we will get into the habit of _drawing_ our web app design before writing the code for it.

We will break the diagrams into two types - **pages** and **user flows**. Here is the list of all pages for the quiz app.

 ![Quiz Pages UML](https://raw.githubusercontent.com/amangup/coding-bootcamp/master/lecture11/quiz_pages_uml1.png)

- The Three section box represents a page, and we put all the basic details there
- The dashed arrow represents a dependency

Here is the user flow diagram

![Quiz user flow](https://raw.githubusercontent.com/amangup/coding-bootcamp/master/lecture11/quiz_user_flow1.png)
 
- The black dot represents the starting point

Both these diagrams capture some essential information, and are going to be quite beneficial to refer back to from time to time. It's good to create diagrams which have essential information, but not contain everything under the sun - such diagrams would be too hard to use.
 
I hope that due to these diagrams, you have a very clear idea of what we're going to build, and you would be able to do it yourself if not for the new DB interaction element.
 
## Defining and creating a Database
 
The database and the tables which we need for the app are created once, and then the app can use it as many times as needed. Since we are using SQLite, the database and table creation will only lead to a new file being created which contains all the structure information and the data. But, as mentioned before, most of the process remains the same for other DBs.
 
Before we define our table structure and create the database, let's take care of the scaffolding that is required to hold a website.
 
### The quiz flask app
 
Let's create a directory structure which is very similar to the fortune teller app we created in the last lecture (in a new project).
 
```
requirements.txt
webapp/
       config.py
       quiz/
                 __init__.py
                 db_tables.py
```

The `db_tables.py` is new and this is where we will define the structure of our table we will use for the quiz app.

For this project, we have a few more dependencies to list in the `requirements.txt`, as shown below. As before, if PyCharm doesn't automatically install the dependencies, then install them manually.

```
Flask==1.0.2
Flask-WTF==0.14.2
Flask-SQLAlchemy==2.3.2
bleach==2.1.3
```

- `Flask-SQLAlchemy` is the main dependency that helps us work with DBs.
- `bleach` is a library written by the Mozilla Foundation to _sanitize_ HTML inputs, i.e., make form inputs secure. We will allow our questions to contain HTML inside them, but limit it to only basic formatting related tags. We'll talk about this again later.

Next is the `__init__.py`, the file where we define the Flask object. For this webapp, we need to add a couple more lines, as shown below.

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from quiz import db_tables
```

- We import the class `SQLAlchemy` which is the class that will help define the structure of the DB and create, read, and write to that DB.
- Further down below, we create the object `db`, which is of type `SQLAlchemy`. Note that it takes the object `app` of type `Flask` (the main class we've been using for making our website work) as an argument. This helps _configure_ the SQLAlchemy object.
- The last import statement is going to import the definition of our tables, which is required to define them.

Before we define the tables, let's take care of the `config.py` file. That class has a new attribute as well:

```python
class Config:
    SECRET_KEY = 'really-hard-password'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////home/aman/quiz.db'
```

- The attribute `SQLALCHEMY_DATABASE_URI` is the path for our DB which in this case is a path of the file (URI stands for [Uniform Resource Identifier](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier). This field is required in the config by `SQLAlchemy` class to know which DB to contact.
    * This is also where we've specified that we are using SQLite. If we were using a different type of database, the URI would change accordingly.

### Defining a table

This section is the critical part, where we will use what we learned in the beginning about tables. Using SQLAlchemy, we can specify the structure of the table as a Python class. In the code below, we define a class that represents the `Question` table which will contain all the questions for the quiz.

The following code contains the contents of `db_tables.py`.

```python
from quiz import db


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.Text)
    option_a = db.Column(db.Text)
    option_b = db.Column(db.Text)
    option_c = db.Column(db.Text)
    option_d = db.Column(db.Text)
    answer = db.Column(db.Integer)

    def __repr__(self):
        return "Q{0}: {1}".format(self.id, self.question_text)
```

Here's how this module works:

- We import the `db` object which is required before we can define any class that represents a table (a _model_ class).
- The name of the class `Question` is also the name of the table in the DB.
- The class inherits from a class called `db.Model`. This is mandatory.
- Each class attribute represents a column in the table, and is actually assigned a value that is an object of the type `db.Column`. The name of the attribute variable is the name of the column in the table.
- The `db.Column` allows you to specify the properties of the column.
  * In this table, we are using two types of columns - `db.Text` and `db.Integer`. These must correspond to the types in the DB, and are not the Python types.
  * The `id` column is the primary key, and that is specified by setting the keyword argument `primary_key` to `True` in the constructor of `db.Column`. This column's value will be automatically set by the DB when you insert new rows.
- Note that `__repr__()` method accesses the columns of the table from `self`. Even though we have not set those variables' values in `self`, we get access to them because `SQLAlchemy` does that for us.

An interesting thing to note is that there is _circular dependency_ - `__init__.py` imports `db_models` and `db_models` imports `db` which is defined in `__init__.py`. This is a thing we should be careful about as normally these can lead to hard to find bugs. This was true for modules containing view functions in the last lecture as well. As long as we import the modules containing DB models and view functions after the `app` and `db` object are defined, we will be fine.
 
    
### Creating the database

The database creation happens once, and then you don't need to worry about it. To do it, you need to run the Python Console (using Pycharm, or by running python in terminal).

At first, you need to add the path to your `webapp` directory to `sys.path`. What this does is gives you access to any packages and modules defined in that directory.

```
>>> sys.path.append('/path/to/webapp')
```

Then, we can import the `db` object, and use a convenient method to create the database.

```
>>> from quiz import db
>>> db.create_all()
>>> db.session.commit()
```

- The `create_all()` method discovers all the model classes we've defined and creates all those tables in the DB. (How this works is [somewhat tricky to understand](https://stackoverflow.com/questions/31082692/how-does-flask-sqlalchemy-create-all-discover-the-models-to-create)).
- We do `db.session.commit()` to make this change stick. 
  * When making changes to the DB, the process always has two parts - one where we define the changes, and the second where we commit them. This process is called a *Transaction*. 
  * All SQL DBs support transactions, and this concept overall is related to some [fundamental properties](https://en.wikipedia.org/wiki/ACID_(computer_science)) which are desired in DBs.
  * We will be using `db.session.commit()` every time we want to make a change in the DB.

Our DB and tables are ready! We can use them to add and query data.

### Using the database in console

Before we write webapp code for working with the DB, let's play with the DB a bit using the Python console itself. We will create a new question and store in the DB. After that, we will read all the contents of the `Question` table.

```
>>> from quiz import db_tables
>>> question = db_tables.Question(question_text="What gas is not a greenhouse gas?", option_a="Methane", option_b="Nitrous Oxide", option_c="Carbon Dioxide", option_d="Hydrogen", answer=4)
>>> db.session.add(question)
>>> db.session.commit()
>>> all_questions = db_tables.Question.query.all()
>>> print (all_questions)
[Q1: What gas is not a greenhouse gas?]
```

- First, we created an object of the `Question` type. That object represents data that we want to insert into the DB. 
   * Note that we didn't define a constructor in that class. `SQLAlchemy` did that for us.
- Then, we use `db.session.add()` method to add the object, which will add the data in `question` object to a new row in the `Question` table in the DB.
- We call `db.session.commit()`, which is the point at which data is actually put into the DB. 
- We can run the method `query.all()` to data from all the rows in the table, which is what we do next. Note that the return value is a list of objects of the `Question` class.
- When we print out the list, the question we added is printed. How the row gets printed is defined in the `__repr__()` method in the `Question` class.

It's important to understand all the steps we just did. Inside our webapp, when we write code to communicate with DB, we will use the same objects and methods.

## Creating the quiz app

Not that we know how we can add questions through the Python console, let's create the actual quiz pages to let the users take the quiz and see their score. This requires us to 
- read the questions from the DB and render them onto a page
- have a form which allows users to give an answer to every question
- Once the answers are submitted, show them the score and tell them the correct answers for each question.

This is a good time to go back and refer to the diagram to see what needs to be done to create these pages. Let's start with the **quiz page**.

### Quiz Page

The quiz page requires multiple elements - the form, the template and the view function. 

If we think about what we need from the form, it's different from what we've tried before. The earlier forms we created had a fixed number of fields. In this case, we need user to choose from four options for each question, and the number of questions are also not fixed (it depends on the data in the DB).

The `WTForms` has anticipated such use cases. There is a _meta field_ called `FieldList` which in turn can generate many copies of the same form as many times as required.

This is how the `forms.py` class looks like:

```python
from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField, FieldList

CHOICES = [('1', 'Option A'),
           ('2', 'Option B'),
           ('3', 'Option C'),
           ('4', 'Option D')]


class QuizForm(FlaskForm):
    answers = FieldList(RadioField('Correct Answer', choices=CHOICES),
                        min_entries=0)
    submit = SubmitField('Submit your answers')
```

- In the class `QuizForm`, the `answers` class attribute is of type `FieldList`. It can be thought as a _list_ of form fields, each of type `RadioField`. 
  - We can call the `append_entry()` method on an object of type `FieldList` to add more elements to that list (we will do that in the view function).
- The `RadioField` is the type of field which allows the user to choose only one option out of many. 
  - The `choices` are provided as a list of tuples, where the first element is the value of the form field if the user selects that, and the second element is the text that user sees against each option.
 
If we look at our pages diagram, we see that we've fulfilled both the dependencies for the quiz page, and we can now write the view function. We add the view function in the file `quiz.py`.

```python
from flask import render_template

from quiz import app, db
from quiz.db_tables import Question
from quiz.forms import QuizForm


@app.route('/')
def quiz():
    questions = Question.query.all()
    form = QuizForm()
    for i, question in enumerate(questions):
        form.answers.append_entry()
        choices = [('1', question.option_a),
                   ('2', question.option_b),
                   ('3', question.option_c),
                   ('4', question.option_d)]
        form.answers.entries[i].choices = choices

    return render_template("quiz.html", questions=questions, form=form)
    
    
@app.route('/score', methods=['POST'])
def score():
    pass    
```

- The first order of business is to compare the details like target, method, view function name and the template with the diagram, and make sure that everything matches.
- In the `quiz()` view function, we query the DB to get all the questions present in the `Question` table. This syntax for the query is identical to what we used while working with the DB in the Python console.
- The QuizForm needs to be updated based on the data we received from the DB.
  - The answers attribute is a `FieldList` and we need to make the list as long as the number of questions. For that, we call `form.answers.append_entry()` as many times as there are questions.
  - We create a new choice selection, where the text for each option is the option text from the Question, instead of just `Option A` which is the default.
- Eventually, we render the `quiz.html` template (which we haven't covered till now). We send the template the list of the questions, and the form - both of which are required for the template to show a quiz to the users.
- Note that we've created an empty view function for the score page. This to make sure our template for the quiz page works (as it tries to create the URL for the score page). 

Finally, we get to the template for the quiz page, the `quiz.html`, which is shown below:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Quiz</title>
</head>
<body>
    <h1>Quiz</h1>
    <p>
    <form action="{{ url_for('score') }}" method="POST">
        {{ form.hidden_tag() }}
        {% for question in questions %}
        <b>Question {{ loop.index }}</b>: {{ question.question_text }}
        <p>
        {{ form.answers.entries[loop.index0]() }}
        {% endfor %}

        {{ form.submit() }}
    </form>
</body>
</html>
```

- The whole page is essentially a form.
- If we refer to our diagrams, we'll find out that the form action should be the URL for the **Score** page.
- For displaying all the questions, we use the for loop syntax in the jinja2 templates.
  - Statements like for loop and if conditions use the `{%` and `%}` style for opening and closing the placeholder.
  - The for statement itself is identical to how it would be in Python code.
  - Since there is no indentation, the for statement needs to indicate where it ends using `{% endfor %}`
  - jinja2 provides us with some variables we can use as indices. We use the variable `loop.index` to show the question number (`loop.index` starts from 1), and `loop.index0` to use as index in the `form.answers.entries` list (`loop.index0` starts from 0).
- To get the statement of the question, we can use the attribute `question_text` of an object of type `Question`.
- To show the options, we need to show an appropriate _entry_ from the `answers` FieldList from the form. To do that, all elements of the FieldList are exposed as the attribute `entries` in (`form.answers`).

The quiz page is now complete. Given that we've already added a question in the DB, when you run this app (you'll need a `debug_server.py` to run the app), you should see that question displayed in the quiz. You should try adding another question into the DB using the Python console, and check if it shows up on your quiz page.
 
Obviously, the submit button will only cause an error right now. Let's build the score page next.
 
### Score page

The purpose of the score page is to tell the user how many questions they got right, and to list all the questions, tell them whether their answer fot that question was right.

From the diagram, we know that we don't any form or a new DB table to write the score page, just the view function and its templates.

We've already created an empty view function for the score page in `quiz.py`. Before we fill it out, let's brainstorm a little how it's going to be implemented
- To calculate the user score, we need to know the correct answers to all the questions, and the user's choices.
- The correct answers are part of the question data, and we can query the `Question` table again.
- To get the user's answer, we need to extract that from the form values (which are available in the dictionary `request.form`). Without looking at the code below, can you figure out what field you need to access in request.form to get the user's choices? (Hint: use view source on the quiz page in your browser).


```python
 # in the import statement "from flask import ...", import request.
 
 @app.route('/score', methods=['POST'])
def score():
    questions = Question.query.all()
    answers = []
    user_score = 0
    for i, question in enumerate(questions):
        user_answer = int(request.form['answers-' + str(i)])
        user_answer_letter = _get_answer_letter_(user_answer)
        if user_answer == question.answer:
            user_score += 1
            answers.append('{0} is correct'.format(user_answer_letter))
        else:
            correct_answer_letter = _get_answer_letter_(question.answer)
            answers.append('{0} is incorrect. Correct answer is {1}'
                           .format(user_answer_letter, correct_answer_letter))

    return render_template('quiz_answers.html', questions=questions,
                           answers=answers, score=user_score)


def _get_answer_letter_(user_answer):
    return chr(ord('A') + user_answer - 1)
```

- The list of questions is queried from the DB  as before.
- In the input tag for the radio fields, the `name` value in those fields are of the type `answers-0`, `answers-1` and so on. So, to get the user's choice, we need to get the values corresponding to the keys `answers-0` (and so on) in the `request.form` dictionary.
- The value in the dictionary can be one of the four strings:`"1"`, `"2"`, `"3"`, `"4"`. To compare that with the answer in the DB (which is stored as an integer), we need to compare the user's choice value to an integer.
- For each question, we are telling the user either the message "A is correct" indicating their answer was right, or the message "A is incorrect. Correct answer is B".
- The template needs to know the questions, the score, and the `answers` list.


The template `quiz_answers.html` for this is similar to the one with quiz page, though there is no form.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Quiz Answers</title>
</head>
<body>
    <h1>Your score is {{ score }}/{{ questions|length }}</h1>
    <p>
        {% for question in questions %}
        <p>
        <b>Question {{ loop.index }}</b>: {{ question.question_text }}
        <p>
        Options:<br>
        <ol type="A">
            <li>{{ question.option_a }}</li>
            <li>{{ question.option_b }}</li>
            <li>{{ question.option_c }}</li>
            <li>{{ question.option_d }}</li>
        </ol>
        <p>
        Your answer: {{ answers[loop.index0] }}
        {% endfor %}
</body>
</html>
```

- The top of the page shows the total score. The syntax `{{ questions|length }}` is used to get the length of a collection type (the `len` built-in function doesn't work in jinja2)
- The rest of the template is just using the `questions` and `answers` lists to show the question and the answers.

Congratulations, you've now built a quiz app! You can add as many questions to the DB, and the quiz app will test the users on all of those questions.

But, adding the questions through the Python console is too much work. We will add the functionality to add questions through the website itself next.

### Add Question Page

The add question page is a simple form which adds the data it collects to the DB. If you look at the user flow diagram, you'll see that the form submit action leads back to the add question page, and then it redirects to the "add question success" page. Why do we do that?

The reason is that when someone submits the form with the question details, we still need to add it to the DB before we can call it a success. In the way we will implement this logic, the user will be asked to resubmit the question if the DB commit fails, which is better than showing an error which is better than showing an error.

Later in the lecture, we will also add _form validation_ - to check if all required fields are present, and the contents are valid. In that case as well, we need to allow user the resubmit the question to pass the validation.

Once that is understood, the add question page is not too complicated. The page just renders the form, and on submit, it reads the values in the form and adds a new row in the DB. When the DB commit is successful, it redirects to the Add Question Success page.

The page diagram for Add Question page shows that we need a form called `QuestionForm` to implement this page. We can add the following class in `forms.py`:

```python
class QuestionForm(FlaskForm):
    question = TextAreaField('Question')
    option_a = StringField('Option A')
    option_b = StringField('Option B')
    option_c = StringField('Option C')
    option_d = StringField('Option D')
    answer = RadioField('Correct Answer',
                        choices=CHOICES)
    submit = SubmitField('Add the Question')
```

- The `QuestionForm` class is straightforward. The only new element is the `TextAreaField`, which allows you to create a bigger field to allow users to enter larger sentences or paragraphs.

Here is the code for `add_question.py`:

```python
from flask import request, render_template, redirect, url_for, flash
from sqlalchemy.exc import SQLAlchemyError

from quiz import app, db, forms
from quiz.db_tables import Question
from quiz.forms import QuestionForm


@app.route('/add_question', methods=['GET', 'POST'])
def add_question():
    if request.method == 'POST':
        question = Question(question_text=request.form['question'],
                                      option_a=request.form['option_a'],
                                      option_b=request.form['option_b'],
                                      option_c=request.form['option_c'],
                                      option_d=request.form['option_d'],
                                      answer=int(request.form['answer']))
        try:
            db.session.add(question)
            db.session.commit()
            return redirect(url_for('add_question_success'))
        except SQLAlchemyError:
            flash("We couldn't add your question due to a technical issue on "
                  "our side. Please try again later.")
            return _render_form_()
    else:
        return _render_form_()


def _render_form_():
    form = QuestionForm()
    return render_template('add_question.html', form=form)


@app.route('/add_question_success')
def add_question_success():
    return render_template('add_question_success.html')
```

- The first view function is `add_question()`. It contains all of the logic described above.
- The easy case is when `request.method` is not `POST`. In that case, we just create a form object and render the `add_question.html` template.
- In case the `request.method` is `POST`, we extract the data from the `request.form` dictionary, create the `Question` object for the row we want to add, and then add it to the DB.
- After the commit, we redirect to the `add_question_success` page.
- There is some new piece of syntax in this code listing - the `try` and `except` keywords.
  - Python language implements a mechanism called **Exceptions** which allows code to raise an Exception when something is wrong. The users of that code can receive the exception and ideally they need to handle it, otherwise it can stop their program from functioning(and we don't want our websites to crash).
  - In our case, the operation `db.session.commit()` interacts with a DB, and there is always a chance of that interaction can fail sometimes. In case of failure, `db.session.commit()` raises an exception of type `SQLAlchemyError`.
  - Using the `try` and `except` syntax, we can run a piece of code that has a chance of failure, and in case of failure, do something appropriate in that situation.
  - This concept is called **Error Handling** and exceptions are used by many languages to allow programmers to implement error handling.
  - You can read more about it here: [https://docs.python.org/3/tutorial/errors.html](https://docs.python.org/3/tutorial/errors.html).
- For our app's logic to work, we want to show the user a message that something went wrong, and then show the user the form again.
  - Flask provides a mechanism to show user messages for special situations which are not typically part of the page that user sees. To add messages to be shown to the user, the `flash()` function is used. 
  - In the template, we can access these messages, and show them only if there is something to show.
 
It's a good idea to spend some time in the section above to properly understand everything. The new concepts introduced here are very important and relevant to real life projects.
   
- Finally, in the same file, we have the view function for the `add_question_success` page, which is pretty much a static HTML page.

The last piece(s) of the puzzle are the templates for both the `add_question` and `add_question_success` pages. The latter is very simple, so let's focus on the former:

Here is the `add_question.html` template:

```html
<!DOCTYPE html>
<head>
    <title>Add a question</title>
</head>
<body>
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <ul style="color:red">
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}

    <h2>Enter the question details:</h2>
    <form action="{{ url_for('add_question') }}" method="POST">
        {{ form.hidden_tag() }}
        <p>
            {{ form.question.label }}<br>
            {{ form.question(rows=10, cols=80) }}
            <p>
            {{ form.option_a.label }}: {{ form.option_a(size=80) }}
            <p>
            {{ form.option_b.label }}: {{ form.option_b(size=80) }}
            <p>
            {{ form.option_c.label }}: {{ form.option_c(size=80) }}
            <p>
            {{ form.option_d.label }}: {{ form.option_d(size=80) }}
            <p>
            {{ form.answer.label }}<br>
            {{ form.answer() }}

        <p>{{ form.submit() }}
    </form>
</body>
</html>
```

- The first part of the template deals with flash messages. There is a function in flask called `get_flashed_messages())` that returns a list of the `messages` that need to be shown to the user. It deletes all the messages from the list which have been read by our app, so that we don't display the same messages again and again.
  - We use `with`, `if` and `for` statements to read all the flashed messages. Note that we use `style="color:red"` so that these messages appear in red and attract users' attention.
- The second part is the form to add the question.
  - As we first saw in the user flow diagram for this page, the form action is the `add_question` page, i.e., it submits the form to itself.
  - Rest of the form fields are present as expected. 
  - Note that when calling `form.question()` method in the template, we set two keyword arguments `rows` and `cols`. Remember that this field was of type `TextAreaField` and these values are used to set the size of that text area as it would appear to the user.
  
**Exercise:** Create the template for Add Question Success page. Make sure it has a link back to the Add question page in case users want to add more questions.

We've added the add question functionality, and now you can use this new page to add questions instead of using the Python console.

## Form validation and input sanitization

In the apps that've created till now, we have used for forms many times for user input, but we've checked if the user input is valid (e.g., all required fields are present). We've been expecting that the user would enter everything properly.

In this section, we will learn how to do form validation. There are many reasons it is required:
- Users might forget to fill some required fields.
- Users might enter a field wrongly (for e.g., email id is not in the proper `name@domain.com` format).
- For security purposes, to make sure that we don't accept values that can execute malicious code on our systems. In our case, we are going to sanitize the input.

### Client side vs. Server side

Form validation can be done on the client side (by running Javascript in the browser) or it can be done on the server side (by looking at the data present as part of the HTTP request in the server). Normally, it would appear that the client side validation is better, as that will tell the user about missing fields or other validation failures immediately, without needing an HTTP request and response. This is true - client side verification is more user friendly.

But it cannot replace server side validation. The HTTP request containing form data to the server can be made without someone browsing the website in a Javascript enabled browser. In essence, client side validation can always be bypassed.

- Thus, all validation must be done at the server side, and especially for websites accessible to the public, no form data should be consumed without such validation. 
- Some or all of that validation can be _duplicated_ on the client side, whose purpose is to have a more user friendly design, not correctness of functionality.

In this tutorial, we will focus on the server side validation, but we will also add very basic client side validation which the browsers implement for us.

### Ensuring required fields are filled

The most common form of validation is to make sure required fields are not left empty.

Let's try to make sure that all fields are present in the Add Question page. If that's not the case, and the form is submitted, we will flash a message telling the user that they haven't filled all the fields.

We've been using the library `WTForms` for helping us create forms, and it also has an in-built mechanism to validate the data user has filled in the form.  To use that, we will update our definition of the `QuestionForm` class as follows:

```python


from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
    question = TextAreaField('Question', validators=[DataRequired()])
    option_a = StringField('Option A', validators=[DataRequired()])
    option_b = StringField('Option B', validators=[DataRequired()])
    option_c = StringField('Option C', validators=[DataRequired()])
    option_d = StringField('Option D', validators=[DataRequired()])
    answer = RadioField('Correct Answer',
                        choices=CHOICES, validators=[DataRequired()])
    submit = SubmitField('Add the Question')
```

- The change is that for every form field, we have a new keyword argument in the constructor, called `validators`. This means that WTForms will apply those validators on the form data for that field.
- That argument is a list of _validators_, which are objects of specific classes that implement the functionality of validation.
- We are using a validator called `DataRequired`, which simply checks if the data we get from user is non-empty.
- The `wtforms.validators` has other validator classes which, for example, can check if the input is a valid email address. If you have a requirement for validation form input, it's always a good idea to check this module first.

To check if the form input passes validation (that we've defined above), we need to give the data to the `QuestionForm` class and then call a method called `validate()`. Knowing that, I have refactored the `add_question()` view function as follows:

```python
@app.route('/add_question', methods=['GET', 'POST'])
def add_question():
    form = QuestionForm(request.form)
    if request.method == 'POST':
        if form.validate():
            try:
                return _add_question_to_db_(request.form)
            except SQLAlchemyError:
                flash("We couldn't add your question due to a technical issue"
                      " on our side. Please try again later.")
        else:
            flash("Not all required fields were filled.")

    return _render_form_(form)


def _add_question_to_db_(formdata):
    question = Question(question_text=formdata['question'],
                        option_a=formdata['option_a'],
                        option_b=formdata['option_b'],
                        option_c=formdata['option_c'],
                        option_d=formdata['option_d'],
                        answer=int(formdata['answer']))

    db.session.add(question)
    db.session.commit()
    return redirect(url_for('add_question_success'))
```

- In the view function, when I construct the `QuestionForm` object, I pass it the data we've got in the form.
  - Note that this line is also executed when the user is first seeing the page (and has not submitted the form). In that case, `request.form` will be empty, and passing this data will have no effect.
- Before we use the data in the form, we call the `form.validate()` method, and _this_ is the point at which validators run and tell us if validation has failed or passed. If it has failed, we flash an appropriate message to the user.
- To make the code more readable, I have moved out some code to new functions.
- The template already handles the flashed messages. It would be user-friendly to add a (static) message to the template saying "All fields are required."

Try to submit the form without setting the right answer, and see what happens.

#### What about client side validation?

It will be helpful if the user's can know immediately if they have missed a field in the form. We are going to use a feature in the latest version of html (HTML5), called the [required attribute](https://www.w3schools.com/tags/att_input_required.asp). If add this attribute to an input tag in HTML, the browser will enforce the policy requiring that field to be non-empty for us.

The cool thing is that `WTForms` adds the `required` automatically when you add a `DataRequired()` validator to the field. However, that works only for some fields right now, and it doesn't work for radio fields automatically. To fix that, we can change the template a bit, and add the `required` attribute ourselves.

Earlier, to create the radio field for `answer`, we used the following method:

```html
 {{ form.answer() }}
```

but, we can do it as follows, instead:

```
{% for subfield in form.answer %}
    {{ subfield(required=True) }}
    {{ subfield.label }}<br>
{% endfor %}
```

- `form.answer` is a RadioField, hence it has many subfields representing each option.
- We can loop over those subfields, and call the method `subfield()` to output the HTML for that subfield only. When calling that method, we can set `required=True`, and that will set that attribute.
  - This can be used generally. If you pass an keyword attribute like `x="y"` in the tag, that will get added to the final HTML. And, if you add `x=True`, `x` will get added as an attribute without any value assigned to it, in the HTML tag.
  
Now, if you test the Add question page, you will see the browser notifying you if there is any field which is left empty.

#### Dynamic forms

Let's turn our attention to the Quiz page now. 
- The first change is that when the form submits, it should post to the quiz page, and not the scores page, so that we have the ability to render the same form if the validation fails. 
- Additionally, we would need to send the form data along when we redirect to scores page because scores page needs it to calculate the score. That is not a good solution, instead we are simply going to eliminate the scores page, and have the quiz page show the scores at the same URL.

Given these two points, let's update our page and user flow diagrams:

 ![Update Quiz Page UML](https://raw.githubusercontent.com/amangup/coding-bootcamp/master/lecture11/quiz_page_uml2.png)

 ![Quiz User flow](https://raw.githubusercontent.com/amangup/coding-bootcamp/master/lecture11/quiz_user_flow2.png)

Let's talk about validation. The form design is a bit more complicated there, because the number of fields is dynamically decided. Specifically,

- When we create `form = QuizForm(request.form)`, the `form` created doesn't know how many answer fields should be present (remember we call `append_entry()` _after_ we create the `form` object.
- Thus, field level validation built into the WTForms doesn't work for us.

Instead, we can do validation ourselves.

After all these changes, the file `quiz.py` looks like this. Go throug this carefully, as there are many changes.

```python
from flask import render_template, request, flash

from quiz import app, db
from quiz.db_tables import Question
from quiz.forms import QuizForm


@app.route('/', methods=['GET', 'POST'])
def quiz():
    questions = Question.query.all()
    form = QuizForm(request.form)
    if request.method == 'POST':
        # we are checking if the number of answers in the form data is the same
        # as the number of questions in the quiz.
        if len(form.answers.entries) == len(questions):
            return _render_score_page_(questions)
        else:
            flash("You must answer all the questions.")

    return _render_quiz_page_(form, questions)


def _render_quiz_page_(form, questions):
    for i, question in enumerate(questions):
        form.answers.append_entry()
        choices = [('1', question.option_a),
                   ('2', question.option_b),
                   ('3', question.option_c),
                   ('4', question.option_d)]
        form.answers.entries[i].choices = choices

    return render_template("quiz.html", questions=questions, form=form)


def _render_score_page_(questions):
    answers = []
    user_score = 0
    for i, question in enumerate(questions):
        user_answer = int(request.form['answers-' + str(i)])
        user_answer_letter = _get_answer_letter_(user_answer)
        if user_answer == question.answer:
            user_score += 1
            answers.append('{0} is correct'.format(user_answer_letter))
        else:
            correct_answer_letter = _get_answer_letter_(question.answer)
            answers.append('{0} is incorrect. Correct answer is {1}'
                           .format(user_answer_letter, correct_answer_letter))

    return render_template('quiz_answers.html', questions=questions,
                           answers=answers, score=user_score)


def _get_answer_letter_(user_answer):
    return chr(ord('A') + user_answer - 1)
```
 
- We changed the `score()` view function into a non-view function which does essentially the same thing. The main difference is that there is no `app.route()` decoration on it.
- The `quiz()` view function now accepts both `GET` and `POST` request.
- The `quiz()` view functions also calls the `_render_score_page_()` when the user has submitted the form properly.
- We do our own validation using the check `len(form.answers.entries) == len(questions)`, to make sure we've got as many answers as there are questions.

On top of this, we can change the template for rendering radio elements as we did in the add questions page, so that we add the `required` attribute to the HTML for those tags, and the browser will do the client side validation for us.

#### Aside: Macros in jinja2

Maybe you've already realized that even though we've added `flash()` messages to the quiz pages's implementation, we haven't changed the template for the quiz page to actually display those messages.

We can copy paste the code from `add_question.html` template to `quiz.html` template. But there is a better way - we are going to define that code as a **macro** in jinja2, and then reuse that macro.

To do that, let's create a new file in the templated directory called `macros.html`. This is not a template for any page to use, but instead, just contains the macros for other templates to use.

```html
{% macro show_flashed_messages() %}
{% with messages = get_flashed_messages() %}
{% if messages %}
<span style="color:red">
    {% for message in messages %}
    {{ message }}
    {% endfor %}
</span>
{% endif %}
{% endwith %}
{% endmacro %}
```

- the syntax for macro definition is similar to the function definition in Python, except that we use the keyword `macro` instead of `def`.
- we need to enclose macro definition in in a set of starting and ending jinja2 control blocks - `{% macro macro_name() %}` and `{% endmacro %}`.
- Macros can take arguments as well.

The `quiz.html` template (and the `add_question.html` template) can be updated to include this macro as follows:

```html
{% from "macros.html" import show_flashed_messages %}
{{ show_flashed_messages() }}
```

- This syntax is also similar to the import syntax for Python.

### Sanitizing input

Until now, we have been assuming that the text we take as input in the add question page has no html tags. Why do we need think about this?
- If we allow tags in the question and choices' texts, then we can allow the question to formatted as the user wants it - make some parts bold or italic, allow text to be colored.
- An HTML tag eventually leads to be some code to be executed in the browser, and a malicious actor can add tags to the question text, which when executed can cause harm. For example, someone can add a `<script>` tag and point to a javascript that can potentially crash the browser or read some data from the computer of the user (the latest way to add malicious code seems to be to run cryptocurrency mining code on unsuspecting users' code). We need to make sure that such malicious code is not allowed to run. 

What would happen, as the webapp is currently implemented, if some added tags in the question and choices' text fields.
- The data stored in the DB will contain the text as entered by the user (this is not good).
- When we display the question using the jinja template, it will automatically [_escape_](http://doc.locomotivecms.com/making-blog/2-6-html-escaping) all the text. That will make sure the HTML tags don't execute any code.

Thus, even though we are storing data in the DB with potentially malicious code, jinja templates are saving us from executing any of it. Ideally,
- we should clean up malicious code even before it enters the DB (just in case someone else is using the same DB and jinja is not there to save them).
- and allow some HTML tags which can be used for formatting.

#### Mozilla bleach library

Mozilla has written a Python library called `bleach` which can be used to implement our needs. It can take a list of _allowed tags_, and given any string, it can ignore the allowed tags and escape all others.

Let's how to use it. In the `add_question.py`, I've added the following function:

```python
import bleach

ALLOWED_TAGS = ['p', 'br', 'i', 'b', 'sub', 'sup', 'code', 'samp', 'var']

def _clean_html_(text):
    return bleach.clean(text, tags=ALLOWED_TAGS, attributes=['style'],
                 styles=['color'])
```

- The function `bleach.clean()` does the sanitization.
- This takes the list of allowed tags, allowed attributes for the tags, and for the `style` attribute (used to add CSS formatting), even the kind of CSS formatting you can add (in this case, you only change color).

We can use the `_clean_html_()` function before we add the data to the DB. In the same file, we can change how we create the Question object.

```python
question = Question(question_text=_clean_html_(formdata['question']),
                    option_a=_clean_html_(formdata['option_a']),
                    option_b=_clean_html_(formdata['option_b']),
                    option_c=_clean_html_(formdata['option_c']),
                    option_d=_clean_html_(formdata['option_d']),
                    answer=int(formdata['answer']))
```

Finally, since we are sanitizing the input ourselves, we have to tell jinja to not automatically escape the text when displaying. To do that, we can add `|safe` in the `quiz.html` and `quiz_answers.html` template as follows:

```html
<b>Question {{ loop.index }}</b>: {{ question.question_text|safe }}
```

and 

```html
{{ subfield.label|safe }}<br>
```

and any place else where we are rendering question or choices' text.

Here is an example of what you can do. In the question shown in the screenshot below, I added bold tag and color CSS formatting - which works as expected. I also tried to add a link, which doesn't show up as a link because mozilla bleach has escaped that HTML, as the `<a>` tag is not allowed.

![Question using HTML](https://raw.githubusercontent.com/amangup/coding-bootcamp/master/lecture11/question_html.png)





