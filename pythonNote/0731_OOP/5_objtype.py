#!/usr/bin/env python
# -*- coding: utf-8 -*

# =======  1. type() =======
"""
<type 'int'>
<type 'NoneType'>
"""
print type(123)
print type(None)


# ======= 2. isinstance() =======
class Animal (object):
    def run(self):
        print('animal ....')

class Bird (Animal):
    def run(self):
        print('Animal - Bird ....')

class Crow (Bird):
    def run(self):
        print('Animal - Bird - Crow ....')

def log(instance):
    instance.run()
    print('isinstance:', isinstance(instance, Animal))

log(Animal())
log(Bird())
log(Crow())

"""
animal ....
('isinstance:', True)
Animal - Bird ....
('isinstance:', True)
Animal - Bird - Crow ....
('isinstance:', True)
"""

# ======= 3. dir() =======

print dir('ABC')

"""
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
"""