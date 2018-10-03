import string

def print_rangoli(size):
    # list of lower case alphabet
    a = list(string.ascii_lowercase)
    seq = a[0:size]
    rev_seq = seq[::-1]
    width = 2*(size + size - 1) - 1
    #print upper pyramid + center
    for i in range(1,size+1):
        str = rev_seq[0:i]+list(reversed(rev_seq[0:i-1]))
        print("-".join(str).center(width,"-"))
    # print lower pyramid
    for i in range(1,size):
        str = rev_seq[0:size-i]+list(reversed(rev_seq[0:size-i-1]))
        print("-".join(str).center(width,"-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)