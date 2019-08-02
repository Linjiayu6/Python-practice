#!/usr/bin/env python
# -*- coding: utf-8 -*

# ====== 1 定制类 ======
class Student (object):
    def __init__ (self, name):
      self.name = name

# <__main__.Student object at 0x10fb34210> 输出的不好看
print Student('string')


# ====== 2 定制类 __str__ ======

class Student1 (object):
    def __init__ (self, name):
        self.name = name
    def __str__ (self):
        return self.name

# name
print Student1('name')
