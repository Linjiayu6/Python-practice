# 函数式编程 Functional Programming

## 1. 面向过程编程设计

函数是Python内建支持的一种封装，我们通过把大段代码拆成函数，通过一层一层的函数调用，就可以把复杂任务分解成简单的任务，这种分解可以称之为面向过程的程序设计。函数就是面向过程的程序设计的基本单元。

## 2. 函数式编程
任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用

## 3. 高阶函数 Higher-order function
### 3.1 map
```
def fx(data):
 return data * 3

L = map(fx, range(5))
```

### 3.2 reduce
reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算.
- reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

```
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
```

### 3.3 filter
和map()类似，filter()也接收一个函数和一个序列。和map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
```
过滤条件为是双数
L = filter(lambda l: l % 2 == 0,[1,2,3,4,5,6])
# [2, 4, 6]
print(L)
```

### 3.4 sorted
https://www.liaoxuefeng.com/wiki/897692888725344/989703140943904
```
L = sorted([11,22,1,5,2])
print(L)
```

## 4. 返回函数
高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
```
def fx(*args):
  def double():
    return map(lambda l: l*2, args)
  return double

init = fx(1,2,3,4,5)
"""
<function double at 0x10b5d2140>
[2, 4, 6, 8, 10]
"""
print(init)
print(init())
```

### 4.1 闭包
注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。

## 5 匿名函数
关键字lambda表示匿名函数，冒号前面的l表示函数参数。
```
L = map(lambda l: l*100, range(1, 5))
```

## 6 装饰器
装饰器的本质是一个函数, 一个通用的功能, 可以用到不同的功能函数上, 避免每次都写重复的功能代码
其实就是: 你将一个函数放入到一个闭包运算中

```
def decorator(func):
  def wrapper(param):
    print 'start'
    func(param)
    print 'end'
  return wrapper

@decorator
def test(param):
  print "run with param %s"%(param)

# test = decorator(test)
test('test ....')

```

## 7 偏函数
Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）

```
import functools
int2 = functools.partial(int, base=2)
print(int2('1000000'))
```
