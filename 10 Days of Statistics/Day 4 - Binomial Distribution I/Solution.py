# Author: Kai Tanaka

from math import factorial

def nCk(n,k):
    nCk=factorial(n)/(factorial(k)*factorial(n-k))
    return nCk

def binomial(n,k,p):
    result = nCk(n,k) * p**k * (1-p)**(n-k)
    return result

ratio = 1.09        # hardcoded 
p = ratio/(1+ratio) # Probability for boy
n = 6               # num of given trials

result = 0
# k = number of successes/boys
for k in range(3,n+1):
    result += binomial(n,k,p)

print("%.3f" %result)