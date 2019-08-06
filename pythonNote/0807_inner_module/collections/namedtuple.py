# -*- coding: utf-8 -*

# ===== 1. 坐标 =====
# tuple 不变集合
# 表示了一个二维坐标, 但是这么表示不明确, 很难看出来是个坐标, 当然你也可以用class
p = (1,2)

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p_ = Point(1, 2)

print p_.x, p_.y


# ===== 2. 圆 =====
# namedtuple('名称', [属性list]): 坐标+半径
Circle = namedtuple('Circle', ['x', 'y', 'r'])
