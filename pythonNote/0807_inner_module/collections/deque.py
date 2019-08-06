# -*- coding: utf-8 -*

from collections import deque

q = deque([1, 2, 3, 4])
q.append('x')
# 0位置插入
q.appendleft('y')

# deque(['y', 1, 2, 3, 4, 'x'])
print q