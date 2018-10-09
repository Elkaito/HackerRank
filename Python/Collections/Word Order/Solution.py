# Author: Kai Tanaka

from collections import OrderedDict

n = int(input())
words = OrderedDict()
for i in range(n):
    word = input()
    if word in words:
        words[word]+=1
    else:
        words[word]=1
# Print num of keys
print(len(words.keys()))
# Print occurences
print(*words.values())