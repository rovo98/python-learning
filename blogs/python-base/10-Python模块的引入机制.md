---
author: rovo98
description: notes.
---

# 深入了解Python模块的引入机制

## Table of Contents

- [模块的好处]()
- [模块的种类]()
- [模块的搜索机制]()
- [模块的引入方式]()
- [import和from]()

### 1.模块的好处

- a)打个比方我们要造一辆自行车，我们不需要去制造橡胶，钢筋，轮胎，我们只需要买一些现成的轮子，龙头，把手，组装一下就可以了。Python也是这样，我们有的时候代码需要一些功能，而这些**功能在标准库里面或者第三方库**里面早就写好了的，我们要做的就是引入而已。
- b)当**代码量变大** 的时候，肯定需要封装和抽象，要提高可维护性，必须要把功能函数模块化。
- c)**模块化还可以避免函数名和变量名冲突**。相同名字的函数和变量完全可以分别存在不同的模块中，Java里面也有类似的概念。

### 2.模块的种类

- 1)用户自己写的自定义模块
- 2)Python的标准库模块
- 3)第三方模块//通过pip install,实际上，Python模块就是py文件
  
### 详解：

假设有一个HiPython目录，它的结构如下：
|----\_\_init\_\_.py
|----main.py
|----sched.py

里面有3个文件\_init\_\_.py,main.py, sched.py，这3个文件解释：
- 一个目录要想作为Python的模块包必须包含有\_\_init\_\_.py这个文件(这是Python设定死的。**原因是Python设计的时候搜索到目录下有这个特殊文件认为这个目录是Python的模块包，否则视为普通文件夹**)
- main.py是我们**自己写**的一个Python文件
- sched.py也是我们自己写的。。(跟标准库中的同名)

```python
====sched.py====
a = 100

====main.py====
import sched
print(sched.a)

>>>100
```

[解析]执行main.py的时候，首先引入了sched模块，这个模块的名字和标准库了的一样，但是这里调用的是我们自己写的模块，**这是Python模块的搜索机制决定的**

### 3.Python模块的搜索机制 -- [go back to top]()

- 1)程序当前目录
- 2)PYTHONPATH目录，也就是环境变量里面设置的PYTHON目录
- 3)标准库目录

#### 当前目录

也就是程序运行的主目录，Python会首先在主目录搜索导入的文件，这个目录总是被先搜索。

####
># PYTHONPATH目录
系统环境变量设置的PYTHON目录

#### 标准库的目录

Python自动搜索标准库安装在机器上的那些目录，比如: c:\Python35\lib

```python
import sys
print('The PYTHONPATH is',sys.path)
# 这里面就是包含Python模块搜索目录list
```

### 4.模块的引入方式 -- [go back to top]()

#### 1).import module

- **这种是完全引入**，比如import os,就会把os下面的所有的变量，函数，类全部引入。然后调用模块里面的函数时，只需要敲os.listdir(),就可以调用模块里面的listdir()函数。	这种引入方式有一个弊端：就是有一些函数不需要用到，但是因为使用的是全部引入的方式，这样当引入外部模块很多的时候，比较浪费性能，开销比较大，所以一般使用第二种引入方式。

#### 2)from module import printer

- **部分引入**，就是只引入需要的函数，还有一个好处是：直接敲printer('something'),而不用module.printer('something')

#### 3)import module as xx

- **别名**，比如:import numpy as np, np就是numpy的别名。

### 5.import和from都是赋值语句
- **就跟def一样，import和from都是可执行语句，而不是编译期间的声明。**
  ==python是动态编译的==，只有到执行的时候，Python才会运行呢这些语句。而且可以嵌套在if语句中。
