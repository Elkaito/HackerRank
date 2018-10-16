# Author: Kai Tanaka

import re

consonants="qwrtypsdfghjklzxcvbnm"

print("\n".join(re.findall('(?<=[%s])([aeiou]{2,})[%s]' %(consonants,consonants),input(),flag = re.I)) or -1)