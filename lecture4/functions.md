# Functions
Functions is a fundamental mechanism designed to write reusable code.

## What is a function?
![Function diagram](https://raw.githubusercontent.com/amangup/coding-bootcamp/master/lecture4/function.png)

- Function is a piece of program that encodes a specific task. You can name it, and run that program again and again by referring to its name.
- You can provide function with input  (called _arguments_ or _parameters_), and you can also make the function _return_ an output.
- If a function doesn't return a value, it's called a _procedure_.
  - This is because it is not a function in the mathematical sense.
  - A procedure exists only for its _side effects_, i.e., it interacts with an I/O device, change the value of an input variable, etc.  

## Basic Function Syntax
```python
# This is a function which finds a statistic with two numbers
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
2. The name of the function is written after that. It's name must follow the same naming rules as a variable. The convention is to use lowercase letters with underscores for `function_name`. If the function is _private_, and you don't want anyone to use it directly, then you should use a variable name starting with underscore, like `_private_do_not_use_`.
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

## Call by Object Reference
- When you call a function, the argument variable _inside the function_ refers to the same memory location as the memory location of the variable you used when calling the function.
- The description of memory location of the object is called the _Object Reference_.
- This mechanism of passing values to function is named **Call by Object Reference**, because the variables inside the functions are created so that they refer to the same memory location as the calling variables.

```python
def add(a, b):
  print ("Address of argument: %s" % id(a))
  r = a + b
  print ("Address of return value: %s" % id(r))
  return r
  
x = 3
y = 6
print("Address of argument value before passing it to function: %s" % id(x))
z = add(x, y)
print("Address of return value after executing the function: %s" % id(z))

Output:
Address of argument value before passing it to function: 140719640004416
Address of argument: 140719640004416
Address of return value: 140719640004608
Address of return value after executing the function: 140719640004608
```

What does this mean for a programmer?
- If the type of argument variable is _mutable_, and if you _mutate_ the variable inside the function, its value changes for the caller of the function as well.
- This is called a side effect, and it's usually **not a recommended practice** to mutate argument variables inside a function. The caller has to create _defensive copies_ before calling a function which mutates its argument variables. 

Here is an example which uses the `list` built-in type. We will talk more about lists later, but for now you can understand it as a type which stores a sequence of values. Unlike the types we have discussed till now (like `int` or `str`), the `list` type is **mutable**.

```python
def test_mutation(alist):
  alist += [10]

alist = [1, 2, 3]
print (alist)
test_mutation(alist)
print (alist)

Output:
[1, 2, 3]
[1, 2, 3, 10]
```

## Function scope
- Variables inside the function, including argument variables, are not visible to the code outside the function. These variables are said to be defined in the **scope** of the function.
- The function can read variables defined in a _larger_ scope, but cannot write to them.

Here is an example:
```python
def function(x):
  summation = x + y
  print ("In function: %s" % (summation))

y = 5
function(2)
print (summation)

Output:
In function: 7
Traceback (most recent call last):
  File "python", line 14, in <module>
NameError: name 'summation' is not defined
```

You can see that the variable `y` is visible inside the function because any variable defined outside any function is in the larger scope. But, the variable `summation`, which is defined inside the function is not visible to the _outside_ scope.

It follows that a variable defined in one function will not be visible in another function. Here is an example that proves that.

```python
def function(x):
  summation = x + y
  print ("In function: %s" % (summation))

def function_error():
  print ("In function_error: %s" % (summation))

y = 5
function(2)
function_error()

Output:
In function: 7
Traceback (most recent call last):
  File "python", line 10, in <module>
  File "python", line 6, in function_error
NameError: name 'summation' is not defined
```

## None type
- In Python, there is a built-in type called `NoneType`, which can only have one value: `None`.
- The word `None` is a reserved keyword in the language and can't be used except as the constant literal for `NoneType`.
- Python automatically generates `None` values when you assign to a variable a function's return value, for a function which doesn't return anything.

Here is an example:
```python
def print_with_greeting(message):
    print ("Hello! Here is your message: %s " % message)

output = print_with_greeting("What are you going to give me in return?")
print (output)

Output:
Hello! Here is your message: What are you going to give me in return? 
None 
```

If you explicitly `return` from a function without a value, even then the return value is `None`. Here is an example showing that. 

```python
def is_double_digit(x):
  if x < 9 or x > 99:
    return
  return True

output = is_double_digit(25)
print (output)

output = is_double_digit(7)
print (output)

Output:
True
None
```

We discussed in the previous lecture how some non-boolean values evaluate to `True` or `False` in a boolean expression. In case of `None`, it evaluates to `False`.

```python
def is_double_digit(x):
  if x < 9 or x > 99:
    return
  return True

age = 3
if not is_double_digit(age):
    print ("Too young or too old.")      
```

One more thing to note is that sometimes a function may return the value `0` in some cases, and the value `None` in other cases. Automatic conversion of values to boolean can lead to wrong code, as shown in the example below:

```python
def safe_divide(numerator, denominator):
    if denominator:
        return (numerator / denominator)

result = safe_divide(5, 0)

if result:
    print ("The output is: %s" % result)
else:
    print ("Invalid arguments to division")

result = safe_divide(0, 5)

if result:
    print ("The output is: %s" % result)
else:
    print ("Invalid arguments to division")
    
Output:
Invalid arguments to division
Invalid arguments to division
```

In the second call to `safe_divide()` above, the arguments and the result were valid. But because both `0` and `None` evaluate to `False`, we couldn't distinguish between the two cases.  

## Default Argument values
- In Python, many times you want to have optional parameters in functions. The caller of the function may not need to specify all the arguments, and the function can use default values for some of those parameters.
- Python allows you to specify a default value to any parameter to the function. 
- This helps to avoid writing multiple functions which have similar behavior.

Here is an example:

```python
def linear_function(x, a = 0, b = 0):
    # calculate the linear function ax + b
    return a * x + b

print (linear_function(5, 2, 1)) # should give us 11
print (linear_function(5, 2)) # should give us 10
print (linear_function()) # should raise an error

Output:
11
10
Traceback (most recent call last):
  File "python", line 7, in <module>
TypeError: linear_function() missing 1 required positional argument: 'x'
``` 

## Keyword arguments
- In some use cases, your python function may have many arguments. In that case, it becomes very hard for users to make sure they provide arguments in the correct order.

As an example of such a function, here is the declaration of one which I recently used. This has eight parameters!
```python
DataFrame.from_csv(path, header=0, sep=', ', index_col=0, parse_dates=True, encoding=None, tupleize_cols=None, infer_datetime_format=False)
```

In the function declared above, if you only wanted to pass the parameters `path`, `sep` and `infer_datetime_format`, then you would have to provide all the eight arguments to the function. Fortunately, there is a better way, as shown below:

```python
data = DataFrame.from_csv(infer_datetime_format=True, path='/data/census_report.csv', sep=';', )
```

You can use the name of the parameter to specify arguments. This method of specifying arguments is called **keyword arguments**.
- You don't have to provide all the arguments, only the ones you care about (assuming the writer of the function has default values for the ones you don't provide).
- You don't have to worry about order in which you provide arguments.
- The way to call a function where you don't use parameter names is called **positional arguments**.
- It is highly recommended that if you use keyword arguments for one argument to the function, you use it for every argument. Using both keyword arguments and positional arguments in one function call becomes very messy.

**The combination of default argument values and keyword arguments is used very often in Python (especially in larger projects). It is quite important to be aware of these features.**

## Docstrings
- Docstrings are a way to document the working or the purpose of a function, from the perspective of the user of that function.
  - Later, we will see that docstrings are used to document modules and classes as well.
- There are ways to automatically create documentation which reads these docstrings to create documentation.

Let's take the example of the `find_stat()` function we defined in the beginning and see how docstrings could be written for that. This is the content of a file using which I generated documentation automatically. 

```python
"""This module contains functions to calculate statistics on data"""


def find_stat(x, y, stat_type):
    """Finds a statistic value for the two values given as input.

    Args:
        - x: first value  
        - y: second value  
        - stat_type: One of "average", "maximum", or "minimum"  

    Returns:
          - the outcome of running the chosen statistic on x and y
    """
    if stat_type == 'average':
        return (x + y) / 2.0
    elif stat_type == 'maximum':
        return max(x, y)
    elif stat_type == 'minimum':
        return min(x, y)

```

Using [sphinx](http://www.sphinx-doc.org/en/stable/) as an automatic documentation tool, I created documentation automatically, which looks like this:

![Sphinx doc screenshot](https://raw.githubusercontent.com/amangup/coding-bootcamp/master/lecture4/sphinx_doc.png)

It is recommended that you write docstrings for every function (except any _private_ functions).

# Built-in functions
- Now that we have learned what functions are, how to use them and how to write them, let's see what kind of functions are built into python.
- [The complete list of built-in functions can be seen here.](https://docs.python.org/3/library/functions.html)
- We have already used a number of functions previously, like:
  - `print()` - to output to screen
  - `input()` - to take input from user
  - `int()`, `float()` or `str()` - to convert between different types.

The code listing shows a few more common ones and how to use them:

```python
# find minimum
>>> min(3, 5, 8)
3

# find maximum
>>> max(2, 6, 99)
99

# get the absolute value. 
# Absolute value of a positive number is itself.
# Absolute value of a negative number is the same number without the negative sign. 
>>> abs(-2.4)
2.4
>>> abs(2.4)
2.4

# eval function calculates an expression using variables which are defined in its scope
# It's useful if you are generating the expression dynamically in your code.
>>> x = 3
>>> y = 2
>>> eval('x * y + 1')
7

# get the length of a string (and for a list and many other types) 
>>> name = 'Aman Gupta'
>>> len(name)
10

# check if a variable is of given type. It's useful if you are defining a function
# to check if two values are equal.
>>> isinstance(name, str)
True
>>> isinstance(name, int)
False

# round a float number to its nearest integer
>>> round(2.45)
2
>>> round(2.99)
3
>>> round(-3.1)
-3

# convert a base 10 number to a binary number
>>> bin(9)
'0b1001'

```
  
# Practice exercises
- Extend the `find_stat()` function described above to take upto three numbers instead of just two, where the third number is optional for the user. If the third number is not provided, then output stats only using the two numbers which are provided.
- Write a function which returns `True` is a number is prime, `False` otherwise.

# Recursion (Advanced topic)
- Recursion is a very useful topic to understand, as it is used in many _algorithms_. It's a powerful programming technique which every good programmer will need at some point or another.
- Recursion means that you call a function from the code within the function itself.

It's best learnt by example. Let's illustrate recursion by solving the following problem:
- **Factorial(n)** is a mathematical function which is commonly used in branches of Math like Combinatorics and Probability.
- It is defined as: Factorial(n) = 1 x 2 x 3 x ... x n. Factorial(0) is defined to be 1.
- Write a program to compute factorial, given an non-negative number as input.

Let's try to solve this using two approaches. First, without using recursion
```python
def factorial_iterative(n):
    if n == 0:
        return 1
        
    i = 1
    factorial = 1
    while i <= n:
        factorial = factorial * i
        i += 1
    return factorial
```

This is a straightforward approach - the code loops from 1 to n, and multiplies each of the numbers in the process.

Let's see how we can do this using recursion:

```python
def factorial(n):
    # Termination condition
    if n == 0:
        return 1
    else:
        # Recursion step
        return n * factorial(n - 1)
```

This function solves the problem correctly. Let's analyze this recursive function in more detail:

- Firstly, we need to understand that the problem definition is such that we can solve it by breaking into smaller subproblems.
  - In this case, we are taking advantage of the fact that this equation is mathematically true: `Factorial(n) = Factorial(n - 1) * n`.
  - This shows that if you want to calculate `Factorial(n)`, you can calculate `Factorial(n - 1)`, i.e., for a smaller number, and multiply that by n.
- In the last line of the function, we are making the _recursive call_.
  - The statement says that it should return an expression. But, that expression includes a function call, so Python must first evaluate that function.
  - That function call is to the same function from where we are calling, but with a _different_ argument (this is very important, otherwise we will keep recursing forever). The different argument describes the _sub-problem_ that we need to solve first, to get to the main result.
- In the first line of the function, we hardcode the answer for the smallest use case.
  - This is called the **termination condition**. **Every recursive function must have a termination condition**, because otherwise we will keep recursing forever and eventually Python will get fed up and raise an error.

Before we look at another example, it is really important that you understand every aspect of whatever has been discussed above. As you will see in assignments, we will use this approach to solve pretty challenging problems and it's quite important to understand this well.

Now let's look at another example. The problem statement is:
- Input a word as input, and print all possible rearragements of the letters of that word. This is called the problem of printing all **Permutations**.

Again, before we go through the recursive solution, let's look at an iterative approach. To do that, let's assume that the word is always a 3 letter word.

```python
def print_permutations(word):
    i = 0
    while i < 3:
        i += 1
        j = 0
        while j < 3:
            j += 1
            if j == i:
                continue
            k = 0
            while k < 3:
                k += 1
                if k == j or k == i:
                    continue
                print (word[i - 1] + word[j - 1] + word[k - 1])

print_permutations('abc')

Output:
abc
acb
bac
bca
cab
cba            
```

This solution needs three nested loops, each iterating over all the characters of the word. If the word was a 4 letter word, we would need four nested loops. It's clear that this is a very cumbersome approach.

Here is the recursive solution for this:

```python
def print_permutations(word, output = ''):
    # Termination condition
    if len(word) == 0:
        print (output)
    else:
        i = 0
        while i < len(word):
            # Recursion step
            word_without_ith_char = word[:i] + word[i+1:] 
            print_permutations(word_without_ith_char, output + word[i])
            i += 1
            
print_permutations('abcd')            
```

This program is much shorter, easier to read, and works with words of any size! Let's see how this works:
- First, let's look at how are we breaking the problem into subproblems:
  - For any word, a permutation can be created by: **choosing one character from the word + a permutation of the remaining word with that character removed**.
- In the recursion step of the program:
  - We are extracting the ith character out of the word and using that in our permuted output.
  - Then we are solving the sub problem of finding all permutations of that smaller word.
- In the termination step of the program:
  - If the word is of length 0, then we are in the smallest possible subproblem. In this case, we just print our output.

For practice exercises on recursion: Just try to solve these same problems again, without looking at the solutions.