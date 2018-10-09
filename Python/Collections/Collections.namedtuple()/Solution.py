# Author: Kai Tanaka

from collections import namedtuple
# Get input
num_of_students = int(input())
Student = namedtuple("Student",input().split())
sum_marks = 0
for i in range(num_of_students):
    # Create named tuple and add marks to sum
    values = Student(*input().split())  
    sum_marks+=int(values.MARKS)
print("%.2f" %(sum_marks/num_of_students))