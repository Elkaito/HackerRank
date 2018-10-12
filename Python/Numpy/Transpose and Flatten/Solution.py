# Author: Kai Tanaka

import numpy

n,m = map(int,input().split())
n_arr = numpy.array([input().split() for i in range(n)],int)
print(n_arr.transpose())
print(n_arr.flatten())