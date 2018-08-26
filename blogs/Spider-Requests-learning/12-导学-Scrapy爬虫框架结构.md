### Scrapy爬虫框架结构

[TOC]

#### 爬虫框架

- 爬虫框架是实现功能的一个软件结构和功能组件集合。
- 爬虫框架是一个半成品，能够帮助用户实现专业网络爬虫。

#### Scrapy爬虫框架 —— “5+2”结构

- ENGINE模块
- SCHEDULER模块
- ITEM PIPELINES模块
- SPIDERS模块
  - 包含MIDDLEWARE模块
- DOWNLOADER模块
  - 包含MIDDLEWARE模块

#### 三条主要数据流

- SPIDERS --> ①(REQUESTS) -- > SCHEDULER

- SCHEDULER -- > ②(REQUESTS) --> ENGINE -- > ③(REQUESTS) --> DOWNLOADER --> ④(RESPONSE) --> ENGINE -->⑤ (RESPONSE) --> SPIDERS

- SPIDERS --> ⑥(ITEMS/REQUESTS) --> ENGINE -->⑦(ITEMS) --> ITEMPIPELINES

  ​                                                                            -->(REQUESTS) --> SCHEDULER

框架入口：SPIDERS, 框架出口：ITEMPIPELINES

这些两个需要用户编写(配置) , 其他的都是已经实现的。

#### Scrapy爬虫框架的解析

##### Engine (框架核心)—— 不需要用户修改

- 控制所有模块之间的数据流
- 根据条件触发事件

##### Scheduler —— 不需要用户修改

- 对所有爬取请求进行调度管理

##### Downloader —— 不需要用户修改

- 根据请求下载网页


- Downloader Middleware (中间件)—— 用户可以配置
  - 目的：实施Engine、Scheduler和Download之间进行用户可配置的控制
  - 功能：修改、丢弃、新增请求或响应

##### Spider —— 用户可配置__用户主要编写这个模块

- 解析Downloader返回的响应(Response)
- 产生爬取项(scraped item)
- 产生额外的爬取请求(Request)
- Spider Middleware (中间件) —— 用户可配置
  - 目的：对请求和爬取项的再处理
  - 功能：修改、丢弃、新增请求或爬取项

##### Item Pipelines —— 用户可配置__完全由用户编写处理

- 以流水线方式处理Spider产生的爬取项。
- 有一组操作顺序组成，类似流水线，每一个操作是一个Item Pipeline类型
- 可能操作包括：清理、检验和查询爬取项中的HTML数据、将数据存储的数据库

#### requests vs. Scrapy

##### 相同点

- 两者都可以进行页面请求和爬取，Python爬虫的两个重要技术路线。
- 两者可用性逗号，文档丰富，入门简单。
- 两者都没有处理js、提交表单、应对验证码等功能(可扩展)。

##### 不同点

|   requests   |    Scrapy     |
| :----------: | :-----------: |
|    页面级爬虫     |     网站级爬虫     |
|     功能库      |      框架       |
| 并发性考虑不足，性能较差 |   并发行好，性能高    |
|   重点在于页面下载   |   重点在于爬虫结构    |
|     定制灵活     | 一般定制灵活，深度定制困难 |
|    上手十分简单    |     入门稍难      |

#### 选用哪个技术路线？

- 非常小的需求，requests库
- 不太小的需求，Scrapy框架


- 定制程度很高的需求(不考虑规模), 自搭框架，requests > Scrapy

#### Scrapy爬虫的常用命令

- Scrapy是为持续运行设计的专业爬虫框架，提供操作的Scrapy命令行。
- Scrapy命令的格式
  - scrapy \<command> \[options] \[args]

##### Scrapy常用命令

|      命令      |     说明     |                    格式                    |
| :----------: | :--------: | :--------------------------------------: |
| startproject |  创建一个新工程   |    scrapy startproject \<name>\[dir]     |
|  genspider   |   创建一个爬虫   | scrapy genspider \[opions]\<name>\<domain> |
|   settings   |  获得爬虫配置信息  |        scrapy settings \[options]        |
|    crawl     |   运行一个爬虫   |          scrapy crawl \<spider>          |
|     list     | 列出工程中所有爬虫  |               scrapy list                |
|    shell     | 启动URL调试命令行 |            scrapy shell [url]            |

##### Scrapy爬虫的命令行逻辑

为什么Scrapy采用命令行创建和运行爬虫？

- 命令行(不是图形界面)更容易自动化，适合脚本控制。


- 本质上，Scrapy是给程序员用的，功能(而不是界面)更重要。

#### Scrapy爬虫的一个简单实例

- 演示HTML页面地址：http://python123.io/ws/demo.html
- 文件名称: demo.html

##### 产生步骤

- 步骤1：建立一个Scrapy爬虫工程
  - 生成的工程目录
    Python123demo/ ——> 外层目录
      Scrapy.cfg  ——> 部署Scrapy爬虫的配置文件
      python123demo/ ——> Scrapy框架的用户自定义Python代码
      	\_\_init\_\_.py       	——> 初始化脚本
      	items.py                 ——> Items代码模板(继承类)
      	middlewares.py    ——> Middlewares代码模板(继承类)
      	pipelines.py     	——> Pipelines代码模板(继承类)
      	settings.py      	——> Scrapy爬虫的配置文件
      	
      	spiders/    ——>  Spiders代码模板目录(继承类)
      		\_\_init\_\_.py 	——> 初始文件，无需修改
      		\_\_pycache\_\_/	——> 缓存目录，无需修改
- 步骤2：在工程中产生一个爬虫
- 步骤3：配置产生的spider爬虫
- 步骤4：运行爬虫，获取网页

#### Scrapy爬虫的基本使用
##### Scrapy爬虫的使用步骤
- 步骤1：创建一个工程和Spider模板
- 步骤2：编写Spider
- 步骤3：编写Item Pipeline
- 步骤4：优化配置策略
##### Scrapy爬虫的数据类型
- Request类
  class scrapy.http.Request()
  - Request对象表示一个HTTP请求
  - 由Spider生成，由Downloader执行

|  属性或方法   |              说明              |
| :------: | :--------------------------: |
|   .url   |      Request对应的请求URL地址       |
| .method  |     对应的请求方法，‘GET’‘POS’等      |
| .headers |          字典类型风格的请求头          |
|  .body   |         请求内容主体，字符串类型         |
|  .meta   | 用户添加的扩展信息，在Scrapy内部模块间传递信息使用 |
| .copy()  |            复制该请求             |

- Response类
  class scrapy.http.Response()
  - Response对象表示一个HTTP响应
  - 由Downloader生成，由Spider处理

|  属性或方法   |            说明            |
| :------: | :----------------------: |
|   .url   |     Request对应的URL地址      |
| .status  |      HTTP状态码，默认是200      |
| .headers |     Response对应的头部信息      |
|  .body   |  Response对应的内容信息，字符串类型   |
|  .flags  |           一组标记           |
| .request | 产生Response类型对应的Request对象 |
| .copy()  |          复制该响应           |

- Item类
  class scrapy.item.Item()
  - Item对象表示一个从HTML页面中提取的信息内容
  - 由Spider生成，由Item Pipeline处理
  - Item类似字典类型，可以按照字典类型进行操作


#### Scrapy爬虫提取信息的方法

##### Scrapy爬虫支持多种HTML信息提取方法

- BeautifulSoup
- lxml
- re
- XPath Selector
- CSS Selector

##### CSS Selector 的基本使用

\<HTML>.css('a::attr(href)').extract()

#### Scrapy股票爬虫实例

步骤

- 步骤1：建立工程和Spider模板
  - \>scrapy startproject BaiduStocks
  - \>cd BaiduStocks
  - \>scrapy genspider stocks baidu.com
  - 进一步修改spiders/stocks.py文件
- 步骤2：编写Spider
  - 配置stocks.py文件
  - 修改对返回页面的处理
  - 修改对新增URL爬取请求的处理
```python
# -*- coding: utf-8 -*-
import scrapy
import re

class StocksSpider(scrapy.Spider):
    name = 'stocks'
    start_urls = ['http://quote.eastmoney.com/stocklist.html']

    def parse(self, response):
        for href in response.css('a::attr(href)').extract():
            try:
                stock = re.findall(r'[s][hz]\{6}',href)[0]
                url = 'https://gupiao.baidu.com/stock/' + stock + '.html'
                yield scrapy.Request(url, callback=self.parse_stock)
            except:
                continue
    def parse_stock(self, response):
        infoDict = {}
        stockInfo = response.css('.stock-bets')
        name = stockInfo.css('.bets-name').extract()[0]
        keyList = stockInfo.css('dt').extract()
        valueList = stockInfo.css('dd').extract()
        for i in range(len(keyList)):
            key = re.findall(r'>.*</dt>',keyList[i])[0][1:-5]
            try:
                value = re.findall(r'\d+\.?.*</dd>',valueList[i])[0][0:-5]
            except:
                value = '--'
            infoDict[key] = value

        infoDict.update(
                {'股票名称':re.findall('\s.*\(',name)[0].split()[0] + \
                 re.findall('\>.*\<',name)[0][1:-1]})

        yield infoDict
```
- 步骤3：编写ITEM Pipeline


##### Scrapy爬虫的优化

settings.py文件

|               选项               |               说明                |
| :----------------------------: | :-----------------------------: |
|      CONCURRENT-REQUESTS       |    Downloader最大并发请求下载数量，默认32    |
|        CONCURRENT_ITEMS        | Item Pipeline最大并发ITEM处理数量，默认100 |
| CONCURRENT_REQUESTS_PER_DOMAIN |       每个目标域名最大的并发请求数量，默认8       |
|   CONCURRENT_REQUESTS_PER_IP   |     每个目标IP最大的并发数量，默认0，非0有效      |
