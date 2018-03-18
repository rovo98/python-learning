#coding=utf-8
import socket
import sys

server = '127.0.0.1'  # 默认服务器ip
try:
    server = sys.argv[1]    #如有输入服务器ip
except:
    pass


localIP = socket.gethostbyname(socket.gethostname())
print('群聊客户端已经启动 本机IP：', localIP)

name = input('请输入你的聊天昵称:')
name = '(' + name + ')'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #TCP
s.connect((server, 5000))

while True:
    data = input('输入内容:')
    if data != '':
        s.send((name+data).encode('utf-8'))