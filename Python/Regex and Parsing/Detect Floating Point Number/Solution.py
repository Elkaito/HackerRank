# Author: Kai Tanaka

import re

def isfloat(num):
    return bool(re.match(r"^[+-]?\d*\.\d+$",num))

n = int(input())
for i in range(n):
    print(isfloat(input()))