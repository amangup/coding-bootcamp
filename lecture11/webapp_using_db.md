# Web Applications using Databases

In the last lecture, we built websites that have no _state_. Irrespective of user and time, they provide the same functionality.

Most websites do have a state, though. The state changes over time, like the list of articles on the home page of a blog (global state), or the user's profile on a social network (user specific state).

The state is represented by data, which is stored in a database (DB). In this lecture, we will learn what databases are and how to build web applications using a database. We will build a quiz app, in which the users can answer quiz questions and know their score. You can also add new questions to the database (which then the users will be asked in the quiz), and eventually we will gate this access by asking _admins_ to login before they can add questions.

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
- A table is defined by a schema, which is the list of all **columns** that the table can contain. Each column has a name, and a type (for the kind of data it stores, like number, string, etc.).

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

- Some columns can be marked as **indexed**. Marking a column as indexed increases the speed of queries which use that column _in a condition_ (we will learn exactly what this means a little later). This speed improvements comes at the cost of more memory and disk space usage.

## Actions

Now that we understand how data is stored in a DB, let's understand what kind of actions we can take.

### Schema changes

The specifications of tables and columns is called a **schema**. The actions you can take are:
- create new databases
- create new tables
- add new columns to the tables
- very rarely, remove or change the type of existing columns.

These actions are one time changes. Some of them need to be done before you can build your web app (create new databases, tables), while the others are somethings that you as you implement new features or modify your web app.

The problem of _data design_ is usually a tough one to solve well. Good data design makes it easy to do actions on the tables. There is a whole [set of principles](https://en.wikipedia.org/wiki/Database_normalization) that are designed to aid data design.

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

We will not use SQL in our tutorial and projects. But familiarity with SQL is expected from developers, and thus it's a good idea to learn it.

### Database solutions
There are many database _solutions_ in the market, essentially software that implements the concepts we discussed above. MySQL and PostgreSQL are two very famous DBs that many companies use (and that is also the primary product of the company Oracle). These databases run as _servers_ where users and applications can log in and execute queries.

For our work, we will use a simpler DB called [SQLite](https://www.sqlite.org/about.html). SQLLite doesn't use a server based design, instead it stores the data in disk files. This helps us avoid setting up a DB server before we can get started (and is used by many developers for this reason). The database interaction code we will write is agnostic to the database solution (i.e., the same code supports many solutions, including SQLite, MySQL and PSQL), thanks to a library called **SQLAlchemy**.

## Modeling websites visually 

In this tutorial, we are going to build a website which let's users take a quiz. As we've already seen, a single website can contain can contain many views, templates, forms, etc. and it can be difficult to remember how each of those are connected. To help create a mental picture, we will get into the habit of _drawing_ our web app design before writing the code for it.

We will break the diagrams into two types - **pages** and **user flows**. Here is the list of all pages for the quiz app.

 ![Quiz Pages UML](https://raw.githubusercontent.com/amangup/coding-bootcamp/master/lecture11/quiz_pages_uml1.png)

- The Three section box represents a page, and we put all the basic details there
- The dashed arrow represents a dependency
