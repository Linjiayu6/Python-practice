# -*- coding: utf-8 -*

# 1.生成为[1x1, 2x2, 3x3, ..., 10x10]
L = []
for i in range(1, 11):
  L.append(i * i)

print(L)

# 但是这么写很蠢, 很长
L1 = [i * i for i in range(1, 11)]
print(L1)

# 2. 奇数*奇数, 生成为[1x1, 3x3, ..., 9*9]
L2 = [j * j for j in range(1, 11) if j % 2 == 1]
print(L2)

# 3. 有两层循环写法
list1 = ['A', 'B', 'C']
list2 = ['X', 'Y', 'Z', 'A']
# ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'BA', 'CX', 'CY', 'CZ', 'CA']
L3 = [ m+n for m in list1 for n in list2 if m != n]
# 1. for m in list1;
# 2. for n in list2;
# 3. if m != n;
# 4. m+n
print(L3)

# 4. Dict写法
Dict = { '1': 9, '2': 8, '3': 7, '4': 6 }
Dict_new = [{ value: key } for key, value in Dict.iteritems()]
print(Dict_new)
# [{9: '1'}, {7: '3'}, {8: '2'}, {6: '4'}]