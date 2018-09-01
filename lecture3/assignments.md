# Problem definitions

## 1: Punctuation spaces

In correctly formed paragraphs, one space must be present after the following punctuation characters - period (.), comma(,), exclamation mark (!) and question mark (?).

Input a paragraph from the user and check if the writer has correctly added these spaces after the punctuation. If there are no errors, output **Correct**. If there is an error, output **Incorrect** and the location of the error as follow: `[word1] + punctuation mark + [first letter of next word]` (see examples).

Assume that the input doesn't contain any other punctuation marks, like colon(:), semi-colon(;), etc. And the sentence will always be non-empty and start with a word.

e.g.
```
Input: 'Thank you, madam.'
Output: 'Correct'
```

```
Input: 'By the way,it is raining outside.'
Output: 'Incorrect: way,i'
```

```
Input: `Hi!You look beautiful.`
Output: `Incorrect: Hi!Y`
```


## 2: Taxes for any income

Calculate federal taxes for someone with any annual income. Single person tax brackets and standard deduction as follows.

- $0 to $9,325 : 10%
- $9,325 to $37,950: 15%
- $37,950  to $91,900: 25%
- $91,900 to $191,650: 28%
- $191,650 to $416,700: 33%
- $416,700 to $418,400: 35%
- $418,400+: 39.6%

Standard deduction: $6,350

e.g.

```
Input: '500000'
Output: '151304.25'
```

## 3: Is Number a prime?

Input a number and check if it is prime. Prime number is a number `p` such that it has no divisors other than 1 and `p`. First few primes are 2, 3, 5, 7, 11, 13, 17, 19, 23.

e.g.
```
Input: '12'
Output: 'No'
```

```
Input: '13'
Output: 'Yes'
```

## 4: Sum of digits (again)

Input a number and print the sum of its digits.

e.g.
```
Input: '125'
Output: '8'
```

## 5: Find largest

Keep asking the user to input a number, until they enter 0 or have entered 10 numbers. Print the largest number as output. Don't consider 0 as part of the input when you compute the maximum.

e.g.
```
Inputs: '2,5,0'
Output: '5'
```

```
Inputs: '4,10,33,9,10,5,45,-1,23,45,99'
Output: '45'
```

## 6: Parenthesis

Input an expression with parenthesis, and check if the parenthesis are properly matching.

e.g.

```
Input: '((x+1)*2)'
Output: 'Yes'
```

```
Input:  '(x-1)/5)'
Output: 'No'
```

## 7: Reversal

Input a word and print it's reverse.

e.g.

```
Input: 'Park'
Output: 'kraP'
```

## 8: Star triangle
 
Input a number N, and write a program to print a right angle with N rows like below using asterisks.

```
*
* *
* * *
```

e.g.
```
Input: '5'
Output:
*
* *
* * *
* * * *
* * * * *
```

## 9: Count vowels

Input a sentence and count the number of vowel characters in that sentence. Both uppercase and lowercase character characters should be counted.

e.g.
```
Input: 'Life is strange'
Output: '5'
```
# Solutions

## 1: Punctuation space

<details>
<summary>Show code:</summary>

```python
para = input()
length = len(para)

last_word = para[0]
punctuation = '.,!?'
i = 1
while i < length:
  last_word += para[i]

  if para[i - 1] in punctuation and para[i] != ' ':
    print("Incorrect: %s" % last_word)
    break
  
  if para[i] == ' ':
      last_word = ''

  i += 1
else:
  print("Correct")
```

</details>

## 2: Taxes for any income

<details>
<summary>Show code:</summary>

```python
annual_income = float(input())

STD_DEDUCTION = 6350

taxable_income = annual_income - STD_DEDUCTION

total_tax = 0.0
if taxable_income > 0:
  total_tax += min(taxable_income, 9325) * 0.1
if taxable_income > 9325:
  total_tax += min(taxable_income - 9325, 37950 - 9325) * 0.15
if taxable_income > 37950:
  total_tax += min(taxable_income - 37950, 91900 - 37950) * 0.25
if taxable_income > 91900:
  total_tax += min(taxable_income - 91900, 191650 - 91900) * 0.28
if taxable_income > 191650:
  total_tax += min(taxable_income - 191650, 416700 - 191650) * 0.33
if taxable_income > 416700:
  total_tax += min(taxable_income - 416700, 418400 - 416700) * 0.35
if taxable_income > 418400:
  total_tax += (taxable_income - 418400) * 0.396

print(total_tax)
```

</details>

## 3: Is Number a prime?

<details>
<summary>Show code:</summary>

```python
number = int(input())
divisor = 2
while divisor * divisor <= number:
  if not number % divisor:
    print("No")
    break
  divisor += 1
else:
  print("Yes")
```

</details>

## 4: Sum of digits (again)

<details>
<summary>Show code:</summary>

```python
number = input()
length = len(number)
sum_digits = 0
i = 0
while i < length:
  sum += int(number[i])
  i += 1

print(sum_digits)
```

</details>

## 5: Find largest

<details>
<summary>Show code:</summary>

```python
i = 0
max_num = -9999999999999
while i < 10:
  number = int(input())
  if number == 0:
    break
    
  if number > max_num:
    max_num = number
    
  i += 1
  
print(max_num)
```

</details>

## 6: Parenthesis

<details>
<summary>Show code:</summary>

```python
expr = input()
length = len(expr)
i = 0
paren_count = 0
while i < length:
  if expr[i] == '(':
    paren_count += 1
  elif expr[i] == ')':
    paren_count -= 1
    
  if paren_count < 0:
    print("No")
    break
  
  i += 1

if paren_count == 0:
  print("Yes")
elif paren_count > 0:
  print("No")
```

</details>

## 7: Reversal

<details>
<summary>Show code:</summary>

```python
word = input()
length = len(word)
reverse_word = ""
i = 1 
while i <= length:
  reverse_word += word[-i]
  i += 1

print(reverse_word)
```

</details>

## 8: Star triangle

<details>
<summary>Show code:</summary>

```python
num = int(input())
i = 0
while i < num:
  line = "* " * i + "*"
  print(line)
  i += 1
```

</details>


## 9: Count vowels

<details>
<summary>Show code:</summary>

```python
sentence = input()
sentence_length = len(sentence)
i = 0
count = 0
while i < sentence_length:
  if sentence[i] in 'aAeEiIoOuU':
    count += 1
  i += 1

print(count)
```

</details>
