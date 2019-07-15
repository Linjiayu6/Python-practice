# -*- coding: utf-8 -*
from urllib2 import urlopen
from bs4 import BeautifulSoup
# 正则引入该包
import re

html = urlopen(
  'https://morvanzhou.github.io/static/scraping/table.html'
).read().decode('utf-8')

soup = BeautifulSoup(html, features='lxml')

# 将所有的img标签内容全部找出来
imgtag_list = soup.find_all("img", {"src": re.compile('\.png')})
# 找出来所以图片的链接内容
img_list = [l['src'] for l in imgtag_list]
print(img_list)
