
# -*- coding: utf-8 -*
from collections import OrderedDict

d = dict([('a', 1), ('b', 2), ('c', 3)])

# {'a': 1, 'c': 3, 'b': 2} key是无序的
print d

d_ordered = OrderedDict([('1', 1), ('b', 'b')])
# OrderedDict([('1', 1), ('b', 'b')])
print d_ordered, d_ordered['b']

# ['1', 'b']
print d_ordered.keys()
