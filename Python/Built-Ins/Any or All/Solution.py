# Author: Kai Tanaka

def is_palindrome(num):
    number = str(num)
    return number == number[::-1]

n = int(input())
nums = list(map(int,input().split()))
print(all(x>=0 for x in nums) and any(is_palindrome(x) for x in nums))