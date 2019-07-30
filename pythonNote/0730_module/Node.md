# 模块

- 举个例子，一个abc.py的文件就是一个名字叫abc的模块。
- 每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的。

## 1. 使用模块
### 1.1 使用模块基本
```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
' a test module '
# __author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；
__author__ = 'Lin JY'

"""
sys模块有一个argv变量，用list存储了命令行的所有参数
运行python hello.py获得的sys.argv就是['hello.py']
运行python hello.py Michael获得的sys.argv就是['hello.py', 'Michael]

$ python hello.py linjiayu1 linjiayu2 linjiayu3
('Too many arguments!', ['hello.py', 'linjiayu1', 'linjiayu2', 'linjiayu3'])
"""
import sys

def test():
  args = sys.argv
  if len(args) == 1:
    print('hello', args)
  else:
    print('Too many arguments!', args)

if __name__ == '__main__':
  test()
  
```

### 1.2 别名
还有类似simplejson这样的库，在Python 2.6之前是独立的第三方库，从2.6开始内置，所以，会有这样的写法：
```
try:
    import json # python >= 2.6
except ImportError:
    import simplejson as json # python <= 2.5
```

### 1.3 作用域
- (1) 正常的函数和变量名是public, 可以直接被引用的, 例如 abc, bcd
- (2) __xxx__ 是特殊变量, 例如上述 __author__，__name__就是特殊变量。我们自己的变量一般不要用这种变量名
- (3) 类似_xxx和__xxx这样的函数或变量就是private, 例如_abc, __abc


```
def _private_1(name):
    return 'Hello, %s' % name

def greeting(name):
    return _private_1(name)
```

## 2. 第三方库 Python packages 
- 类似npm这样
- 地址: https://pypi.org/
- 其他说明: https://www.liaoxuefeng.com/wiki/897692888725344/923030461085920
- 安装: pip install xxx

## 3. __future__
- 为了兼容Python 2.7和Python 3.x的改动
- 从Python 2.7到Python 3.x就有不兼容的一些改动, 要直接把代码升级到3.x是比较冒进的，因为有大量的改动需要测试

- Python提供了__future__模块，把下一个新版本的特性导入到当前版本，于是我们就可以在当前版本中测试一些新版本的特性。

```
# still running on Python 2.7

from __future__ import unicode_literals

print '\'xxx\' is unicode?', isinstance('xxx', unicode)
print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
print '\'xxx\' is str?', isinstance('xxx', str)
print 'b\'xxx\' is str?', isinstance(b'xxx', str)
```