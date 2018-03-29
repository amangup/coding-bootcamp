# Variables

## What is a variable?
 - Variables are essentially containers designed to store data. You can think of it as a box containing a piece of paper on which you have written a number.
 - This container is stored in memory (the box is kept in the cupboard).
 - Each variable has a name which is used to refer to the contents of the container.
 - Once you have defined a variable, you can use it as many times as you need.
 - As the name suggests, you can change the value assigned to a variable.
    - in Python, when you do this, the variable name gets associated with an entirely different container that contains the new value that you assigned to the variable.
    - the old container gets repurposed to store some other data.
 - The size of this container can vary depending on the data. If the variable contains your name, or a number, then it's size is not that large. On the other hand, a variable can store the complete contents of the Lord of the Rings books. That variable occupies a large amount of space in memory.
    - The amount of memory space is measured in bytes.
     
## How to define variables?     
     
In Python (and in almost all other programming languages), variables are assigned a value using an **=** (equal to) symbol. The variable name is written on the left hand side of this symbol, and the right hand side can be a _constant_, as shown in examples below:

```python
name = 'Lucy'
age = 32
weather = 'Cloudy'
waiter_tip = 9.21
is_working_day = True
```

The right hand side can also be other variables, or expressions, as shown in examples below:
```python
x = 2018
year = x
next_year = year + 1
```

## Variable naming rules

Variable names must follow certain rules:
- They can start with an alphabet or an _underscore_ **_** symbol.
  - Conventially, variable names starting with an _underscore_ have a special purpose.
- They can have numbers and underscores after the starting character.
- The names are case sensitive.
- You cannot use reserved words for variable names. Examples of reserved words are `if`, `return`, `import`, `def`, etc. The complete list can be [seen here:](https://docs.python.org/3/reference/lexical_analysis.html#keywords)
- Good Practice 1: Name of the variable should represent the data it contains.
- Good Practice 2: Variable names should be of the form `words_with_underscores`, using only small letters.

The examples below illustrate the naming rules.
```python
alphabet = 'X'
_special_variable_ = 'avoid using this'

# This will raise an error
2moro = 'invalid variable name'

gr8 = 'valid variable name'
normal = 'a normal variable'
NORMAL = 'is not the same as the variable normal'

# This too will raise an error
return = 'another invalid variable name'

# bad practice
g = 100000

# good practice
population = 100000
salary = 100000

# follow python convention
fishes_in_tank = 5

# this goes against python convention
fishesInTank = 5
```

# Variable Types
- A variable type represents the kind of data it contains, like a number, a sentence, etc.
- Variables in python can be of infinite types.
    - Programmers can define new types, so there is no limit on types of variable.
- Python has many inbuilt types. Of those, the following ones are usually called _primitive_ types, and are the most commonly used:
  - numerical types: `int` and `float`
    - `int` variables store numbers which are whole numbers (also called integers).
    - `float` variables store numbers which have decimal parts (also called real numbers). `float` is short for _Floating-point numbers_.
  - `str` - the string type
    - The string variable contains a _string_ of characters. Thus it can be a word, a sentence, a password containing special characters, etc.
  - `bool` - short for Boolean, name after [George Boole](https://en.wikipedia.org/wiki/George_Boole). 
    - This type of variable can hold only two values - `True` or `False`.
    
The following examples illustrate the all these types

```python
>>> age_in_years = 30
>>> type(age_in_years)
<class 'int'>

>>> taxi_fare = 5.34
>>> type(taxi_fare)
<class 'float'>

>>> state = 'California'
>>> type(state)
<class 'str'>

>>> earth_is_flat = False
>>> type(earth_is_flat)
<class 'bool'>
```

## Numeric Types
Let's discuss the numeric types in more detail. 
- The main advantage of numeric types is that you can do calculations with numeric variables. 
- Python language defines many _operators_ which can be used to add, subtract, divide and perform more kinds of operations on any two numerical variables and constants.

Here is the list of main operators:
- Addition: **+**
- Subtraction: **-**
- Multiplication: __*__
- Division: **/**
- Exponent: __**__
- Remainder or Modulo = **%**

Some examples showing how to use these operators are shown below:

```python
ironman_distance = 2.4 + 112 + 26.2

# Combining variables and constants
onroad_distance = ironman_distance - 2.4

yards_in_mile = 1760
# Using variables for both operands
distance_yards = ironman_distance * yards_in_mile

world_record_time_hrs = 7.75
# This evaluates to 18.1419...
avg_speed_mile_per_hour = ironman_distance / world_record_time_hrs

# This evaluates to 1024
num_bacteria_10th_gen = 2 ** 10

# This evaluates to 18. 21st Century is now an adult!
years_in_21st_century = 2018 % 100 
```

### Operator precedence
In an expression with multiple operators, python uses a precedence order to calculate the result. The order in which it applies the operators is as follows:

1. Parenthesis - evaluate the expression in the innermost parenthesis first.
2. Exponent
3. Division, Multiplication, Remainder
4. Addition, Subtraction

In the following example, `(9 - 4)` is evaluated first, `5 * 5` second, and `3 + 25` last.

```python
>>> complicated_expr = 3 + 5 * (9 - 4)
>>> print (complicated_expr)
28
```

In practice, it is recommended that you use parenthesis wherever possible to clarify the order of calculations.
```python
>>> complicated_expr = (3 + 5) * (9 - 4)
>>> print (complicated_expr)
40
```

### Implicit Conversion between numeric types
- If you add a `float` variable and an `int` variable, python will automatically _convert_ the `int` variable to `float`, and then perform the addition.
  - Technically, Python can only operate on two variables of the same type. That is why it needs to do the conversion.
- In any operation involving a `float` and an `int`, the `int` variable will always be converted to `float`. The `float` variable will never be converted to the `int` type.
- If you divide two `int` variables, the output will be of type `float`.

An example illustrating _implicit conversion_.

```python
>>> average = (5 + 10) / 2
>>> type(average)
<class 'float'>
```

### Explicit Conversion between numeric types
You can also explicitly convert variables between `int` and `float` types.
  - `float()` converts an `int` to `float`
  - `int()` converts a `float` to `int`
  
Explicit conversion is most useful to convert a `float` to an `int`, as shown below.

```python
>>> age_in_days = 10000
>>> age_in_years = age_in_days / 365
>>> print (age_in_years)
27.397260273972602
>>> print (int(age_in_years))
27
```

Note that `int()` will just truncate the decimal part of a `float` number. It will not round the value to the nearest integer (or to the smaller or larger integer).

```python
>>> print (int(-5.3))
-5
```

### Practice exercises
1. Take someone's age as input, and tell them in what year will they retire.
2. If first day of the year is Monday, what will be the 100th day of year be? 


## String Type
- As mentioned before, it is used to store a _string of characters_.
- String constants can be defined using `'single quotes'` or `"double quotes"`.

Some examples:
```python
name = "Luke Skywalker"
password = 'l1gh+s@b3r'
multiline_quote = ("In the long run men only hit what they aim at. Therefore," 
"though they should fail immediately, they had better aim at something high.")

>>> tabbed_name = 'Luke\tSkywalker'
>>> print (tabbed_name)
Luke	Skywalker

>>> newline_name = 'Luke\nSkywalker'
>>> print (newline_name)
Luke
Skywalker
```

### String Operators
- Concatenation: **+**
- Repetition: __*__
- Index: **[]**
- Slice: **[a:b]**
- Membership: **in**
- Inverse of membership: **not in**
- String formatting: **%**

Some examples showing how to use the operators above:

```python
>>> address = '123 California Ave,' + 'Apt 42'
>>> print (address)
123 California Ave,Apt 42

>>> lyrics = "Friday," * 5
>>> print (lyrics)
Friday,Friday,Friday,Friday,Friday,

>>> last_name = 'Smith'
>>> print (last_name[0])
S

>>> month = 'January'
>>> month_code = month[0:3]
>>> print (month_code)
Jan

>>> name = 'Ben Solo'
>>> is_hans_son = 'Solo' in name
>>> print (is_hans_son)
True

>>> team = 'Poe, Chewbacca, Phasma'
>>> is_good_side = 'Phasma' not in team
>>> print (is_good_side)
False

>>> favorite_movies = 'My favorite movies are %s, %s and %s' % ('Lord of the Rings', 'Star Wars', 'Forrest Gump')
>>> print (favorite_movies)
My favorite movies are Lord of the Rings, Star Wars and Forrest Gump
```

### Conversion to and from string:
- `int()` and `float()` convert a string to the corresponding type of number.
  - If the string is not a number, an error is raised.
- `str()` converts numbers to strings.

A few examples

```python
>>> age_str = '45'
>>> type(age_str)
<class 'str'>
>>> age = int(age_str)
>>> print (age)
45
>>> type(age)
<class 'int'>

>>> error = float('Luke')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: 'Luke'

>>> integer_part = 35
>>> fractional_part = 99
>>> number_str = str(integer_part) + "." + str(fractional_part)
>>> print (number_str)
35.99
```

## Boolean Type
- Boolean variables can represent either `True` or `False`
- In future lectures, we will learn the concept of branching: Running different code is a variable or expression is `True` or `False`.
- These are the common _tests_ to get a boolean variable:
  - Equals: **==**
  - Not Equal: **!=**
  - Greater than (or equals to): **>**, **>=**
  - Less than (or equals to): **<**, **<=**

Following examples check out how these operators are used.

```python
>>> name = 'Luke'
>>> is_equal = (name == 'Luke')
>>> print (is_equal)
True

>>> is_unequal = (name != 'Anakin')
>>> print (is_unequal)
True

>>> print (5 > 4)
True
>>> print (2.0 <= 1.9)
False
```
  
### Boolean operators
- Two boolean variables can be combined to get a new boolean value using the following operators:
  - And: `and`
  - Or: `or`
  - Not: `not`
 
```python
>>> wind = 'windy'
>>> rain_chance = 30
>>> going_running = (wind != 'windy') and (rain_chance < 50)
>>> print (going_running)
False

>>> sick = False
>>> holiday = False
>>> going_to_work = (not sick) and (not holiday)
>>> print (going_to_work)
True

>>> not_going_to_work = sick or holiday
>>> print (not_going_to_work)
False
``` 
## Practice exercises
- Take account balance as input, and print a sentence which says "Your account balance is 350 dollars".
- Take two names as input, and check if either of them is Matthew.