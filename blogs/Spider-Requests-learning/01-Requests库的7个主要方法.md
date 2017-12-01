# Requests库的7个主要方法

### Table of contents
- [requests库的主要方法(基础方法)]("#requests库的主要方法(基础方法)")
  - [1.requests库的get()方法]("#1.requests库的get()方法")
  - [Response对象的属性]("#Response对象的属性")
  - [2.Requests库的head()方法]("#2.Requests库的head()方法")
  - [3.Requests库的post()方法]("#3.Requests库的post()方法")
  - [4.Requests库的put()方法]("#4.Requests库的put()方法")

|         方法         |               说明                |
| :----------------: | :-----------------------------: |
| requests.request() |       构造一个请求，支撑以下各方法的基础方法       |
|   requests.get()   |    获取HTML网页的主要方法，对应于HTTP的GET    |
|  requests.head()   |   获取HTML网页头信息的方法，对应于HTTP的HEAD   |
|  requests.post()   | 向HTML网页提交POST请求的方法，对应于HTTP的POST |
|   requests.put()   |  向HTML网页提交PUT请求的方法，对应于HTTP的PUT  |
|  requests.patch()  |  向HTML网页提交局部修改请求，对应于HTTP的PATCH  |
| requests.delete()  |   向HTML页面提交删除请求，对应HTTP的DELETE   |

#### requests库的主要方法(基础方法)

requests.request(method, url, **kwargs)

- method: 请求方式，对应get/put/post等7种
  - r = requests.request('GET',url, **kwargs)
  - r = requsts.request('HEAD',url, **kwargs)
  - r = requests.request('POST',url, **kwargs)
  - r = requests.request('PATCH',url, **kwargs)
  - r = requests.request('delete', url, **kwargs)
  - r = requests.request('OPTIONS',url, **kwargs)


- url: 拟获取页面的URL链接
- **kwargs: 控制访问的参数，共13个
  - 1)params:字典或字节序列，作为参数增加到URL中
  - 2)data: 字典、字节序列或者文件对象，作为Request的内容
  - 3)json : JSON格式数据，作为Request内容
  - 4)headers : 字典，HTTP定制头
  - 5)cookies : 字典或CookieJar，Request中的cookie
  - 6)auth : 元组，支持HTTP认证功能
  - 7)files : 字典类型，传输文件
  - 8)timeout : 设定的超时时间，秒为单位
  - 9)proxies : 字典类型，设定访问代理服务器，可以增加登录认证
  - 10)allow_redirects : True/False, 默认为True,重定向开关
  - 11)stream : True/False, 默认为True ,获取内容立即下载开关
  - 12)verify : True/False , 默认为True ， 认证SSL证书开关
  - 13) cert : 本地SSL证书路径
  
#### 1.requests库的get()方法：

```python
r = requests.get(url)    #构造一个向服务器请求资源的Request对象
#返回一个包含服务器资源的Response对象
```

完整方法：requests.get(url, params=None, **kwargs)

url: 拟获取页面的url链接

 params: url中的额外参数， 字典或字节流格式， 可选

**kwargs : 12个控制访问的参数，与request()的一样

实际上是这样的：

```python
def get(url, params=None, **kwargs):
    #Sends a GET request.
    
    #:param url: URL for the new :class :'Request' object.
    #:param params: (optional) Dictionary ro bytes to be sent in the query
    #:return: :class :'Request <Response>' object
    #:rtype: requests.Response
    
    kwargs.setdefault('allow redirect', True)
    return request('get', url, params=params, **kwargs)
```

例子：

```python
import requests
r = requests.get("http://www.baidu.com")
print(r)
type(r)
r.headers

"""输出：
200
<class 'requests.models.Response'>
{'Transfer-Encoding': 'chunked', 'Pragma': 'no-cache', 'Connection': 'Keep-Alive', 'Last-Modified': 'Mon, 23 Jan 2017 13:27:52 GMT', 'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 'Server': 'bfe/1.0.8.18', 'Set-Cookie': 'BDORZ=27315; max-age=86400; domain=.baidu.com; path=/', 'Content-Encoding': 'gzip', 'Date': 'Sat, 15 Jul 2017 13:27:01 GMT', 'Content-Type': 'text/html'}
"""
```

#### Response对象的属性

|         属性          |              说明               |
| :-----------------: | :---------------------------: |
|    r.status_code    | HTTP请求的返回状态，200表示连接成功，404表示失败 |
|       r.text        |  HTTP响应内容的字符串形式，即，url对应的页面内容  |
|     r.encoding      |   从HTTP header中猜测的响应内容编码方式    |
| r.apparent_encoding |   从内容中分析出的响应内容编码方式(备用编码凡是)    |
|      r.content      |        HTTP响应内容的二进制形式         |

[注]：**r.encoding: 如果header中不存在charset， 则认为编码为ISO-8859-1**

#### 2.Requests库的head()方法

```python
r = requests.head('http://httpbin.org/get')
r.headers
r.text
"""输出：
{'Access-Control-Allow-Credentials': 'true', 'X-Processed-Time': '0.000805139541626', 'Via': '1.1 vegur', 'Access-Control-Allow-Origin': '*', 'X-Powered-By': 'Flask', 'Content-Length': '267', 'Server': 'meinheld/0.6.1', 'Content-Type': 'application/json', 'Date': 'Sat, 15 Jul 2017 14:23:41 GMT', 'Connection': 'keep-alive'}

'' -- r.text
"""
```

#### 3.Requests库的post()方法

```python
payload = {'key1':'value1', 'key2':'value2'}
r = requests.post('http://httpbin.org/post', data = payload)
r = requests.post('http://httpbin.org/post', data = 'ABC')
#向URL POST一个字典自动编码为form(表单)
print(r.text)
"""输出:
{
  "args": {}, 
  "data": "ABC",    --- > 向URLPOST一个字符串，自动编码为data
  "files": {}, 
  "form": {
    "key1": "value1", 
    "key2": "value2"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Content-Length": "23", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.18.1"
  }, 
  "json": null, 
  "origin": "120.85.181.141", 
  "url": "http://httpbin.org/post"
"""
```

#### 4.Requests库的put()方法

```python
payload = {'key1':'value1', 'key2':'value2'}
r = requests.put('http://httpbin.org/put', data = payload)
print(r.text)
#此方法与post方法类似，只不过是替换了URL位置上资源的内容
```

