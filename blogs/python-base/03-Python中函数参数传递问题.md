# Python中函数的参数传递问题

## Table of Contents

- [python中函数的参数传递方式]()
- [python中函数的参数传递种类]()
	- [1. 位置参数]()
	- [2. 默认参数]()
	- [3. 关键字参数]()
	- [4. 任意多位置参数]()
	- [5. 任意多关键字参数]()
- [综合实例]()

### Python中函数的参数传递方式

- Python函数参数传递是通过**对象引用**，参数传递过程中将整个对象传入。
  - 对于可**可变对象**的修改，在函数的内部和外部都可见，调用者和被调用者共享这个对象
  - 而对于**不可变对象**，由于并不能真正被修改，因为修改是通过生成一个新的对象，然后赋值来实现的。

### Python中的参数传递种类 -- [go back to top]()

- 位置参数
- 默认参数  --> 在函数运行前就被赋了值
- 关键字参数 --> 通过变量的名字进行匹配，而不是位置
- 可变长度参数
  - 任意多个非关键字可变长参数(元组)
  - 任意多个关键字变量参数(字典)


#### 1.位置参数

```python
def printMessage(message,times):
	print(message * times)

printMessage('Hi python:', 2)
#将'Hi python'赋值给message,2赋值给times
>>>Hi python:Hipython
```

#### 2.默认参数 -- [go back to top]()

当调用含有默认参数的函数且没有给默认参数赋值，默认参数使用默认值

```python
def printMessage(message,times=2):
	print(message * times)
printMessage('Hi python')
>>>Hi python:Hi python
```

#### 3.关键字参数

当我们使用的函数传递参数希望通过变量名进行匹配时，使用关键字参数

```python
def func(a,b=10,c=20):
	print('a is:',a,'b is:',b,'c is:',c)

func(3,7)#没有关键字就使用默认的位置传递
>>>a is: 3 b is 7 c is 20

func(25,c=24)#使用关键字参数传递，跳过b，直接到c的赋值
>>>a is 25 b is 10 c is 24

func(c=50,a=100)#使用关键字参数不需要按照位置
>>>a is 100 b is 10 c is 50
```

#### 4.任意多个位置参数的函数 -- [go back to top]()

```python
def printScore(msg,*values):
	if not value:
		print(msg)
	else:
		values_str = ','.join(str(x) for x in values)
		print('{},{}'.format(msg,values_str))

printScore('My score are',100,90,80)
>>>My score are,100,90,80
```

**参数values前面加 * ，变成(msg,*values)，**表示只有第一个参数的msg是调用者必须要指定的，该参数后面，**可以跟任意数量的位置参数**(主要是任意数量，包含0个)
其中原理：其实是Python会自动把* 操作符后面的**形参变成元组传递给函数**

##### 5.任意多个关键字参数 -- [go back to top]()

```python
def printLog(msg,**theRest):
	if not theRest:
		print(msg)
	else:
		for key,value in theRest.items():
			print('{},{}={}'.format(msg,key,value))

printLog('Log info',verson='1.0',platform='win')
>>>Log info,verson=1.0
>>>Log inof,platform=win
```

原理：python把**后面的参数当作字典来处理，传给函数。

#### 综合例子： -- [go back to top]()

```python
def total(initial=5,*numbers,**keywords):
	count = initial
    
	for num in numbers:
		count += num
        
	for key in keywords:
		count += keywords.get(key)
	return count

print(total(10,1,2,3,apple=50,orange=100))
>>>166
```
