# Object Oriented Programming

- A **class** provides the _means_ for bundling data and functionality together.
- An **object** represents an instance of that data, and the functionality is (usually) designed to act on the data - either to modify that data, to extract new information from that data, or both.
- The data is stored in variables that are attributes of the class. The functionality is implemented in methods (which are essentially functions, but inside a class).

Before we start looking at Python syntax for defining classes and creating objects, let's try to understand object using an analogy of a real life object. We will look at a watch, and how that fits into the structure described above.

## A watch as object

![A chronograph watch](https://raw.githubusercontent.com/amangup/coding-bootcamp/master/lecture8/watch_face.jpg)

- This is a watch which shows the time as hours, minutes, seconds, shows the date, and has a chronograph complication (i.e., it works as a stop watch). It has one crown (to set time and date), and two pusher buttons to operate the chronograph. There are additional sub-dials and hands on the dial to indicate the current reading of the chronograph.

### The class definition

- In case of the watch, the class definition is a design made by Omega where they intended to provide the functionality described above, and then they decided to call this model "Omega Speedmaster Dark Side of the Moon", which can be thought of as a name of the class.

### The object instance

- If someone has a personal watch, then that **object** becomes an _instance_ of this class.
- Every watch has a serial number, which can be thought as the name of the object instance.
- Since there probably thousands of real watches of this model which exist in reality, the number of objects we can create of a class are limited only by physical limitations (in computers, that is memory) and demand.

### The object has data

![A watch movement](https://raw.githubusercontent.com/amangup/coding-bootcamp/master/lecture8/watch_movement.jpg)

- The current positioning of the gears in the movement encodes the data stored in one physical watch, which is the hour, minute, second and the date at any given moment. The chronograph indications are also data values stored in this object. All of these values can be thought of as variables containing data.
- Any two watches will likely have different values for these _variables_.

### The object provides functionality

- **Modifying the data**: One can use the crown of the watch to modify the time and date. The push buttons allow us to operate the chronograph mechanism in the watch.
- **Fetching the data**: The dial and watch hands can be thought as functionality that allows us to read the data stored in the variables.
- **In built functionality**: It keeps on updating the time using its mechanism which measures how much time has elapsed since you last set the watch.

## What is Object Oriented Programming (OOP)?

- Continuing the analogy, if we assume living beings are also objects, most of our life is lived as interaction with objects.
- In programming, this equates to writing programs such that every piece of data is stored in an object, and all functionality must be executed via and (implemented as) methods on objects.
- Python is not a _pure_ OOP language - every piece of data _is_ stored in an object (every built-in type is a class), but functionality can be implemented outside methods in classes. For example, we can write functions which are not associated with any class (Java doesn't allow this) and even write _procedural code_ outside any function (most languages don't allow this. This is a feature usually associated with _scripting_ languages).

Below, I show an example of how we can do exactly the same thing in an OOP way and in a Non OOP way.

**Non-OOP way:**

```python
def add_score(name, score, leaderboard):
    leaderboard.append((name, score))

def get_top_scores(n, leaderboard):
    return sorted(leaderboard, key=lambda x: x[1], reverse=True)[:n]

stranger_things = []
add_score("MADMAX", 751300, stranger_things)
add_score("DUSTIN", 650990, stranger_things)
add_score("MADMAX", 641183, stranger_things)
add_score("MADMAX", 620784, stranger_things)
add_score("DUSTIN", 552415, stranger_things)

# Get the top 3 scores
print(get_top_scores(3, stranger_things))
```

**OOP way:**

In this example, ignore the syntax for defining a class for the moment, and remember that we have using methods on objects to act on them (like `sort()` on `list` class).
 
```python
class Leaderboard:
    def __init__(self):
        self.leaderboard = []

    def add_score(self, name, score):
        self.leaderboard.append((name, score))

    def get_top_scores(self, n):
        self.leaderboard.sort(key=lambda x: x[1], reverse=True)
        return self.leaderboard[:n]

ready_player_one = Leaderboard()
ready_player_one.add_score("Daito", 107000)
ready_player_one.add_score("Parzival", 110000)
ready_player_one.add_score("Aech", 108000)
ready_player_one.add_score("Art3mis", 109000)
ready_player_one.add_score("Shoto", 106000)

# Get the top 3 scores
print(ready_player_one.get_top_scores(3))
```
## Defining a class
- Python has a reserved keyword called `class` which is used to define a class.
- Inside a class, you can define methods using practically the same syntax as a function. The differences are:
  - These methods must be inside the class block.
  - Each method must have `self` as the first argument. An explanation for `self` is coming up soon.
- Each data attribute must referred to using `self.<variable_name>` notation.
- The naming notation for class names is to use `CamelCase` names, where the first word is also capitalized. (note how `CamelCase` kind of looks like it has a hump in in the middle :-))
- The notation for naming of data attributes and methods is the same as for variables and functions, which we are familiar with.
  - Usually, users of a class don't directly access the data attributes of a class. They interact with the object by using only the methods. To emphasize this, we may prefix data attributes with an underscore. We will follow this notation.

Since we started our lecture with how the real life object watch is similar to the idea of objects in programming, let's define a class that imitates the functionality of a real life object. To keep it simple, we will only implement the time functionality, and not the date and chronograph functions.

```python
import datetime

class Watch:   
    def set_time(self, hour, minute, secs):
        self._time = datetime.datetime(1, 1, 1, hour, minute, secs)
        self._start_timestamp = datetime.datetime.now().timestamp()
                
    def get_time(self):
        current_timestamp = datetime.datetime.now().timestamp()        
        time_now = self._time + datetime.timedelta(seconds=current_timestamp - 
            self._start_timestamp)
        return (time_now.hour, time_now.minute, time_now.second)        
```

To understand this code, we must first understand what `self` means:

- When you are writing functionality inside the methods of a class, there is an assumption that this code can only get executed _on_ an object of this class.
- To keyword `self` literally refers to that object. It is as a variable which is an object of the class we are defining (in this case, the class `Watch`).
- We need the object reference because the data attributes that we are using (like `time` or `start_timestamp`) are unique to an object, and the method must do transformations on the data of a specific object. If we have one `time` value for all objects of this class, that would be wrong.
- It's like how every kid refers to their mother as _Mom_.

Given this understanding, let's see how the class works:
- The method `set_time()` takes hours, minute, secs and sets some variables accordingly. We need to store the values of the hour, minute, secs (for which we create a `datetime` object). In addition we set the variable `self._start_timestamp` which will be used to measure how much time has elapsed since `set_time()` was called.
- The method `get_time()` needs to find how much time has passed since `set_time()` was called, and then add that time to the value of hour, minute, secs which was set. It returns the newly computed hour, minute, sec that represents the current time.
- The variables that are prefixed with `self.` are not attributes of the class. These variables' scope is the method in which they are defined.

Here is an example which uses this class


```Python
import time

my_watch = Watch()
my_watch.set_time(3, 30, 0)
print ("Before time:", my_watch.get_time())
time.sleep(15)
print ("After time:", my_watch.get_time())
```

Output is:

```
Before time: (3, 30, 0)
After time: (3, 30, 15)
```

- Note how we create an object of the class: We use the syntax `ClassName()`.
- In the second line, we set time to 3:30:00
- We print the time (which outputs 3:30:00), wait for 15 seconds, and print the time again (which then outputs 3:30:45)

## Init method

- Most classes have a special method called `__init__()` which is automatically run when someone creates an object of this class. This method is called a **constructor**, and is used to do any mandatory initialization for any object.

Let's add that to class:

```python
class Watch:   
    def __init__(self):
        # We set time to 10:10, following the trend of analog watches being
        # usually set to 10:10 when photographed.
        self.set_time(10, 10, 0)
        
    # The two other methods are same as before        
```

```Python
my_watch = Watch()
print ("Time:", my_watch.get_time())
```

Output is:
```
Time: (10, 10, 0)
```

- The `__init__()` method can also take more arguments. In the example below, me modify the `Watch` class so that the user can specify if they want to denote hours in 12-hour format or 24-hour format.


```python
import datetime

class Watch:   
    def __init__(self, format_12_hour=False):
        self._format_12_hour = format_12_hour
        self.set_time(10, 10, 0)
        
    def set_time(self, hour, minute, secs):
        hour = self._convert_hour_format_(hour)
        self._time = datetime.datetime(1, 1, 1, hour, minute, secs)
        self._start_timestamp = datetime.datetime.now().timestamp()
                
    def get_time(self):
        current_timestamp = datetime.datetime.now().timestamp()        
        time_now = self._time + datetime.timedelta(seconds=current_timestamp - 
            self._start_timestamp)
        return (self._convert_hour_format_(time_now.hour), time_now.minute,
            time_now.second)
        
    def _convert_hour_format_(self, hour):
        if self._format_12_hour and hour >= 12:
            return hour - 12
        else:
            return hour
```

We can these use this class as follows:

```Python
my_watch = Watch(True)
my_watch.set_time(20, 30, 00)
print ("Time:", my_watch.get_time())
```

Output is:
```
Time: (8, 30, 0)
```

- Note that we started the name of method `_convert_hour_format_()` with an underscore because it's an internal method and not expected to be used by users of the class `Watch`.

**Exercise:** Update the `Watch` class to contain the method `advance_hour()` which moves the time ahead by one hour.

## Inheritance
- Inheritance is the main feature of OOP, and it makes it much more useful. Without this feature, OOP has little value.
- It basically means that you can create new classes which are **child** classes of some class. That parent class is usually called **base class**.
- When you inherit from a base class, all the data attributes and method automatically become a part of your class.
- You can define new data attributes and methods, and use the data attributes and methods of the base class in your new methods.
- This allows anyone to extend the functionality of a class. This concept can also be used to define an application interface (API) which subclasses can implement (this is illustrated in assignments).
- If some code is written to expect an object of the base class, you can instead pass an object of the child class and that code will continue to work (unless you override a base class method _wrongly_, discussed below).

### Inheriting from a base class
- In this section, we will look at the syntax for inheritance. We will implement the a function called GMT. Essentially, this allows the watch wearer to track the time in second time zone. The minute and second values remain the same.

```python
class GmtWatch(Watch):
    def __init__(self, format_12_hour=False):
        Watch.__init__(self, format_12_hour)
        self._gmt_hour_offset = 0

    def set_gmt_hour_offset(self, offset):
        if self._format_12_hour:
            self._gmt_hour_offset = offset % 12
        else:
            self._gmt_hour_offset = offset % 24
            
    def get_gmt_time(self):
        hour, minute, secs = self.get_time()
        hour = (hour + self._gmt_hour_offset) % 24
        return (self._convert_hour_format_(hour), minute, secs)
```

A few things to note
- When writing the class name, we specify the name of the base class in parenthesis
- The first method we write is a method which already exists in the base class `Watch` - the `__init__()` method.
  - This is called **method overriding**.
  - In this case, we wan't to do the initialization which the base class does, and also do some more initialization which we need for the GMT function.
  - The syntax to call a method of the base class is: `BaseClassName.method_name(self, arguments)`
- We have defined new methods `set_gmt_hour_offset()` and `get_gmt_time()` in the same way as any method for a class.
- In both methods, we are accessing data attributes and methods of the base class.

Let's see what happens when we use this class:

```python
gmt_watch = GmtWatch(True)
gmt_watch.set_time(20, 30, 00)
print ("Time:", gmt_watch.get_time())
print ("GmtTime:", gmt_watch.get_gmt_time())
# If time is in PDT, this would give us EDT
gmt_watch.set_gmt_hour_offset(3)
print ("GmtTime after offset:", gmt_watch.get_gmt_time())
```

Output is:
```
Time: (8, 30, 0)
GmtTime: (8, 30, 0)
GmtTime after offset: (11, 30, 0)
```

### On overriding methods
- When you create a child class using a base class, frequently you would need to override a method of the base class. When you do that it's important to not break the functionality of the base class method semantically.
- In most cases when you override a method, the best practice is to call the base class' method as the first line in your overriding method definition (as we did in the `GmtWatch` class' `__init__()` method).
  - If we didn't do that, the `GmtWatch` wouldn't function as a simple `Watch` (in fact, since GMT function uses the basic watch functionality, nothing would work as expected). 

**Exercise:** Write a class called `Chronograph` which extends the `Watch` class and implements the chronograph functionality. A chronograph can be started, paused, and reset back to zero. At any time, the current value of chronograph indications can also be read.


## More features in class
- Many times, there is use for variables in a class whose value is common for all objects of the class. These are called **class variables**.
- To create class variables, you can just create a variable inside the class definition, but outside any method definition.

An example:

```python3
class Dog:
    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
```

Example usage

```
> d = Dog('Fido')
> e = Dog('Buddy')
> print(d.kind)                  # shared by all dogs
'canine'
> print(e.kind)                  # shared by all dogs
'canine'
> print(d.name)                  # unique to d
'Fido'
> print(e.name)                  # unique to e
'Buddy'
```