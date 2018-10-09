# Author: Kai Tanaka

from collections import defaultdict

n,m = list(map(int,input().split()))
d = defaultdict(list)
word_group_B = []
# Store word group A in defaultdictionary with index as value
for i in range(1,n+1):
    d[input()].append(i)
# Store word group B:
for i in range(0,m):
    word_group_B.append(input())
    
for word in word_group_B:
    if word in d:
        print (*d[word])
    else:
        print (-1)