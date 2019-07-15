
# -*- coding: utf-8 -*

# use python to login
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
import re

"""
<!DOCTYPE html>
<html lang="cn">
<head>
	<meta charset="UTF-8">
	<title>Scraping tutorial 1 | 莫烦Python</title>
	<link rel="icon" href="https://morvanzhou.github.io/static/img/description/tab_icon.png">
</head>
<body>
	<h1>爬虫测试1</h1>
	<p>
		这是一个在 <a href="https://morvanzhou.github.io/">莫烦Python</a>
		<a href="https://morvanzhou.github.io/tutorials/data-manipulation/scraping/">爬虫教程</a> 中的简单测试.
	</p>

</body>
</html>
"""

html  = urlopen(
  'https://morvanzhou.github.io/static/scraping/basic-structure.html'
).read().decode('utf-8')

# find h1 tag content
res = re.findall(r"<h1>(.+?)</h1>", html)
print(res[0])

"""
如果是这种情况p, 里面还有a标签 等其他内容
<p>
		这是一个在 <a href="https://morvanzhou.github.io/">莫烦Python</a>
		<a href="https://morvanzhou.github.io/tutorials/data-manipulation/scraping/">爬虫教程</a> 中的简单测试.
	</p>
"""
# re.DOTALL if multi line  flags=re.DOTALL 来对这些 tab, new line 不敏感
res1 = re.findall(r"<p>(.*?)</p>", html, flags=re.DOTALL)
print("\nPage paragraph is: ", res1[0])
