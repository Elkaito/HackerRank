# Author: Kai Tanaka

def geometric(p,k):
    result = ((1-p)**(k-1))*p
    return result

#Hardcoded values
p = 1/3
result = 0
for k in range(1,6):
    result += geometric(p,k)

print("%.3f" %result)