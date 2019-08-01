#!/usr/bin/env python
# -*- coding: utf-8 -*

# ====== 1 ======
"""
限制值的输入, 例如score, 范围是在1-100分之间
- 1. 限制值
"""
class Student (object):
    def get_score(self):
        return self._score

    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError('Score must be integer')
        if score < 0 or score > 101:
            raise ValueError('Score must between 0 ~ 100')
        self._score = score

s = Student()
# 这样不做校验不合适
# s.score = 999
s.set_score(99)
print s.get_score()


# ====== 2 简化流程 有没有既能检查参数，用类似属性这样简单的方式来访问类的变量 ======
class Student1 (object):
    
    # 把一个getter方法变成属性，只需要加上@property就可以了
    @property
    def score(self):
        return self._score

    # @property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
    @score.setter
    def score(self, score):
        self._score = score

s1 = Student1()

s1.score = 11  # 类似上面1例子的 实际转化为s.set_score(11)
print s1.score # 类似上面1例子的 实际转化为s.get_score()
