# Object Oriented Programming

- A **class** provides the _means_ for bundling data and functionality together.
- An **object** represents an instance of that data, and the functionality is (usually) designed to act on the data - either to modify that data, to extract new information from that data, or both.
- The data is stored in variables that are members of the class. The functionality is implemented in methods (which are essentially functions, but inside a class).

Before we start looking at Python syntax for defining classes and creating objects, let's try to understand object using an analogy of a real life object. We will look at a watch, and how that fits into the structure described above.

## A watch as object

** omega moonwatch **

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

## Defining a class

## Creating and using objects

## Inheritance

## Other features of a class definition
