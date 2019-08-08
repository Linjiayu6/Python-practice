# -*- coding: utf-8 -*

"""
1. 访问list中元素
- L[index] eg: L[0] L[-1]
- L[first: last] eg: index from first to last - 1 and len = last - first
- L[first:] eg: L[2:] 从第二个开始到最后
"""
L = range(1, 6) # [1, 2, 3, 4, 5]
print L[0] # 1
print L[-1] # 5
print L[2:4] # [3,4]


"""
2. 基本用法
- 长度 len(L)
- 合并 L = L1 + L2
- 重复 [L] * 5
- 值是否在数组中 'j' in L; 不在 'j' not in L
- 迭代 for i in L: xxx
"""

print len(L)
print [1,2,3] + [4,5,6]
print ['L'] * 6
print 4 in L

"""
5
[1, 2, 3, 4, 5, 6]
['L', 'L', 'L', 'L', 'L', 'L']
True
"""

"""
3. 其他
- 求数组中最大值, 最小值: max(L) min(L)
- 字符串/元组 变为 列表: list(seq)
"""
L1 = [1,2,3,4,5]
print max(L1) # 5
print min(L1) # 1

print list('09876') # ['0', '9', '8', '7', '6']
print list((1,2,3,4)) # [1, 2, 3, 4]

"""
4. 方法
- 添加元素: list.append(值)
- 删除元素by索引: list.pop(index索引)
- 删除列表中某个值by匹配第一个值: list.remove(值)
- 某个元素在list中出现的个数: list.count(值)
- 获取值的索引: list.index(值)
- 排序: sorted(list); list.sort()
- 反转: 是0这个位置去了 -1, 1值去了-2 list.reverse()
"""
L2 = [6, 6, 6, 7, 8]
L2.append(9)
print L2 # [6, 6, 6, 7, 8, 9]

print L2.pop(0) # 6
print L2 # [6, 6, 7, 8, 9]

# [6, 6, 7, 8, 9]
L2.remove(7)
print L2 # [6, 6, 8, 9]

print L2.count(6) # 2
print L2.index(9) # 3

L3 = [10, 2, 6, 6, 6, 7, 8]
print sorted(L3) # [2, 6, 6, 6, 7, 8, 10]

L3.reverse() # [8, 7, 6, 6, 6, 2, 10]
print L3

L3.sort()
print L3 # [2, 6, 6, 6, 7, 8, 10]
L3.sort(reverse=True)
print L3 # [10, 8, 7, 6, 6, 6, 2]