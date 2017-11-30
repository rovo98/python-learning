### Python多线程

#### 1.GIL全局解释器锁
Python的代码执行是由Python虚拟机(又名解释器主循环)进行控制的
- Python在设计的时候是这样考虑的，在主循环中同时只能有一个控制线程在执行，就像单核CPU系统中的多进程一样。
- 内存中可以有许多程序，但是在任意给定时刻只能有一个程序在运行。
- 同理，尽管PYthon解释中可以运行多个线程但是在任意给定时刻只有一个线程会被解释器执行。

这个GIL就好比一个严厉的二管家，他会保证同时只能有一个线程运行的。
在多线程环境中，Python虚拟机将按照下面所述的方式执行：
1).设置GIL.
2).切换进一个线程去运行。
3).执行下面的操作之一：
   a).指定数量的字节码指令
   b).线程主动让出控制权(可以调用time.sleep(0)来完成)
4).吧线程设置会睡眠状态(切换出线程)
5).解锁GIL。
6).重复上述步骤。

#### 2.什么是线程
- 1).线程(有时候称为轻量级进程)与进程类似，不过他们是在同一个进程下执行的.
	- 线程会共享相同的上下文。一个进程中的个县城与主线程共享同一片数据空间，因此相比于独立的进程而言，线程见得信息共享和通信更加容易。
	- 线程一般是以并发方式执行的，正是由于这种并行和数据供为，使得多任务的协作成为可能。
- 2).Python线程中的模块：thread和threading模块
Python提供了多个模块来支持多线程编程，包括thread、threading和Queue模块等。
- 程序是可以使用thread和threading模块来创建于管理线程。他恍然大模块提供了基本的线程和锁定支持。
- 而threading模块提供了更高级别、功能更全面的线程管理
- 一般我们建议使用threading(thread有很多缺陷，比如不支持守护线程，当主线程结束时，所有其他线程也都强制结束，而且Python3现在主推threading)

#### 3.Python中线程的使用
##### 1).线程的创建，启动，阻塞
```python
import threading 
from time import sleep,ctime

def loop(nsec):
	print('Start loop :{:>30}'.format(ctime()))
	print('Sleep {}'.format(nsec))
	sleep(nsec)
	
def main():
	print('Starting :{:>30}'.format(ctime()))
	t = threading.Thread(target=loop,args=(3,))
	
	t.start() # start the thread
	t.join()  # wait for thread finish
	
	print('All Done :{:>30}'.format(ctime()))
	
if __name__== "__main__":
	main()
```
