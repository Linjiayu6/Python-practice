# 面向对象编程 Object Oriented Programming

## 1. 面向过程 vs 面向对象
- 面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。

- 而面向对象的程序设计把计算机程序视为【一组对象】的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递。

```

#!/usr/bin/env python

# -*- coding: utf-8 -*

"OOP VS PO"
__name__ = 'Lin JY'

# =========== 1. PO ===========
std1 = {
  'name': 'Jessica',
  'age': 18
}
std2 = {
  'name': 'Krystal',
  'age': 16
}

def printout(student):
  print(student['name'], student['age'])

printout(std1)
printout(std2)
"""
('Jessica', 18)
('Krystal', 16)
"""


# =========== 2. OOP ===========
class Student(object):
  def __init__(self, name, score):
    self.name = name
    self.score = score

  def print_out(self):
    print(self.name, self.score)

st1 = Student('jesscia', '100')
st2 = Student('krystal', '90')
st1.print_out()
st2.print_out()

```

## 2. Class Instance

### 2.1 class
- 0x1032f8c10是内存地址
```
# 类
class Student(object):
    pass

# 实例
instance = Student()

# <class '__main__.Student'>
print(Student)
# 输出: <__main__.Student object at 0x1032f8c10>
print(instance)
```

### 2.2 __init__
- 注意到__init__方法的第一个参数永远是self，表示创建的实例本身;
- 因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身;
```
# 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上
class Student1(object):
    # self为创建实例本身 就可以把各种属性绑定到self
    def __init__(self, name, score):
        self.name = name
        self.score = score

instance_st1 = Student1('linjiayu', 180)
print(instance_st1.name)
print(instance_st1.score)
```

### 2.3 数据封装
- !!! 各种函数的self必须传
  
```
# ========== 3 数据封装 ==========
class Student2(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def printout(self):
        level = self.scoreLevel()
        print('name:', self.name, ' score: ', self.score, 'level', level)

    def scoreLevel(self):
        if self.score >= 90:
            return 'A'
        else: 
            return 'C'

instance_st2 = Student2('Sensational', 90)
instance_st2.printout()
```

## 3. 访问限制

### 3.1 随便变更对象的属性和方法

- 在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。

```
# =======  1. 访问限制 - 随意变更对象内容 =======
class Student(object):
    def __init__(self, name):
        self.name = name
    def printout(self):
        print(self.name)
        
instance_st = Student('linjiayu')
instance_st.printout()

# 从外部修改内容
instance_st.name = 'who are you'
# 值已经变化了 输出为'who are you'
instance_st.printout()
```

### 3.2 定义私有属性
- 我们想内部属性不想被外部属性访问到, 可以变成私有属性
```
class Student1(object):
    def __init__(self, name):
        self.__name = name
    def printout(self):
        print(self.__name)
        
instance_st1 = Student1('linjiayu')
instance_st1.printout()

# 从外部修改内容
instance_st1.name = 'who are you'
# 没有变化输出为'linjiayu'
instance_st1.printout()
```

### 3.3 允许外部去修改或获取变量(get, set)

- 允许外部 修改 或 获取 变量;
- 这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮;
- 这样只是确定了 无法从外部直接 实例变量.__name和实例变量.__score了, 修改变量;

```
# =======  3. 访问限制 - 想要获取内部信息怎么办 =======
class Student2(object):
    def __init__(self, name):
        self.__name = name
    # 允许外部获取
    def get_name(self):
        return self.__name
    # 允许外部修改
    def set_name(self, name):
        self.__name = name
        

instance_st2 = Student2('xxxxxx')
print(instance_st2.get_name())
instance_st2.set_name('xxxx change to AAAA')
print(instance_st2.get_name())
```

- _private / __private 是私有变量
- 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”;
- public 共有变量
- __name__ 特殊变量
- 总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉


## 4. 继承和多态
- 在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）


### 4.1 继承
- 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()
- 在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处: 多态

```
# =======  1. 继承 =======
class Animal(object):
    def run(self):
        print('class Animal is running....')

class Dog(Animal):
    # 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()
    # 在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处: 多态
    def run(self):
        print 'Dog is running...'

class Cat(Animal):
    pass

# 类Dog有Animal的run方法了
Dog().run()
Cat().run()

```

### 4.2 多态
```
# =======  2. 多态 =======
animal = Animal() # animal是Animal类型
dog = Dog() # dog是Dog类型

"""
True
True
True
False

看来dog不仅仅是Dog，还是Animal！
但是animal 不是Dog 反过来不太行;
"""
print isinstance(animal, Animal)
print isinstance(dog, Dog)
print isinstance(dog, Animal)
print isinstance(animal, Dog)
```


- 由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思
- 就是父类有run()方法,子类调用也同样有该方法

```
def run_twice(animal):
    animal.run()

"""
Dog is running...
class Animal is running....
Cat is running...
"""
run_twice(Dog())
run_twice(Animal())
run_twice(Cat())
```

### 4.3 小结
- 继承: 可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写;
- 多态: 在调用类实例方法的时候，尽量把变量视作父类类型，这样，所有子类类型都可以正常被接收;

## 5. 获取对象信息

### 5.1 type()
```
"""
<type 'int'>
<type 'NoneType'>
"""
print type(123)
print type(None)
```

### 5.2 isinstance()
- 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数
```
class Animal (object):
    def run(self):
        print('animal ....')

class Bird (Animal):
    def run(self):
        print('Animal - Bird ....')

class Crow (Bird):
    def run(self):
        print('Animal - Bird - Crow ....')

def log(instance):
    instance.run()
    print('isinstance:', isinstance(instance, Animal))

log(Animal())
log(Bird())
log(Crow())
```

### 5.3 dir()
- 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法

```
print dir('ABC')

"""
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
"""
```

### 5.4 len() / __len__()
```
'ABC'.__len__()
```

### 5.5 hasattr()
- 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态

- 场景说明: 
假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。
请注意，在Python这类动态语言中，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。

- 详情请见: https://www.liaoxuefeng.com/wiki/897692888725344/923030517708128