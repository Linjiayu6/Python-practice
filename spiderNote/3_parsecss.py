
# -*- coding: utf-8 -*
from bs4 import BeautifulSoup
try:
  from urllib.request import urlopen
except ImportError:
  from urllib2 import urlopen

html = urlopen(
  # 'https://www.weibo.com/login.php'
  'https://morvanzhou.github.io/static/scraping/list.html'
).read().decode('utf-8')

soup = BeautifulSoup(html, features='lxml')
# get contents of class, 获取li标签的class为month的信息
month_list = soup.find_all('li', { "class": "month"})
print(month_list)
# 获取标签内容

l_text = [l.get_text() for l in month_list]
print(l_text)
