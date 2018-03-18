#coding=utf-8
import socket
import sys

MAX_BYTES = 65535

server = '127.0.0.1'
try:
    server = sys.argv[1]
except:
    pass

print('显示从服务器传来的聊天信息')
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 4900))

while True:
    data, address = sock.recvfrom(MAX_BYTES)
    print(data.decode('utf-8'))