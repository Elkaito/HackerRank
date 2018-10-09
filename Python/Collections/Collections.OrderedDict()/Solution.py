# Author: Kai Tanaka

from collections import OrderedDict

n = int(input())
products = OrderedDict()
for i in range(n):
    # rpartition returns a tuple containing the left part of the string split by " "
    # therefore item[0] = name and item[2]=quantity
    item = input().rpartition(" ")
    if item[0] in products:
        products[item[0]]+=int(item[2])
    else:
        products[item[0]]=int(item[2])
        
for name in products:
    print(name, products[name])