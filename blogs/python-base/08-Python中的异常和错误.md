---
author: rovo98
description: notes.
---

# Python中的异常和错误

## Table of Contents

- [分类]()
- [1.变量或者函数名拼写错误:NameError]()
- [2.方法名拼写错误: AttributeError]()
- [3.列表越界: IndexError]()
- [4.忘记在if/for/while/def 声明后面添加 :]()
- [5.在循环语句中忘记调用len()：TypeError]()
- [6.尝试连接非字符串值与字符串：TypeError]()
- [7.访问未初始化的本地变量:UnboundLocalError]()
- [8.打开一个不存在的文件:IOError]()
- [9.除数为0: ZeroDivisionError]()

### 分类

-  **语法上的错误**，比如代码不符合解释器或者编译器的语法
-  **参数输入错误**，比如应该输入整数，结果却输入一个字符串
-  **逻辑上的漏洞**，比如不合法的输入或者算法上计算有些问题
-  **程序运行错误**，比如要读入文件，而传进来的文件名不存在

#### 1.变量或者函数名拼写错误:NameError
访问一个**不存在的变量，**比如打印一个从来没有**定义过的变量**或者把**函数名**写错了。

```python
language = 'Python'
print('Welcome to study :'+Language)
>>> NameError: name 'Language' is not defined

price = ruond(4.2)
print(price)
>>> NameError: name 'ruond' is not defined
```

#### 2.方法名拼写错误: AttributeError

访问一些**位置的对象属性**，比如字符串里面一些内置函数名拼错了

```python
line = 'Python is easy'
print(line.upperr())
>>> AttributeError: 'str' object has no attribute 'upperr'
```

#### 3.列表越界: IndexError -- [go back to top]()

比如访问list 的时候，**索引超过了**列表的最大索引

```python
names = ['XiaoMing','LaoWang','ZhangLi']
print(names[3])
>>> IndexError: list index out of range
```

#### 4.忘记在if/for/while/def 声明后面添加 : 

SyntaxError
```python
score = 95
if score>90
	print('very good')
>>> SyntaxError: invalid syntax
```

#### 5.在循环语句中忘记调用len()：TypeError -- [go back to top]()

有时想通过索引来迭代一个list内的元素，for循环中我们经常使用range()函数，但是要**记得加入len()而不是直接返回这个列表**

```python
companies = ['Google','Apple','Facebook']
for i in range(companies):
	print(i)
>>> TypeError: range() integer end argument expected, got list
```

#### 6.尝试连接非字符串值与字符串：TypeError

```python
score = 82
print("Jack's score is" + score)
>>> TypeError: cannot concatenate 'str' and 'int' objects
```

#### 7.访问未初始化的本地变量:UnboundLocalError

在变量使用的时候，特别是在**函数内部和外部用相同的变量名，**经常会出现这样的错误

```python
x = 10
def func() :
	print(x)
	x = 1
	
func()
print('Value of x is',x)
>>> UnboundLocalError: local variable 'x' referenced before assignment
```

**注意在函数func中x是局部变量，因为在函数内部又对x进行了赋值为1，这样全局变量，若想要对函数外部的全局变量进行修改，应使用global声明为全局变量
**

```python
x = 10 
def func():
	global x
	print(x)
	x = 1
func()
print('Value of x is',x)
```

#### 8.打开一个不存在的文件:IOError -- [go back to top]()

有的时候我们会**访问一个文件，**或者定义函数去传入一个文件名，然后去读取
很有可能这个**文件名根本不存在**:

```python
f = open('price.txt')
>>> IOError: [Errno 2] No such file or directory : 'price.txt'
```

#### 9.除数为0: ZeroDivisionError

```python
nums = [10, 20, 0, 30]
for n in nums:
	print(100 / n)
>>> ZeroDivisionError: division by zero
```
