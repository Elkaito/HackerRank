# Author: Kai Tanaka

if __name__ == '__main__':
    N = int(input())
    list = [] # empty list

    for n in range(N):
        cmd = input().split()
        func=cmd[0]
        if func == "print":
            print(list)
        #use eval() function
        else:
            args=cmd[1:]
            eval("list."+ func +"(" + ",".join(args) + ")")