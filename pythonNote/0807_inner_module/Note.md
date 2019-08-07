# 常用内建模块

## 1. collections 集合模块, 集合类

### 1.1 namedtuple
- p = (1, 2) 定义坐标, 不是很明确, 很难看出这个tuple是用来表示一个坐标的, 但是类定义, 又有点小题大做
- 
```
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p_ = Point(1, 2)

print p_.x, p_.y
```

```
# namedtuple('名称', [属性list]): 坐标+半径
Circle = namedtuple('Circle', ['x', 'y', 'r'])
```

### 1.2 deque
- 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。

- deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈

```
from collections import deque

q = deque([1, 2, 3, 4])
q.append('x')
# 0位置插入
q.appendleft('y')

# deque(['y', 1, 2, 3, 4, 'x'])
print q
```

### 1.3 defaultdict
- 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict


```
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'

# abc
print dd['key1']
# N/A
print dd['key2']
```


### 1.4 OrderedDict

- 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序
- 如果要保持Key的顺序，可以用OrderedDict
- d_ordered = OrderedDict([(k,v), (k,v)])
- d_ordered.keys()
```
from collections import OrderedDict

d = dict([('a', 1), ('b', 2), ('c', 3)])

# {'a': 1, 'c': 3, 'b': 2} key是无序的
print d

d_ordered = OrderedDict([('1', 1), ('b', 'b')])
# OrderedDict([('1', 1), ('b', 'b')])
print d_ordered, d_ordered['b']

# ['1', 'b']
print d_ordered.keys()
```

### 1.5 Counter
- Counter是一个简单的计数器

```
>>> from collections import Counter
>>> c = Counter()
>>> for ch in 'programming':
...     c[ch] = c[ch] + 1
...
>>> c
Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})
```

## 2. base64

## 3. struct
- Python没有专门处理字节的数据类型。但由于str既是字符串，又可以表示字节，所以，字节数组＝str。而在C语言中，我们可以很方便地用struct、union来处理字节，以及字节和int，float的转换

## 4. hashlib

- Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。

### 4.1 MD5
```
# -*- coding: utf-8 -*

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?')

# d26a53750bc40b38b65a520292f69306
print md5.hexdigest()
```

### 4.2 sha1
```
# -*- coding: utf-8 -*

import hashlib

sha1 = hashlib.sha1()

# 如果数据量很大，可以分块多次调用update()
sha1.update('how to use sha1 in ')
sha1.update('python hashlib?')

# 2c76b57293ce30acef38d98f6046927161b46a44
print sha1.hexdigest()

```

## 5. itertools
- Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
- import itertools
- 知道就行了, 就是个迭代器
  
```
import itertools

# # repeat('A', 10)
ns = itertools.repeat('A', 10)

# repeat('A', 10)
print(ns)

for i in ns:
    print(i)
```

## 6. XML
## 7. HTMLParser
- 爬虫需要
```
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

parser = MyHTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')

```