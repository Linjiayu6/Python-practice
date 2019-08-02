# 错误、调试和测试

## 1. 错误处理
- Python内置的try...except...finally用来处理错误十分方便。出错时，会分析错误信息并定位错误发生的代码位置才是最关键的。

### 1.1 try... except
1. try
2. except StandardError, e:
3. finally 不管是否成功都会执行, 不是必须的;
   
```
"""
当我们认为某些代码可能会出错时，就可以用try来运行这段代码，
如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，
即except语句块，执行完except后，
如果有finally语句块，则执行finally语句块，至此，执行完毕。
"""
try:
    print 'try .....'
    r = 10 / 0
    print '10 / 0', r
except StandardError, e:
    print 'except:', e
finally:
    print 'finally .....'
print 'END.......'

"""
$ python try.py
try .....
except: integer division or modulo by zero
finally .....
END.......

"""
```

### 1.2 记录错误
- 如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。

```
import logging

def foo(s):
    return 10 / int(s)

def main():
    try:
        foo('0')
    except StandardError, e:
        # logging.exception(e)
        # 如果没有一行就会输出
        """
        $ python log.py
          File "log.py", line 11
            main()
            ^
        IndentationError: expected an indented block
        """
main()

"""
同样是出错，但程序打印完错误信息后会继续执行，并正常退出
通过配置，logging还可以把错误记录到日志文件里，方便事后排查。

ERROR:root:integer division or modulo by zero
Traceback (most recent call last):
  File "log.py", line 8, in main
    foo('0')
  File "log.py", line 4, in foo
    return 10 / int(s)
ZeroDivisionError: integer division or modulo by zero
"""
```

### 1.3 自定义抛出错误
- 因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。

```
class FooError(StandardError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')
```

## 2. 调试
- print 方式
- 或者 logging方式

### 2.1 print粗暴
### 2.2 断言
```
# err.py
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')
```
### 2.3 logging
- 把print替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件
- 这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。

```
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print 10 / n
```

### 2.4 pdb
- pdb.set_trace()运行到这里会自动暂停, 类似JS的debugger 


## 3. 单元测试
## 4. 文档测试
