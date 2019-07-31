#!/usr/bin/env python
# -*- coding: utf-8 -*

# =======  1. 访问限制 - 随意变更对象内容 =======
class Student(object):
    def __init__(self, name):
        self.name = name
    def printout(self):
        print(self.name)
        
instance_st = Student('linjiayu')
instance_st.printout()

# 从外部修改内容
instance_st.name = 'who are you'
# 值已经变化了 输出为'who are you'
instance_st.printout()

# =======  2. 访问限制 - 变为私有属性 禁止外部去访问 =======
class Student1(object):
    def __init__(self, name):
        self.__name = name
    def printout(self):
        print(self.__name)
        
instance_st1 = Student1('linjiayu')
instance_st1.printout()

# 从外部修改内容
instance_st1.name = 'who are you'
# 没有变化输出为'linjiayu'
instance_st1.printout()

# =======  3. 访问限制 - 想要获取内部信息怎么办 =======
class Student2(object):
    def __init__(self, name):
        self.__name = name
    # 允许外部获取
    def get_name(self):
        return self.__name
    # 允许外部修改
    def set_name(self, name):
        self.__name = name
        

instance_st2 = Student2('xxxxxx')
print(instance_st2.get_name())
instance_st2.set_name('xxxx change to AAAA')
print(instance_st2.get_name())