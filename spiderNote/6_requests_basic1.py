
# -*- coding: utf-8 -*
"""
pip install requests

页面提交post信息 http://pythonscraping.com/pages/files/form.html
接口 http://pythonscraping.com/pages/files/processing.php
body: firstname, lastname
"""
import requests
import webbrowser

# 打开 该搜索, get方法
param = {"wd": "亲爱的热爱的"}  # 搜索的信息
r = requests.get('http://www.baidu.com/s', params=param)
print(r.url)
webbrowser.open(r.url)

# post方法提交信息
data = {'firstname': '亲爱的', 'lastname': '热爱的' }
r = requests.post('http://pythonscraping.com/files/processing.php', data=data)
print(r.text)
