# 面向对象编程 Object Oriented Programming

## 1. 面向过程 vs 面向对象
- 面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。

- 而面向对象的程序设计把计算机程序视为【一组对象】的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递。

```

#!/usr/bin/env python

# -*- coding: utf-8 -*

"OOP VS PO"
__name__ = 'Lin JY'

# =========== 1. PO ===========
std1 = {
  'name': 'Jessica',
  'age': 18
}
std2 = {
  'name': 'Krystal',
  'age': 16
}

def printout(student):
  print(student['name'], student['age'])

printout(std1)
printout(std2)
"""
('Jessica', 18)
('Krystal', 16)
"""


# =========== 2. OOP ===========
class Student(object):
  def __init__(self, name, score):
    self.name = name
    self.score = score

  def print_out(self):
    print(self.name, self.score)

st1 = Student('jesscia', '100')
st2 = Student('krystal', '90')
st1.print_out()
st2.print_out()

```

