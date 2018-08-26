# -*- coding: utf-8 -*-

__author__  = 'rovo98'
__date__ = '2018.3.22'


# Do slice for list.

L = ['mshinoda', 'Sarah', 'John', 'Tom']

print('前三个元素:')
print(L[0:3])
print(L[:3])

L1 = list(range(100))
print('前十个:')
print(L1[:10])
print('后十个:')
print(L1[-10:])
print('第十个到20个:')
print(L1[10:20])

print('ABCDEF'[:3])


# A demo for slice exercise.
def trim(s):
    """
    Return the substring of s without emtpy space
    :param s: the string to be operated.
    :return: the substring s without empty space
    """
    # remove the empty space from the left.
    n = 1
    while s[n-1:n] == ' ':
        n = n + 1
    s = s[n-1:]

    # remove the empty space from the right side.
    n = 1
    while ' ' in s[-n:]:
        s = s[:-n]
    return s

# Driver the program to test the function above.
if __name__ == '__main__':
    print(trim('   hello, world!    '))