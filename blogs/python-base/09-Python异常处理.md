---
author: rovo98
description: notes.
---

# Python异常处理

## Table of Contents

- [基本语法]()
- [try-except]()
- [try-except-finally]()

### 1.基本语法介绍

Python中有一套异常处理；机制，来帮助我们进行错误处理，语法比较简单

#### 1)try-except语句

```python
try:
	do something
except Exception,e:
	handle error
else:
	pass
```
- try语句是用来捕获异常的
- except语句是用来处理不同的异常，**Exception**是异常的种类
- e表示异常信息
- else表示若没有发生异常，当try执行完毕后，就会执行else

#### 2)try-except-finally语句 -- [go back to top]()

```python
try:
	do something 
except Exception, e:
	handle error
finally:	
	do finally
```
- try语句用来捕获异常，若没有发生异常，执行try之后，直接执行finally
- 若try发生异常，首先执行except部分处理错误，然后才是执行finally

