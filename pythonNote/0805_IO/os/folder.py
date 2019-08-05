# -*- coding: utf-8 -*

import os

# 绝对路径
# /Users/xxx/xxx/Spider-python/pythonNote/0805_IO/os
folder = os.path.abspath('.')
# 新增操作 os.mkdir(folder+'/create')
# 删除操作 os.rmdir(xxxx)


# 拆分路径
# ('/Users/michael/testdir', 'file.txt')
print os.path.split('/Users/michael/testdir/file.txt')

# 获取文件夹下所有文件
print [x for x in os.listdir('.')]
# 输出内容为: ['folder.py', 'os.py', 'create']