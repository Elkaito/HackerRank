# Author: Kai Tanaka

n = input()
a = set(input().split())
m = input()
b=  set(input().split())

x = a.difference(b)
y = b.difference(a)
result = x.union(y)
print("\n".join(sorted(result,key=int)))