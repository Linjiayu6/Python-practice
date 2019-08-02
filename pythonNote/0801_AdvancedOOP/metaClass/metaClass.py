#!/usr/bin/env python
# -*- coding: utf-8 -*

# 当Python解释器载入hello模块时
from hello import HelloClass

# h实例变量 HelloClass类
h = HelloClass()
h.sayHello()

# type()函数可以查看一个类型或变量的类型
# <class 'hello.HelloClass'> h是实例 它的类型是class
print type(h)
# <type 'type'> HelloClass类 类的类型是type
print type(HelloClass)