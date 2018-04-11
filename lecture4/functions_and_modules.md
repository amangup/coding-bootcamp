# Functions
Functions is a fundamental mechanism designed to write reusable code.

## What is a function?
![Lock screen](https://raw.githubusercontent.com/amangup/coding-bootcamp/master/lecture4/function.svg.png)

- Function is a piece of program that programs a specific task. You can name it, and run that program again and again by referring to its name.
- You can provide function with input  (called _arguments_ or _parameters_), and you can also make the function _return_ the output.
- If a function doesn't return a value, it's called a _procedure_.
  - This is because it is not a function in the mathematical sense.
  - A procedure exists only for its _side effects_, i.e., it interacts with an I/O device, change the value of an input variable, etc.  

## Basic Function Syntax
```python
# This is a function which finds average of two numbers
def find_stat(x, y, stat_type):
    if stat_type == 'average':
        return (x + y) / 2.0
    elif stat_type == 'maximum':
        return max(x, y)
    elif stat_type == 'minimum':
        return min(x, y)

# This is a function which doesn't return anything. It's only there for the 
# side effect of printing a sentence.
def pretty_print(x, y, stat_type):
    # a function is calling another function.
    stat_output = find_stat(x, y, stat_type)
    # print is also a function built into python
    print ("The %s of %s and %s is %s." % (stat_type, x, y, stat_output))

pretty_print (5, 25, 'maximum')
```

```python
import sys

# This function has no input argument or return value.
def print_memory_error():
    print ("System is out of memory. Exiting...")

memory_usage_gb = 8.1 
if memory_usage_gb > 8.0:
    print_memory_error()
    # the following line exits the program.
    sys.exit(1)
```

Discussion of function syntax:
1. The keyword `def` is used to tell python that we are defining a function.
2. The name of the function is written after that. It's name must follow the same naming rules as a variable. The convention is to use lowercase letters with underscores for `function_name`.
3. The parenthesis contains the list of arguments. These are the variables you can use inside the function to do what it needs to do.
4. There is a colon after the parenthesis, and an indented section after that. This format is identical to what we saw for `if` and `while` statements.
5. Inside the function you can use the `return` keyword to return a value. You can only return one value, and once the return statement is executed, control returns to the next line of the function call.
6. To _call_ the function, you use the function name and provide values for arguments in parenthesis.

## Why use functions?
Technically speaking, functions are not _required_ to achieve a certain functionality. But here are the reasons why the concept of functions is indispensable.

- Reusability
  - This is the main reason why functions exist. 
  - Programmers hate to duplicate code at multiple places. If that code needs to change, then you have to fix it at all the places. You might make a mistake in one of the copies. etc.
  - Instead, you can write a function, and use it as many times as you want.
- Abstraction and modularity
  - The _user_ of the function doesn't always need to understand how the function works.
  - For example, we will learn about _modules_ and the `math` module. It contains the functions like logarithm. We don't need to know how to calculate the logarithm, we can just use the code someone else wrote and then shared it.
  - In team development, different programmers can work on different modules and build on top of each other's code.
