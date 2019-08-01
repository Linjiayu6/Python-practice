#!/usr/bin/env python
# -*- coding: utf-8 -*

# ====== 1 ======
# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。
class Animal(object):
    pass

class Runnable(object):
    def run(self):
        print 'running......'

class Dog(Animal, Runnable):
    pass

# ====== 2 Mixin ======
class Animal(object):
    pass

class RunnableMixin(object):
    def run(self):
        print 'running......'

class Dog(Animal, RunnableMixin):
    pass