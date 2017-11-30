### Python内置函数(buit-in function)

#### 1.sorted()
##### (1).对于一个列表排序
```python
sorted([100, 98, 102, 1, 40])
>>>[1,40,98,100,102]
```
##### (2).通过key参数/函数排序
比如一个长列表里面嵌套了很多字典元素，要按照每个元素的长度大小排序
```python
L = [{1:5,3:4}, {1:3, 6:3}, {1:1, 2:4, 5:6}, {1:9}]
new_list = sorted(L, key=lambda x:len(x))
print(new_list)
>>>[{1:9},{1:5,3:4},{1:3,6:3},{1:1,2:4,5:6}]
```
##### (3).对由tuple组成的List列表
比如下面是学生里面的年龄的一个list
```python
students = [('wang','A',15),('li','B',12),('zhang','B',10)]
# 比较每个元组的第三项
print(sorted(students,key=lambda student:student[2]))
>>>[('zhang','B',10),('li','B',12),('wang','A',15)]
```
##### (5).用cmp函数排序
```python
students = [('wang','A',15),('li','B',12),('zhang','B',10)]
# 比较元组的第一项
print(sorted(students,cmp=lambda x,y:cmp(x[0],y[0])))
>>>[('li','B',12),('wang','A',15),('zhang','B'10)]
```

####2.map()
- map可以根据提供的函数对指定序列做映射，它接受**一个函数和一个list**，并通过把函数f作用在list的每一个元素上，然后返回**一个新的list**，map函数的入参也可以是**多个**。[注意]这个函数必须要有返回值，不然会出现：
  返回的新list是[None,None,....,None]
```python
def fun(x):
	return x * x
print(map(fun,[1,2,3,4,5]))
>>>[1,4,9,16,25]

def add_x_y(x,y):
	return x + y

c = map(add_x_y,[1,2,3,4,5],[10,11,12,13,14])
print(c)
>>>[11,13,15,17,19]
```

#### 3.enumerate()
- Python中，**迭代**永远是取出元素本身，而非元素的索引，有的时候我们需要知道元素的索引，比如在一个很长的列表里面是一些网站名，我们希望在打印的时候，也能**列出索引**。若没有这个函数，我们需要再加一个变量，在循环打印的时候让这个计数变量递增，现在有了这个enumerate，就不用这么麻烦了。
```python
# 普通方法
webList = ['sohu','yahoo','sina','apple','dianping']
i = 0
for element in webList:
	webList[i] = '%d:%s' % (i,webList[i])
	i += 1
print(webList)
>>>['0:sohu','1:yahoo','2:sina','3:apple','4:dianping']

# 用enumerate
for index,webname in enumerate(webList):
	print(index,webname)
>>>(0, 'sohu')
>>>(1, 'yahoo')
>>>(2, 'sina')
>>>(3, 'apple')
>>>(4, 'dianping')
```

#### 4.zip()
- zip函数接受任意多个(包括0个、1个)序列作为参数，返回一个tuple列表
```python
x = [1,2,3]
y = [4,5,6]
z = [7,8,9]
print(xyz = zip(x,y,z))
>>>[(1,4,7),(2,5,6),(3,6,9)]

aList = [1,2,3,4,5]
bList = ['a','b','c','d','e']
new_list = zip(aList, bList)
print(new_list)

>>>[(1,'a'),(2,'b'),(3,'c'),(4,'d'),(5,'e')]
# 快速的构建一个字典
new_dict = dict(new_list)
print(new_dict)

>>>{1:'a',2:'b',3:'c',4:'d',5:'e'}
```
#### 5.filter()
- filter函数接受一个函数f和一个list，这个函数f作用是对每一个元素进行判断，返回True或者False，这样可以**过滤**一些**不符合条件的**元素，然后返回符合条件的list。
```python
# 定义过滤函数，符合条件list元素将返回True，否则返回False
def is_even(x):
	return x % 2 == 0
print(filter(is_even,[1,2,3,4,5]))
>>>[2,4]
# 在处理文本时，可以处理字符串的空格，回车和空字符
def is_not_empty(x):
    return x and len(x.strip())>0
print(filter(is_not_empty,['aaa',None,' ','book','End','\t','\n']))

>>>['aaa','book','End']
```
#### 6.reduce()
- reduce函数的用法和map类似，也是一个函数f和一个list，但是函数的入口参数一定要**两个**，reduce也是对每个元素进行反复调用，最后返回最终的值，而map是返回一个list
```python
from functools import reduce
def add(x, y):
	return x + y
print(add, [1,2,3,4,5])

>>>15
```
