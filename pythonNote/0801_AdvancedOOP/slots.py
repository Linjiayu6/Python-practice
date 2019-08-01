#!/usr/bin/env python
# -*- coding: utf-8 -*

# ====== 1 ======
"""
1. 我们可以对任何一个实例绑定一个属性 或者是 方法
"""
class Student (object):
    pass

s = Student()
s.name = 'LinJY'

# 给实例绑定一个方法
from types import MethodType
def getName(self):
    print self.name

s.getName = MethodType(getName, s, Student)

print s.name
s.getName()

# ====== 2 __slots__ ======
class Student1(object):
    __slots__ = ('name', 'age')
    # 只接收name 和 age

s1 = Student1()
s1.name = 'linjiayu' # 绑定属性'name'
s1.age = '18' # 绑定属性'age'
# 这个会报错的
# s1.score = 100 # 绑定属性'score'

"""
Traceback (most recent call last):
  File "slots.py", line 33, in <module>
    s1.score = 100 # 绑定属性'score'
AttributeError: 'Student1' object has no attribute 'score'
"""

# ====== 3 __slots__ 只对当前类起作用 ======
class Student2(Student1):
    pass
s2 = Student2()
s2.score = '100'