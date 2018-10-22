# Data analysis

We have learnt enough programming and Python to apply what've we understood to analyzing some real world data.

This is a both a tutorial and an exercise. First, we will learn how to read data from files. Then, we will understand that data that we are looking at in this tutorial (data from CA public school system), and pose some questions which we will answer using the data. This tutorial will show you how to answer a few of those questions and the rest will be left as an exercise.

Let's start!

## Reading a text file
- It is common to read data from a file on a disk and then operate on it.
- A lot of files are stored in a **text** format, which essentially means that they are human readable. There are also many formats in which the data can be stored in a non-human-readable form - those files are said to have been stored in **binary** format. Image files are an example of data stored in binary format.
- Reading a file from disk is an _input_ operation. The program is contacting the _outside world_ when it is reading a file.
- Python has a built-in function called `open()` that is typically used to read a file. It returns a _file object_ which has methods to read data from the file.
- Python also has a `with` statement which makes it convenient to read files (to be more specific: file objects need to be _closed_ due to [various reasons](https://stackoverflow.com/questions/25070854/why-should-i-close-files-in-python). `with` statement automatically closes the file for you.)

In the following example, we open a file, read its content line by line, and count how many characters are present in each line.

Let's say the file content is this, and we name the file `quotes.txt`.

```text
Be yourself; everyone else is already taken.
You know you're in love when you can't fall asleep because reality is finally better than your dreams.
Be the change that you wish to see in the world.
No one can make you feel inferior without your consent.
If you tell the truth, you don't have to remember anything.
```

Here is the code:

```python
with open("quotes.txt") as quotes_file:
    for i, line in enumerate(quotes_file):
        print ("Line %s has %s characters" % (i + 1, len(line)))
```

You can see that the object `quotes_file` can be treated as a list (it is of type `iterable`) where each element of the list is a string containing a line from the file. The list has all the lines in order in which they appear in the file. 

The output is:
```
Line 1 has 45 characters
Line 2 has 103 characters
Line 3 has 49 characters
Line 4 has 56 characters
Line 5 has 60 characters
```

This is all we need to understand about reading a file to get started with data analysis.

## The data
We are going to look at some data from the California Public School System. Specifically, it is the demographic information of all the students and staff in CA public schools for the school year 2016-17.

There are two files. These files have not been reformatted in any way - their contents are exactly as they are available online.

1. `ca_student_data_2016.csv` - This contains the data for all students. The data format is [described here](https://www.cde.ca.gov/ds/sd/sd/fsenr.asp).

2. `ca_teacher_data_2016.csv` - This contains the data for all staff. The data format is [described here](https://www.cde.ca.gov/ds/sd/df/fsstaffdemo15.asp).

The questions we are looking to answer are:

1. How many teachers are there in California?
2. How many students are there in California?
3. How much percent of the teachers are female in California?
4. What is the minimum, median and maximum age of a teacher in every County?
5. Create a histogram that shows the number of teachers with every education level.
6. Create a histogram that shows the male to female ratio of teachers with years of teaching experience. For example, can we find out if there is a close to even ratio between male to female teachers among new teachers, but much more skewed towards female teachers among teachers with experience?
7. Sort the counties by their teacher to student in K-12 grades, with the county that has the highest teacher to student ratio appearing first.
8. Create a histogram that shows the number of students in each grade from K to 12.
9. Create a histogram that shows female to male ratio of students in each grade from K to 12.

## Reading the data files
The data files are structured like a table - every row has many columns of data.
- The first row has headers which explain what the column contains.
- Every row is separated by a `TAB` character
- Not all values are "sanitized". For example, in the staff data, County names have a bunch of extra spaces at the end - and we will have to remove those. These kinds of issues are not unusual in data files, and we have to take care of them ourselves.

We would want to read the file to get a list of _records_, where each record is data from one row. The data in each row will be represented as a dictionary, so that we can access any column in the row by its column name. E.g., we want to access the age in any one record as `record['Age']`. Thus, when we read a file, we want to create a **list of dictionaries**.

Keeping all this in mind, here is the function which reads a file:

```python
def get_records(filename, seperator="\t"):
    records = []

    with open(filename) as data_file:
        for i, line in enumerate(data_file):
            row = line.split(seperator)
            if i == 0:
                column_names = row
            else:
                column_values = row
                items = zip(column_names, column_values)
                records.append(dict(items))

    return records
```

Let's go over what is happening in this function:
- We are going through the file line by line, and using `enumerate()` to get the row numbers while we iterating.
- When we are on the very first row, we know that row contains the names of the columns in the data. We store the contents of that row and keep it for future in the variable `column_names`.
- For every other row, the contents of the row are the values corresponding to the column names. Our goal is to create a dictionary where the keys are the column names, and the values are the contents of that specific row.
- To create the dictionary, we _zip_ the keys and values to create a sequence (iterable) of tuples of the type `(key1, value1), (key2, value2), ...`
- If we convert this _typecast_ this sequence to the _dict_ type, we get the dictionary that we want.


## Answering the first question: Number of teachers

Before we delve into the code, let's figure out what we need to do get to the answer.
- Every row in the data contains information about a staff member.
- To know if the staff member is a teacher or not, we need to look at the column titled **FTE Teaching**. This column tells us if this staff member works as a teacher. If the value of this column > 0, then this staff member is a part time or a full time teacher.
- To solve the problem: We count the number of records which have the value of column **FTE Teaching** > 0.

Here is the code that does that:

```python
staff_records = get_records("ca_staff_data_2016.csv")
num_teachers = 0
for record in staff_records:
    is_teacher = float(record["FTE Teaching"]) > 0
    if is_teacher:
        num_teachers += 1
        
print("Number of teachers: %s" % num_teachers)
```

Since we are looking at teacher records, why not look at another question about teachers.

## Answering the third question: Percent of female teachers
This should be easy once we've understood how we solved the previous problem.

- We need to find the gender of a teacher. There is a column called **GenderCode** which we can use.
- Count the number of female teachers, and then divide by the total number of teachers to get the percent of female teachers

We modify the code for the previous answer to solve this:
```python
staff_records = get_records("ca_staff_data_2016.csv")
num_teachers = 0
num_female_teachers = 0
for record in staff_records:
    is_teacher = float(record["FTE Teaching"]) > 0
    gender = record["GenderCode"]
    if is_teacher:
        num_teachers += 1
        if gender == "F":
            num_female_teachers += 1
        
print("California has %.2f percent female teachers" %
      ((num_female_teachers / num_teachers) * 100))
```

Let's look at the student records now.

## Answering the second question: Number of students
The student records are organized a bit differently. Each row in this file doesn't just contain information about any  one student, but a group of students all of whom satisfy the same criteria (belong to the same district, go to the same school, are of the same gender, and so on)

To find the total number of students:
- In every row, the column **ENR_TOTAL** contains the count of total enrolled students for that category of students. We just need to sum this column over all rows to get our answer.

This should be simple:

```python
student_records = get_records("ca_student_data_2016.csv")
num_students = 0
for record in student_records:
    num_students += int(record["ENR_TOTAL"])
    
print("Number of students: %s" % num_students)
```

Let's go back to the staff data file, and answer a more complex question.

## Answering the fourth question: Age statistics of teachers
Let's consider the SAN FRANCISCO county. There must be thousands of teachers in this county (this data says there are 3672). We want to know how old is the youngest teacher among them, how old is the oldest teacher among them, and what is the [median](https://simple.wikipedia.org/wiki/Median) age. And we need to get this data for each County.

Let's divide this problem into two parts:
1. Get the ages of all teachers in each County.
- From the description of the problem statement, it looks like we need a map from County Name to the _list of ages_ for all teachers.
- To get the County Name, there is a header title called **CountyName**.
- To get the age, there is a header title called **Age**.

Let's create this map:

```python
staff_records = get_records("ca_staff_data_2016.csv")
county_ages = {}
for record in staff_records:
    is_teacher = float(record["FTE Teaching"]) > 0
    if is_teacher:
        county = record["CountyName"].strip()
        age = int(record["Age"])

        ages_list = county_ages.get(county, [])
        ages_list.append(age)
        county_ages[county] = ages_list            
```

The first few lines of this code are similar to what we did previously. The crucial part is this:

```python
ages_list = county_ages.get(county, [])
ages_list.append(age)
county_ages[county] = ages_list            
```

- In every iteration, we need to append the age of the current teacher in the list of ages associated with the current teacher's county.
- In the first line of this segment, we get that list from the `county_ages` dictionary. If that list is not in the dictionary, we create a new list (look at the [description of the `get()` function here](https://docs.python.org/3.6/library/stdtypes.html#dict.get)).
- We then append the age of the current teacher to that list, and then put that list back into the dictionary.

The key value pairs in the `county_ages` dictionary look like this:

```
'ALPINE': [46, 35, 35, 52, 71, 53, 53, 51, 57, 33, 62, 57]
```

I checked - all of Alpine County is a protected forest and there is only one school there!

2. For each County, find the min, median and max ages.

- To find the median age, we need to sort the list of ages, and then pick the middle element in the list.
- Once the list is sorted, the first value in the list is the minimum, and the last value in the list is the maximum.
- Since the statistics are also defined _per County_, we need to create another dictionary which maps County Name to the age statistics.

```python
county_age_stats = {}
for key, value in county_ages.items():
    value.sort()
    county_age_stats[key] = (value[0], value[int(len(value) / 2)],
                             value[-1])

import pprint
print("Teacher age statistics in every county (min, median, max):")
pprint.pprint(county_age_stats)
```

We are using the pprint _module_ which is short for "pretty print". That prints the content of the dictionary `county_age_stats` nicely.

## Rest are exercises

- The rest of the questions are left as an exercise. They all use similar concepts as the ones we've used in the four questions above.
- Once you are familiar with analyzing this data yourself, you should generate your own questions. Curiosity is a good trait for data analysts! Try to learn more about the status of California schools.


