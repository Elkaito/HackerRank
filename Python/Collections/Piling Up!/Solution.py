# Author: Kai Tanaka

from collections import deque

num_test_case = int(input())
for i in range(num_test_case):
    message = "Yes"
    num_cubes = int(input())
    d = deque(map(int, input().strip().split()))
    for max_side in reversed(sorted(d)):
        if d[0]!=max_side and d[-1]!=max_side:
            message="No"
            break;
        elif d[0]==max_side:
            d.popleft()
        else:
            d.pop()
    print(message)