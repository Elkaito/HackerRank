# Author: Kai Tanaka

A = input().split()
n = int(input())
message = True
for i in range(n):
    B = input().split()
    for elem in B:
        if len(B) >= len(A) or elem not in A:
            message = False

print(message)