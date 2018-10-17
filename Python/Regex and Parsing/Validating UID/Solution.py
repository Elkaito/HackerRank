# Author: Kai Tanaka

import re

n = int(input())

for i in range(n):
    UID = input()
    if re.match(r'[a-zA-Z0-9]{10}',UID):
        # Check if unique characters
        no_duplicates = (len(UID) == len(set(UID)))
        #number of uppercase chars
        num_upper = 0 
        #number of digits
        num_digts = 0
        for char in UID:
            if(char.isdigit()):
                num_digts += 1
            if(char.isupper()):
                num_upper += 1
        if(no_duplicates and (num_upper >= 2) and (num_digts >= 3)):
            print ("Valid")
        else:
            print ("Invalid")