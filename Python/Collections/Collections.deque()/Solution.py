# Author: Kai Tanaka

from collections import deque
d = deque()
n = int(input())
for i in range(n):
    cmd, *arg = input().split()
    getattr(d, cmd)(*arg)
print(*[elem for elem in d])