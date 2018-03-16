# !\usr\bin\env python
# -*- coding:utf-8 -*-
import requests
import re

# 获取网页信息
def getHTMLText(url):
  try:
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text
  except:
    return ""
# 解析提取相关信息
def parsePage(ilt, html):
  try:
    plt = re.findall(r'"view_price":"[\d.]*"', html)
    tlt = re.findall(r'"raw_title":".*?"', html)
    for i  in range(len(plt)):
      price = eval(plt[i].split(':')[1])
      title = eval(tlt[i].split(':')[1])
      ilt.append([price, title])
  except:
    print("")

# 打印信息
def printGoodsList(ilt):
  tplt = "{:4}\t{:8}\t{:16}"
  print(tplt.format("序号", "价格", "商品名称"))
  count = 0
  for item in ilt:
    count += 1
    print(tplt.format(count, item[0], item[1]))

# 主函数
def main():
  goods = '书包'
  start_url = 'https://s.taobao.com/search?q='+goods
  depth = 2
  infoList = []
  for i in range(depth):
    try:
      url = start_url + '&s=' + str(44*i)
      html = getHTMLText(url)
      parsePage(infoList, html)
    except:
      continue
  printGoodsList(infoList)

if __name__ == "__main__":
  main()
