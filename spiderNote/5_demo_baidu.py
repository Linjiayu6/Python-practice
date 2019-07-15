#!/usr/bin/env python  
# -*- coding: utf-8 -*
from urllib2 import urlopen
from bs4 import BeautifulSoup
import re
import random

base_url = "https://baike.baidu.com"
his = [{ "title": '1', "url": "/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"}]

# 读取html
def readHtml ():
  url = base_url + his[-1]['url']
  html = urlopen(url).read().decode('utf-8')
  return BeautifulSoup(html, features='lxml')

# 获取该页面的所有A标签href内容
def getATags (html):
  # 找到的是a标签的所有内容, 我们需要的是href里面的内容
  a_list = html.find_all('a', {
    'target': '_blank',
    'href': re.compile("^/item/(%.{2})+$")
  })
  return [l['href'] for l in a_list]

# 在找到的列表中, 随机找一个url再接下来的爬虫
def randomUrl (html, tagList):
  # 在tagList这里, 随机选择1个值
  if len(tagList) != 0:
    # title = html.find('h1').get_text()
    selectedUrl = random.sample(tagList, 1)[0]
    his.append({ 'title': html.title.get_text(), 'url': selectedUrl })

"""
我们想随机选择要爬虫的页面内容
在该页基础上, 找到其他合法的地址 
例如 <a target=_blank href="/item/%E6%90%9C%E7%B4%A2%E7%AD%96%E7%95%A5">搜索策略</a>
"""

for i in range(10):
  html = readHtml()
  tagList = getATags(html)
  randomUrl(html, tagList)
  print(len(his) - 1, his[-1])
  