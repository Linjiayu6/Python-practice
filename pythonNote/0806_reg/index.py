# -*- coding: utf-8 -*

import re
# 因此我们强烈建议使用Python的r前缀，就不用考虑转义的问题
# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None

print re.match(r'^\d{3}\-\d{5}$', '010-12345')
# 返回值 <_sre.SRE_Match object at 0x105536b90>

# 2. 切分字符串

string = 'a b   c'
# ['a', 'b', '', '', 'c']
print string.split(' ')
# ['a', 'b', 'c']
print re.split('\s+', string)

['a', 'b', 'c', 'd']
string1 = 'a,b, c  d'
print re.split('[\s\,]*', string1)

string2 = 'a,b,; c  ;d'
# ['a', 'b', 'c', 'd']
print re.split('[\s\,\;]*', string2)


# 3. 分组
# 注意到group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串。
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print m.group()
print m.group(0)
print m.group(1)
print m.group(2)

# 提取子串非常有用
print m.groups()

"""
010-12345
010-12345
010
12345
('010', '12345')
"""

# 4. 贪婪匹配
# ('102300', '')

# 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了
print re.match(r'^(\d+)(0*)$', '102300').groups()

# 非贪婪 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配
# ('1023', '00')
print re.match(r'^(\d+?)(0*)$', '102300').groups()

# 5. 编译
"""
1. 编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
2. 用编译后的正则表达式去匹配字符串。
"""
# compile
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# use
print re_telephone.match('010-12345').groups()
# ('010', '12345')