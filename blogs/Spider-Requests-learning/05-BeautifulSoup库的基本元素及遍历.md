---
author : rovo98
description: notes.
---

# BeautifulSoup库的基本元素及遍历

## Table of Contents

- [基于bs4库HTML元素的遍历方法](https://github.com/rovo98/python-learning/blob/master/blogs/Spider-Requests-learning/05-BeautifulSoup%E5%BA%93%E7%9A%84%E5%9F%BA%E6%9C%AC%E5%85%83%E7%B4%A0%E5%8F%8A%E9%81%8D%E5%8E%86.md#基于bs4库的html的遍历方法)
	- [标签树的下行遍历](https://github.com/rovo98/python-learning/blob/master/blogs/Spider-Requests-learning/05-BeautifulSoup%E5%BA%93%E7%9A%84%E5%9F%BA%E6%9C%AC%E5%85%83%E7%B4%A0%E5%8F%8A%E9%81%8D%E5%8E%86.md#1标签树的下行遍历)
	- [标签树的上行遍历](https://github.com/rovo98/python-learning/blob/master/blogs/Spider-Requests-learning/05-BeautifulSoup%E5%BA%93%E7%9A%84%E5%9F%BA%E6%9C%AC%E5%85%83%E7%B4%A0%E5%8F%8A%E9%81%8D%E5%8E%86.md#2标签树的上行遍历----go-back-to-top)
	- [标签树的平行遍历](https://github.com/rovo98/python-learning/blob/master/blogs/Spider-Requests-learning/05-BeautifulSoup%E5%BA%93%E7%9A%84%E5%9F%BA%E6%9C%AC%E5%85%83%E7%B4%A0%E5%8F%8A%E9%81%8D%E5%8E%86.md#3标签树的平行遍历)

|      基本元素       |                    说明                    |
| :-------------: | :--------------------------------------: |
|       Tag       |      标签，最基本的信息组织单元，分别用<>和</>标明开头和结尾      |
|      Name       | 标签的名字，\<p>...\</p>的名字是‘p’等等，格式：\<tag>.name |
|   Attributes    |       标签的属性，字典形式组织，格式：\<tag>.attrs       |
| NavigableString | 标签内非属性字符串，\<>...\</>中的字符串，格式：\<tag>.string |
|     Comment     |        标签内字符串的注释部分，一种特殊的Comment类型        |

引入--BeautifulSoup的导入及使用

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup("<html>data</html>", "html.parser")
soup1 = BeautifulSoup(open('E:\demo.html'), "html.parser")
```

### 基于bs4库的HTML的遍历方法

#### 1.标签树的下行遍历

|      属性      |                说明                |
| :----------: | :------------------------------: |
|  .contents   |     子节点的列表，将\<tag>所有儿子节点存入列表     |
|  .children   | 子节点的迭代类型，与.contents类似，由于循环遍历儿子节点 |
| .descendants |  **子孙**节点的迭代类型，包含所有子孙节点，用于循环遍历   |

#### 2.标签树的上行遍历 -- [go back to top](https://github.com/rovo98/python-learning/blob/master/blogs/Spider-Requests-learning/05-BeautifulSoup%E5%BA%93%E7%9A%84%E5%9F%BA%E6%9C%AC%E5%85%83%E7%B4%A0%E5%8F%8A%E9%81%8D%E5%8E%86.md#beautifulsoup库的基本元素及遍历)

|    属性    |           说明           |
| :------: | :--------------------: |
| .parent  |        节点的父亲标签         |
| .parents | 节点先辈标签的迭代类型，用于循环遍历先辈节点 |

#### 3.标签树的平行遍历

|         属性         |              说明              |
| :----------------: | :--------------------------: |
|   .next_sibling    |    返回按照HTML文本顺序的下一个平行节点标签    |
| .previous_sibling  |    返回按照HTML文本顺序的上一个平行节点标签    |
|   .next_siblings   |  迭代类型，返回按照HTML文本顺序的后续所有节点标签  |
| .previous_siblings | 迭代类型，返回按照HTML文本顺序的前驱所有平行节点标签 |

