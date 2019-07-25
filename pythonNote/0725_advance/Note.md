# 高级特性

## 1. 切片
### 1.1 取一个list或tuple的部分元素

从start开始, 取end-start的数字
```
  L[start: end]

  List = [1, 2, 3, 4, 5, 6]
  # 索引 1,2,3,4 结果: [2, 3, 4, 5]
  print(List[1:5])
```

### 1.2 负数
```
  print('取最后一个值', List[-1])
  # List[-2:] 从-2位置开始, -2-(0) = 2个元素 结果: [5, 6]
  print('取区间', List[-2:])
  # List[-2:] 从-2位置开始, -2-(-1) = 1个元素 结果: [5]
  print('取区间', List[-2:-1])
```

### 1.3 其他

```
  # 创建1-100的tuple
  L = range(1, 101)
  print(L)
  print(L[-10:])
  # 从索引1开始, 到索引8, 每两个取一个 结论: [2, 4, 6, 8]
  print(L[1:9:2])
  # 所有数据, 每10个取一个 结论: [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
  print(L[::10])
```

## 2. 迭代
- 你可以通过for in 来处理循环;
- for(i = 0; i < len(L); i++)

### 2.1 迭代List/Tuple
- * [list, tuple, dict 都可以迭代];
  因为Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。
   ```
    >>> d = {'a': 1, 'b': 2, 'c': 3}
    >>> for key in d:
    ...     print key
    ...
    a
    c
    b
   ```

### 2.2 迭代dict
- 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.itervalues()，如果要同时迭代key和value，可以用for k, v in d.iteritems()。
  ```
  for value in Dict.itervalues():
    print(value)

  for key, value in Dict.iteritems():
    print(key, value)

  ```
### 2.3 迭代string
- * [string 可以迭代];
  
### 2.4 是否可以迭代判断
  ```
    >>> from collections import Iterable
    >>> isinstance('abc', Iterable) # str是否可迭代
    True
    >>> isinstance([1,2,3], Iterable) # list是否可迭代
    True
    >>> isinstance(123, Iterable) # 整数是否可迭代
    False
  ```

### 2.5 如何索引+value 迭代返回呢?
Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
  ```
  L = (5, 4, 3, 2, 1)

  for i, value in enumerate(L):
    print(i, value)
    '''
    (0, 5)
    (1, 4)
    (2, 3)
    (3, 2)
    (4, 1)
    '''
  ```

## 3.列表生成式
### 3.1 简易写法
- 举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用range(1, 11)：

- 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
  ```
    # 生成为[1x1, 2x2, 3x3, ..., 10x10]
    L = []
    for i in range(1, 11):
      L.append(i * i)

    print(L)

    # 但是这么写很蠢, 很长
    L1 = [i * i for i in range(1, 11)]
    print(L1)
  ```

### 3.2 有判断条件写法
```
  L2 = [j * j for j in range(1, 11) if j % 2 == 1]
```

### 3.3 两层循环写法
```
  list1 = ['A', 'B', 'C']
  list2 = ['X', 'Y', 'Z', 'A']
  
  # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'BA', 'CX', 'CY', 'CZ', 'CA']

  L3 = [ m+n for m in list1 for n in list2 if m != n]
  # 1. for m in list1;
  # 2. for n in list2;
  # 3. if m != n;
  # 4. m+n
  print(L3)
```

### 3.4 Dict写法
```
  Dict = { '1': 9, '2': 8, '3': 7, '4': 6 }
  Dict_new = [{ value: key } for key, value in Dict.iteritems()]
  print(Dict_new)
```


## 4.生成器
- 背景: 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

- 解决: 在Python中，这种一边循环一边计算的机制，称为生成器（Generator）。

- 创建: 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator

```
  # list
  L = [x * x for x in range(10)]
  # tuple
  TupleGenerator = (x * x for x in range(10))

  print(L)
  # <generator object <genexpr> at 0x103c06a00>
  print(TupleGenerator)
  print(TupleGenerator.next()) # 0
  print(TupleGenerator.next()) # 1
  print(TupleGenerator.next()) # 4
  print(TupleGenerator.next()) # 9
  print(TupleGenerator.next()) # 16

  # 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
```

但是使用xx.next()太变态了, 还是使用for in 来循环输出结果
```
>>> g = (x * x for x in range(10))
>>> for n in g:
...     print n
...
0
1
4
9
16
25
36
49
64
81
```