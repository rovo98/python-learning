# -*- coding: utf-8 -*-

__author__ = 'rovo98'
__date__ = '2018.4.2'

# Creating list by using List Comprehensions.

list = list(range(1, 11))
print(list)

# naive way to create [1x1, 2x2, ..., 10x10]
L = []
for i in range(1, 11):
    L.append(i * i)
print('list created using naive way:', L)

L1 = [x * x for x in range(1, 11)]
print('list created using list comprehensions:', L1)

# more examples
L2 = [x * x for x in range(1, 11) if x % 2 == 0]
print(L2)

L3 = [m + n for m in 'ABC' for n in 'XYZ']
print(L3)

d = {'x':'A', 'y':'B', 'z':'C'}
L4 = [k + '=' + v for k, v in d.items()]
print(L4)

def toLowerAlpha(L):
    return [s.lower() if isinstance(s, str) else s for s in L]

#Driver the program to test the method above.
if __name__ == '__main__':
    testList = ['Hello', 'World', 18, 'Apple', None]
    print(toLowerAlpha(testList))