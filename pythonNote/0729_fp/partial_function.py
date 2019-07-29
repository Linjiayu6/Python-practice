# -*- coding: utf-8 -*

# ======= 1 ========
# int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：
print(int('12345'))

# ======= 2 结果64 string转换二进制========
print(int('1000000', 2))

# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
import functools
int2 = functools.partial(int, base=2)
print(int2('1000000'))
