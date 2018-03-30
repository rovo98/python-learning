# -*- coding:utf-8 -*-
# author : rovo98
# date: 2018.3.19


import socket
from threading import *

# The chat server
class Server:
    def __init__(self):
        """
        :param self.MAX_BYTES: the maximum bytes of one message.
        :param self.links:     a list containing ip addresses of all clients.
        :param self.localIP:  the ip address of this server.
        :param self.sock:     the socket obj.
        :return:
        """
        self.MAX_BYTES = 65535
        self.links = {}       # allocate a list to store all client address.
        self.localIP = socket.gethostbyname(socket.gethostname())      # 获取本地的ip
        self.tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
        self.udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # UDP

    # 接受信息的函数
    def process_message(self, client_sock):
        try:
            while True:
                data = client_sock.recv(self.MAX_BYTES)  # 收到的信息
                info = data.decode('utf-8')           # 将收到的bytes按utf-8解码
                info = eval(info)

                if info.get('type') == 'm':
                    user_info = info.get('user_info')
                    user_name = self.links.get(user_info[1], None)
                    if user_name is None:
                        print('新连接地址: %s' % (user_info[1]))
                        self.links[user_info[1]] = user_info[0]
                    else:
                        msg = '客户端' + user_info[1] + '创建了一个新的客户端:' + user_info[0]
                        self.udp_sock.sendto(msg.encode('utf-8'),
                                         (user_info[1], 6666))

                elif info.get('type') == 'd':
                    recv_data = info.get('data')
                    if recv_data != '':
                        ip = client_sock.getpeername()[0]    # 获取发送方的ip
                        data = str(ip) + recv_data     # 将发送方发送的信息处理
                        data = data.encode('utf-8')          # 以utf-8的方式编码成bytes
                        for client in self.links.keys():                # 将信息发送给其他的所有客户端
                            try:
                                self.udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # udp
                                self.udp_sock.sendto(data, (str(client), 6666))
                            except Exception as e:          # 移除不响应的客户端
                                self.links.pop(client)
        except Exception as e:
            print('线程出错:', e)

    # start up the chat server.
    def run(self):
        try:

            print('聊天服务器已经启动 本服务器IP: ', self.localIP)
            self.tcp_sock.bind(('', 8686))
            self.tcp_sock.listen(5)
            print('等待连接...')

            while True:
                clientSock = self.tcp_sock.accept()[0]   # 获取客户端连接
                t = Thread(target=self.process_message, args=[clientSock])  # 以线程处理客户端连接
                t.setDaemon(1)
                t.start()
        except Exception as e:
            print('server 错误: ', e)


# Driver the program to test the method above.
if __name__ == "__main__":
    chatServer = Server()
    chatServer.run()