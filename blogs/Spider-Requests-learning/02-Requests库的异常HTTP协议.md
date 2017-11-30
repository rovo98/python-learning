### 理解Requests库的异常HTTP协议

[TOC]

|          异常             |         说明          |
| :-----------------------: | :---------------------: |
| requests.ConnectionError  | 网络连接错误异常，如DNS查询失败、拒绝连接等 |
|    requests.HTTPError     |        HTTP错误异常         |
|   requests.URLRequired    |         URl缺失异常         |
| requests.TooManyRedirects |    超过最大重定向次数，产生重定向异常    |
|  requests.ConnectTimeout  |       连接远程服务器超时异常       |
|     requests.Timeout      |     请求URL超时，产生超时异常      |

Response的异常：

|          异常          |               说明                |
| :------------------: | :-----------------------------: |
| r.raise_for_status() | 如果不是200， 产生异常requests.HTTPError |

**爬取网页的通用代码框架**

```python
import requests
def getHTMLText(url) :
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status() #如果状态不是200， 引发requests.HTTPError异常
        r.encoding = r.apparent_encoding #将encoding 设置为'utf-8'，一般用于没有charset的header
        return r.text
    except:
        return '产生异常'
if __name__ == '__main__':
    url = "http://www.baidu.com"
    print(getHTMLText(url))
```

#### 1、HTTP协议

HTTP --> ， Hypertext Transfer Protocol, 超文本传输协议

HTTP是一个基于“请求与响应”模式的、无状态的应用层协议。

HTTP协议采用URL作为定位网络资源的标识。

**URL格式：**http://host\[:port][path]

HTTP URL的理解：

URL 是通过HTTP协议存取资源的Internet路径，一个URL对应一个数据资源。

#### 1.1HTTP协议对资源的操作

|   方法   |               说明               |
| :----: | :----------------------------: |
|  GET   |          请求获取URL位置的资源          |
|  HEAD  | 请求获取URL位置资源的响应消息报告，即获取该资源的头部信息 |
|  POST  |       请求URL位置的资源后附加新的数据        |
|  PUT   |   请求向URL位置存储一个资源，覆盖原URL位置的资源   |
| PATCH  |  请求局部更新URL位置的资源，即改变该处资源的部分内容   |
| DELETE |         请求删除URL位置存储的资源         |

**理解PATCH和PUT的区别**：

假设URL位置有一组数据UserInfo， 包括UserID、UserName等20个字段

 需求：用户修改了UserName，其他不变。

*采用PATCH，仅向URL提交UserName的剧本更新请求。

*采用PUT，必须将所有20个字段一并提交URL，未提交字段被删除。

==PATCH的好处：==节省网络带宽

