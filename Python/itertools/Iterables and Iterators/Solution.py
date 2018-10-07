# Author: Kai Tanaka

from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

comb = list(combinations(letters,k))
tupel_with_a = []
for elem in comb:
    if "a" in elem:
        tupel_with_a.append(elem)
print(len(tupel_with_a)/len(comb))