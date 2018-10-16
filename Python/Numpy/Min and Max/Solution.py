# Author: Kai Tanaka

import numpy as np

n,m = map(int,input().split())
a = np.array([input().split() for i in range(n)], dtype = int)

print(max(np.min(a,axis=1)))


