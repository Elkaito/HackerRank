# Author: Kai Tanaka

from collections import Counter

# Get input
num_shoes = int(input())
shoe_sizes = list(map(int,input().split()))
n = int(input()) # num of customers
profit = 0     

shoe_stock = Counter(shoe_sizes)

for i in range(n):
    desired_size, price = list(map(int,input().split()))
    if shoe_stock[desired_size]>0:
        shoe_stock[desired_size] -= 1
        profit += price
        
print(profit)