#!/usr/bin/env python
# -*- coding: utf-8 -*


# ========== 1 ==========
# 类
class Student(object):
    pass

# 实例
instance = Student()

# <class '__main__.Student'>
print(Student)
# 输出: <__main__.Student object at 0x1032f8c10>
print(instance)

# ========== 2 ==========
# 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上
class Student1(object):
    # self为创建实例本身 就可以把各种属性绑定到self
    def __init__(self, name, score):
        self.name = name
        self.score = score

instance_st1 = Student1('linjiayu', 180)
print(instance_st1.name)
print(instance_st1.score)


# ========== 3 数据封装 ==========
class Student2(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def printout(self):
        level = self.scoreLevel()
        print('name:', self.name, ' score: ', self.score, 'level', level)

    def scoreLevel(self):
        if self.score >= 90:
            return 'A'
        else: 
            return 'C'

instance_st2 = Student2('Sensational', 90)
instance_st2.printout()