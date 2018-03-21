# -*- coding: utf-8 -*-
# author: rovo98
# date: 2018.3.19

print('包含中的str')
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))

# encoding and decoding
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# ignoring errors
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))