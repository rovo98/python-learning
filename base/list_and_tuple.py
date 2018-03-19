# -*- coding: utf-8 -*-
# author: rovo98
# date: 2018.3.19

# A demo for list.
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# print 'Apple'
print(L[0][0])
# print 'Python'
print(L[1][1])
# print "Lisa'
print(L[2][2])

for i in range(0, 3):
    print(L[i][i])

# A demo for tuple

t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2].insert(1, 'new')
t[2].pop()
t[2].extend(['hello', 'world'])
print(t)