# -*- coding: utf-8 -*-
from collections import Iterable

__author__ = 'rovo98'
__date__ = '2018.4.2'


# Iteration in python

# the same way to other language.

list = [1, 2, 3, 4, 5]
for i in range(len(list)):
    print(list[i], end=" ")
print()

# the python way to iterates items in collection
print('the python way:')
for item in list:
    print(item, end=" ")
print()

# how to check whether an object is iterable or not?
print('check if str is iterable or not:')
print(isinstance('abc', Iterable))
print('check if list is iterable or not:')
print(isinstance([1, 2, 3], Iterable))
print('check if integer is iterable or not:')
print(isinstance(123, Iterable))

# add indices for iteration
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)


# A demo for iteration exercise.

def findMinAndMax(L):
    min = L[0]
    max = L[0]
    for item in L:
        if min > item:
            min = item
        if max < item:
            max = item

    return min, max

# Driver the program to test the method above.
if __name__ == "__main__":
    testList = [7, 1, 3, 9, 5]
    print(findMinAndMax(testList))