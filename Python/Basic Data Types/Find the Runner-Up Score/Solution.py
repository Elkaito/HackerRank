# Author: Kai Tanaka

n = int(input())
arr = map(int, input().split())
# convert to list with unique elements
unique_arr = list(set(arr))
# remove max score
first_score=max(unique_arr)
unique_arr.remove(first_score)

print(max(unique_arr))  