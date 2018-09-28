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
        
# Read input
n = int(input())
x = list(map(float,input().strip().split()))
y = list(map(float,input().strip().split()))

result = getPearsonCo(x,y)

print("%.3f" %result)


