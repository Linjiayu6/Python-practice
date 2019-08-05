# IO编程

- IO在计算机中指Input/Output，也就是输入和输出
- 涉及到数据交换的地方，通常是磁盘、网络等，就需要IO接口
  
- IO编程中，Stream（流）是一个很重要的概念，可以把流想象成一个水管，数据就是水管里的水，但是只能单向流动。Input Stream就是数据从外面（磁盘、网络）流进内存，Output Stream就是数据从内存流到外面去。对于浏览网页来说，浏览器和新浪服务器之间至少需要建立两根水管，才可以既能发数据，又能收数据。
- 同步IO 异步IO. 使用异步IO来编写程序性能会远远高于同步IO，但是异步IO的缺点是编程模型复杂
- 想想看，你得知道什么时候通知你“汉堡做好了”，而通知你的方法也各不相同。如果是服务员跑过来找到你，这是回调模式，如果服务员发短信通知你，你就得不停地检查手机，这是轮询模式。总之，异步IO的复杂度远远高于同步IO
- https://www.liaoxuefeng.com/wiki/897692888725344/923055899540352


## 1. 文件读写

### 1.1 读文件
- f = open(path, 'r') 读文件, 占用内存
- f.read() 输出文本内容
- f.close() 用完释放掉内存资源
  
```
    def readFile ():
    try:
        # r: read
        f = open('./hello.txt', 'r')
        # <open file './hello.txt', mode 'r' at 0x10f8155d0>
        print f
        print f.read()

    except IOError:
        print 'No this file'

    finally:
        # close file 
        # 文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的
        if f:
            f.close()
```

### 1.2 二进制文件

- 前面讲的默认都是读取文本文件，并且是ASCII编码的文本文件。要读取二进制文件，比如图片、视频等等
- f = open('/Users/michael/test.jpg', 'rb')

```
def readRB ():
    img = open('./img.png', 'rb')
    print img.read()
    img.close()
```

### 1.3 写文件
- f = open('path', 'w')
- f.write('content')
```
def writeContent ():
    f = open('./write.txt', 'w')
    f.write('wirte content')
    f.close()
```

### 1.4 with调用帮助我们调用close
- with 语句适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的“清理”操作，释放资源，比如文件使用后自动关闭／线程中锁的自动获取和释放等。
- with open(path) as f:
    f.xxxx()

```
def useWith ():
    with open('./write.txt') as f:
        print f.read()

useWith()
```


## 2. 操作文件和目录

### 2.1 os module

```
import os
# posix, 如果是posix，说明系统是Linux、Unix或Mac OS X
print os.name

# 详情
# ('Darwin', 'linjiayudeMacBook-Pro.local', '17.7.0', 'Darwin Kernel Version 17.7.0: Wed Apr 24 21:17:24 PDT 2019; root:xnu-4570.71.45~1/RELEASE_X86_64', 'x86_64')
print os.uname()

# 环境变量
"""
{'LESS': '-R', 'VERSIONER_PYTHON_PREFER_32_BIT': 'no', .....
"""
print os.environ

"""
/Users/linjiayu/pay/flutter/flutter_bash_profile/bin:/Users/linjiayu/.yarn/bin:/usr/local/bin:/Users/linjiayu/.nvm/versions/node/v10.0.0/bin:/Users/linjiayu/bin:/usr/local/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/go/bin
"""
print os.getenv('PATH')

```

### 2.2 创建文件夹 / 删除、操作
- os.mkdir(folderpath)
- os.rmdir(folderpath)
- 绝对路径 os.path.abspath('.')
- 拆分路径 os.path.split('/Users/michael/testdir/file.txt') -> ('/Users/michael/testdir', 'file.txt')
- os.path.splitext('/path/to/file.txt') -> ('/path/to/file', '.txt')
- 重命名 os.rename('test.txt', 'test.py')
- 删掉文件 os.remove('test.py')
- 遍历文件夹下的所有文件内容 [x for x in os.listdir('.')]
- https://www.liaoxuefeng.com/wiki/897692888725344/923055916315360

```
import os

# 绝对路径
# /Users/xxx/xxx/Spider-python/pythonNote/0805_IO/os
folder = os.path.abspath('.')
os.mkdir(folder+'/create')

# 删除操作 os.rmdir(xxxx)

# ('/Users/michael/testdir', 'file.txt')
print os.path.split('/Users/michael/testdir/file.txt')
```

## 3. 序列化

Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块

### 3.1 JSON
- import json
- json_str = json.dumps(dictionary)
- dictionary = json.loads(json_str)
  
```
# JSON方法
import json

json_str = json.dumps(d)
# {"age": "18", "univ": "HKBU", "name": "LinJY"}
print type(json_str)
# <type 'str'>

# {u'age': u'18', u'univ': u'HKBU', u'name': u'LinJY'} <type 'dict'>
json_obj = json.loads(json_str)
print json_obj, type(json_obj)
```

### 3.2 JSON进阶

- Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化

- 错误的原因是Student对象不是一个可序列化为JSON的对象
```
import json

# 用class来表示对象
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

# <__main__.Student object at 0x1085d9350>
s = Student('lin', '100')

"""
抛出异常: 错误的原因是Student对象不是一个可序列化为JSON的对象。
TypeError: <__main__.Student object at 0x1022d72d0> is not JSON serializable
"""
s_str = json.dumps(s)
print s_str
```

- 是因为默认情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象
- 我们需要手动转化为dict类型, 再操作json.dumps(dict)
```
# 需要转化一次
def toDict(class_obj):
    return dict(
        name = class_obj.name,
        score = class_obj.score
    )

# parse() 对象或字典类型 {'score': '100', 'name': 'lin'}
s_dict = toDict(s)

# stringify() {"score": "100", "name": "lin"}
print json.dumps(s_dict)
```