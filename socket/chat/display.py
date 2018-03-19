# -*- coding: utf-8 -*-
# author: rovo98
# date: 2018.3.19

import socket


# the screen to show the message.
class Display:

    def __init__(self):
        """
        constructor of this display
        """
        self.MAX_BYTES = 65535
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp

    def run(self):
        """
        start up the display
        :return:
        """
        print('显示从服务器传来的聊天信息')
        self.sock.bind(('', 4900))  # 绑定在4900端口用户接受服务器传来的信息

        while True:
            data, address = self.sock.recvfrom(self.MAX_BYTES)
            print(data.decode('utf-8'))


# Driver the program to test the class.
if __name__ == "__main__":
    screen = Display()
    screen.run()