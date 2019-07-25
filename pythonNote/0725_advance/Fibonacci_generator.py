# -*- coding: utf-8 -*

"""
比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
1, 1, 2, 3, 5, 8, 13, 21, 34, ...
"""

def Fibonacci(Max):
  n, a, b = 0, 0, 1
  while n < Max:
    print b
    a, b = b, a + b
    n = n + 1

Fibonacci(5)
