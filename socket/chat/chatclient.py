# -*- coding:utf-8 -*-

__author__ = 'rovo98'
__date__  = '2018.3.19'

import socket
import sys

# the chat client.
import os


class Client:

    def __init__(self):
        """
        constructor of chat client
        :param self.socket: the socket obj
        :param self.server: the ip address of chat server
        :param self.userName: the identifier of this client.
        :param self.otherInfo: the other info of this client.
        :param self.localIP: the ip address of this client.
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # use TCP
        self.server = '127.0.0.1'
        self.localIP = socket.gethostbyname(socket.gethostname())

    def connect_to_server(self, server, port):
        """
        connect to the server.
        :param server: the ip address of target server
        :param port: the port the server binding at
        :return:
        """
        self.socket.connect((server, port))

    def run(self):
        try:
            self.server = sys.argv[1]  # 使用用户提供的服务器ip如果有的话
        except Exception as e:
            print("使用默认服务器ip地址")
        try:
            self.connect_to_server(self.server, 8686)
        except Exception as e:
            print('errors:', e)
            print('连接服务器失败，请确保服务器已经启动。。。')
            os.system(exit(1))

        print('群聊客户端已经启动 本机IP：', self.localIP)
        self.userName = input('请输入你的聊天昵称:')
        name = '(' + self.userName + '):'
        self.socket.send(("{'type':'m','user_info':['" + self.userName+"','"+self.localIP+ "']}").encode('utf-8'))

        while True:
            data = input('输入内容:')
            if data != '':
                self.socket.send(("{'type':'d',  'data':'"+(name + data)+"'}").encode('utf-8'))


# Driver the program to test the chat client.
if __name__ == "__main__":
    client = Client()
    client.run()
