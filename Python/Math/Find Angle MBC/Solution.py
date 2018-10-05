# Author: Kai Tanaka

import math

AB = int(input())
BC = int(input())
AC =math.hypot(AB,BC)                      
degree=round(math.degrees(math.acos(BC/AC)))

print(str(degree)+"°")