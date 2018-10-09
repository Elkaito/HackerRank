# Author: Kai Tanaka
from collections import Counter

if __name__ == '__main__':
    s = input()
    logo = Counter(s.strip()) 
    s_logo = sorted(logo.most_common(), key=lambda x: (-x[1],x[0]))
    for i in range(3):
        print("{} {}".format(s_logo[i][0],s_logo[i][1]))