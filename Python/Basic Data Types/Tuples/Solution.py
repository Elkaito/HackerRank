# Author: Kai Tanaka

n = int(input())
integer_list = map(int, input().split())
tp=tuple(integer_list)
print(hash(tp))