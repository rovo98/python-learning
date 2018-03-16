# !\usr\bin\env python
# -*- coding:utf-8 -*-
import requests
import re
import datetime

# 获取网页信息
def getHTMLText(url):
  try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url,timeout=30, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text
  except:
    print("获取失败")
    return ""
	
# 提取相关信息
def parsePage(ilt, html):
  try:
    plt = re.findall(r'"sku_price":"[\d.]*"', html)
    nlt = re.findall(r'"sku_name":".*?"', html)
    for i in range(len(plt)):
      price = eval(plt[i].split(':')[1])
      name = (nlt[i].split(':')[1])
      name = name.replace('<font class=\\','')
      name = eval(name)
      ilt.append([price, name])
  except:
    print("提取出现问题")
	
# 打印信息
def printGoodsList(ilt):
  ilt.sort(key=lambda x:x[0])
  tpl = "{:4}\t{:8}\t{:16}"
  print("筛选条件>>>屏幕尺寸：5.5-5.1英寸 运行内存：4GB CPU核数：八核 电池容量：4000mAh-5999mAh 网络：全网通")
  print(tpl.format("序号", "价格", "名称"))
  count = 0
  for item in ilt:
    count += 1
    print(tpl.format(count, item[0], item[1]))
	
# 主函数
def main():
  goods = '安卓手机'
  span = '244_30816@3753_173@2005_75948@3803_90189@2943_77734'
  depth = 2
  infoList = []
  start_url = 'http://gou.jd.com/search?keyword=' + goods
  for page in range(depth):
    try :
      url = start_url  + '&ev=' + span + '&page=' + str(page+1)
      html = getHTMLText(url)
      parsePage(infoList, html)
    except:
      continue
  printGoodsList(infoList)


if __name__ == "__main__":
  start_time = datetime.datetime.now()
  main()
  end_time = datetime.datetime.now()
  interval = (end_time - start_time).seconds
  print('\n完成，用时:'+str(interval)+'秒!')
