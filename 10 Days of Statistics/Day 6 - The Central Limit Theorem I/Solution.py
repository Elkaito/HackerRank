# Author: Kai Tanaka

from math import sqrt,erf

# Cumulative distribution function for the standard normal distribution
def cumulative(x,mu,std):
    param = (x-mu)/(std*sqrt(2))
    return 0.5 * ( 1 + erf(param) )

# Hardcoded values
mean = 205
std = 15
n = 49
maxWeight = 9800

sampleMean = n* 205
sampleStd = sqrt(n)*std
result = cumulative(maxWeight,sampleMean,sampleStd)

print("%.4f" %result)
