# Assignments

This is the set of assignments for the lecture modules. You can implement the solutions on your local machine in an IDE (like PyCharm). For some cases, there are no exact test cases to check correctness; in those cases some strategy to check correctness will be described.

## Problem 1
Monte Carlo algorithms are a set of algorithms that use some form of randomization to calculate the answer to the question. These algorithms don't always find the best possible solution, but with large sample set, it's result can be quite close to the real answer.

In this problem, we are going to use a monte carlo method to estimate the value of mathematical constant `pi`. Remember that the area of a circle with radius `r` is `pi * r * r`.

![Diagram](https://raw.githubusercontent.com/amangup/coding-bootcamp/master/lecture7/pi.gif)

The above diagram shows a circle drawn such that it's radius is 1.0 units. There is also a square in that diagram, whose side is 2.0 units. For the circle in the diagram, the area is `pi * 1.0 * 1.0 = pi`. For the square in the diagram, the area is `2.0 * 2.0 = 4.0`.

Let's say you generate one random point whose x coordinate lies in `(-1.0, 1.0)`, and the y coordinate also lies in `(-1.0, 1.0)`. This random point will always be inside the square. Some of those points will also be inside the circle. How do we figure out if the point is inside the circle? We can use the fact that the distance of the point `(x, y)` from the center `(0, 0)` is `x^2 + y^2`. Considering the radius of our circle is `1.0`, the point is inside the circle if `x^2 + y^2 < 1.0`.

Write a function `monte_carlo_pi(n)` which generates n random points as described above, where `n` is a reasonably large number. All points are inside the square, so the number of those points can be assumed to be the area of the square (`= 4.0`). Many of the points will be inside the circle, the number of such points can be assumed to be the area of the circle (`= pi`). Thus the ratio of points inside the circle to the total number of points should equal `pi / 4.0`. Use this algorithm to make the function return the estimated value of `pi`.

e.g.

```python
print(monte_carlo_pi(1000000))
3.143512
```

You should try different values of the argument `n` in this function, and notice how accuracy of the value of `pi` increases as `n` increases.

## Problem 2
When we discussed sorting algorithms, we learnt that insertion sort algorithm has `O(n^2)` time complexity whereas the best algorithms (as Python's internal sorting algorithm) has the time complexity of `O(n * log n)`. In this exercise, we are going to test if that makes a difference in actual running time.

We are going to compare the running time of `insertion_sort()` as written in lecture 6, and Python's internal sorting algorithm.

- To calculate the running time of an algorithm, use the function `process_time()` in the module `time`.
- To be able to note the difference between running times, we need a large list to sort. Use random number generation (and generate numbers between 0 and 100) to create a list which is arbitrarily long.

Write a function `compare_sort_times(n)`, where n is the size of the list which you generate, and print the time it takes to sort using the insertion sort algorithm and the time it takes using Python's internal sorting algorithm.

e.g.

```python
compare_sort_times(50000)
```
Output is:

```
Python's sort time in milliseconds: 15.625
Insertion sort time in milliseconds: 33750.0
```
 
## Problem 3
A watch dial maker uses an automatic laser engraving machine to mark the hour markers on the dial. The machine assumes that the dial is present on the Cartesian plane, with its center at coordinates (0, 0). It needs to know the exact coordinates of the twelve hour marking points to do the engraving.

The dial maker makes different dials with different radii. Write a function `hour_marker_coords(distance)`, where `distance` is the distance between the center and the hour marker, that returns the list of coordinates (as tuples) for the tweleve hour markers, starting from the 12 o clock marker and working clockwise from there.

![Diagram](https://raw.githubusercontent.com/amangup/coding-bootcamp/master/lecture7/sides_of_right_triangle.gif)

The diagram above shows how you can calculate the coordinates given the radius and angle.

You will need to use the `math` module to solve this problem.

e.g.

```python
print (hour_marker_coords(2.0))
[(0.0, 2.0), (0.9999999999999999, 1.7320508075688774), (1.7320508075688772, 1.0000000000000002), (2.0, 1.2246467991473532e-16), (1.7320508075688774, -0.9999999999999996), (0.9999999999999999, -1.7320508075688774), (2.4492935982947064e-16, -2.0), (-0.9999999999999994, -1.7320508075688776), (-1.732050807568877, -1.0000000000000009), (-2.0, -3.6739403974420594e-16), (-1.7320508075688772, 1.0000000000000002), (-1.0000000000000009, 1.7320508075688767)]
```

Note that due to floating point representation's inaccuracy, numbers like `1.0` can sometimes be represented as `0.9999999999999999`.

## Problem 4
You are writing a scheduling assistant which automatically schedules a meeting at the next available slot. You are given the length of meeting to schedule, and a list of already reserved time slots, and you are to return the time at which the assistant schedules the meeting.

The assistant should select the first available time slot, such that:
- earliest scheduled time is _tomorrow_, in the morning at 9 am,
- the time slot doesn't overlap with any already reserved time slot

Write a function `schedule_meeting(length_in_mins, reserved_slots)`, where `reserved_slots` is a list of tuples containing the start time of that slot in the format like `2018-05-30 13:30`, and its length in minutes.

It's obvious that you will need to use the `datetime` module for this problem. Take your time on this one as this will probably take more effort than you might think.

e.g.

```python
print(schedule_meeting(120, [('2018-06-02 08:00', 120),
                             ('2018-06-02 11:00', 60)]))
```

Output is:
```
2018-06-02 12:00
```

e.g. 2

```python
print(schedule_meeting(60, [('2018-06-02 09:00', 30),
                             ('2018-06-02 11:00', 60)]))
```

Output is:
```
2018-06-02 09:30
```                             
                             

## Problem 5
You have to implement a file garbage collection mechanism. There are some directories which are used as temporary directories inside which the operating system stores files which are not important for future. This mechanism keeps a check on the number of files in such a directory. If the number of files increase beyond a threshold, it deletes the oldest files so that the number of files remains in control. 

Write a function `garbage_collection(directory, k)` that takes as input the path of a directory, and the number `k` which is the maximum number of files to keep. You have to make sure that you only keep the latest `k` files _undeleted_. Use an infinite `while` loop to make sure program never exits, and after every hour, check for the current status of files in a directory, and keep only the latest `k` files.

- You need to use the `glob` module to get the list of files, and `os` module to get the last modified timestamp (using `os.path.getmtime()` function) and `os.remove()` function to delete any file.
- Use the `sleep()` function in the `time` module to wait for one hour between runs.

**To Test:**
Change the interval to one minute, and create files manually using a text editor. As you create more files, the older files should be deleted by your program.

