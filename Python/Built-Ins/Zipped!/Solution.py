# Author: Kai Tanaka

n , x = list(map(int,input().split()))
students = []
for i in range(x):
    students.append(map(float,input().split()))
individual_score = map(sum,zip(*students))
for score in individual_score:
    print(score/x)