# coding=utf-8
import socket, sys
from threading import *

MAX_BYTES = 65535

# 接受信息的函数
def handleMessage(clientSock):
    try:
        while True:
            data = clientSock.recv(MAX_BYTES)       #收到的信息
            info = data.decode('utf-8')             #将收到的bytes按utf-8解码
            if info != '':
                ip = clientSock.getpeername()[0]    #获取发送方的ip
                data = str(ip) + ':' + info  # 将发送方发送的信息处理
                data = data.encode('utf-8')  # 以utf-8的方式编码成bytes
                for client in links:                #将信息发送给其他的所有客户端
                    try:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        sock.sendto(data, (str(client), 4900))
                    except Exception as e:          #移除不响应的客户端
                        links.remove(client)
    except Exception as e:
        print('线程出错:', e)


# Driver the program to test the method above.
if __name__ == "__main__":
    try:
        links = [ ]
        localIP = socket.gethostbyname(socket.gethostname()) #获取本地的ip
        print('聊天服务器已经启动 本服务器IP: ', localIP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
        s.bind(('', 5000))
        s.listen(5)
        print('等待连接...')
        while True:
            clientSock, clientAddress = s.accept()          #获取客户端连接
            if clientAddress[0] not in links:               #将还未在连接表的客户端连接加入表中
                links.append(clientAddress[0])
                print('新连接，连接IP为:', clientAddress[0])
            t = Thread(target=handleMessage, args=[clientSock]) #以线程处理客户端连接
            t.setDaemon(1)
            t.start()
    except Exception as e:
        print('server 错误: ', e)