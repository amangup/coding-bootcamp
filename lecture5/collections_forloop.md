# Collection types and for loop

We are going to learn about types which can be described as a collection of values. Then we will learn how to iterate over all values of that collection using the `for` loop statement.

## List
- A sequence of values.
- These values can be of _any type_ (`int`, `str`, `list`, `tuple`, `dict`, custom types, etc.)
- The `list` type is similar to the `str` type, and most of the things we learned for strings apply for lists.

### Creating lists
- A list can be defined by using the square brackets and specifying a sequence of elements, as follows.

```python
# You can leave a comma at the end
weekdays = ["Sun's day", "Mani's day", "Tyr's day", "Odin's day", "Thor's day",
            "Frigg's day", "Saturn's day",]
print(type(weekdays))
<class 'list'>
```

- We can use the built-in function `range()` to create a list.

```python
# list() function can convert some types to a list
nums = list(range(10))
print (nums)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```python
# Left argument is included, right argument is excluded
nums = list(range(-7, 5))
print (nums)
[-7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
```

- If you want to create a list of size n, but with the same element, you can use the `*` (asterisk) operator

```python
batman = ['Na'] * 10
print (batman)
['Na', 'Na', 'Na', 'Na', 'Na', 'Na', 'Na', 'Na', 'Na', 'Na']
```

- List can contain items of different types.
- Most other languages _do not_ support this.

```python
mixed = [1, 'b', ['another', 'list']]
print (len(mixed))
3
```

### Reading elements from list

#### The basic case: getting one item from a list.
- This is called indexing.
- The return type is not a list, but the type of the item inside the list

```python
# lists are 0-indexed
third_weekday = weekdays[2]
print(type(third_weekday))
<class 'str'>
```

```python
# lists can also take negative numbers as index.
# The last item is indexed at -1, second last at -2, and so on.
second_last_weekday = weekdays[-2]
print (second_last_weekday)
Frigg's day
```

- If you use an index which is too large (or too small, for negative indices), Python raises an error.

```python
print (weekdays[7])
print (weekdays[-8])

# Both cause an error similar to the one below:
Traceback (most recent call last):
  File "python", line 5, in <module>
IndexError: list index out of range
```

- Here is a visual guide to remember how positive indices map to negative indices.

```
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```


#### Getting multi-item sublists through slicing
- Slices lets you get a part of the list.
- The slicing notation is the same for lists and strings.
- By giving start and end indices, you can get all items in between
- The syntax for getting a slice is `[start_index_included: end_index_excluded]`.
- Whenever you slice a list, you get a _new_ list - the original remains totally intact.

```python
# Getting the five work days in the week. Note that:
# the start index is 1, so this slice will not include Sunday, which is 
#   the 0th element.
# the end index is 6, but since it is exluded, it will include days upto 
#   Friday, which is the 5th element.
work_week = weekdays[1:6]
print (work_week)
["Mani's day", "Tyr's day", "Odin's day", "Thor's day", "Frigg's day"]
```

- We can also use negative indices to specify our slice

```python
work_week = weekdays[1:-1]
print (work_week)
["Mani's day", "Tyr's day", "Odin's day", "Thor's day", "Frigg's day"]
```

- If you use indices which are outside the range, Python doesn't raise an error! It includes everything possible in the output, and ignores indices
outside the range.

```python
print (weekdays[1:9])
["Mani's day", "Tyr's day", "Odin's day", "Thor's day", "Frigg's day", "Saturn's day"]
```
```python
print (weekdays[-100:3])
["Sun's day", "Mani's day", "Tyr's day"]
```

- If the start index >= end index (start index points point to an item which is the same or to the right of the item pointed to by the ending index), you get an empty list.
- One way to remember that is by noting that the length of the output list is `end_index - start_index` (as long as both indices are positive and in the range of list). If this number is 0 or negative, then output will be an empty list.

```python
print (weekdays[3:2])
[]
```
```python
# Both 0 and -7 point to the same item in the list
print (weekdays[0:-7])
[]
```

You can leave out one of the start or the end index.
- If you leave out the start index, it will automatically be assumed to be 0
- If you leave out the end index, it will automatically be assume to be the length of list.

```python
first_five_days = weekdays[:5]
print (first_five_days)
["Sun's day", "Mani's day", "Tyr's day", "Odin's day", "Thor's day"]
```

```python
last_two_days = weekdays[-2:]
print (last_two_days)
["Frigg's day", "Saturn's day"]
```

- It is recommended that if you can leave out one of the indices, you do so, as it reduces visual noise while reading the code.

- Understanding this, and the fact that a slice always creates a new list, we find an easy way to create a copy of the list:

```python
weekdays_copy = weekdays[:]
```

#### Stride
The final feature of slicing that we will discuss is called **stride**.

- The notation of slicing allows for a third input. Thus, the notation becomes `[start:end:stride]`.
- The stride parameter allows us to choose an element from the list after a given interval, as described by the stride value.

e.g.

```python
# This will give us every other parameter
odd_weekdays = weekdays[::2]
print (odd_weekdays)
["Sun's day", "Tyr's day", "Thor's day", "Saturn's day"]
```

- As with index parameters, the stride parameter also accepts negative values. In this case, Python starts from the back of the list, and picks up elements as it goes towards the start of the list.

```python
reverse_odd_weekdays = weekdays[::-2]
print (reverse_odd_weekdays)
["Saturn's day", "Thor's day", "Tyr's day", "Sun's day"]
```

- This gives us a convenient way to reverse any list (or string):

```python
reverse_weekdays = weekdays[::-1]
print (reverse_weekdays)
["Saturn's day", "Frigg's day", "Thor's day", "Odin's day", "Tyr's day", "Mani's day", "Sun's day"]
```

- You can specify the start and end parameters as well along with stride

```python
even_weekdays = weekdays[1::2]
print (even_weekdays)
["Mani's day", "Odin's day", "Frigg's day"]
```

When you use a negative value for the stride parameter, then 
- the start index must point to the "rightmost" element that should be picked (and that will picked first), and 
- end specifies the left most element in the list that _could_ be picked up.

```python
reverse_even_weekdays = weekdays[-2::-2]
print (reverse_even_weekdays)
["Frigg's day", "Odin's day", "Mani's day"]
```

- In practice it is hard to understand the slice notation if you specify all three parameters, and thus it is not recommended that you use it. In the case you need that functionality, you should slice twice - once with start and end parameters, and then again with the stride parameter.

### Aside: Methods in a class
In Python, every **type** (like `int`, `float`, `str`) is implemented as a **class**. A value of these types is an **object** of that class. Most classes define **methods** that usually operate on the data in the object.

The notation looks like this: `obj` is an object. To call a method, we use the dot syntax.

```python
obj.method_name()
```

Some examples of methods on primitive types:

```python
x = 2.0
print (type(x))
# is_integer() is a method in the float class
print (x.is_integer())
<class 'float'>
True
```

```python
name = "Merlin"
# isupper() and upper() are methods in the str class 
print (name.isupper())
print (name.upper())
False
MERLIN
```

There are many more methods you can use in these classes (especially, [in the string class](https://docs.python.org/3/library/stdtypes.html#string-methods)) which are useful. In the next section, we will look at the most commonly used methods in the list class.

Later in this course, we will develop a better understanding of the concepts of classes, objects and methods as we will learn to create our own classes.


### Modifying a list

- List is a **mutable** type. That means that when you modify the list,
  the same list object is changed, and a new one is not created.
- List class defines many methods. The complete list is [available here](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists).

- We are going to illustrate the most commonly used ones:

```python
shopping_list = ['milk', 'strawberries', 'tomatoes']
print (len(shopping_list))
3

# We use the append method to add a new element
shopping_list.append('chips')
print(shopping_list)
['milk', 'strawberries', 'tomatoes', 'chips']

# We can extend the list by adding items from another list
shopping_list.extend(['butter', 'oil'])
print(shopping_list)
['milk', 'strawberries', 'tomatoes', 'chips', 'butter', 'oil']

# The last statement is identical to the statement using the + operator
shopping_list += ['butter', 'oil']
print(shopping_list)
['milk', 'strawberries', 'tomatoes', 'chips', 'butter', 'oil']

# Items in the list are ordered. This means that sometimes we may
# want to insert an element somewhere in between.
shopping_list.insert(1, 'coconut water')
print(shopping_list)
['milk', 'coconut water', 'strawberries', 'tomatoes', 'chips', 'butter', 'oil']

# We can remove a specific item in the list
shopping_list.remove('butter')
print(shopping_list)
['milk', 'coconut water', 'strawberries', 'tomatoes', 'chips', 'oil']

# What happens if we try to remove an item not in the list?
shopping_list.remove('beer')
Traceback (most recent call last):
  File "main.py", line 28, in <module>
    shopping_list.remove('beer')
ValueError: list.remove(x): x not in list

# Thus, if we are using the remove method, we may want to check
# if an item is in the list before that.
if 'beer' in shopping_list:
    shopping_list.remove('beer')

# Another way to remove an item is to say that you don't need
# the item at the ith position.
# pop() method also returns the value that was removed
removed_item = shopping_list.pop(2)
print (removed_item)
strawberries

print (shopping_list)
['milk', 'coconut water', 'tomatoes', 'chips', 'oil']
```

#### Assignment to list slices
- Lists can also be modified by assigning a new list to an index or slice

```python
# Change the 2nd element
shopping_list[1] = 'beer'
print (shopping_list)
['milk', 'beer', 'tomatoes', 'chips', 'oil']

# Replace a slice
# Note that 3 items are replaced by 2 items.
shopping_list[2:] = ['apple juice', 'iced coffee']
print (shopping_list)
['milk', 'beer', 'apple juice', 'iced coffee']

# Delete some items
shopping_list[:2] = []
print (shopping_list)
['apple juice', 'iced coffee']

# Clear the whole list
shopping_list[:] = []
print (len(shopping_list))
0
```

## Tuples
- Tuples are used to store sequences of items like lists
- To create a tuple, we use parenthesis

```python
biodata = ("Luke Skywalker", "Male", 19, "force sensitive",)
print (biodata[2])
19
```

```python
# it can can be converted from a list
numbers = tuple([1, 2, 3])
print (numbers)
print (type(numbers))
(1, 2, 3)
<class 'tuple'>

# You can use the list() method to convert it back to a list
numbers_list = list(numbers)
print (numbers_list)
print (type(numbers_list))
[1, 2, 3]
<class 'list'>
```

- Tuples are useful because **they are immutable** (as we will see in dictionaries, dictionary keys need to be immutable).

```python
biodata[1] = "Female"
Traceback (most recent call last):
  File "main.py", line 12, in <module>
    biodata[1] = "Female"
TypeError: 'tuple' object does not support item assignment
```

- Tuple values can be _unpacked_

```python
name, gender, age, force_sensitivity = biodata
print (name)
Luke Skywalker
```

## The for loop
- Now that we understand sequence types, we can learn about the `for` statement.
- The `for` statement is a looping mechanism, like the `while` statement, but it is much more convenient to use in practice.
- Instead of looping until a condition becomes false, the `for` loop iterates over a sequence. It automatically identifies when the code should exit the loop, and as a programmer you don't have to worry about incrementing the index.
- The syntax is shown in the example below. Note that the use of colon and indented block is done in the same way as in the `while` statement.

Here are some examples:

```python
# print numbers from 0 to 9
# Strictly speaking, range() doesn't return a list
# But, it is something called iterable, which is acceptable in the for statement
for i in range(10):
    print (i)
```

```python
# iterate over the shopping list
shopping_list = ['milk', 'strawberries', 'tomatoes']
for item in shopping_list:
    print (item)
```
- Let's look at an example where we create a bill of items.

```python
# Let's include the number and cost of items in the shopping list. 
shopping_list = [('milk', 2, 2.76), ('strawberries', 1, 4.99), ('tomatoes', 10, 0.99)]

total_cost = 0
# We are unpacking a tuple in the `for` statement.
for item, number, cost in shopping_list:
    total_cost_per_item = number * cost
    print ("%s - %s : %s" % (item, number, total_cost_per_item))
    total_cost += total_cost_per_item

print ("Total bill: %s" % total_cost)

Output:
milk - 2 : 5.52
strawberries - 1 : 4.99
tomatoes - 10 : 9.9
Total bill: 20.41
```

- `break` and `continue` statements work as they do in the `while` loop.

```python
shopping_list += [('beer', 6, 1.99)]
total_cost = 0
for item, number, cost in shopping_list:
    # Can't buy beer!
    if item == 'beer':
        continue

    total_cost += number * cost

print (total_cost)

Output:
20.41
```

- The `else` clause also works the same way as it does in `while` statement

```python
total_cost = 0
for item, number, cost in shopping_list:
    if item == 'beer':
        print ("Check the ID before proceeding.")
        break

    total_cost += number * cost
else:
    print (total_cost)

Output:
Check the ID before proceeding.
```

## Dictionaries
- Dictionary is another _collection_ type.
- Dictionary is a **mapping** from keys to values. E.g., let's say you want to store the population of major cities in the USA. Then that can be specified as a mapping as follows: City name --> City population.
- In a dictionary, you cannot have two identical keys. In many problems, this is desired. For example, in the case of city population map, we don't want the same city to be present twice.
- There is _no order_ in the keys of a dictionary. That is why we don't call it a _sequence_.
- Like the list, dictionary is a mutable type.

Here are some ways to create a modify the dictionary:

```python
# Create a dictionary
city_population = {"New York City": 8550405, "Los Angeles": 3971883,
                   "Chicago": 2720546, "Houston": 2296224,
                   "Philadelphia": 1567442, "Phoenix": 1563025,
                   "San Antonio": 1469845, "San Diego": 1394928,
                   "Dallas": 1300092, "San Jose": 1026908}

print (type(city_population))
<class 'dict'>

print (len(city_population))
10
```

```python
# Access one element
print (city_population["Dallas"])
1300092

# Add a new element
city_population["San Francisco"] = 864816
print (len(city_population))
11

# Modify an existing element
# Note that syntax for adding and modifying is the same
# If the key already exists, the value is modified
# Otherwise the new key and value are added
city_population["Houston"] = 2450000
print (city_population["Houston"])
2450000

# You can delete an element
# del is a python language reserved keyword
del city_population["San Diego"]
print (len(city_population))
print ("San Diego" in city_population)
10
False
```

```python
# You can create an empty dictionary and start filling items
# in that
months = {}
months["January"] = 31
months["February"] = 28

# and so on
```

- The key type in the dictionary should always be immutable

```python
# This would raise an error
neighborhood_population = {}
neighborhood_population[["San Francisco", "North Beach"]] = 12000

Traceback (most recent call last):
  File "main.py", line 3, in <module>
    neighborhood_population[["San Francisco", "North Beach"]] = 12000
TypeError: unhashable type: 'list'
```
```python
# We should use tuples instead
neighborhood_population[("San Francisco", "North Beach")] = 12000
print (neighborhood_population)
{('San Francisco', 'North Beach'): 12000}
```


- We can iterate over all elements of the dictionary

```python
# In the following code, let's find the largest neighborhood
# in each city

neighborhood_population = {}
neighborhood_population[("San Francisco", "Downtown")] = 43000
neighborhood_population[("San Francisco", "Western Addition")] = 51000
neighborhood_population[("San Francisco", "Outer Sunset")] = 47000
neighborhood_population[("San Francisco", "Mission")] = 55000
neighborhood_population[("San Francisco", "SoMa")] = 40000

neighborhood_population[("New York", "Flatbush")] = 111000
neighborhood_population[("New York", "Upper West Side")] = 137000
neighborhood_population[("New York", "Borough Park")] = 106000
neighborhood_population[("New York", "Crown Heights North")] = 103000
neighborhood_population[("New York", "Jackson Heights")] = 113000

# largest_hood will store a map from city --> (neighborhood, population)
largest_hood = {}
# Note that we are using the items() method in the class dict
for key, value in neighborhood_population.items():
    print ("processing: ", key)
    print ("debug:", largest_hood, end = "\n\n")

    # Unpacking the key
    (city, neighborhood) = key
    # We are using the get(key, default_value) method in the dict class
    # This returns the value associated with the key in dict, if that key
    # is present in the class. Otherwise, it returns default_value
    current_max = largest_hood.get(city, ('default', 0))[1]

    if value > current_max:
        largest_hood[city] = (neighborhood, value)    

Output:
processing:  ('San Francisco', 'Downtown')
debug: {}

processing:  ('San Francisco', 'Western Addition')
debug: {'San Francisco': ('Downtown', 43000)}

processing:  ('San Francisco', 'Outer Sunset')
debug: {'San Francisco': ('Western Addition', 51000)}

processing:  ('San Francisco', 'Mission')
debug: {'San Francisco': ('Western Addition', 51000)}

processing:  ('San Francisco', 'SoMa')
debug: {'San Francisco': ('Mission', 55000)}

processing:  ('New York', 'Flatbush')
debug: {'San Francisco': ('Mission', 55000)}

processing:  ('New York', 'Upper West Side')
debug: {'San Francisco': ('Mission', 55000), 'New York': ('Flatbush', 111000)}

processing:  ('New York', 'Borough Park')
debug: {'San Francisco': ('Mission', 55000), 'New York': ('Upper West Side', 137000)}

processing:  ('New York', 'Crown Heights North')
debug: {'San Francisco': ('Mission', 55000), 'New York': ('Upper West Side', 137000)}

processing:  ('New York', 'Jackson Heights')
debug: {'San Francisco': ('Mission', 55000), 'New York': ('Upper West Side', 137000)}
```






