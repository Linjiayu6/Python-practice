# -*- coding: utf-8 -*

# ----  dictionary ----
dictionary = {
  'name': 1,
  'age': 2 
}

# {'age': 2, 'name': 1}
print(dictionary)
print(dictionary['name'])

# 判断是否有该值
print('name' in dictionary)
# 获取值
print(dictionary.get('age'))
# 删除值
print(dictionary.pop('age'))

# ----  set ----
s = set([2, 1, 2, 3, 2, 1, 7, 3])
print(s) # 返回值为 set([1, 2, 3, 7]) 重复元素在set中自动被过滤

# 增加值 .add(x)
s.add(10)
print(s) # set([1, 2, 3, 10, 7])

# 删除值
s.remove(1)
print(s) # set([2, 3, 10, 7])