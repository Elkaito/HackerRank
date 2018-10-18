# Author: Kai Tanaka

import re

def replace_and_or(match):
    if match.group()=="||":
        return "or"
    else:
        return "and"
    
n = int(input())
for i in range(n):
    print (re.sub(r'(?<= )(&&|\|\|)(?= )', replace_and_or, input()))