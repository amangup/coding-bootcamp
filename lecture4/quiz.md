# Quiz
A multiple choice quiz with 8 questions where each question has a code listing and you have to choose an answer which corresponds to the output of that code listing.

**Question 1**

```python
x = 10
print (next_number(x))

def next_number(i):
  return i + 1
```

Options:  
a: 11   
b: 10  
c. Python raises an error  
d. None of the above

**Question 2**
```python
def find_sum(n):
  i = 1
  while i <= n:
    summation += i
    i += 1

summation = 0
find_sum(5)
print (summation)
```

Options:  
a: 10  
b: 15  
c: 0  
d: Python raises an error  

**Question 3**
```python
def power():
  return n ** n
    
n = 1
power_sum = 0
while n <= 3:
  power_sum += power()
  n += 1
  
print (power_sum)
```

Options:  
a: 5  
b: 32  
c: 0  
d: Python raises an error  

**Question 4**
```python
def replace_char(string, to_find, replacement):
  i = 0
  while i < len(string):
    if string[i] == to_find:
      string[i] = replacement

    i += 1

word = "zoom"
replace_char(word, 'z', 'b')
print(word)
```

Options:  
a: zoom  
b: boom  
c: None  
d: Python raises an error

**Question 5**
```python
def get_sum(n):
  result = 0
  while n > 0:
    result += n
    n -= 1
  return result

n = 5
print (get_sum(n), get_sum(n + 1))
```

Options:  
a: 15 1  
b: 10 1  
c: 0 0  
d: 15 21

**Question 6**
```python
def get_sum_step(max, step):
  result = 0
  while max != 0:
    result += max
    max -= step
    
  return result
    
print (get_sum_step(10, 2))
print (get_sum_step(10, 3))
```

Options:  
a:  
30  
22  

b:  
20  
18  

c:  
0  
0  

d: None of the above  
 
**Question 7**
```python
def get_num_words(string):
  last_word = ''
  num_words = 0
  i = 0
  while i < len(string):
    if string[i] == ' ':
      if last_word:
        num_words += 1
      last_word = ''
      continue
    
    last_word += string[i]
    i += 1

  return num_words
  
print (get_num_words("a set of words that is complete in itself"))
```

Options:  
a: 8  
b: 9  
c: 0  
d: None of the above  

**Question 8**
```python
# No leap year, m in [1, 12]
def days_in_month(m):
  if (m < 8 and m % 2 == 1) or (m > 8 and m % 2 == 0):
    return 31
  elif (m < 8 and m % 2 == 0) or (m > 8 and m % 2 == 1):
    if m == 2:
      return 28
    else:
      return 30

i = 1
while i <= 12:
  print (i, days_in_month(i))
  
  i += 1
```

Which month's output is incorrect? Options:  
a: Every month's output is correct  
b: m = 2  
c: m = 7  
d: m = 8  

**Question 9**
```python
def sum(n, total=100):
  if n == 0 or n == 1:
    return n
  else:
    return sum(n - 1, total + n)

print(sum(5))
```

Options:  
a: 15  
b: 14  
c: 115  
d: 114  

