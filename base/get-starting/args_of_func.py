# -*- coding: utf-8 -*-
# author: rovo98
# date: 2018.3.19

# position arguments

def position_power(x):
    return x * x


# default arguments

def default_power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# var args

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum


# keyword args

def person(name, age, **kw):
    print('name:', name, 'age', age, 'other:', kw)


# named fixed keyword args

def fixed_person(name, age, *, job, city):
    print('name:', name, 'age:', age, 'job', job, 'city', city)


# A demo
def product(x, *args):
    s = x
    for n in args:
        s = s * n
    return s

# Driver the program to test the functions above.
if __name__ == "__main__":
    # default and position args.
    print(position_power(2))
    print(default_power(2, 3))

    # var args
    l = [1, 3, 4, 5]
    print(calc(*l))
    extra = {'hobbits': 'basketball, game', 'etc': '...'}
    person('john', 11, **extra)
    fixed_person('john', 11, job='null', city='null')

    # product function test.
    print('product(5) = ', product(5))
    print('product(5, 6) = ', product(5, 6))
    print('product(5, 6, 7) =', product(5, 6, 7))
