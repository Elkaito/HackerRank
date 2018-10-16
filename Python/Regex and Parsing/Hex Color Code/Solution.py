# Author: Kai Tanaka

import re

n = int(input())

for i in range(n):
    match = re.findall(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', input())
    if match:
        print(*match, sep='\n')