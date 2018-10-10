# Author: Kai Tanaka

import re

n = int(input())
for i in range(n):
    regex = input()
    is_valid = True
    try:
        re.compile(regex)
    except re.error:
        is_valid = False
    print(is_valid)