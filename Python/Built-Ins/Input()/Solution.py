# Author: Kai Tanaka

x , k = map(int,input().split())
print(eval(input().replace("x",str(x))) == k)