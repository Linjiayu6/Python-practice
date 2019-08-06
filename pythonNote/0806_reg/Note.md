# 正则表达式

## 1. 匹配规则
- \d: 数字
  eg: '\d\d\d'可以匹配'010';
      '00\d'可以匹配'007'，但无法匹配'00A'
    
- \w: word 一个字母或数字
  eg: '\w\w\d'可以匹配'py3'

- \s: 一个空格

- \: 转义字符

- . 是匹配任意字符
  eg: 'py.'可以匹配'pyc'、'pyo'、'py!'等等

- *: 任意个数字符(0+)

- ?: 用?表示0个或1个字符

- {n}表示n个字符

- 用{n,m}表示n-m个字符

- []要做更精确地匹配 eg: [0-9a-zA-Z\_] 可以匹配一个数字、字母或者下划线 [xxx]里面的内容是或的关系
- A|B 或

- ^ 开头
  
- $ 结束

## 2. re模块
- import re
- re.match(正则, string)
```
import re
# 因此我们强烈建议使用Python的r前缀，就不用考虑转义的问题
# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None

print re.match(r'^\d{3}\-\d{5}$', '010-12345')
# 返回值 <_sre.SRE_Match object at 0x105536b90>
```

## 3. 切分字符串
- re.split('规则', string)

```
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
```

## 4. 分组 Group
除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组

- m.group()
- m.groups()
```
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
```

## 5. 贪婪匹配

```
# 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了
print re.match(r'^(\d+)(0*)$', '102300').groups()

# 非贪婪 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配
# ('1023', '00')
print re.match(r'^(\d+?)(0*)$', '102300').groups()
```

## 6. 编译执行
- a = re.compile(正则)
- a.match(string).groups()
  
```
"""
1. 编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
2. 用编译后的正则表达式去匹配字符串。
"""
# compile
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# use
print re_telephone.match('010-12345').groups()
# ('010', '12345')
```