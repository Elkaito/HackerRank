# Author: Kai Tanaka

import re

match = re.search(r"([a-z0-9])\1+", input())
print(match.group(1) if match else -1)  
