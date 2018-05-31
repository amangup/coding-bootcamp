# Modules

- Modules are a way to split large amounts of code into multiple files.
- It is a good practice to break large amounts of code into _logical modules_. Python language helps you in doing that by defining syntax to use code written in other files.

## Importing and using modules

Let's say there was some code which was reused multiple times in different parts of your project. As an example, we write some utility function for working with dictionaries. We call this file `dict_utils.py`

```python
sample_dict = {1:'a', 2:'b', 3:'c'}

def get_keys_sorted_by_value(adict):
    return sorted(adict, key=adict.get)
    
def get_sorted_values(adict):
    return sorted(adict.values())

def get_inverse_dict(adict):
    inverse = {}
    for key, value in adict.items():
        inverse[value] = key

    return inverse
    
def create_dict(keys, values):
    adict = {}
    for key, value in zip(keys, values):
        adict[key] = value
    return adict
```

Let's write another file (`dict_utils_test.py`) which contains this code:

```python
import dict_utils

print(dict_utils.sample_dict)
x = dict_utils.sample_dict
print(dict_utils.get_inverse_dict(x))
```

This outputs the following:

```
{1: 'a', 2: 'b', 3: 'c'}
{'a': 1, 'b': 2, 'c': 3}
```

There are two new syntax elements being used here:
1. We use the `import` keyword to refer to another module. This lets python _import_ the variables and functions defined inside that module
2. You use the `<module_name>.<symbol>` notation to access any variable, function (or class) in that module.

### Module level code

Sometimes, there is code at the _root_ level of a module, that is not inside functions. For example, let's add the following line at the end of dict_utils.py

```python
print ("This is the dict_utils module. Use it for all your dictionary needs.")
```

Let's say we run the `dict_utils_test.py` file. This is what we would see as the output:

```
This is the dict_utils module. Use it for all your dictionary needs.
{1: 'a', 2: 'b', 3: 'c'}
{'a': 1, 'b': 2, 'c': 3}
```

- As you can see, the print statement gets executed. 
- This happens because when python executes the `import dict_utils` statement, it runs all the code inside the module. 
- All the variables and functions are just definitions, and cause no impact unless you use them (e.g., we defined the `get_sorted_values` function but since we didn't use it, it sits there silently).
- Any code which is defined at the root level will get executed.

### Module name
- Python sets a variable called `__name__` which programmers can use to identify which module they are in.

For example, let's modify the print statement in dict_utils.py to this:

```python
print ("This is the module with name %s. Use it for all your dictionary needs" % __name__)
```

We get the folliwing output.

```
This is the module with name dict_utils. Use it for all your dictionary needs
```

- Thus, when we import the module, the variable `__name__` inside _that_ module is set to be equal to the name of that module. This can be useful (to name loggers, to identify the main module, etc.)

### The main module
- Whenever you run a python program, you are always running one specific python file. If you are using the command line, you would be using a command like `python3 my_program.py` to run your program.
- The `__name__` variable is set to `__main__` in that case (irrespective of the name of your file).
- This is useful if your program has code which other files can use, but you want it to do something on it's own as well.

As an example, let's modify the print statement in `dict_utils.py` one more time.

 ```python
if __name__ == '__main__':
    print ("Variable __name__ is %s" % __name__)
    print ("This is the dict_utils module. Use it for all your dictionary needs")
```
 
If we run our `dict_utils_test.py` file again, we get the following output: 
 
```
{1: 'a', 2: 'b', 3: 'c'}
{'a': 1, 'b': 2, 'c': 3}
```

- Note that we don't see the output the print statements. As we saw in the previous section,
when we import a module, it's `__name__` is set to the module name. Thus, the if statement evaluates to false and the print statements don't run.

What if ran the `dict_utils.py` itself? We get the following output:

```
Variable __name__ is __main__
This is the dict_utils module. Use it for all your dictionary needs
```

- We see that the variable `__name__` is set to `__main__`.
- Because of this, the if statement becomes true, and the print statements get executed.

### Standard practice for main
- Whenever you write any program, it is possible that someone might want to use that program as a module in the future.
- Thus, it is common practice to write your code so that _root level_ code is inside the if check which ascertains if the variable `__name__` is `__main__`.
- If you see any python program from an established programmer, this is how they write their _main_ file:


```python
def main():
    # Do your work here
    pass


if __name__ == '__main__':
    main()
```
   
## Modules in Python standard library
- Python has a very large number of modules built into its **standard library**.
- An even larger number of modules are available which written by other programmers and shared for you to use for free.

In the following sections, I am going to highlight a few popular built-in modules and show how to use _third party_ modules.

### datetime module

- The module datetime defines many types inside it, like `date`, `time`, `datetime`.

Here is a tiny sample of its capabilities.

```python
> import datetime

# In computer science, timestamp is defined as the number of seconds elapsed since
# the beginning of the day of January 1st, 1970. This is the standard value to use
# as time in programming.
> print(datetime.datetime.now().timestamp())
1527668953.615421

# Print current date. Python has a standard notation for representing time and date
> print(datetime.datetime.now().strftime('%Y-%m-%d'))
2018-05-30

# Print current date and time in New York City
> import pytz
> timezone = pytz.timezone('America/New_York')
> print(datetime.datetime.now(timezone).strftime('%Y-%m-%d, %H:%M:%S'))
2018-05-30, 04:38:43

# Convert current time to timestamp
> parsed_time = datetime.datetime.strptime("2018-05-30-4", "%Y-%m-%d-%H")
> print(parsed_time.timestamp())
1527652800.0
```    

- The full documentation is [available here](https://docs.python.org/3/library/datetime.html).

### math module
- This is another super useful module, defining a number of mathematical functions.

```python
# Get the gcd of two integers
> import math
> print(math.gcd(32, 48))
16

> print(math.floor(-3.45))
-4

> print(math.log2(65536))
16.0

> print(math.pi)
3.141592653589793
```

- The full documentation for the math module is [available here](https://docs.python.org/3/library/math.html).

### random module
- `random` module is useful in certain cases. For example, 
  - If we want to test a new UI, we may want to show the new UI only on a random selection of 1% users.
  - There are many algorithms (called **Randomized Algorithms**) which sometimes perform better than any non-randomized equivalent (Quick sort is a popular example).
  
Here is some sample usage:

```python
> import random
# For getting a random integer
> print(random.randint(5,10))
7
> print(random.randint(5,10))
9

# For getting a random float in the range [0.0, 1.0)
> print(random.random())
0.304776972595302

# Print True with 25% probability, False otherwise
# If you run this many times, you will see number of Trues and False
# according to the probability (more or less) 
> print(True if random.random() <= 0.25 else False)
False

# It even supports some distributions other than uniform 
> print (random.gauss(mu=0.5, sigma=0.25))
0.6755629832260551
```

### os module
- `os` module is used to execute code and perform actions that you would normally do in the command line, for example getting a list of files, getting the creation timestamp of a file, etc.
- Most real projects use this module for some use case.

Here is an example of using the `os` module's path submodule, and its function
`os.path.getctime()` to get the creation time of files in a directory.

```python
# Here is some code to list all files in descending order of their creation 
# timestamp
import glob  # This is a module frequently used if you are handling files. 
import os
dir_location = "/home/aman/aman_code/coding-bootcamp/*"
list_of_files = glob.glob(dir_location)
print(sorted(list_of_files, key=os.path.getctime, reverse=True))
```

Output is:
```
['/home/aman/aman_code/coding-bootcamp/lecture7', '/home/aman/aman_code/coding-bootcamp/lecture6', '/home/aman/aman_code/coding-bootcamp/lecture5', '/home/aman/aman_code/coding-bootcamp/README.md', '/home/aman/aman_code/coding-bootcamp/file~', '/home/aman/aman_code/coding-bootcamp/lecture2', '/home/aman/aman_code/coding-bootcamp/lecture4', '/home/aman/aman_code/coding-bootcamp/lecture3', '/home/aman/aman_code/coding-bootcamp/lecture1', '/home/aman/aman_code/coding-bootcamp/Syllabus for Python Coding Bootcamp.pdf']
```

### Using third party modules
- Third party modules are libraries written by community members, who (usually) share their module for free.
- They are not already part of your installation, but you can install them using the pip3 utility.

PyCharm is useful help you install modules. We have to structure our project in a certain way, and then PyCharm asks you by itself to install modules which are not already installed on your computer.

For a small project, here is a very simple project structure to have:
```
Readme.rst
requirements.txt
my_project/my_main.py
my_project/my_utils.py
...
```

Note the file `requirements.txt`. It's sole purpose is to list out all third party modules which are required for this project to run. Let's create a requirements.txt with only one third party module:

```
tinydb==3.9.0
```

This module uses a file to create a _tiny_ database of data. Let's create a project folder called `test_tinydb` and create a file called `tinydb_sample.py`, which contains:

```python
import os
import tinydb

db_filename = 'test_db.json'

# First let's delete the file we will use for db
if (os.path.exists(db_filename)):
    os.remove(db_filename)
    
db = tinydb.TinyDB(db_filename)
db.insert({'name': 'Luke', 'age': 19})
db.insert({'name': 'Anakin', 'age': 42})

Jedi = tinydb.Query()
print(db.search(Jedi.name == 'Luke'))
```

PyCharm should highlight that this module is not installed, asking you to install it. You can also install this from the command line using the following command:

```
pip3 install -r requirements.txt
```

Once the package is installed, the above program should work and print the record associated with Luke.
