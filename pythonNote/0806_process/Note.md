
# 进程和线程

- 本章除了概念, 代码部分没有怎么看, 还是多看看官方案例吧

- 多任务: 就是操作系统可以同时运行多个任务
  eg: 打个比方，你一边在用浏览器上网，一边在听MP3，一边在用Word赶作业，这就是多任务，至少同时有3个任务正在运行。还有很多任务悄悄地在后台同时运行着，只是桌面上没有显示而已。

- 单核CPU: 操作系统轮流让各个任务交替执行。任务1执行0.01秒，切换到任务2，任务2执行0.01秒，再切换到任务3，执行0.01秒……这样反复执行下去。

- 如果多核情况, 但是任务数量远远多于CPU的核心数量?
  操作系统也会自动把很多任务轮流调度到每个核心上执行。

- [Process: 一个任务就是一个进程]
  eg: 比如打开一个浏览器就是启动一个浏览器进程，打开一个记事本就启动了一个记事本进程

- [Thread: 线程 一个进程内部需要有很多子任务, 子任务是线程]
  有些进程还不止同时干一件事，比如Word，它可以同时进行打字、拼写检查、打印等事情。在一个进程内部，要同时干多件事，就需要同时运行多个“子任务”，我们把进程内的这些“子任务”称为线程


# 1. 多进程 multiprocessing

## 1.1 多进程

- Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。

- 子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。


```

import os

print 'Process (%s) start...' % os.getpid()
pid = os.fork()
if pid == 0 :
    print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())

else:
    print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)

"""
Process (65306) start...
I (65306) just created a child process (65307).
I am child process (65307) and my parent is 65306.
"""
```

## 1.2 进程间通信
- https://www.liaoxuefeng.com/wiki/897692888725344/923056295693632


## 1.3 Pool

# 2. 多线程 threading

## 2.1 创建多线程
```
# -*- coding: utf-8 -*

import time, threading

def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print 'thread %s ended.' % threading.current_thread().name

print 'thread %s is running...' % threading.current_thread().name
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print 'thread %s ended.' % threading.current_thread().name
```
- 由于任何进程默认就会启动一个线程，我们把该线程称为主线程
- 主线程又可以启动新的线程
- current_thread()函数，它永远返回当前线程的实例
- 主线程实例的名字叫MainThread

## 2.2 Lock

- 多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，[线程之间共享数据] 最大的危险在于多个线程同时改一个变量，把内容给改乱了

数据共享搞乱情况:
```
import time, threading

# 假定这是你的银行存款:
balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance
```