# !\usr\bin\env python
# -*- coding:utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup
import traceback
import datetime

# 获取网页内容，返回response对象.text
def getHTMLText(url, code='utf-8'):
  try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url, timeout=30, headers=kv)
    r.raise_for_status()
    r.encoding = code
    return r.text
  except:
    print('网页获取失败')
    return ""

# 获取所有的股票信息
def getStockList(lst, stockURL):
  html = getHTMLText(stockURL, 'GB2312')
  soup = BeautifulSoup(html, 'html.parser')
  a = soup.find_all('a')
  for i in a:
    try:
      href = i.attrs['href']
      res = re.findall(r'[s][hz]\d{6}', href)[0]
      lst.append(res)
    except:
      continue
  print('共有'+str(len(lst))+'支股票')
# 获取每一只个股的信息，并写入文本中
def getStockInfo(lst, stockURL, fpath):
  count = 0
  for stock in lst:
    url = stockURL + stock + '.html'
    html = getHTMLText(url)
    try:
      if html == "":
        continue
      soup = BeautifulSoup(html, 'html.parser')
      stockInfo = soup.find('div',attrs={'class':'stock-bets'})
      if stockInfo is None:
        continue
      count += 1
      infoDict = {}
      print("\r正在爬取第{:d}支股!进度：{:.2f}%".format(count,count/len(lst)*100),end="")
      name = stockInfo.find(attrs={'class':'bets-name'})
      infoDict.update({'股票名称':name.text.split()[0]})
      keyList = stockInfo.find_all('dt')
      valueList = stockInfo.find_all('dd')
      for i  in range(len(keyList)):
        key = keyList[i].text
        value = valueList[i].text
        infoDict[key] = value

      with open(fpath, 'a', encoding='utf-8')as f :
        f.write(str(infoDict)+ '\n')
    except:
      traceback.print_exc()

# Driver the program to test the method above.
def main():
  stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
  stock_info_url = 'https://gupiao.baidu.com/stock/'
  output_file = 'E://BaiduStockInfo.txt'
  slist = []
  getStockList(slist, stock_list_url)
  getStockInfo(slist, stock_info_url, output_file)

if __name__ == "__main__":
  start = datetime.datetime.now()
  main()
  end = datetime.datetime.now()
  interval = (end - start).seconds
  print('\n完成,用时'+str(interval)+'秒！')
