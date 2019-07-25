# Python 函数

## 1. 调用函数
http://docs.python.org/2/library/functions.html#abs

### 1.1 内置函数
eg: abs(-20) ...

### 1.2 数据类型转换
eg:
- int('100')
- str(1.23)
- bool(1)

## 2. 定义函数
```
def x():
  return
```
1. 什么都不做 pass
```
def x():
  if a > 10:
    pass
```

2. 返回多个值
```
def x ():
  return a, b

a, b = x()
或者
value = x()

Python的函数返回多值其实就是返回一个tuple(不可变的数组)

```

## 3. 函数的参数
```
name: required
gender: options
def fx(name, gender = 1):
  xxxxx
```

### 3.1 参数
```
def y(L = []):
    L.append(1)
    print L
y() # [1]
y() # [1, 1]
y() # [1, 1, 1]

# ???? 因为默认参数L也是一个变量, 它指向对象[], 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了
# 所以，定义默认参数要牢记一点：默认参数必须指向不变对象！

def y1(L = None):
    if L is None:
        L = []
    L.append(1)
    print L
y1() # [1]
y1() # [1]
```

### 3.2 可变参数
```
def y2(*nums):
    print(nums)
```

### 3.3 关键字参数
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

关键字参数有什么用？它可以扩展函数的功能.

```
def keyParams (a, b, **kv):
    print(a, b, kv)

# (1, 2, {})
keyParams(1, 2)
# (1, 2, {'cityId': 666, 'cityName': 'Beijing'})
keyParams(1, 2, cityId = 666, cityName = 'Beijing')
```

### 3.4 参数组合
1. 必选参数
2. 默认参数 a = []
3. 可变参数 *args: *args是可变参数，args接收的是一个tuple
4. 关键字参数 **kw: **kw是关键字参数，kw接收的是一个dict

```
def combine (required, options = 1, *args, **kv):
  xxxxx

combine(
  '2required value',
  200, 
  4,(1,2),6,[1],7,
  name='linjiayu', age=18, key='value'
)
```

## 递归函数
https://www.liaoxuefeng.com/wiki/897692888725344/897693398334720