import random

def monte_carlo_pi(n):
    count_in_circle = 0
    for i in range(n):
        x = random.random() * 2.0 - 1.0
        y = random.random() * 2.0 - 1.0
        if (x ** 2 + y ** 2) < 1.0:
            count_in_circle += 1

    return (count_in_circle / n) * 4.0

#print(monte_carlo_pi(100000000))

def insert_sorted(sorted_list, element):
    for i, item in enumerate(sorted_list):
        if element <= item:
            sorted_list.insert(i, element)
            break
    else:
        sorted_list.append(element)

def insertion_sort(unsorted_list):
    sorted_list = []
    for item in unsorted_list:
        insert_sorted(sorted_list, item)
    return sorted_list

import time

def compare_sort_times(n):
    list_to_sort = []
    for i in range(n):
        list_to_sort.append(random.random() * 100.0)

    start1 = time.process_time()
    sorted(list_to_sort)
    end1 = time.process_time()
    print("Python's sort time in milliseconds:", (end1 - start1) * 1000.0)


    start2 = time.process_time()
    insertion_sort(list_to_sort)
    end2 = time.process_time()
    print("Insertion sort time in milliseconds:", (end2 - start2) * 1000.0)


#print(compare_sort_times(50000))

import math

def hour_marker_coords(distance):
    points = []
    for i in range(12):
        theta = i * math.pi / 6
        x = distance * math.sin(theta)
        y = distance * math.cos(theta)
        points.append((x, y))

    return points

#print (hour_marker_coords(2.0))

import datetime


def schedule_meeting(length_in_mins, reserved_slots):
    earliest_start = datetime.datetime.now()
    earliest_start = earliest_start.replace(day=earliest_start.day + 1, hour=9,
                                            minute=0, second=0, microsecond=0)
    earliest_start = earliest_start.timestamp()

    reserved_timestamps = []
    for slot, length in reserved_slots:
        start_timestamp = datetime.datetime.strptime(slot, "%Y-%m-%d %H:%M").timestamp()
        end_timestamp = start_timestamp + length * 60
        if start_timestamp < earliest_start:
            earliest_start = max(earliest_start, end_timestamp)
            continue

        reserved_timestamps.append((start_timestamp, end_timestamp))

    reserved_timestamps.append((earliest_start, earliest_start))
    reserved_timestamps.sort()

    length_in_secs = length_in_mins * 60
    for i in range(len(reserved_timestamps) - 1):
        slot = reserved_timestamps[i]
        potential_start = slot[1]
        potential_end = potential_start + length_in_secs
        if potential_end <= reserved_timestamps[i + 1][0]:
            # Hurrah! We found a time slot
            break
    else:
        # our new slot's start time will be at the end of last reserved time slot
        slot = reserved_timestamps[-1]
        potential_start = slot[1]

    return datetime.datetime.strftime(
        datetime.datetime.fromtimestamp(potential_start), "%Y-%m-%d %H:%M")


print(schedule_meeting(60, [('2018-06-02 09:00', 30),
                            ('2018-06-02 11:00', 60)]))









