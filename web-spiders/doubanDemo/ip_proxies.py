# -*- coding: utf-8 -*-
import random

import requests
from bs4 import BeautifulSoup as bs

__author__ = 'rovo98'


class IPProxy:
    def __init__(self, headers, url='http://www.xicidaili.com/nn/'):
        self.url = url
        self.headers = headers
        self.proxy_list = []
        self.ip_list = []
        self.get_ip_list()

    def get_ip_list(self):
        web_data = requests.get(self.url, headers=self.headers)
        soup = bs(web_data.text, 'lxml')
        ips = soup.find_all('tr')

        for i in range(1, len(ips)):
            ip_info = ips[i]
            tds = ip_info.find_all('td')
            self.ip_list.append(tds[1].text + ':' + tds[2].text)

        for ip in self.ip_list:
            self.proxy_list.append('http://' + ip)

    # return a random proxy ip.
    def get_random_ip(self):
        proxy_ip = random.choice(self.proxy_list)
        proxies = {'http': proxy_ip}
        return proxies


# Driver the program to test the class.
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    print('test')
    proxy_ip = IPProxy(headers=headers)
    print(proxy_ip.get_random_ip())
