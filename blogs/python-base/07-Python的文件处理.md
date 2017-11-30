### Python的文件处理

[TOC]

#### Python的文件处理简单分为：
- 文件的读写和关闭
- 文件的模式
- 文件的读取位置
#### 1.文件的读写和关闭
Python中要想获得文件里的内容，先要**打开文件**，然后才能读和写。而且写完之后，**一定要关闭**。Python中对文件的打开是通过**open函数**来获得一个句柄。
- 获得**读**的句柄f，就可以进行f.read()进行读入。
- 获得**写**的句柄f，就可以进行f.write()进行写入。
- 当文件处理结束后，关闭文件
##### 1)文件的打开
```python
file_obj = open(filename,mode='r',buffering=-1)
# 一共有3个参数，第一个是强制参数，后面两个是可选的
# mode可以是读，写或者追加，一般默认是读文件
# buffering主要是缓冲区，若写100，表示缓冲区为100.
```
##### 2)文件的读取
```python
f = open(r'somefile.txt')
f.readline() # 表示读取文件的一行
f.readlines() #表示把文件从头到尾都读取出来，并保存为一个列表
```
##### 3)文件的写入
```python
f = open(r'somefile.txt')
f.write() #表示把字符串写入
f.writelines() #表示把一个列表写入
```
##### 4)文件的关闭
- 普通的关闭方法
```python
f = open(r'somefile.txt')
pass # do something
f.close()
```
- 懒人方法
```python
with open(r'somefile.txt')
	f.writelines()
```
通常使用的是with方法
#### 2.文件的模式
**open函数的模式参数**

|  值   |    描述    |
| :--: | :------: |
| ''r' |   读模式    |
| 'w'  |   写模式    |
| 'a'  |   追加模式   |
| 'b'  |  二进制模式   |
| '+'  |  读/写模式   |
| 'r+' | 以读写模式打开  |
| 'w+' | 以读写模式打开  |
| 'a+' | 以读写模式打开  |
| 'rb' | 以二进制模式打开 |
#### 3.文件的读取位置
有时候我们只想**读文件的一部分内容，**或者我们需要从**文件的某个位置读数据，**此时就应该使用seek()函数。
```python
file_obj.seek(offset,whence=0)
# seek 主要是在文件中移动指针，从whence(0表示文件头,
# 1表示当前位置，2表示文件尾)偏移offset个字节。
```
例如：
```python
====123.txt====
123456789

# 从头读3个字符
f = open(123.txt)
f.seek(0,0)
print(f.read(3))
f.close()
>>>123

# 从尾读3个字符
f = open(123.txt)
f.seek(-3,2) # 表示从文件指针指向尾部，-3表示向前移动3个字节
print(f.read(3))
f.close()
>>>789
```
#### 实例
|---abc1109.txt---
Google
Micrisoft
BaiDu
Facebook
|----demo.py---
##### 1.把abc1109.txt里面的内容读取出来，写到一个新的文件中，按照下面的格式：
|----Output------
1:Google
2:Micirisoft
3:BaiDu
4:Facebook
```python
def read_File(): 读取文件内容
	with open(abc1109.txt)as f:
		lines = f.readlines()
	return lines
def write_File(content=[]) :
	with open(newFile.txt,'w') as f:
		f.writelines(content)

new_lines = [] 
for index,line in enumerate(read_File()):
	new_lines.append(str(index+1)+': '+line)
write_File(new_lines)
```
##### 例子2:修改文件名
原来的：
|-----abc1109.txt-----
|-----new_abc1109.txt-----
|----demo.py-----
```python
import os
def rename_Files():
	file_list = os.listdir('.')# 列出目录下的所有文件
	for file_name in file_list:
		if file_name.endwith('txt'): #找到txt文件
			# 把文件名里面的数字去掉
			new_file_name = file_name.translate(None,'0123456789')
			print(new_file_name)
			os.renmae(file_name,new_file_name)
rename_Files()
>>>|----abc.txt---
>>>|----new_abc.txt---
>>>|----demo.py---
```
