import itertools

# ==== 1. repeat ===== 
# # repeat('A', 10)
ns = itertools.repeat('A', 10)

# repeat('A', 10)
print(ns)

for i in ns:
    print(i)


# ==== 2. chain ===== 
"""
A
B
C
X
Y
Z
"""
for c in itertools.chain('ABC', 'XYZ'):
    print(c)

# ==== 2. chain ===== 
r = map(lambda x: x*x, [1, 2, 3])
print(r)