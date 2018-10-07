# Author: Kai Tanaka

from itertools import product

"""
(f(x1) + f(x2) + ... + f(xn)) % m  <=>
(f(x1) % m + f(x2) % m + ... + f(xn) % m)
"""
def f(nums):
    return sum(i**2 for i in nums) % m

k, m = map(int,input().split())
# list of i lists
x_i = []
for i in range(k):
    x_i.append([int(num) for num in input().split()][1:])
    
# get all possible combinations of the k lists and apply function
combs = list(product(*x_i))
candidates = list(map(f, combs))

# result is the maximum:
print(max(candidates))
    
