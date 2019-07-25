# -*- coding: utf-8 -*

L = range(5)
Dict = {
  'NAME': 11,
  'ID': 5,
  'AGE': 100
}

for item in L:
  print(item)

# 取的是key值
for key in Dict:
  print(key)

"""
0
1
2
3
4
AGE
NAME
ID
"""

# 取的是value值
for value in Dict.itervalues():
  print(value)

"""
ID
100
11
5
"""

# key, value都想获取
for key, value in Dict.iteritems():
  print(key, value)
"""
('AGE', 100)
('NAME', 11)
('ID', 5)
"""