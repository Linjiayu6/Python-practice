# -*- coding: utf-8 -*

# tuple: 另一种有序列表叫元组。tuple和list非常类似，但是tuple一旦初始化就不能修改
# 当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
# 它也没有append()，insert()这样的方法

# 意义: 因为tuple不可变，所以代码更安全。如果可能, 能用tuple代替list就尽量用tuple

a_tuple = ('1', '3', '2')
print(a_tuple)


# 为什么说tuple不变, 但是依旧变化了呢。
# https://www.liaoxuefeng.com/wiki/897692888725344/923028986786528 详解
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
