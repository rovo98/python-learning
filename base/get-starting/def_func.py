# -*- coding: utf-8 -*-
# author: rovo98
# date: 2018.3.19

# This is a demo to define a function


import math

# Returns the solution of ax^2 + bx +c = 0
def quadratic(a, b, c):
    delta = b*b - 4 *a*c
    if delta < 0:
        return None
    elif delta == 0:
        return -b / (2*a)
    else:
        x1 = (-b - math.sqrt(delta))  / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        return x1, x2

# Driver the program to test the function above.
if __name__ == "__main__":
    print('quadratic(2, 3, 1) = ', quadratic(2, 3, 1))
    print('quadratic(1, 3, -4) = ', quadratic(1, 3, -4))
