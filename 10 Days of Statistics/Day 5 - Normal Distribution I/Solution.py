# Author: Kai Tanaka

from math import sqrt,erf

# Cumulative distribution function for the standard normal distribution
def cumulative(x,mu,std):
    param = (x-mu)/(std*sqrt(2))
    return 0.5 * ( 1 + erf(param) )

# read input 
mu , std = [float(num) for num in input().split()]
a = float(input())                                # question 1
b, c = [float(num) for num in input().split()]    # question 2

# calculate cumulative probability
ans1 = cumulative(a, mu, std)
ans2 = cumulative(c, mu, std) - cumulative(b, mu, std)

# print results
print("%.3f" %ans1)
print("%.3f" %ans2)