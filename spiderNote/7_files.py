
# -*- coding: utf-8 -*

"""
https://morvanzhou.github.io/learning-steps/
找到了这个网址, 我们就能开始下载了. 
为了下载到一个特定的文件夹, 我们先建立一个文件夹吧. 并且规定这个图片下载地址.

在 urllib 模块中, 提供了我们一个下载功能 urlretrieve. 使用起来很简单. 
输入下载地址 IMAGE_URL 和要存放的位置. 图片就会被自动下载过去了.
"""

import requests

IMAGE_URL = "https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png"
r = requests.get(IMAGE_URL, stream=True)    

# 下载文件到 该目录下
aim = '/Users/linjiayu/LinProject/Spider-python/spiderNote/7_files_img.png'
with open(aim, 'wb') as f:
  f.write(r.content)
