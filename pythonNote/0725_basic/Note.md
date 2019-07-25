# Python 基础

## 1. 数据类型
1. Integer
2. Float eg:  3.14
   整数运算永远是精确的, 而浮点数运算则可能会有四舍五入的误差
   无论整数做除法还是取余数，结果永远是整数，所以，整数运算结果永远是精确的
    <pre>
      >>> 10 / 3
      3
      >>> 10.0 / 3
      3.3333333333333335
    </pre>
3. String
4. Boolean True, False
5. None 空值

## 2. 变量
说明地址: https://www.liaoxuefeng.com/wiki/897692888725344/897693179535744

<pre>
a = 'ABC'
b = a
a = 'XYZ'
print b

1. 执行a = 'ABC'，解释器创建了字符串'ABC'和变量a，并把a指向'ABC'
2. 解释器创建了变量b，并把b指向a指向的字符串'ABC'
3. 解释器创建了字符串'XYZ'，并把a的指向改为'XYZ'，但b并没有更改
4. b值为'ABC'
</pre>

## 3. 常量
全部大写的变量名表示常量
PI = 3.14159265359

## 4. list / tuple 
### 4.1 list
Python内置的一种数据类型是列表：list。
list是一种有序的集合，可以随时添加和删除其中的元素。

### 4.2 tuple
另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改

现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法

详解: https://www.liaoxuefeng.com/wiki/897692888725344/923028986786528
<pre>
>>> t = ('a', 'b', ['A', 'B'])
>>> t[2][0] = 'X'
>>> t[2][1] = 'Y'
>>> t
('a', 'b', ['X', 'Y'])
</pre>

表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素

## 5. 循环两种
### 5.1 for ... in
<pre>
  names = [1, 2, 3, 4]
  for name in names:
    print(name)
</pre>

### 5.2 while

## 6. 使用dict和set
### 6.1 dict
= dictionary 其他语言是个map (key-value)存储
<pre>
和list比较，dict有以下几个特点：
查找和插入的速度极快，不会随着key的增加而增加；
需要占用大量的内存，内存浪费多。

而list相反：
查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
</pre>

### 6.2 set
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

set和dict的唯一区别仅在于没有存储对应的value
