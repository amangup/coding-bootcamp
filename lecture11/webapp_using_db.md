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
    SQLALCHEMY_DATABASE_URI = 'sqlite:///home/aman/quiz.db'
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

Before we write webapp code for working with the DB, let's play with the DB a bit using the Python console itself.
