# Author: Kai Tanaka

from itertools import permutations

str,k = input().split()
[print(*elem, sep="") for elem in list(permutations(sorted(str),int(k)))]