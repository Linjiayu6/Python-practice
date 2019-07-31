#!/usr/bin/env python
# -*- coding: utf-8 -*

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
    def run(self):
        print 'Cat is running...'

# 类Dog有Animal的run方法了
Dog().run()
Cat().run()
"""
输出结果
Dog is running...
class Animal is running....
"""

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


# =======  2.1 多态 =======
def run_twice(animal):
    animal.run()

"""
由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思

Dog is running...
class Animal is running....
Cat is running...
"""
run_twice(Dog())
run_twice(Animal())
run_twice(Cat())

