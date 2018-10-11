# Author: Kai Tanaka

string = input()

# decompose string in to upper,lower and even/odd digit
upper=[]
lower=[]
odd=[]
even=[]

for char in sorted(string):
    if char.isupper():
        upper.append(char)
    elif char.islower():
        lower.append(char)
    else:
        if int(char)%2==1:
            odd.append(char)
        else:
            even.append(char)
            
print("".join(lower + upper + odd + even))