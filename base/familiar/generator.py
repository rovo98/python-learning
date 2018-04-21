# -*- coding: utf-8 -*-

__author__ = 'rovo98'
__date__ =  '2018.4.21'



# A simple test for using gerator.

g = (x for x in range(10))

print('A simple test for using generator:')
for item in g:
    print(item, end=' ')
print('\n')


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

def triangles():
    L = [1]
    while True:
        yield L
        L = [L[x] + L[x+1] for x in range(len(L) - 1)]
        L.insert(0, 1)
        L.append(1)


# Driver the program to test the methods above.
if __name__ == '__main__':
    g1 = fib(8)
    print(next(g1), 'and ', next(g1), 'and ', next(g1))
    t = triangles()
    for x in range(10):
        print(next(t))