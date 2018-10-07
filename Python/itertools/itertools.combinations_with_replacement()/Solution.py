# Author: Kai Tanaka

from itertools import combinations_with_replacement

str,k = input().split()
[print(*elem, sep="") for elem in list(combinations_with_replacement(sorted(str),int(k)))]