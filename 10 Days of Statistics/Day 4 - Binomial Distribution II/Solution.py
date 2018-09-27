# Author: Kai Tanaka

from math import factorial

def nCk(n,k):
    nCk=factorial(n)/(factorial(k)*factorial(n-k))
    return nCk

def binomial(n,k,p):
    result = nCk(n,k) * p**k * (1-p)**(n-k)
    return result

p = 0.12            # probability that piston rejected
n = 10              # total piston batch 

result = 0
# k = number of rejections

# no more than 2 rejects
for k in range(0,3):
    result += binomial(n,k,p)   
print("%.3f" %result)

# at least 2 rejects
result = 1 - binomial(n,0,p) - binomial(n,1,p)
print("%.3f" %result)