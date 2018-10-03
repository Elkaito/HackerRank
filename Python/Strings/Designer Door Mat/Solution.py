# Author: Kai Tanaka

x,y = map(int,input().split())
n = x//2

# Print upper half pyramid
for i in range(0,n):
    upper_pyramid = ".|" + 2*i*"..|" + "."
    print(upper_pyramid.center(y,"-"))

# print center message
print("WELCOME".center(y,"-"))

# Print lower half pyramid
for i in range(n-1,-1,-1):
    lower_pyramid = ".|" + 2*i*"..|" + "."
    print(lower_pyramid.center(y,"-"))
