
# -*- coding: utf-8 -*

# list
L = [x * x for x in range(10)]
# tuple
TupleGenerator = (x * x for x in range(10))

print(L)
# <generator object <genexpr> at 0x103c06a00>
print(TupleGenerator)
print(TupleGenerator.next()) # 0
print(TupleGenerator.next()) # 1
print(TupleGenerator.next()) # 4
print(TupleGenerator.next()) # 9
print(TupleGenerator.next()) # 16

# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
