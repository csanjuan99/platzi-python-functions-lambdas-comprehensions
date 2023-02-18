import sys

# print(sys.path)
print(sys.argv)

import re

text = 'Mi numero de telefono 312 430 3694, el codigo de pais es 57, mi numero de la suerte es 7'
print(re.findall(r'\d{3} \d{3} \d{4}', text))

import time
local = time.localtime()
datetime = time.asctime(local)
print(time.time(), local, datetime)


import collections

# Counter
c = collections.Counter('gallad')
print(c)