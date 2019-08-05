
# -*- coding: utf-8 -*

# js对象序列化JSON.stringify()与反序列化JSON.parse()

# 1. 定义一个dictionary, 序列化

"""
[我们把变量从内存中变成可存储或传输的过程称之为序列化]

在Python中叫pickling，
在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思
"""
d = dict( name = "LinJY", age = "18", univ = "HKBU" )
print d
# {'age': '18', 'univ': 'HKBU', 'name': 'LinJY'}

# 2. 反序列化
"""
[把变量内容从序列化的对象重新读到内存里称之为反序列化]

Python提供两个模块来实现序列化：cPickle和pickle。
这两个模块功能是一样的，区别在于cPickle是C语言写的，速度快，
pickle是纯Python写的，速度慢，跟cStringIO和StringIO一个道理。
用的时候，先尝试导入cPickle，如果失败，再导入pickle
"""

try:
    import cPickle as pickle
except ImportError:
    import pickle

# pickle.dumps()方法把任意对象序列化成一个str
# object -> str
string = pickle.dumps(d)
print string
"""
(dp1
S'age'
p2
S'18'
p3
sS'univ'
p4
S'HKBU'
p5
sS'name'
p6
S'LinJY'
p7
s.
"""

# JSON方法
import json

json_str = json.dumps(d)
# {"age": "18", "univ": "HKBU", "name": "LinJY"}
print type(json_str)
# <type 'str'>

# {u'age': u'18', u'univ': u'HKBU', u'name': u'LinJY'} <type 'dict'>
json_obj = json.loads(json_str)
print json_obj, type(json_obj)