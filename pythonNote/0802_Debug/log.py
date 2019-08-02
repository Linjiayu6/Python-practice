#!/usr/bin/env python
# -*- coding: utf-8 -*

import logging

def foo(s):
    return 10 / int(s)

def main():
    try:
        foo('0')
    except StandardError, e:
        logging.exception(e)

        # 如果没有一行就会输出
        print 'Error'
        """
        $ python log.py
          File "log.py", line 11
            main()
            ^
        IndentationError: expected an indented block
        """
main()

"""
同样是出错，但程序打印完错误信息后会继续执行，并正常退出
通过配置，logging还可以把错误记录到日志文件里，方便事后排查。

ERROR:root:integer division or modulo by zero
Traceback (most recent call last):
  File "log.py", line 8, in main
    foo('0')
  File "log.py", line 4, in foo
    return 10 / int(s)
ZeroDivisionError: integer division or modulo by zero
"""