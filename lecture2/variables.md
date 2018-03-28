# Variables

 - Variables are essentially containers design to store data. You can think of it as a box containing a piece of paper on which you have written a number.
 - This box or container is stored in memory.
 - Each variable has a name which is used to refer to the contents of the box.
 - Once you have defined a variable, you can use it as many times as you need.
 - As the name suggests, you can change the value assigned to a variable.
    - in Python, when you do this, the variable name gets associated with an entirely different box that contains the new value that you assigned to the variable.
    - the old box gets repurposed to store some other data.
 - The size of this box can vary depending on the data. If the variable contains your name, or a number, then it's size is not that large. On the other hand, a variable can store the complete contents of the Lord of the Rings books. That variable occupies a large amount of space in memory.
    - The amount of memory space is measured in bytes.
     
In Python (and in almost all other programming languages), variables are assigned a value using **=** (equal to) symbol. The variable name is written on the left hand side of this symbol, and the right hand side can be a _constant_, as shown in examples below:

```python
name = 'Lucy'
age = 32
weather = 'Cloudy'
waiter_tip = 9.21
is_working_day = True
```

The right hand side can also be other variables, or expressions, as shows in examples below:
```python
x = 2018
year = x
next_year = year + 1
```

Variable names must follow certain rules:
- They can start with an alphabet or an _underscore_ **_** symbol.
  - Conventially variable names starting with an _underscore_ have a special purpose.
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