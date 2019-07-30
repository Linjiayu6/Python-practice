#!/usr/bin/env python
# -*- coding: utf-8 -*-

'module: private'
import sys
# 我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来
# 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public
def _private_1(name):
    return 'Hello, %s' % name

def greeting(name):
    return _private_1(name)

# third-party module
print('====== 第三方模块 =====')
print(sys.path)
