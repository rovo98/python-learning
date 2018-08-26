# -*- coding: utf-8 -*-
# author : rovo98
# date: 2018.3.19

# This is a demo of using if statement.

height = 1.75
weight = 80.5

bmi = 80.5 / (1.75 * 1.75)
print('bmi = %.2f' % bmi)
if (bmi < 18.5):
    print('体重过轻')
elif (bmi >= 18.5 and bmi < 25):
    print('体重正常')
elif (bmi >= 25 and bmi < 32):
    print('肥胖')
elif (bmi >= 32) :
    print('严重肥胖')