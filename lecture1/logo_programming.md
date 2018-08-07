# Logo Programming language

[Logo](https://en.wikipedia.org/wiki/Logo_(programming_language)) is a programmming language that was designed for educational reasons. In my view, it's one of the cutest and fun ways to get introduced to programming.

In the logo programming language, you instruct a _turtle_ to move around on the screen, while it draws a line underneath as it moves. This allows you to draw any shape and pattern that you like, using programming! It's not just a toy language -  it has many features available in otherwise serious and popular programming languages.

This page has some very simple programs to get you familiar with Logo. To learn more, I highly recommend [reading this tutorial](http://abz.inf.ethz.ch/wp-content/uploads/unterrichtsmaterialien/primarschulen/logo_heft_en.pdf).

We also need an _interpreter_, where we can write our programs and see the output. The website [http://www.calormen.com/jslogo/](http://www.calormen.com/jslogo/) allows you to do that.

## Simple programs

At any point, to clear the screen, you can use the following command:

```
clearscreen
```

You can also show or hide the turtle pointer using the following commands:

```
hideturtle
showturtle
```

### Letter T

![Letter T](https://github.com/amangup/coding-bootcamp/blob/master/lecture1/images/letter_T.png)

```
forward 200
right 90
forward 100
back 200
```

- `forward` is used to move forward, `back` is used to move backward, and `right` is used to turn the turtle clockwise.


### An arrow

![An arrow](https://github.com/amangup/coding-bootcamp/blob/master/lecture1/images/arrow.png)


```
forward 200
left 135
forward 50
back 50
left 90
forward 50
```

### A Triangle

![Triangle](https://github.com/amangup/coding-bootcamp/blob/master/lecture1/images/Triangle.png)


```
left 30
forward 200
left 120
forward 200
left 120
forward 200
```

- We are repeating the same commands multiple times for the triangle. I wonder if we can do something about that and save some typing effort...

### A hexagon

![Hexagon](https://github.com/amangup/coding-bootcamp/blob/master/lecture1/images/hexagon.png)

```
repeat 6 [forward 100 right 60]
```

- You can repeat the same command multiple times by using the instruction `repeat <number of times> [command]`

### A Circle

![Circle](https://github.com/amangup/coding-bootcamp/blob/master/lecture1/images/circle.png)

```
repeat 360 [forward 1 right 1]
```

- As you can see, the creation of circle is just an extension of the creation of a hexagon.

- What is the radius of this circle? (remember `2 x pi x radius = circumference`)

### A circle inside a square

![Square and Circle](https://github.com/amangup/coding-bootcamp/blob/master/lecture1/images/square_circle.png)

```
repeat 4 [forward 200 right 90]
penup
forward 150
right 90
forward 100
pendown
repeat 360 [forward 314/360 right 1]
```

- `penup` command stops the turtle from drawing anything when you just want to move the turtle. `pendown` brings the drawing back.
- The command for drawing a circle was created to draw a circle of radius = 50.

### A Blue star

![A Blue Star](https://github.com/amangup/coding-bootcamp/blob/master/lecture1/images/blue_star.png)

```
setpencolor 1
repeat 5 [right 15 forward 100 right 150 forward 100 left 93]
```

- `setpencolor` sets the color of the line you are drawing. The commands accepts a color number - and I checked that 0 is for black, 1 for blue, 2 for green and 4 for red. Experiment yourselves with other colors!

That's the end of samples.

## Exercises

Here are a couple of exercises, which you can use to practice further

### Olympic rings

![Olympic Rings](https://github.com/amangup/coding-bootcamp/blob/master/lecture1/images/olympic_rings.png)

### Deathly Hallows from Harry Potter

![Deathly Hallows](https://github.com/amangup/coding-bootcamp/blob/master/lecture1/images/deathly_hallows.png)
