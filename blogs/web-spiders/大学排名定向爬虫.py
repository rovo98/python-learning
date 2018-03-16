# !\usr\bin\env python
# -*- coding:utf-8 -*-
import requests
import bs4
from bs4 import BeautifulSoup


# 获取相关网页信息
def getHTMLText(url):
  try:
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text
  except:
    return ""  # 爬取失败返回空字符


# 提取网页有效内容
def fillUnivList(uList, html):
  soup = BeautifulSoup(html, "html.parser")
  for tr in soup.find('tbody').children:
    if isinstance(tr, bs4.element.Tag):
      tds = tr('td')
      uList.append([tds[0].string, tds[1].string, tds[3].string])


# 打印信息
def printUnivList(uList, num):
  print("{0:^10}\t{1:{3}^10}\t{2:^10}".format("排名", "学校名称", "总分", chr(12288)))
  for x in range(num):
    u = uList[x]
    print(u[0], u[1], u[2])
    print("{0:^10}\t{1:{3}^10}\t{2:^10}".format(u[0], u[1], u[2], chr(12288)))
    print("Suc" + str(num))


def main():
  uinfo = []
  url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html'
  html = getHTMLText(url)
  fillUnivList(uinfo, html)
  printUnivList(uinfo, 20)  # 20 univ


# Driver the program to test the methods above.
if __name__ == '__main__':
  main()
