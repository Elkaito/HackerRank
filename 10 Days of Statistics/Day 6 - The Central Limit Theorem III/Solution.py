# Auhtor: Kai Tanaka

from math import sqrt

# Hardcoded values
mean = 500
std = 80
n = 100
zScore = 1.96

marginError = zScore * std / sqrt(n)
I1=mean - marginError
I2=mean + marginError
print("%.2f" %I1)
print("%.2f" %I2)