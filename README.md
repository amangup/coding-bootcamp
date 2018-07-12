# Coding bootcamp

This is the material that is used for the [free coding bootcamp](https://www.meetup.com/SF-Free-Coding-Bootcamp/) meetup that I run in SF. The material contains a collection of lectures, assignments and occasional quizzes.

This bootcamp **uses Python as the language of choice** to introduce programming. It's a very popular language and is being used more and more frequently for production systems - including webserver frameworks, data analysis and machine learning.

The material is organized by lecture. The Readme inside every lecture directory contains the details about that lecture.

# The Syllabus
This the list of topics we discuss in the lecture series. 
- All lectures after the first one has a set of assignments.
- Some lectures are long and cannot be covered in one bootcamp class. Thus, it takes more classes than the number of lectures to go through them.

The lectures are designed to teach enough Python for one to be able to write meaningful real life applications themselves. The final project is to create a web app which is an online E-book reader. I will also discuss the ways you can use this learning to become a professional programmer in the last lecture.

Currently, the first bootcamp session is not complete, and thus more lectures will be created in the following weeks. I will keep updating this page when new lectures get added.

### Lecture 1 - What is programming?
The first lecture introduces what a computer is, and what programming is. In the class, we also write our first little program.

### Lecture 2 - Variables and Expressions
In this lecture we start learning Python, by understanding what a variable is, and how we can use constants and variables in expressions. We learn about the basic data types built into Python.

### Lecture 3 - If statements and while loops
We look at conditional logic in this lecture. Based on certain criteria, we can execute some code but not other (using `if` statements) or execute the same code numerous times (using `while` statements).

### Lecture 4 - Functions and recursion
The concept of _functions_ is introduced, which is used to modularize the code. We also discuss the topic of recursion using functions, and learn how it can be used to solve some interesting problems.

### Lecture 5 - Collection data types and for loops
We start looking at more advanced datatypes; specifically we learn about types which can store a collection of data. That allows me to also introduce the `for` loop statement, which makes writing loops easier.

As an application of what've learnt till now, we do some data analysis on real life data. We use the data from California Public School system to gain insights about the system (like what is the average student:teacher ratio)

### Lecture 6 - Algorithms
We discuss a computer science topic - Algorithms. We define what an Algorithm is, look at some fundamental algorithms in computer science, and understand what it means for an algorithm to be good by using the measure of Time Complexity.

### Lecture 7 - Python Modules
This is a shorter lecture where we discuss Python _modules_. Modules are useful to package a bunch of code and share it with others. We will learn how to create our own modules and to use Python's built in modules and third party modules.

Assignments to this lecture are some of my favorite.

### Lecture 8 - Object Oriented Programming
We cover the topic of Object Oriented Programming (OOP), and learn how to do write that style of programs in Python. This is a very fundamental concept without which it is practically impossible to work on any real life application.

### Lecture 9 - Internet and the World Wide Web
We take a break from programming and learn how the Internet and the World Wide Web works. It sets us up for the next lectures, which are all about creating web sites using Python.

### Lecture 10 - Web App development using Flask
In this lecture we will learn how to create websites using a popular Python web development framework called Flask. The lecture is a tutorial in which we create a Fortune teller app that shows the user a random _fortune_. 

The assignments make you develop a few more interesting websites, and you'll also learn some very important concepts while doing them (like REST APIs, JSON, etc.)


# Installing Python on your computer

Follow the instructions below to install Python interpreter and PyCharm Integrated Development Environment on your computer.

## Windows
### Installing Python interpreter

1. Download the Python executable installer, which is labeled **Windows x86-64 executable installer** from here: https://www.python.org/downloads/release/python-365/

2. Run the downloaded file (may need privileges).

### Installing PyCharm

1. Download the PyCharm installer from the link here: https://download.jetbrains.com/python/pycharm-community-2018.1.2.exe

2. Run the installer to install PyCharm.

3. After it is installed, you can run PyCharm. It's opening screen will help you create a new project and you can try to write some code and run it. You might be asked to configure the Python intepreter, and you can use the instructions here to do that: https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html

## Mac OS

### Installing Python interpreter

1. Download the Python executable installer, which is labeled **macOS 64-bit installer** from here: https://www.python.org/downloads/release/python-365/

2. Run the downloaded file (may need privileges).

### Installing PyCharm

1. Download the PyCharm installer from the link here: https://download.jetbrains.com/python/pycharm-community-2018.1.2.dmg

2. Run the installer to install PyCharm.

3. After it is installed, you can run PyCharm. It's opening screen will help you create a new project and you can try to write some code and run it. You might be asked to configure the Python intepreter, and you can use the instructions here to do that: https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html

## Ubuntu

### Installing Python interpreter

1. In your terminal, run the following commands:
```bash
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python3.6
```
Enter your password when asked.

2. Run `python3 -V` to verify python is working.

### Installing PyCharm

1. Download the PyCharm archive from the link here: https://download.jetbrains.com/python/pycharm-community-2018.1.2.tar.gz

2. Copy this file to the directory where you want to install PyCharm. Then run `tar xzf pycharm-community-2018.1.2.tar.gz`.

3. Go to the `<pycharm_directory>/bin` and run `./pycharm.sh` to run PyCharm.

4. It's opening screen will help you create a new project and you can try to write some code and run it. You might be asked to configure the Python intepreter, and you can use the instructions here to do that: https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html
