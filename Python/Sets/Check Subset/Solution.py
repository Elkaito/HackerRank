# Author: Kai Tanaka

n = int(input())
for i in range(n):
    a = input()
    A = input().split()
    b = input()
    B = input().split()
    message = True
    for elem in A:
        if elem not in B:
            message = False
    print(message)