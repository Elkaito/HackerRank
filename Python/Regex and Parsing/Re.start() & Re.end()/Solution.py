# Author: Kai Tanaka

import re 

s = input()
k = input()
n = len(k)

if not re.search(k, s):
    print('(-1, -1)')
    
for i in range(0,len(s)-n+1):
    if(k == s[i:i+n]):
        print("({}, {})".format(i, i+n-1))