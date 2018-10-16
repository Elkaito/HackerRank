# Author: Kai Tanaka

import numpy as np

n,m,p = map(int,input().split())
n_arr = np.array([input().split() for i in range(n)],int)
m_arr = np.array([input().split() for i in range(m)],int)
print(np.concatenate((n_arr,m_arr)))