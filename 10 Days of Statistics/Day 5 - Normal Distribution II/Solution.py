# Author: Kai Tanaka

from math import sqrt,erf

# Cumulative distribution function for the standard normal distribution
def cumulative(x,mu,std):
    param = (x-mu)/(std*sqrt(2))
    return 0.5 * ( 1 + erf(param) )

# read input 
mu , std = [float(num) for num in input().split()]
a = float(input())                               
b = float(input())

# calculate cumulative percentage: hence 100 * x
ans1 = 100 * (1 - cumulative(a, mu, std))
ans2 = 100 * (1 - cumulative(b, mu, std))
ans3 = 100 * cumulative(b, mu, std)

# print results
print("%.2f" %ans1)
print("%.2f" %ans2)
print("%.2f" %ans3)