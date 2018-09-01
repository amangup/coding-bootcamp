# Problem Definitions

## 1: GDP growth

The US GDP in 2017 was $19.739 Trillions. Input a target year, and output the expected GDP for US in that year. Assume that GDP grows by 2% every year. 

Output: Simply print the expected GDP for the target year

e.g.
```
What is the target year for which you want to know US GDP? 2020 
20.947184712000002
```

## 2: Fahrenheit to Celsius

Input temperature in Fahrenheit, and print the same temperature in Celsius.

e.g.
```
What is the temperature in Fahrenheit? 32
0.0
```

## 3: Hodor Hodor Hodor

Take a string as input, and print it 5 times with a space in between.

e.g.
```
Enter a string: Hodor
Hodor Hodor Hodor Hodor Hodor
```

## 4: Has a or b

Input a string and check if it contains the lowercase letters 'a' or 'b'.

e.g.
```
Enter a string: The War on Drugs
True
```

```
Enter a string: Beirut
False
```

## 5: Find last digit

Input an integer and print it's last digit.

e.g.
```
Enter an integer: 42
2
```

## 6: Calculate federal taxes

Calculate federal taxes for someone with annual income in the range of $100,000 to $190,000 using the single person tax brackets and standard deduction as follows.

- $0 to $9,325 : 10%
- $9,325 to $37,950: 15%
- $37,950  to $91,900: 25%
- $91,900 to $191,650: 28%

Standard deduction: $6,350

e.g.
```
What is your income ($100,000 - $190,000)? 100000
19203.75
```

## 7: Hourly pay

Input someone's hourly pay and check if they earn more than or equal to $1,500 on a fortnightly basis. Assume they work 40 hours a week. Print True if yes, False otherwise.

e.g.

```
What is your hourly_pay? 25
True
```

## 8: Movie runtime

For a movie, input its runtime length in seconds and print it out in Hours:Minutes:Seconds.

e.g.
```
What is the length of the movie in seconds? 10000
2:46:40
```

## 9: Modern Olympics

Input a year (1896 or later) and print True if the Summer Olympics were organized in that year (or will be), False otherwise.

e.g.
```
Enter a year? 1896
True
```

## 10: Suitcases in a car trunk

Input the volume of car's trunk in gallons, and the volume of one suitcase, and print the number of suitcases you can fit in that trunk.

e.g.
```
What is the volume of the trunk in US gallons? 110
What is the volume of the suitcase in US gallons? 12
9
```
 
## 11: Sum of digits

Input a 3 digit integer, and print the sum of its digits.

e.g.
```
Enter a number (100 - 999)? 360
9
``` 

## 12: Integer memory size

This problem requires you to use the internet to find answers and learn more about python and programming.

Input an integer, and print the number of bytes of memory space that the variable containing the integer takes up.

e.g.
```
Enter an integer? 2
28
```

## 13: ASCII values

This problem requires you to use the internet to find answers and learn more about python and programming.

Input a string, and print the ASCII value of its first and last characters. Output both the values in the same line separated by a space.

e.g.
```
Enter a string: What's an ASCII character?
87 63
```

## 14: Print formatting

This problem requires you to use the internet to find answers and learn more about python and programming.

Enter a real number and print it out rounded to only two decimal places.

e.g.
```
Enter a real number: 19.3
19.30
```

```
Enter a real number: 2.348
2.35
```

## 15: Bill for items

This problem requires you to use the internet to find answers and learn more about python and programming.

For a person buying a large number of same items, ask the price of the item and number of items purchased, and output the total bill.

e.g.
```
Enter price of the item: 2.1
Enter number of items: 3
6.3
```

# Solutions

## 1: GDP growth

<details>
<summary>Show code:</summary>

```python
us_gdp_2017_trillions = 19.739
target_year = int(input("What year do you want to know US GDP for?"))

years_diff = target_year - 2017
gdp_growth_rate = 0.02

us_gdp_target_year = us_gdp_2017_trillions * ((1 + gdp_growth_rate) ** years_diff)
print(us_gdp_target_year)
```

</details>

## 2: Fahrenheit to Celsius

<details>
<summary>Show code:</summary>

```python
fahrenheit = float(input("What is the temperature in Fahrenheit?"))
celsius = (fahrenheit - 32) * 5 / 9

print(celsius)
```
</details>

## 3: Hodor Hodor Hodor

<details>
<summary>Show code:</summary>

```python
input_str = input("Enter a string:")
output_str = (input_str + ' ') * 4
output_str = output_str + input_str
print(output_str)
```

</details>

## 4: Has a or b

<details>
<summary>Show code:</summary>

```python
input_str = input("Enter a string:")
has_a_b = 'a' in input_str or 'b' in input_str
print(has_a_b)
```

</details>

## 5: Find last digit

<details>
<summary>Show code:</summary>

```python
input_int = int(input("Enter an integer:"))
last_digit = input_int % 10
print(last_digit)
```
</details>

## 6: Calculate federal taxes

<details>
<summary>Show code:</summary>

```python
annual_income = float(input("What is your income ($95,000 - $190,000)?"))
standard_deduction = 6350
tax_slab1 = 9325 * 0.1
tax_slab2 = (37950 - 9325) * 0.15
tax_slab3 = (91900 - 37950) * 0.25
tax_slab4 = (annual_income - standard_deduction - 91900) * 0.28

total_tax = tax_slab1 + tax_slab2 + tax_slab3 + tax_slab4
print(total_tax)
```

</details>

## 7: Hourly pay

<details>
<summary>Show code:</summary>

```python
hourly_pay = float(input("What is your hourly_pay?"))
hours_per_week = 40
fornightly_pay = hourly_pay * hours_per_week * 2

print(fornightly_pay >= 1500)
```
</details>

## 8: Movie runtime

<details>
<summary>Show code:</summary>

```python
movie_runtime_secs = int(input("What is the length of the movie in seconds?"))
seconds = movie_runtime_secs % 60
minutes = int(movie_runtime_secs / 60) % 60
hours = int(movie_runtime_secs / 3600)
print("%s:%s:%s" % (hours, minutes, seconds))
```

</details>

## 9: Modern Olympics

<details>
<summary>Show code:</summary>

```python
year = int(input("Enter a year?"))
is_olympic_year = (year % 4 == 0)
print(is_olympic_year)
```

</details>

## 10: Suitcases in a car trunk

<details>
<summary>Show code:</summary>

```python
volume_trunk = float(input("What is the volume of the trunk in US gallons?"))
volume_suitcase = float(input("What is the volume of the suitcase in US gallons?"))
num_suitcases_in_trunk = int(volume_trunk / volume_suitcase)

print (num_suitcases_in_trunk)
```

</details>

## 11: Sum of digits

<details>
<summary>Show code:</summary>

```python
input_int = int(input("Enter a number (100 - 999)?"))
ones_digit = input_int % 10
tens_digit = int(input_int / 10) % 10
hundreds_digit = int(input_int / 100) % 10
sum_of_digits = ones_digit + tens_digit + hundreds_digit

print(sum_of_digits)
```

</details>

## 12: Integer memory size

<details>
<summary>Show code:</summary>

```python
input_int = int(input("Enter an integer?"))
from sys import getsizeof

print(getsizeof(input_int))
```

</details>

## 13: ASCII values

<details>
<summary>Show code:</summary>

```python
input_str = input("Enter a string:")
ascii_first = ord(input_str[0])
ascii_second = ord(input_str[-1])

print("%s %s" % (ascii_first, ascii_second))
```

</details>

## 14: Print formatting

<details>
<summary>Show code:</summary>

```python
real_num = float(input("Enter a real number:"))
print ("%.2f" % real_num)
```

</details>

## 15: Bill for items

<details>
<summary>Show code:</summary>

```python
price_of_item = float(input("Enter price of the item:"))
num_items = int(input("Enter number of items:"))
price_cents = price_of_item * 100
total_bill_cents = num_items * price_cents

print(total_bill_cents / 100)
```

</details>