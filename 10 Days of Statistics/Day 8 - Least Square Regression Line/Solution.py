# Author: Kai Tanaka

from math import sqrt

def getMean(data):
    return sum(data)/len(data)

def getStd(data):
    mu = getMean(data)
    n = len(data)
    return (sum([(i - mu)**2 for i in data]) / n)**0.5

# Calculates Pearson coefficient
def getPearsonCo(x,y):
    mu_x = getMean(x)
    mu_y = getMean(y)
    n = len(x)
    std_x = getStd(x)
    std_y = getStd(y)
    numerator = 0
    for i in range(0,n):
        numerator += (x[i]-mu_x)*(y[i]-mu_y)
    return numerator/(n*std_x*std_y)
        
x = [95,85,80,70,60]
y = [85,95,70,65,70]
mu_x = getMean(x)
mu_y = getMean(y)
std_x = getStd(x)
std_y = getStd(y)

# Calculate regression function
"""
 Regression function: y = a + b * x
 a = mean_y - b * mean_x
 b = p * (std_y/std_x)
"""
p = getPearsonCo(x,y)
b = p * (std_y/std_x)
a = mu_y - b * mu_x
pred_y = a + b*80
print("%.3f" %pred_y)