
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
