# Author: Kai Tanaka

def geometric(p,k):
    result = (1-p)**(k-1)*p
    return result

#Hardcoded values
p = 1/3
k = 5
result = geometric(p,k)
print("%.3f" %result)