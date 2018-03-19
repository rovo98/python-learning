# -*- coding: utf-8 -*-
# author: rovo98
# date: 2018.3.19

# this is a demo using dict and set

d = {'mshinoda':'mike mshinoda', 'chester':'chester benington'}

if 'Thoma' in d:
    print(d['Thoma'])
else :
    print('Thoma is not in dict')

print(d.get('Thoma', -1))

for sName, fullName in d.items():
    print('%s, his full name is %s.' % (sName, fullName))


s = {1, 2, 3, 4, 2, 1}
print(s)
s.add(10)
s.remove(2)
print('The new set:', s)
