# 面向对象高级编程
我们会讨论多重继承、定制类、元类等概念

## 1. 使用__slots__
- 我们可以为实例绑定任意一个方法和属性, 但是如果只想指定绑定的值, 就需要用__slots__
- 使用__slots__要注意，__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的

### 1.1 我们可以对实例绑定任一一个属性或者是方法
```
"""
1. 我们可以对任何一个实例绑定一个属性 或者是 方法
"""
class Student (object):
    pass

s = Student()
s.name = 'LinJY'

# 给实例绑定一个方法
from types import MethodType
def getName(self):
    print self.name

s.getName = MethodType(getName, s, Student)

print s.name
s.getName()

```

### 1.2 想限制添加的属性使用__slots__
如果我们想要限制class的属性怎么办？
比如，只允许对Student实例添加name和age属性. 
只能添加部分我们指定的属性, 不是所有的属性

```
class Student1(object):
    __slots__ = ('name', 'age')
    # 只接收name 和 age

s1 = Student1()
s1.name = 'linjiayu' # 绑定属性'name'
s1.age = '18' # 绑定属性'age'
# 这个会报错的
s1.score = 100 # 绑定属性'score'

"""
Traceback (most recent call last):
  File "slots.py", line 33, in <module>
    s1.score = 100 # 绑定属性'score'
AttributeError: 'Student1' object has no attribute 'score'
"""
```

### 1.3 但是对继承的子类不起作用
- 使用__slots__要注意，__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的
```
# ====== 3 __slots__ 只对当前类起作用 ======
class Student2(Student1):
    pass
s2 = Student2()
s2.score = '100'
```




- 其实是简化 可读可写的流程, 把setter 和 getter通过装饰器的方式标明出来

### 2.1 使用@property背景
- 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改

```
class Student (object):
    def get_score(self):
        return self._score

    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError('Score must be integer')
        if score < 0 or score > 101:
            raise ValueError('Score must between 0 ~ 100')
        self._score = score

s = Student()
# 这样不做校验不合适
# s.score = 999
s.set_score(99)
print s.get_score()
```

### 2.2 使用@property

```
class Student1 (object):
    
    # 把一个getter方法变成属性，只需要加上@property就可以了
    @property
    def score(self):
        return self._score

    # @property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
    @score.setter
    def score(self, score):
        self._score = score

s1 = Student1()

s1.score = 11  # 类似上面1例子的 实际转化为s.set_score(11)
print s1.score # 类似上面1例子的 实际转化为s.get_score()

```

## 3. 多重继承

### 3.1 多重继承例子
- 例如: 
  Dog -> Animal, Dog -> Runnable
  Crow -> Bird, Crow -> Flyable
  狗继承动物的特性 + 也可以跑
  继承多个类
```
# ====== 1 ======
# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。
class Animal(object):
    pass

class Runnable(object):
    def run(self):
        print 'running......'

class Dog(Animal, Runnable):
    pass

```

### 3.2 Mixin
- Mixin的目的就是给一个类增加多个功能
- 上面的例子, 主线是Animal, Runnable可以改为RunnableMixin, 这样的目的是为了更好的看出来继承的关系。

```
class Animal(object):
    pass

class RunnableMixin(object):
    def run(self):
        print 'running......'

class Dog(Animal, RunnableMixin):
    pass
```