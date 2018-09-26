# Author: Kai Tanaka

# Get input
size = int(input())
numbers = list(map(int, input().split()))

# Calculate Mean
total = 0
for i in numbers:
    total += i
mean = total/size

# Calculate Median 
numbers.sort()
if size % 2 == 0:
    median = (numbers[int(size/2)]+numbers[int(size/2-1)])/2
else:
    median = numbers[int((size+1)/2)]
    
# Calculate Mode
maxOccurence = max([numbers.count(i) for i in numbers])
mode = [num for num in numbers if numbers.count(num) == maxOccurence][0]

# Print results
print(mean)
print(median)
print(mode)
