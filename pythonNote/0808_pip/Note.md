
# 常用第三方模块 Python Library

- 类似npm发布一样 https://pypi.python.org/

## 1. Python Imaging Library 图片库
- 图像处理标准库
- sudo easy_install --find-links http://www.pythonware.com/products/pil/ Imaging

- 图像缩放
```
# -*- coding: utf-8 -*

import Image

# 打开一个jpg图像文件，注意路径要改成你自己的:
im = Image.open('/Users/linjiayu/LinProject/Spider-python/pythonNote/0808_pip/test.png')

# <PngImagePlugin.PngImageFile image mode=RGB size=461x307 at 0x106F6D830>
print im
# 获得图像尺寸:
w, h = im.size
print w, h

# 缩放到50%:
im.thumbnail((w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
im.save('/Users/linjiayu/LinProject/Spider-python/pythonNote/0808_pip/test_save.png')
```

## 2. 要生成字母验证码图片
- https://www.liaoxuefeng.com/wiki/897692888725344/966759628285152