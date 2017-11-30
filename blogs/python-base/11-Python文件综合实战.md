### 融合多个技巧的Python文件-综合实战应用

[TOC]

#### 案例
	假如我们有一个目录里面包含若干个文件和子目录：
问题1：我们要统计该目录下有多少个文件并显示出来(包含子目录)
问题2：该目录总共的大小可以按M，也可以按K显示
问题3：贵啊目录下最大的文件和最小的文件，以及对应大小

目录为：'C:\myPython',结构如下:

```python
|---demo---
	|--demo_01.exe  14,390KB
	|--demo_02.msi  17,412KB
	|--other
		|--info.doc 2,329KB

|---log---
	|--1110_log.txt  1,382KB
	|--1111_log.txt  1,364KB
	|--1112_log.txt  1,368KB

|---pic---
	|--0127_1.jpg  92KB
	|--0127_2.jpg  89KB
	|--0127_3.jpg  71KB
```
#### 深入分析
程序其实就是**数据结构+算法**，所以我们先确定自己的数据结构，还有算法
##### 1)因为要列出**最大/最小**的文件名字和大小，数据结构我们采用Python的字典
##### 2)**算法**的话，先把目录下的**全部文件和目录列出**
- 若是文件就统计大小
- 若是子目录，就继续寻找该目录下的子文件，然后 不断重复刚才的过程，因为我们不知道有多少层嵌套的子目录，最好用递归
##### 3)最后是显示，要按MB，KB显示，需要我们定义一个扩展的函数入参结构，用默认位置参数

#### 源码
##### 1.获得单个文件的大小和名字
```python
# -*- coding:utf-8 -*-
from __future__ import division
import os
files_dict = dict() # 定义一个全局数据结构
def getFileSize(file):
	if os.path.exits(file): # 判断文件是否存在
		size = os.path.getsize(file) # 获得文件大小
		files_dict[file] = size  # 更新字典
```
##### 2.列出目录下所有的文件和子目录内的文件
```python
def listFiles(path='.'): # 传入路径，默认为当前目录
	if not os.path.exits(path): # 判断是否是有效目录
		print('path error')
		return None
	file = ''
	try:
		for file in os.listdir(path) :# 列出目录下的所有文件和目录
			filepath = os.path.join(path,file) # 构造出全路径文件
			if os.path.isdir(filepath) : # 判断是否为目录
				print(filepath)
				listFiles(path=filepath) # 继续递归子目录
			elif os.path.isfile(filepath): # 判断是否文件
				print(filepath)
				getFileSize(filepath)  # 获得文件大小
	except TypeError: # 若出错，打印出错的文件
		print(file)
```
##### 3.统计文件大小并按MB，KB显示
```python
def displayFilesSize(files=[],size_KB=False,size_MB=False):
	if size_KB: # 若要KB显示
		return str(round(sum(files)/1024,2)) + 'K'
	elif size_MB: # 若要MB显示
		return str(round(sum(files)/(1024*1024),2)) + 'M' 
	else:
		return str(round(sum(files),2)) + 'byte'
```
##### 4.主函数
```python
if __name__ == "__main__":
	mypath = r'C:\myPython'  # 注意使用原生字符串
	listFiles(mypath)
	all_files_size = displayFileSize(files_dict.values(),size_MB=True)
	print('\n Total>: files num={0},size={1}\n'.format(len(files_dict),all_files_size))
	
	if len(files_dict)>1:
		new_files_dict = zip(files_dict.values(),files_dict.keys())
		print(max(new_files_dict))
		print(min(new_files_dict))
```
