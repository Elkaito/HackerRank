#!/bin/python3

import math
import os
import random
import re
import sys
#!/bin/python3
import re

nm = input().split()

n = int(nm[0])

m = int(nm[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

result = []
for i in range(m):
    for elem in matrix:
        result.append(elem[i])
result = ''.join(result)
for replace in re.findall(r'\w(\W+)\w', line):
    replace = '\\'+'\\'.join([ch for ch in replace])
    line = re.sub(replace, ' ', line, count=1)

print(result)