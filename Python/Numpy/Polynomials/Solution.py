# Author: Kai Tanaka

import numpy as np

coef = np.array(input().split(), dtype =float)
x = int(input())
print(np.polyval(coef,x))