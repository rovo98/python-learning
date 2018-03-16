# !\usr\bin\env python
# -*- coding:utf-8 -*-
import requests
import bs4
from bs4 import BeautifulSoup

#获取网页信息
def getHTMLText(url):
  try:
    r = requests.get(url, timeout = 30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text
  except:
    return ""
#提取需要的信息
def fillInfoList(uList, html):
  soup = BeautifulSoup(html, "html.parser")
  i = 0
  for tr in soup.find('tbody').children:
    if i > 3:
      if isinstance(tr, bs4.element.Tag):
        tds = tr('td')
        for i in range(9):
          tds[i].string = tds[i].string.strip()
        uList.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string, tds[4].string,
                      tds[5].string, tds[6].string, tds[7].string, tds[8].string ])
    i += 1
#打印信息
def printInfoList(uList):
  print("{0:^10}\t{1:^5}\t{2:{9}^9}\t{3:{9}^10}\t{4:{9}^10}\t{5:^8}\t{6:^5}\t{7:^5}\t{8:^5}".format(
    "本省排名","全国排名","学校名称","所在地区","类型","总分","科学研究","人才培养","综合声誉",chr(12288)
  ))
  for x in uList:
    print("{0:^10}\t{1:^10}\t{2:{9}^10}\t{3:{9}^10}\t{4:{9}^10}\t{5:^10}\t{6:^10}\t{7:^10}\t{8:^10}".format(
      x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],chr(12288)))
#主函数
def main():
  info = []
  url = 'http://www.gxeduw.com/gaokao/201378350.html'
  html = getHTMLText(url)
  fillInfoList(info, html)
  printInfoList(info)
if __name__ == "__main__":
  main()
