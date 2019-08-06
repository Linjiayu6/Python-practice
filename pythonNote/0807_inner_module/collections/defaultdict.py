
from collections import defaultdict

dd = defaultdict(lambda: 'N/A')

dd['key1'] = 'abc'

# abc
print dd['key1']
# N/A
print dd['key2']
