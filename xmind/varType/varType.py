
"""
Numbers
String
List
Tuple
Dictionary
"""

# Numbers: int, long, float, complex

print int(3.6) # 3
print int('3') # 3
print int('10', 8)


dict1 = {'runoob': 'runoob.com', 'google': 'google.com'};
print str(dict1) # "{'google': 'google.com', 'runoob': 'runoob.com'}"

dict2 = dict(key = 'value', key1= 'value2')
print dict2 # {'key1': 'value2', 'key': 'value'}

dict3 = dict(zip(['k1','k2'], ['v1','v2']))
print dict3 # {'k2': 'v2', 'k1': 'v1'}

dict4 = dict([('one', 1), ('two', 2), ('three', 3)])
print dict4 # {'three': 3, 'two': 2, 'one': 1}