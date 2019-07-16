
# -*- coding: utf-8 -*
"""
模拟登陆
cookie登陆
http://pythonscraping.com/pages/cookies/login.html
1. 登陆需要种下cookie信息
2. 我们用种下的cookie信息再次去登陆
"""
import requests

firstbody = {'username': 'darling', 'password': 'password' }
r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=firstbody)
# {'username': 'darling', 'loggedin': '1'}
print(r.cookies.get_dict())

# 第二次用cookie信息去登陆别的地址, 这样就能已登录的名义访问 get 的页面了.
r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
print(r.text)


"""
当然还有session登陆
详见 https://morvanzhou.github.io/tutorials/data-manipulation/scraping/3-01-requests/
"""