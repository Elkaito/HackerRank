# Author: kai Tanaka

import numpy as np

a = np.array(input().split(),dtype=int)
b = np.array(input().split(),dtype=int)
print(np.inner(a,b), np.outer(a,b) ,sep="\n")