# Problem definitions

## 1: Kth order statistic

Write a function `kth_smallest(alist, k)` which returns the kth smallest number in `alist` (which contains numbers). If `k > len(alist)`, return None.

Hint: Check out the `sorted()` built-in function.

e.g.

```
print(kth_smallest([1, 5, 3, 25, 6], 4))
Output: 6
```

```
print(kth_smallest([1, 10, 3], 4))
Output: None
```

## 2: Rotation

Write a function `rotate_forward(alist, k)` which returns a new list that has all its elements shifted by `k` positions to the right. The items which exceed the boundary of the list should cycle back to the starting of the list.

Can you handle the case of `k < 0` gracefully?

e.g.
```
print(rotate_forward(['a','b','c','d','e','f'], 2))
Output: ['e', 'f', 'a', 'b', 'c', 'd']
```

```
print(rotate_forward(['a','b','c','d','e','f'], -2))
Output: ['c', 'd', 'e', 'f', 'a', 'b']
```

## 3: Reverse inplace

Write a function `reverse_inplace(alist)` which reverses the list _in-place_, i.e., you will mutate the same list instead of creating a new list.

Note: While using the `reverse()` method in the list class is a valid solution, I would like you to try and implementing this yourself using a `for` loop.

The function should return nothing.

e.g.

```
alist = [1,2,3,4,5]
reverse_inplace(alist)
print(alist)

Output: [5,4,3,2,1]
```

## 4: Join by Seperator

Write a function `join(alist, seperator)` which creates a string that contains the elements of `alist` in order, and each consecutive pair of values is separated by the string `separator`.

e.g.
```
print(join([1,2,3,4,5], "-"))
Output: 1-2-3-4-5
```

## 5: Anagrams

Write a function `is_anagram(word, anagram)` which checks if the variable `anagram` represents the anagram of the variable `word`. The variables can have different spaces, and different case of letters - but if the combination of letters are the same, then they still are anagrams of each other.

Hint: check out the methods of the `str` class.

e.g.
```
print(is_anagram("funeral", "Real fun")
Output: True
```

```
print(is_anagram("batman", "robin"))
Output: False
```

## 6: Insertion sort

**This assignment is designed to teach how a simple sorting algorithm works. Do not use list.sort() method or sorted() built-in function!**

Part 1:  
Write a function `insert_sorted(sorted_list, element)`, where you insert the `element` in such a way that the list remains sorted after the insertion. This insertion is done in-place, i.e., no new list is created.

e.g.

```
alist = [1,3,5,7,9]
insert_sorted(alist, 4)
print(alist)

Output: [1,3,4,5,7,9]
```

Part 2:  
Write a function `insertion_sort(unsorted_list)` which uses the function `insert_sorted` and returns a new list which has all elements of `unsorted_list` sorted in an ascending order. 

e.g.

```
print(insertion_sort([6,1,5,2,4,3]))

Output: [1,2,3,4,5,6]
```

## 7: Dot Product

In mathematics, a **vector** is defined as the sequence of numbers. In vector mathematics, there is another concept called the **dot product**.

If a Vector1 is defined by values `[a1, a2, a3, ..., an]`  
and Vector2 by values `[b1, b2, b3, ..., bn]`

The dot product is defined as: `a1*b1 + a2*b2 + a3*b3 +  ... + an*bn`

i.e., the corresponding elements are multiplied and a new vector is created.

This concept has many uses in geometry (like finding out how far a location is from a certain street).

Write a function `dot_product(vector1, vector2)` where `vector1` and `vector2` are lists representing the vectors, and you return the sum of pairwise products of elements of these lists.

e.g.
```
print(dot_product([1, -1, 1], [2, 3, 4]))
Output is: 1
```

```
print(dot_product([0, 1, 0], [1, 0 0])
Output is: 0
```

## 8: Area of a polygon

You have to write a function that computes the area of a polygon in the 2-D x-y plane. The link below explains the formula which can be used to find the area of any polygon.

https://www.mathopenref.com/coordpolygonarea.html 

Write a function `polygon_area(coordinates)` where `coordinates` is a list of two-tuples representing points on the x-y plane. Use the  mathematical formula described on the page above to calculate the area of the polygon. Assume that the coordinates are ordered to be in clockwise order when traversing the edges of the polygon.

Hint: You will need to use the `abs()` built-in function

e.g.

```
coordinates = [(0, 0), (0, 1), (1, 1), (1, 0)]
print(polygon_area(coordinates)]

Output is: 1
```

## 9: City connections

Let's say we assign each major city in the US a number starting from 0, 1, 2, 3 and so on. We want to create a convenient table to know if any two cities are connected by a direct flight. To do so, we are going to create a table of connections.

You have to write a function `city_flight_table(n, direct_flights)` where `n` is the number of cities (numbered from 0 to n-1), and `direct_flights` is a list of two-tuples `(a, b)` which indicate that city a and city b have a direct flight connecting them (both ways).

The  output will be a 2-Dimensional list (a list of lists) which contains Boolean values - let's call it `table`. Both `table[a][b]` and table`[b][a]` will be `True` if cities a and b are connected by a direct flight, `False` otherwise. A city is always directly connected to itself.

e.g.

```
num_cities = 3
direct_flights = [(0, 1), (1, 2)]
table = city_flight_table(num_cities, direct_flights)

print(table[0][2])
print(table[1][2])
print(table[2][1])
print(table[2][2])

Output is:
False
True
True
True
```

## 10: Histogram

A histogram is a statistic about any piece of data where we measure the frequency with which each item appears in the data. We will write a program to compute the histogram, and then use it.

Part 1:  
Write a function `get_histogram(alist)` which takes a list, and returns a dictionary which represents the histogram of the list.

e.g.

```
print(get_histogram(["Male", "Male", "Female", "Male", "Female"]))        
Output is: {'Male': 3, 'Female': 2}
```

Part 2:  
Write a function `count_unique(alist)` which returns the number of unique elements in the list.

e.g.

```
print(count_unique(["Mark", "John", "Mark", "Matthew", "John"]))
Output is: 3
```

Part 3:  
Write a function `find_mode(alist)` that finds the most commonly occurring element in the list (called the **mode** of the list).

E.g.

```
print(find_mode([1, 2, 1, 3, 1, 2])
Output is: 1
```

## 11: Inventory value

You are a shopkeeper who has a large inventory of items. Every day you write down the total value of your inventory in your account books. It's a cumbersome process, so you learned how to write code, and you want the computer to calculate that value.

Write a function `inventory_value(item_count, item_value)` to calculate the value of your inventory. Your input consists of two dictionaries: 

- `item_count` contains the mapping from item name --> item quantity
- `item_value` contains the item price for each item name.

If an item is one dictionary but not in another, ignore that item.

e.g.

```
item_count = {"bread": 15, "milk": 10}
item_value = {"bread": 1.99, "milk": 2.99, "butter": 3.99}
print(inventory_value(item_count, item_value))

Output is: 59.75 
```

## 12: Selling from inventory

For any inventory system, one of the basic tasks is to update the inventory count when items are sold. 

Write a function `sell_from_inventory(item_count, item_to_sell, sell_count)` which takes the dictionary indicating the current inventory (`item_coun`t), the item name to be sold (`item_to_sell`) and the quantity to be sold (`sell_count`). 

- It returns `True` if that sale can be made (i.e., inventory has enough items for the sale), or `False` otherwise. 
- Update the inventory to reflect the new item counts after the sale is made.
- If the there is no more inventory for that item after the sale, remove it from the item count dictionary.


E.g.

```
item_count = {"bread": 15, "milk": 10}
print(sell_from_inventory(item_count, "bread", 15))
print(item_count)

Output is:
True
{"milk": 10}
```

E.g.

```
item_count = {"bread": 15, "milk": 10}
print(sell_from_inventory(item_count, "milk", 15))
print(item_count)

Output is:
False
{"bread": 15, "milk": 10}
```

## 13: A tale of two inventories

You are given two dictionaries which represent inventories of different departments in a store. Write a function `merge_inventory(item_count_a, item_count_b)` that outputs a new dictionary which represents the combined inventory of both departments. Note that two departments may store the same item.

E.g.

```
item_count_a = {"notebooks": 100, "pens": 500, "glue": 25}
item_count_b = {"thread": 250, "needle": 100, "glue": 25}
print(merge_inventory(item_count_a, item_count_b))

Output is: 
{'notebooks': 100, 'pens': 500, 'glue': 50, 'thread': 250, 'needle': 100} 
```

## 14: Group By, Sum

In data transformations, a very common operation is to "Group By" by a certain set of _keys_ in data, and then "Sum" the values. For example, your data might be a list of items in your credit card bill. Each line has a date, the seller's name, purchase category (clothing, restaurant, groceries, etc.) and the amount spent. You might want to know how much money you spent on each category. To calculate that, you can "group" all purchases by the purchase category (for each category), and then sum the amount spent for each group.

You have to write a function `group_by_sum(records, key_indices, value_index)` where:

- `records` is a list that represents the source data. Each element in the list is a tuple that represents one row of data. All tuples are of the same length. You can think of each element of tuple as a column of data.
- `key_indices` are the indices in a tuple in `records` list that represent the key (the category columns)
- `value_index` is the index in a tuple in `records` that represent the value (the money column).

The function returns a dictionary which groups by the tuple elements represented by `key_indices`, and then sums the value at the `value_index` in each group. The key of the output dictionary is a tuple containing all the columns indexed by the `key_indices`, and the value of the output dictionary is just a number.

The example below should make it clearer.

```
records = [("Feb", "Cole Hardware", "Household", 50.0), 
           ("Feb", "Tony's Pizza", "Dining", 70), 
           ("Feb", "Piccolo Forno", "Dining", 40),
           ("Mar", "Comcast", "Online Services", 75), 
           ("Mar", "Mama's", "Dining", 80)]         
print(group_by_sum(records, [0, 2], 3))

Output is:
{('Feb', 'Household'): 50.0, ('Feb', 'Dining'): 110, ('Mar', 'Online Services'): 75, ('Mar', 'Dining'): 80}
```


## 15: Word count
Take a string paragraph as input, and count the number of times each word appears in that paragraph. You are to 
- ignore all punctuation characters `(, . ; " ? !)` 
- ignore the parenthesis characters 
- ignore the difference in case of the words. If the same word appears in different cases (e.g., "Mother" and "mother"), they are to be considered the same word. Output all words in lower case.

Write a function `word_count(para)` which returns a dictionary containing the word count.

Hint: use str class's method `lower()`

e.g.

```
para = ('A paragraph (from the Ancient Greek paragraphos, "to write beside" '
        'or "written beside") is a self-contained unit of a discourse in '
        'writing dealing with a particular point or idea. Though not '
        'required by the syntax of any language, paragraphs are usually '
        'an expected part of formal writing, used to organize longer prose.')
print(word_count(para))

{'a': 4, 'paragraph': 1, 'from': 1, 'the': 2, 'ancient': 1, 'greek': 1, 'paragraphos': 1, 'to': 2, 'write': 1, 'beside': 2, 'or': 2, 'written': 1, 'is': 1, 'self-contained': 1, 'unit': 1, 'of': 3, 'discourse': 1, 'in': 1, 'writing': 2, 'dealing': 1, 'with': 1, 'particular': 1, 'point': 1, 'idea': 1, 'though': 1, 'not': 1, 'required': 1, 'by': 1, 'syntax': 1, 'any': 1, 'language': 1, 'paragraphs': 1, 'are': 1, 'usually': 1, 'an': 1, 'expected': 1, 'part': 1, 'formal': 1, 'used': 1, 'organize': 1, 'longer': 1}
```

## 16: Merge lists to dictionary

There are two lists whose values correspond to each other (for e.g., one list contains names of people, and the other contains their height in inches). Write a function `merge_to_dict(alist, blist)` which returns a new dictionary using first list's values as the dict keys, and the second list's values as the corresponding dict values. Return `None` if the operation fails.

The operation can fail if:
- The two lists are not of the same length
- The first list has duplicate values

e.g.
```
country = ["Canada", "Greenland", "India", "Siberia"]
weather = ["Cold", "Very Cold", "Very Hot", "Freezing"]
print (merge_to_dict(country, weather))

Output is:
{'Canada': 'Cold', 'Greenland': 'Very Cold', 'India': 'Very Hot', 'Siberia': 'Freezing'}
```

# Solutions

## 1: Kth order statistic

<details>
<summary>Show code:</summary>

```python
def kth_smallest(alist, k):
    sorted_list = sorted(alist)
    if k <= len(alist):
        return sorted_list[k - 1]
```

</details>

## 2: Rotation

<details>
<summary>Show code:</summary>

```python
def rotate_forward(alist, k):
    if alist:
        k = k % len(alist)
    return alist[-k:] + alist[:-k]
```

</details>

## 3: Reverse inplace

<details>
<summary>Show code:</summary>

```python
def reverse_inplace(alist):
    for i in range(0, int(len(alist) / 2)):
        alist[i], alist[-i - 1] = alist[-i - 1], alist[i]
```

</details>

## 4: Join by Seperator

<details>
<summary>Show code:</summary>

```python
def join(alist, separator):
    return separator.join(alist)
```

</details>

## 5: Anagrams

<details>
<summary>Show code:</summary>

```python
def _sanitize_(word):
    return word.replace(" ", "").lower()

def is_anagram(word, anagram):
    return sorted(_sanitize_(word)) == sorted(_sanitize_(anagram))
```

</details>

## 6: Insertion sort

<details>
<summary>Show code:</summary>

```python
def insert_sorted(sorted_list, element):
    for i, item in enumerate(sorted_list):
        if element <= item:
            sorted_list.insert(i, element)
            break
    else:
        sorted_list.append(element)

def insertion_sort(unsorted_list):
    sorted_list = []
    for item in unsorted_list:
        insert_sorted(sorted_list, item)
    return sorted_list
```

</details>

## 7: Dot Product

<details>
<summary>Show code:</summary>

```python
def dot_product(vector1, vector2):
    dot_sum = 0
    for a, b in zip(vector1, vector2):
        dot_sum += a * b
    
    return dot_sum
```

</details>


## 8: Area of a polygon

<details>
<summary>Show code:</summary>

```python
def polygon_area(coordinates):
    area = 0
    for i in range(len(coordinates)):
        j = (i + 1) % len(coordinates)
        area += (coordinates[i][0] * coordinates[j][1] - 
                coordinates[i][1] * coordinates[j][0])
        

    return abs(area) / 2.0
```

</details>

## 9: City connections

<details>
<summary>Show code:</summary>

```python
def city_flight_table(n, direct_flights):
    table = []
    for i in range(n):
        table.append([False] * n)
        table[i][i] = True
    
    for a, b in direct_flights:
        table[a][b] = True
        table[b][a] = True
        
    return table
```

</details>

## 10: Histogram

<details>
<summary>Show code:</summary>

```python
def get_histogram(alist):
    histogram = {}
    for item in alist:
        histogram[item] = histogram.get(item, 0) + 1
    return histogram

def count_unique(alist):
    return len(get_histogram(alist))
    
def find_mode(alist):
    max_key = None
    max_count = 0
    for key, count in get_histogram(alist).items():
        if count > max_count:
            max_count = count
            max_key = key
            
    return max_key            

# You can also use the max() built in function by telling it to
# find maximum by the value of a dict (histogram.get() is a method
# that returns the value for the key in histogram)
def find_mode_alternate(alist):
    histogram = get_histogram(alist)
    if histogram:
        return max(histogram, key=histogram.get)
```

</details>

## 11: Inventory value

<details>
<summary>Show code:</summary>

```python
def inventory_value(item_count, item_value):
    total_sum = 0
    for item, count in item_count.items():
        # item_value.get() is a method that returns
        # that returns the value for the key in item_value.
        # If the key is not found, it returns the 2nd argument as
        # a default value, which in this case is None
        value = item_value.get(item, None)
        if value:
            total_sum += count * value
            
    return total_sum
    
def inventory_value_alt(item_count, item_value):
    total_sum = 0
    # The dict.keys() returns an object which implements the class 
    # 'set'. The & operator finds the intersection of two sets.
    for item in (item_count.keys() & item_value.keys()):
        total_sum += item_count[item] * item_value[item]
        
    return total_sum
```

</details>

## 12: Selling from inventory

<details>
<summary>Show code:</summary>

```python
def sell_from_inventory(item_count, item_to_sell, sell_count):
    count = item_count.get(item_to_sell, 0)
    if count >= sell_count:
        if count == sell_count:
            del item_count[item_to_sell]
        else:
            item_count[item_to_sell] -= sell_count
            
        return True
        
    return False
```

</details>

## 13: A tale of two inventories

<details>
<summary>Show code:</summary>

```python
def merge_inventory(item_count_a, item_count_b):
    merged = item_count_a.copy()
    for item, count in item_count_b.items():
        merged[item] = merged.get(item, 0) + count
        
    return merged
```

</details>

## 14: Group By, Sum

<details>
<summary>Show code:</summary>

```python
def _multi_index_get_(atuple, indices):
    output = []
    for i in indices:
        output.append(atuple[i])
        
    return tuple(output)

def group_by_sum(records, key_indices, value_index):
    group_sums = {}
    for record in records:
        key = _multi_index_get_(record, key_indices)
        group_sums[key] = group_sums.get(key, 0) + record[value_index]
    
    return group_sums
```

</details>

## 15: Word count

<details>
<summary>Show code:</summary>

```python
def word_count(para):
    count_dict = {}
    last_word = ""
    chars_to_ignore = ',.;"?!()'
    for char in para:
        if char in chars_to_ignore:
            continue
        
        if char is " ":
            last_word = last_word.lower()
            count_dict[last_word] = count_dict.get(last_word, 0) + 1
            last_word = ""
        else:
            last_word += char
            
    if last_word:
        count_dict[last_word] = count_dict.get(last_word, 0) + 1

    return count_dict
```

</details>

## 16: Merge lists to dictionary

<details>
<summary>Show code:</summary>

```python
def merge_to_dict(alist, blist):
    if len(alist) != len(blist):
        return None
        
    new_dict = {}
    for a, b in zip(alist, blist):
        if a in new_dict:
            return None
        new_dict[a] = b
        
    return new_dict
```

</details>
