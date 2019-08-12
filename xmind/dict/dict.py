# 1. dictionary { key: value, k1: v1 }

Dict = { 
  'J': 'Jessica',
  'K': 'Krystal'

}

# 2. get value by key
print Dict['J'], Dict # Jessica {'K': 'Krystal', 'J': 'Jessica'}

# 3. add key:value
Dict['L'] = 'Lin'
print Dict # {'K': 'Krystal', 'J': 'Jessica', 'L': 'Lin'}

# 4. update / change value by key
Dict['L'] = 'Hong Kong'
print Dict # {'K': 'Krystal', 'J': 'Jessica', 'L': 'Hong Kong'}

# 5. del, clear
del Dict['L']
print Dict # {'K': 'Krystal', 'J': 'Jessica'}

# clear all
# Dict.clear()
# print Dict # {} 

# 6. len, cmp, str(dict), type
print len(Dict) # 2
print str(Dict) # <type 'str'>: {'K': 'Krystal', 'J': 'Jessica'}


# 7. 
"""
dict.clear()
dict.copy()
dict.get(key, default=None)
dict.has_key(key)
dict.items()
dict.keys()
dict.values()
dict.setdefault(key, default=None)
pop(key[,default])
popitem()
"""

D1 = {
  "100": 111,
  "200": 222,
  "300": 333
}

print D1.get('300') # 333
print D1.has_key('400') # False
print D1.keys(), D1.values() # ['300', '200', '100'] [333, 222, 111]
# return tuple in form of [(key, value), (key, value), ...]
print D1.items() # [('300', 333), ('200', 222), ('100', 111)]

# delete key
D1.pop('100')
print D1 # {'300': 333, '200': 222}

for Key in D1:
    # key
    print Key

for Tuple in D1.items():
    key, value = Tuple
    print key, value