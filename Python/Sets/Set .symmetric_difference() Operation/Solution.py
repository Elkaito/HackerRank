# Author: Kai Tanaka

n = int(input())
a = set(input().split())
m = int(input())
b = set(input().split())
x = a.union(b)
y = a.intersection(b)
print(len(x.difference(y)))
