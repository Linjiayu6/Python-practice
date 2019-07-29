# -*- coding: utf-8 -*

# ======= 1. map ========
def fx(i):
  return i * 5

# L = map(函数方法, 数据)
L = map(fx, range(2, 6))
print(L)

# ======= 2. map ========
# ['0', '1', '2', '3', '4']
L1 = map(str, range(5))
print(L1)

# ======= 3. reduce ========
# 求和
def add(d1, d2):
  print(d1, d2)
  return d1 + d2

L_reduce = reduce(add, [1,2,3,4])
"""
输出为:
(1, 2)
(3, 3)
(6, 4)
"""
print(L_reduce)

# ======= 4. reduce ========
# 要把序列[1, 3, 5, 7, 9]变换成整数13579
def reduce_add (d1, d2):
  print(d1, d2)
  return d1*10 + d2
L_reduce_1 = reduce(reduce_add, [1, 3, 5, 7, 9])
"""
(1, 3) - 13
(13, 5) - 135
(135, 7) - 1357
(1357, 9) - 13579
"""
print(L_reduce_1)

# ======= 5. map 练习 ========
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
L_pratice = map(lambda L:L.title(),['adam', 'LISA', 'barT'])
print(L_pratice)

