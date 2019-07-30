#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
' a test module '
# __author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；
__author__ = 'Lin JY'

"""
sys模块有一个argv变量，用list存储了命令行的所有参数
运行python hello.py获得的sys.argv就是['hello.py']
运行python hello.py Michael获得的sys.argv就是['hello.py', 'Michael]

$ python hello.py linjiayu1 linjiayu2 linjiayu3
('Too many arguments!', ['hello.py', 'linjiayu1', 'linjiayu2', 'linjiayu3'])
"""
import sys

def test():
  args = sys.argv
  if len(args) == 1:
    print('hello', args)
  else:
    print('Too many arguments!', args)

if __name__ == '__main__':
  test()
