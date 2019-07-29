# -*- coding: utf-8 -*

# ======= 1 ========
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


# ======= 2. 闭包 ========
def count():
  fs = []
  for i in range(1, 4):
    def f():
      print()
    fs.append(f)
  return fs

"""
9
9
9
全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
"""
f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())