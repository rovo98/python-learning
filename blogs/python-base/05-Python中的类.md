### Python中的类

[TOC]

#### 1.类和类的实例
- **类其实是一种数据结构**，我们可以用它来定义对象，一个类会包含属性和行为特性.类是现实世界的实体以编程形式出现.
- python中的类的声明**用class 关键字**来命名。
- **python类分为两种：**经典类(旧类)，新式类。新式类主要是从python2.2以后开始引入的，目前以用新式类为(python3.x中默认都是新式类)
  新式类和经典类的区别：**类内置的属性，多重继承的搜索顺序和父类初始化**
```python
# 经典类 :
class OldStyle():
	```define ClassName class``` # 类的文档说明
	class_suite
# 新式类 :
class NewStyle(object): # 括号内的object是一个父类，是Python里类的祖宗
	```define ClassName class``` #类的文档说明
	class_suite
#如果说类是一种数据结构定义的类型，那么实例就是声明这种类型的变量
class Dog(object):
	```This is Dog class```
	pass

dog_obj = Dog()
print(dog_obj)
>>>  < __main__.Dog instance at 0x000000000000000245A54B >
```
#### 2.类的初始化
- 类的初始化函数**是用\_\_init\_\_来完成的**。
- **注意\_\_init\_\_()不是类的构造函数，**只是用来**初始化**。
```python
class Dog(object):
	```define Dog class```
	def __init__():
		print('Init the Dog')
dog_obj = Dog()
>>> Init the Dog
```
1).**当Dog类声明一个dog_obj对象实例时**，Python会自动去检查那时候实现的\_\_init\_\_方法，做一些实例对象的初始化工作。
2).\_\_init\_\_()方法在Python中有特殊的含义，用来一些命名约定来**进行访问控制**
3).self参数，Python中特有的，当\_\_init\_\_()被调用时，**实例对象**作为**第一个参数**被传进去，相同与Java中的this，也就是说self其实是类的对象的地址。
```python
class Dog(object):
	```define Dog class```
	def __init__():
		print('Init the Dog')
		print(self)
		
dog_obj = Dog()
print(dog_obj)
>>> Init the Dog
>>> < __main__.Dog object at 0x0000000000000264AB70 >
>>> < __main__.Dog object at 0x0000000000000264AB70 >
# self 的地址和dog_obj对象的地址是一样的
```
#### 3.类的删除
- 类既然有初始化，就一定有是删除，python中用一个\_\_del\_\_()来负责清理类的对象，
- 当这个对象没有人用了就会被清理掉，python使用引用计数方法来追踪的
- 引用一次加1，当引用计数为0时，python内置的一个垃圾对象回收机制就会调用类里面的\_\_del\_\_()方法
```python
class Dgo(object):
	```define Dog class```
	def __init__():
		print('Init the Dog')
	def __del__():
		print('Del the Dog')
dog_obj = Dog()
del dog_obj
>>> Init the Dog
>>> Del the Dog
```
#### 4.类的属性
- 类里面定义
- 类的初始化函数里面定义
  1)类里面定义：假设有一个Student类，里面有name和age属性
```python
class Student(object):
	name = 'wang'
	age = 10
```
name 和 age都是Student类的属性，所以Student类的对象实例都共享name,age
换句话说：s1,s2两个对象里面的name 和age都是一样的.
```python
s1 =  Student()
print(s1.name, s1.age)
>>> wang 10

s2 = Student()
print(s2.name, s2.age)
>>> wang 10

print(Student.name,Student.age)
>>> wang 10
```
再看看对象的属性：
```python
class Student(object):
	name = 'wang'
	age = 10
	def __init__(self,name,age):
		self.name = name
		self.age = age

s1 = Student('Li',20) # 初始化对象实例s1
print(s1.name,s1.age)
>>> Li 20

s2 = Student('Xu',25) # 初始化对象实例s2
print(s2.name, s2.age)
>>> Xu 25

print(Student.name,Student.age)
>>> wang  10
```
#### 5.类中的方法
- 实例方法
- 类的方法
- 类的静态函数
##### 1)类的实例方法
类的实例方法一般是有一个显著的特征就是**会带有self参数，它的第一个正式参数为self**这些方法会访问实例的属性.
```python
class Kls(object):
	def __init__(self, data):
		self.data = data
	def printd(self):
		print(self.data)

ik1 = Kls('arun')
ik2 = Kls('seema')
ik1.printd()
>>>arun

ik2.printd()
>>>seema
```
##### 2)类的静态函数
类中的方法一般有self的方法也叫绑定对象方法，**那python种有没有没带self的，有的，静态函数方法就是其中一个**
- 静态方法徐亚哟有一个修饰关键字@staticmethod,表示下面声明的是一个静态方法，
- 这个是Python中的一种特殊用法，其实就是用了一个装饰器的技巧.
  ** 同Java类似，静态方法是与类相关的操作，但是不会依赖和改变类、实例的状态，调用静态方法无需创建对象** 
  例子：
  有一个机器人的类，有两个方法重启(do_Reset)和保存数据(save_DB),这两个方法操作之前都需要检查指令。
```python
IND = 'ON'
def check_Indication():
	return (IND == 'ON')

class Robot(object):
	def __init__(self,data):
		self.data = data
		
	def do_Reset(self):
		if check_Indication():
			print('Reset done for :{0}'.format(self.data))
	
	def save_DB(self):
		if check_Indication():
			self.db = 'new db connection'
			print('DB connection ready for :'.format(self.data))
			
robot1 = Robot('No1_Machine')
robot1.do_Reset()
robot1.save_DB()
>>> Reset done for : No1_Machine
>>> DB connection ready for : No1_Machine

robot2 = Robot('No2_Machine')
robot2.do_Reset()
robot2.save_DB()
>>> Reset done for : No2_Machine
>>> DB connection ready for : No2_Machine
```
使用静态方法：
```python
IND = 'ON'
class Robot(object):
	num = 0
	def __init__(self, data):
		self.data = data
	@staticmethod
	def check_Indication(): # 静态方法
		Robot.num += 1
		return (IND == 'ON')
	
	def do_Reset(self):
		if Robot.check_Indication():
			print('Reset done for :{0}'.format(self.data))
	
	
	def save_DB(self):
		if Robot.check_Indication():
			self.db = 'new db connection'
			print('DB connection ready for :{0}'.format(self.data))

robot1 = Robot('No1_Machine')
robot1.do_Reset()
robot2.sava_DB()
>>> Reset done for No1_Machine
>>> DB connection ready for No1_Machine

robot2 = Robot('No2_Machine')
robot2.do_Reset()
robot2.save_DB()
>>> Reset done for No2_Machine
>>> DB connection ready for No2_Machine
```
##### 3)类的方法
类方法：**只在类中运行的方法，而不在实例中运行的方法**
用@classmethod装饰器来修饰
例子：
  有一个Student 类，想要记录有多少个学生
```python
def get_num_of_instance(cls_obj):
	return cls_obj.num_student
	
class Student(object):
	num_student = 0
	def __init__(self):
		Student.num_student += 1
	
s1 = Student()
s2 = Student()
total_num = get_num_of_instace(Student)
print(total_num)
>>> 2

```
使用类方法：
```python
class Student(object):
	num_student = 0
	def __init__(self):
		Student.num_student += 1
		
	@classmethod
	def get_num_of_instance(cls):
		return cls.num_student
		
s1 = Student()
s2 = Student()
total_num = Student.get_num_of_instance()
print(total_num)
>>> 2
```
##### 4)类方法、静态函数、实例方法之间的调用关系
- 1)静态方法在访问本类的成员时，只允许访问静态成员(即静态成员变量和静态方法),而不允许访问实例成员变量和实例方法；实例方法则无此限制
- 2)实例方法可以访问实例属性和 类属性，也可以访问静态方法和类方法
- 3)类方法可以被对象调用，也可以被实例调用；传入的都是类对象，主要用于工厂方法，具体的实现交给子类处理。
- 4)静态方法参数没有实例参数self，也就不能调用实例参数，实例方法
