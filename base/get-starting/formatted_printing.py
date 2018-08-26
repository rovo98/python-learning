# -*- coding: utf-8 -*-
# author: rovo98
# date: 2018.3.19

# formatted print using '%'

print('Hello, %s', 'world')
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# %s is always works

print('Age: %s. Gender: %s' % (25, True))

print('growth rate: %d %%' % 7)

# formatted print using format() method.

print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))


# A demo

s1 = 72
s2 = 85
r = (85 - 72) / 72 * 100
print('Improved rate: %2.1f' % r)
print('Improved rage: {0:2.1f}'.format(r))
