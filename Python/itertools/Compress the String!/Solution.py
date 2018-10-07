# Author: Kai Tanaka

from itertools import groupby

seq = list(map(int,input()))
print(*[(len(list(count)), int(num)) for num, count in groupby(seq)])