# -*- coding: utf-8 -*-
# author: rovo98
# date: 2018.3.19

# using a loop to create a list
l = list(range(10))
print(l)

# sum up all num in the range of [0,100]
sum = 0
for x in range(101):
    sum = sum + x
print('SUM : ', sum)

# A loop demo.
L = ['Bart', 'Lisa', 'Adam']

for name in L:
    print('Hello, %s' % name)


# print the odd numbers in the range of [0, 10]
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)