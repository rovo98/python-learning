# -*- coding: utf-8 -*-

__author__ = 'rovo98'
__date__ = '2018.3.21'


# These are demos for recursion function

# 递归
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


# 尾递归，相当于循环
def fact_improved(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


def hano(n, a, b, c):
    if n == 1:
        print(a, '---->', c)
    else:
        hano(n - 1, a, c, b)  # 将a上n-1个盘子移动到b
        hano(1, a, b, c)  # 将a的最后一个盘子移动到c
        hano(n - 1, b, a, c)  # 将b上的n-1个盘子移动到c


# Driver the program to test the functions above.
if __name__ == '__main__':
    print('fact(10) = ', fact(10))
    print('fact_improved(10) = ', fact_improved(10))
    print('hano tower test:')
    hano(3, 'A', 'B', 'C')
