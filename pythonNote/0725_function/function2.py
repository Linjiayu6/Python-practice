# -*- coding: utf-8 -*

# 4. ========== 关键字参数 ========== 
def keyParams (a, b, **kv):
    print(a, b, kv)

# (1, 2, {})
keyParams(1, 2)
# (1, 2, {'cityId': 666, 'cityName': 'Beijing'})
keyParams(1, 2, cityId = 666, cityName = 'Beijing')

print(' ========== 组合参数 ========== ')
# 5. ========== 组合参数 ========== 
def combine (required, options = 1, *args, **kv):
  print(required, options)
  print('args', args)
  print('kv', kv)

combine('1required value')
# ('2required value', 200)
# ('args', (4, (1, 2), 6, [1], 7))
# ('kv', {'age': 18, 'name': 'linjiayu', 'key': 'value'})
combine(
  '2required value',
  200, 
  4,(1,2),6,[1],7,
  name='linjiayu', age=18, key='value'
)