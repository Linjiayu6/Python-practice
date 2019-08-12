
# 1. create a tuple
# T = ()
T = (1, 2, 3, 4, 5)

# 2. get value by index R: 2
print T[1]

# 3. get value by indexssss R: (3, 4, 5)
print T[2:6]

# 4. update value - forbidden
# TypeError: 'tuple' object does not support item assignment
# T[1] = 666

# 5. merge Two tuples
T1 = (1,2,3)
T2 = (2,3)
T3 = T1 + T2
# (1, 2, 3, 2, 3)
print T3


# 6. del tuple
del T1
del T2
del T3

# 7. len, merge, copy, in, for
print len(T) # 5
print (1,2,3) + (1,2,3) # (1, 2, 3, 1, 2, 3)

print ('hi') * 5 # hihihihihi
print ('hi',) * 5 # ('hi', 'hi', 'hi', 'hi', 'hi')

print [1] * 5 # [1, 1, 1, 1, 1]
print [1,] * 5 # [1, 1, 1, 1, 1]

print 6 in T # False
for val in T:
    print val

# 8. cmp, max/mix, tuple(list)
T4 = (1,2)
T5 = (1,2)
print cmp(T4,T5) # 0
print max(T4), min(T5) # 2 1

print tuple([4,5,6])
print list((4,5,6))

# 9. for better storage
name, age, height = ('JY', 18, '190cm')
print name

# 10. Hashable
D = {
  ('Jessica', 1999): 1,
  ('Krystal', 2000): 2
}
# [('Krystal', 2000), ('Jessica', 1999)]
print D.keys()
print D.keys()[0][1] # 2000

# Deconstruction
for T in D.keys():
    name, year = T
    # Krystal-2000  Jessica-1999
    print name + '-' + str(year)