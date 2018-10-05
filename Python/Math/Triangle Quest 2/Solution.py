# Author: Kai Tanaka

"""
The pattern is:
1 * 1 = 1
11 * 11 = 121
111 * 111 = 12321
1111 * 1111 = 1234321
...

"""


for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(round(1/9*10**i)**2)