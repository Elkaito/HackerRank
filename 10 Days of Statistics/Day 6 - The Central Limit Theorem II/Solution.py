# Author: Kai Tanaka

from math import sqrt,erf

# Cumulative distribution function for the standard normal distribution
def cumulative(x,mu,std):
    param = (x-mu)/(std*sqrt(2))
    return 0.5 * ( 1 + erf(param) )

# Hardcoded values
mean = 2.4
std = 2.0
n = 100
numTickets = 250

sampleMean = n* mean
sampleStd = sqrt(n)*std
result = cumulative(numTickets,sampleMean,sampleStd)

print("%.4f" %result)
