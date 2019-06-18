from urllib.request import urlopen
u =urlopen('http://localhost:15000/fib.py')
data=u.read().decode('utf8')

import sys
print(sys.meta_path)