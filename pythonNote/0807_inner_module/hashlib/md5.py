# -*- coding: utf-8 -*

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?')

# d26a53750bc40b38b65a520292f69306
print md5.hexdigest()
