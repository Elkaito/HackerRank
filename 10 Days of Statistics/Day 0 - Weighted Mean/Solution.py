# Author: Kai Tanaka

# Get input
size = int(input())
numbers = list(map(int, input().split()))
weights = list(map(int, input().split()))

# Calculate weighted mean
total=0
sum_weights=0
for i in range(size):
    total += numbers[i]*weights[i]
    sum_weights+=weights[i]

w_mean=total/sum_weights

print("%.1f" %w_mean)