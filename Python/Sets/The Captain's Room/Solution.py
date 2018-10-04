# Author: Kai Tanaka

# Get input
k = int(input())
room_list=list(map(int,input().split()))
# Unique room numbers
rooms= list(set(room_list))

sum_list = sum(room_list)
sum_rooms = 0
for num in rooms:
    sum_rooms+=num*k
print((sum_rooms-sum_list) // (k-1))