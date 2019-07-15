
# -*- coding: utf-8 -*
from bs4 import BeautifulSoup
try:
  from urllib.request import urlopen
except ImportError:
  from urllib2 import urlopen


# urlopen 请求该地址, read读取信息
html = urlopen(
  # 'https://www.weibo.com/login.php'
  'https://morvanzhou.github.io/static/scraping/basic-structure.html'
).read().decode('utf-8')
# print(html)

"""
BeautifulSoup 简化我们去匹配标签信息内容
- 将读取的信息放入 BeautifulSoup
- 使用 BeautifulSoup 选取tag信息等 (代替正则表达式)
pip install beautifulsoup4 --user

https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id9
lxml HTML 解析器
error: bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: lxml. Do you need to install a parser library?
download: sudo pip3 install lxml
"""
soup = BeautifulSoup(html, features='lxml')

# print(soup.a) 只会match到第一个a标签内容
a_list = soup.find_all('a')
# a_href = for l in a_List:
# for l in a_List:
#   # <a href="https://morvanzhou.github.io/">莫烦Python</a>
#   # l['href']: https://morvanzhou.github.io/
#   print(l['href'])

href_list = [l['href'] for l in a_list]
# ['https://morvanzhou.github.io/', 'https://morvanzhou.github.io/tutorials/data-manipulation/scraping/']

print(href_list)