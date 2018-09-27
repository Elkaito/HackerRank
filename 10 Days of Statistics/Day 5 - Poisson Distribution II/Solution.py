# Author: Kai Tanaka

"""
useful formula:
https://s3.amazonaws.com/hr-assets/forumImages/1493252111-f9aacb7071-poisson.png
"""

X, Y = [float(num) for num in input().split()]

dailyCostX = 160 + 40*(X + X**2)
dailyCostY = 128 + 40*(Y + Y**2)

print("%.3f" %dailyCostX)
print("%.3f" %dailyCostY)