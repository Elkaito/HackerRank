# Auhtor: Kai Tanaka

import numpy as np

n = int(input())
a = np.array([input().split() for i in range(n)], dtype = float)

print(round(np.linalg.det(a),2))