# Author: Kai Tanaka

import numpy as np

a = np.array(input().split(), dtype = float)

np.set_printoptions(sign=" ") # Output of testcases have extra space

print(np.floor(a), np.ceil(a), np.rint(a), sep="\n")