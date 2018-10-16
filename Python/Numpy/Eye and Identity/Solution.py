# Author: Kai Tanaka

import numpy as np

n,m = map(int,input().split())
"""
Error on the part of the problem creator 
where there's too much whitespace in the expected output.
We need to add extra space in the output.
Credits to nprajilesh:
https://www.hackerrank.com/challenges/np-eye-and-identity/forum/comments/461853
"""
np.set_printoptions(sign=' ')
print (np.eye(n,m))