# Author: Kai Tanaka

# imports
from math import sqrt

N = int(input())
numbers = list(map(int, input().split()))

# Calculate Mean
total = 0
for i in numbers:
    total += i
mean = total/N

# Calculate Standard Deviation
sum = 0
for j in range(N):
    sum += (numbers[j] - mean)**2
    
std = sqrt(sum/N)

print("%.1f" %std)