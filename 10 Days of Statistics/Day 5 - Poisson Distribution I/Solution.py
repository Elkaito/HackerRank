# Author: Kai Tanaka

from math import factorial,exp

def poisson(mu, k):
    result = (mu**k/factorial(k))*exp(-mu)
    return result 
    
mu = float(input())
k = int(input())

result = poisson(mu,k)
print("%.3f" %result)