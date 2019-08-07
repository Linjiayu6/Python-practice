# -*- coding: utf-8 -*

import hashlib

sha1 = hashlib.sha1()

# 如果数据量很大，可以分块多次调用update()
sha1.update('how to use sha1 in ')
sha1.update('python hashlib?')

# 2c76b57293ce30acef38d98f6046927161b46a44
print sha1.hexdigest()
