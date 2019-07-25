# -*- coding: utf-8 -*

# list是一种有序的集合
a_list = ['1', 1, 2, 3]
print(a_list, len(a_list))
print(a_list[0])
print(a_list[-1])

# 类似push: append
a_list.append('4')
# 插入指定的位置
a_list.insert(1, ['lin', 'jia', 'yu'])

# ['1', ['lin', 'jia', 'yu'], 1, 2, 3, '4']
print(a_list)
# yu
print(a_list[1][2])
