# Conditionals

- The main feature of conditional code is to run special code when a _condition_ is met.
- It is also called branching.
- It is one of the most common mechanisms in programming and practically all programming languages support this mechanism (with their own syntax)

Let's look at some examples how conditional code could be useful in real programs.

![Lock screen](https://raw.githubusercontent.com/amangup/coding-bootcamp/master/lecture3/phone_unlock.jpg)

A phone gets unlocked only if the code is correct, not otherwise.

![Google France](https://raw.githubusercontent.com/amangup/coding-bootcamp/master/lecture3/google-france.png)

If you type google.com in your browser while you are in france, Google will show you the Google homepage in french.

![Tetris](https://raw.githubusercontent.com/amangup/coding-bootcamp/master/lecture3/tetris.jpg)

In a video game, your score depends on your actions.

## Writing conditional code
- The _condition_ in the conditional code can be any boolean variable, constant or an expression that evaluates to a boolean value.
   - This is the reason why comparison operators are so frequently used in coding.
   
Here is an example of the `if` condition.

```python
unlock_code = 2348
code_entered = 1234

if code_entered == unlock_code:
    # If block starts

    print ("Welcome!")
    print ("If you are a thief and just guessed the right code, log out!")

    # if block ends

print ("This gets printed irrespective.")
```

Some elements to consider:
- The indentation. 
  - Python uses that to know if you're inside an if block. 
  - Indentation is used many, _many_ times in Python.
  - You can use spaces, or use the tab character. It is recommended that you use spaces. Most editors can be changed to add 4 spaces when you press the tab key. The good ones have this setting as default.
  - I can't overestimate the importance of getting indentation right in Python.

- The colon.
  - Tells python to expect an indented block after that line.
  - Without the colon, python will raise an error.
  - If you start an if statement (with the colon), and don't put an indented block after it, then the python will raise an error too.


There is a way to visualize conditional code with a **flow diagram** as shown below:

![If flow diagram](https://raw.githubusercontent.com/amangup/coding-bootcamp/master/lecture3/if_diagram.jpg)


### Else clause
- If you want to run one segment of code only if the condition is true, and another segment of code _only if the condition is false_, then we use the `else` condition.

Let's update the example we used above with an `else` clause.

```python
unlock_code = 2348
code_entered = 1234

if code_entered == unlock_code:
    # If block starts
    print ("Welcome!")
    print ("If you are a thief and just guessed the right code, log out!")

    # if block ends
else:
    # else block starts    
    print ("Try again")
    
    # else block ends

print ("This still gets printed irrespective.")
```

- Note that the `else` keyword is not indented. It is on the same _level_ as the `if` keyword. This is important to be aware of. If `if` and `else` do not have the same level of indentation, python will not be able to match them up.

The flow diagram can also be updated as shown below:

![If-else flow diagram](https://raw.githubusercontent.com/amangup/coding-bootcamp/master/lecture3/if-else_diagram.jpg)

### Elif keyword
- `elif` is a short form for `else if`.
- It allows you to check multiple conditions and execute the right code if only one condition can be true.
- It is there for convenience, and helps keep the code looking organized.

Let's take an example where we input a number and print it out as a word. First, let's try to implement it without `elif`.
```python
input_num = 3

if input_num == 1:
    print ("One")
else:
    if input_num == 2:
        print ("Two")
    else:
        if input_num == 3:
            print ("Three")
        else:
            if input_num == 4:
                print ("Four")
```

And we could carry on like this.

Let's see how the same code looks like if we use `elif`.                

```python
input_num = 3

if input_num == 1:
    print ("One")
elif input_num == 2:
    print ("Two")
elif input_num == 3:
    print ("Three")
elif input_num == 4:
    print ("Four")
```

It's obvious that the second listing of code is shorter and easier to read.

## Practice exercises
- Input two integers, `a` and `b`, and check if `a` is divisible by `b`
- Given the 3 letter name of the month, print the number of days in that month. (Assume it's not a leap year).

# Looping
- Looping mechanism allows us to run the same segment of code again and again.
- Every loop must have an _exit condition_. Otherwise, the code inside the loop will keep getting executed forever.

The movie Groundhog day is a perfect example:

**Spoilers start**

In the movie, Phil is a weatherman, and also a mean guy who only thinks about himself. He goes out of town to report weather, and wakes up every day to the _same_ day, and the same events repeat in the same order (like traveling backward in time). Only he remembers every _run_ of that same day. This is equivalent to running a code in loop - where the same code is running again and again, but something changes in every loop (otherwise what's the point?)

Over the course of the movie, he becomes a better, more helpful, person and in the end gets out of this loop. Him becoming a nicer person is the exit condition in this example.

**Spoilers end**

## Writing looping code
For writing loops in Python, we use the `while` keyword.

Here is an example, which prints the first 10 numbers.

```python
i = 1
while i <= 10:
    # Body of loop starts    
    print (i)
    i += 1
    
    # Body of loop ends
```

- Note that the basic syntax is _identical_ to an `if` condition code, with the keyword `if` replaced by the keyword `while`. 
- The different keyword changes the meaning of the code.

Here is the flow diagram looks like for a while loop.

![loop diagram](https://raw.githubusercontent.com/amangup/coding-bootcamp/master/lecture3/loop_diagram.jpg)

### Infinite Loops

- Normally, every loop must have an exit condition. But there are some scenarios where _infinite_ loops are useful. Here is an example:

```python
while True:
    year = int(input("Enter an year to check if it's a leap year:"))
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        print ("It's a leap year")
    else:
        print ("It's not a leap year")
```

- Most websites are in effect an infinite loop. Whenever user types the address of the website, there is some code waiting to show you the content of the website. It keeps on doing the same thing forever, for every user who requests a web page. 

- Sometimes our code becomes an infinite loop, even if that is not our intention. Here is a funny example of that: [Google Home and Amazon Echo stuck in an infinite loop](https://en.wikipedia.org/wiki/File:Google_Home_vs._Amazon_Echo.webm)

### Break keyword

- `break` keyword allows you to get out of the loop even if the while loop condition is not met.

An example of an infinite loop, which exits once you enter the right answer:

```python
while True:
    answer = input("What is the answer to life, the universe and everything?")
    if answer == "42":
        print ("You got it!")
        break
    
    print ("Medidate, and try again")
    
print ("Congratulations! You have achieved nirvana!")
```

### continue keyword
- `continue` keyword allows you to go back to the starting of the loop body without executing the rest of it.

Here is an example:

```python
while True:
    number = int(input("Enter a number:"))
    if number % 2 == 1:
        print ("You are odd! We don't serve your type here.")
        continue
        
    print ("Your half is %s", int(number / 2))   
```

### while-else clause
- Python supports the use of `else` clause with while statement, similar to how it's used with `if` statement.
- The code inside the `else` block is executed once, whenever the condition in the `while` statement becomes `False`. If the condition is False to begin with, only the code in `else` block will be executed.
- If you break out of a loop, then the `else` code block is _not_ executed.
- Using `continue` doesn't effect the behaviour of while-else.

Here are some examples to show how this works:
```python
i = 0
while i < 2:
    print (i)
    i += 1
else:
    print ("We are done looping.")

Output:
0
1
We are done looping.
```

```python
i = 1
while i < 1:
    print (i)
    i += 1
else:
    print ("We never started looping!")

Output:
We never started looping!
```

```python
i = 0
while i < 5:
    if i % 2 == 1:
        break
    print (i)
    i += 1
else:
    print ("break stole away the attention")
  
Output:
0  
```

# Empty values in boolean expressions
- In Python3, certain values of variables (or expressions or constants) can represent `True` or `False`, even if the variables are not of type `bool`.
- This feature is there to make code writing a bit easier.
- In the following cases, the value is evaluated to `False`:
  - an `int` value is 0
  - a `float` value is 0.0
  - a `string` value is "" (empty string)
  - There are more cases as well (for types we will learn about later)- essentially empty value for a built-in type will always evaluate to `False`.
- If the value doesn't evaluate to `False`, it evaluates to `True`.

```python
money = 0
if money:
    print ("One Modelo for me")
else:
    print ("No money for beer!")

Output:
No money for beer!
```
```python
numerator = 5.0
denominator = 2.0

if denominator:
    print (numerator / denominator)
else:
    print ("Can't divide by 0")
    
Output:
2.5    
```

## Practice exercises
- Update the lock screen example, where you give the user 3 tries, and write "Success!" if the user succeeds within 3 tries, or write "Locked for one hour" if the user fails all 3 tries.
- Calculate this expression upto 10 terms: 1 + 1/2 + 1/4 + 1/8 + 1/16 + 1/32 + ...
