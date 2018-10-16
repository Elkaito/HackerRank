# Author: Kai Tanaka

import numpy as np
n,m = map(int,input().split())
a = np.array([input().split() for i in range(n)], dtype = int)
np.set_printoptions(legacy='1.13') # Output of testcases have extra space
print(np.mean(a,axis=1),np.var(a,axis=0),np.std(a),sep="\n")



