# Problem definitions

## 1: More Primes 

This assignment has two parts. The first part is to write a function `is_prime()` that checks if the given positive integer is prime or not. This is how it should work:

```
print (is_prime(3))
Output: True
```

```
print (is_prime(15))
Output: False
```

In part 2, you will write a function `count_primes()`, which given a positive integer N, finds how many numbers between 2 and N are prime. You should make use of the `is_prime()` function that you have already written. The expected functionality is as follows:

```
print (count_primes(5))
Output: 3
```

```
print (count_primes(45))
Output: 14
```

## 2: Pythagoras

This assignment has two parts.  For the first part, write a function `is_pythagorean()` which checks three variables `x`, `y`, `z` satisfy the Pythagorean equation `x^2 + y^2 = z^2`.

The function should behave as follows:

```
print (is_pythagorean(3, 4, 5))
Output: True
```

```
print (is_pythagorean(4, 5, 6))
Output: False
```

In the second part, write a function called `count_pythagorean_triplets()` which takes an integer `n`, and counts how many triplets of numbers (x, y, z) satisfy the Pythagorean equation where `x, y, z <= n`. Note that triples like (3, 4, 5) and (4, 3, 5) (where you just interchanged x and y) are counted as one.

It should work as follows:

```
print (count_pythagorean_triples(5))
Output: 1
```

```
print (count_pythagorean_triples(100))
Output: 52
```

## 3: Longest Sentence

This assignment requires you to write two functions.

1. Write a function `count_words()`, which takes a string (sentence or paragraph) counts how many words are there in that string. Different words will always be separated by a space character. Make sure your function ignores any extra spaces.

Examples:
```
print(count_words(" In another moment down went Alice after it,   "
"never once considering how in the world she was to get out again"))

Output: 21
```


2. Write a function `longest_sentence()`, which takes a paragraph string as input and returns the number of words in the longest sentence in that paragraph. A sentence will always end in a period (.), exclamation mark (!) or a question mark (?).

Examples:

```
print (longest_sentence("It was all very well to say ‘Drink me,’ "
"but the wise little Alice was not going to do that in a hurry. "
"‘No, I’ll look first,’ she said, ‘and see whether it’s marked "
"“poison” or not’; for she had read several nice little histories "
"about children who had got burnt, and eaten up by wild beasts "
"and other unpleasant things, all because they would not remember "
"the simple rules their friends had taught them: such as, "
"that a red-hot poker will burn you if you hold it too long; "
"and that if you cut your finger very deeply with a knife, "
"it usually bleeds; and she had never forgotten that, if you "
"drink much from a bottle marked ‘poison,’ it is almost certain "
"to disagree with you, sooner or later. "))

Output: 108
```

## 4: Sum of digits part 3

What are all the numbers > 0 who sum of digits = 2? They are the following:
2  
11  
20  
101  
110  
200  
1001  

and so on.

If we were to limit the possible candidates to those numbers which has exactly 3 digits, then we find that there three such numbers.

Write a function that takes as input as sum of digits and the number of digits, and returns the count of numbers satisfying that criteria.

e.g.

```
print(numbers_with_sum_of_digits(2, 3))
Output: 3
```

```
print(numbers_with_sum_of_digits(19, 2))
Output: 0
```

```
print(numbers_with_sum_of_digits(19, 3))
Output: 45
```

## 5: GCD

A **common divisor** of two numbers `a` and `b` is a number `g` such that `g` divides both `a` and `b`. The _greatest_ common divisor (or GCD), is the largest such `g`.

Write a function that takes two positive integers `a` and `b` as input and outputs the GCD of those two numbers. The answer will always be 1 or greater.

```
print (gcd(5, 4))
Output: 1
```

```
print (gcd(4, 6))
Output is: 2
```

```
print (gcd(5, 5))
Output is: 5
```

## 6: Exponent

In this assignment, we will write a function where we calculate the exponent using only other mathematical operators (+, -, *, /, %). We will not use the inbuilt operator `**`.

Write a function `exp(num, power)` which outputs `num` raised to `power`. `num` and `power` are both non-negative integers.

e.g.
```
print (exp(2, 3))
Output: 8
```

```
print (exp(10, 0))
Output: 1
```

## 7: City travel

**This is a challenging problem, especially the 2nd part. Perseverance is required to get it right. If you get this right, you have understood the use of recursion really well.**

Suppose a city has blocks with horizontal streets label 1st street, 2nd street and so on (upto 100th street), and all of these streets are one way streets. The vertical streets are labeled Ave A, Ave B and so on (they have 26 avenues, including avenue Z). The image below shows how the street map looks like.

![City streets](https://raw.githubusercontent.com/amangup/coding-bootcamp/master/lecture4/city_streets.png)

**Part 1:**
Suppose you are on foot, which means you don't have to worry about one way streets, and want to go from one intersection to another. How many paths are there for you to reach your destination? Assume that you only want to walk the least distance possible.

e.g.
```
print(num_paths_walking(1, 'A', 2, 'B'))
Output is: 2
```

e.g.
```
print(num_paths_walking(1, 'A', 3, 'C'))
Output is: 6
```

**Part 2:**
Now suppose you are driving a car, and can't go the wrong way on one way streets. How many ways are there to reach the destination from  the starting intersection while travelling the least distance possible?

e.g.
```
print(num_paths_car(1, 'A', 2, 'B'))
Output is: 1
```

```
print(num_paths_car(1, 'A', 3, 'C'))
Output is: 3
```

```
print(num_paths_car(1, 'B', 1, 'A'))
Output is: 1
```

# Solutions

## 1: More primes

<details>
<summary>Show code:</summary>

```python
def is_prime(num):
    if num > 1:
        i = 2
        while i * i <= num:
            if (num % i) == 0:
                return False
            i += 1
        return True
    else:
        return False
 
def count_primes(n):
    count = 0
    i = 2
    while i <= n:
        if is_prime(i):
            count += 1
        i += 1
    return count
```

</details>

## 2: Pythagoras

<details>
<summary>Show code:</summary>

```python
def is_pythagorean(x, y, z):
  return (x * x) + (y * y) == (z * z)

def count_pythagorean_triplets(n):
  count_triples = 0
  i = 2
  while i < n - 2:
    i += 1
    
    j = i
    while j < n - 1:
      j += 1
      
      k = j
      while k < n:
        k += 1
        if is_pythagorean(i, j, k):
          count_triples += 1
  
  return count_triples
```

</details>

## 3: Longest Sentence

<details>
<summary>Show code:</summary>

```python
def count_words(sentence):
  count = 0
  last_word = ''
  
  i = 0
  while i < len(sentence):
    if sentence[i] == ' ':
      if last_word:
        count += 1
      last_word = ''
    else:
      last_word += sentence[i]
    
    i += 1

  if last_word:
    count += 1
      
  return count
  
def longest_sentence(para):
  max_sentence_length = 0
  last_sentence = ''

  i = 0
  while i < len(para):
    if para[i] in '.!?':
      word_count = count_words(last_sentence)
      max_sentence_length = max(word_count, max_sentence_length)
      last_sentence = ''
    else:
      last_sentence += para[i]
      
    i += 1
      
  return max_sentence_length
```

</details>

## 4: Sum of digits part 3

<details>
<summary>Show code:</summary>

```python
def numbers_with_sum_of_digits(sum_of_digits, num_digits, first_digit=True):
	# Termination condition is when we have to count single digit numbers
    if num_digits == 1:
        if sum_of_digits <= 9:
            return 1
        else:
            # If sum of digits >= 10, then no single digit number will
            # satisfy the criteria
            return 0
    else:
        i = -1
        count = 0
        while i < 9:
            i += 1
            # i is our candidate for the next digit in the number

            # we cannot have 0 as the leftmost digit
            if first_digit == True and i == 0:
                continue

            # This is the main recursion step. To count numbers with
            # n digits, we assume that the current digit is 'i', and
            # then we have to find the count for numbers with
            # sum of digits = sum_of_digits - i, and number of digits = n - 1
            if sum_of_digits >= i:
                count += numbers_with_sum_of_digits(sum_of_digits - i, 
                                                    num_digits - 1, False)
        return count
```

</details>

## 5: GCD

<details>
<summary>Show code:</summary>

```python
def gcd(a, b):
  if a < b:
    temp = a
    a = b
    b = temp

  if a % b == 0:
    return b
  else:
    return gcd(b, a % b)
```

</details>

## 6: Exponent

<details>
<summary>Show code:</summary>

```python
def exp(num, power):
  if power == 0:
    return 1
  else: 
    return num * exp(num, power - 1)

# Can you figure out why this is fast?  
def exp_fast(num, power):
  if power == 0:
    return 1
  else:
    if power % 2 == 0:
      half_power = exp_fast(num, power / 2)
      return half_power * half_power
    else:
      return num * exp_fast(num, power - 1)
```

</details>

## 7: City travel

<details>
<summary>Show code:</summary>

```python
def get_next_step(start, end):
    # direction is +1 or -1 depending on whether we want to go towards
    # higher street/avenue to reach end, or lower street/avenue (respectively)
    direction = int((end - start) / abs(end - start))

    # we travel one block at a time
    return start + direction

def num_paths_walking(start_st, start_av, end_st, end_av):
    # Termination condition: If we have reached the destination, that is one
    # path
    if start_st == end_st and start_av == end_av:
        return 1
    else:
        # Recursion step. We can either travel along the avenue or the street
        num_paths = 0

        # In this case, we travel along the avenue
        if start_st != end_st:
            num_paths += num_paths_walking(
                get_next_step(start_st, end_st), start_av, end_st, end_av)

        # In this case, we travel along the street
        # We use ord() and chr() to convert lettered Avenue names to integer
        # and vice versa.
        start_av_int = ord(start_av)
        end_av_int = ord(end_av)
        if start_av_int != end_av_int:
            next_av_int = get_next_step(start_av_int, end_av_int)
            num_paths += num_paths_walking(start_st, chr(next_av_int), end_st,
                                           end_av)

        return num_paths


def num_paths_car(start_st, start_av, end_st, end_av, original_start = True):
    # Termination condition: If we have reached the destination, that is one
    # path
    if start_st == end_st and start_av == end_av:
        return 1
    else:
        # Recursion step. We can either travel along the avenue or the street
        num_paths = 0

        # We check if we can travel along the current street if wanted to reach
        # end_av from start_av. This is required because all numbered streets
        # are One Way only.
        #
        # We can go towards increasing avenues on odd numbered streets, and
        # towards decreasing avenues on even numbered streets.
        start_av_int = ord(start_av)
        end_av_int = ord(end_av)
        is_one_way_direction = (end_av_int > start_av_int
                                and start_st % 2 == 1) or (
                end_av_int < start_av_int and start_st % 2 == 0)

        # We travel along the avenue
        if start_st != end_st:
            num_paths += num_paths_car(get_next_step(start_st, end_st),
                                       start_av, end_st, end_av, False)
                                       
        # The following is a special case when the original input "forces us"
        # to go the wrong way on a one way street (original input has same
        # start and end streets, but the end avenue is in the opposite direction
        # to the one way direction of the street).
        #
        # In this case, our first step is to travel to the next street,
        # and then continue as usual.
        elif original_start and not is_one_way_direction:
            if start_st < 100:
                num_paths += num_paths_car(start_st + 1, start_av, end_st, end_av,
                                           False)
            if start_st > 1:                                        
                num_paths += num_paths_car(start_st - 1, start_av, end_st, end_av,
                                           False)

        # If the one way direction allows us, we travel along the street
        if start_av_int != end_av_int:
            next_av_int = get_next_step(start_av_int, end_av_int)
            if is_one_way_direction:
                num_paths += num_paths_car(start_st, chr(next_av_int), end_st,
                                           end_av, False)

        return num_paths
```

</details>
