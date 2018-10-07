# Author: Kai Tanaka

from itertools import combinations

str, k = input().split()
for i in range(1,int(k)+1):
    [print(*elem, sep="") for elem in list(combinations(sorted(str),i))]