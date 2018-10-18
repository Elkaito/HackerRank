# Author: Kai Tanaka

import re

n = int(input())

for i in range(n):
    card_num = input() 
    if re.match(r'^(?![\d-]*(\d)(-?\1){3})[456]\d{3}-?(\d{4}-?){3}$',card_num):
        print("Valid")
    else:
        print("Invalid")