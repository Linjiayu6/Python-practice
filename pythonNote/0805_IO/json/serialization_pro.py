# -*- coding: utf-8 -*
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
# s_str = json.dumps(s)
# print s_str

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
