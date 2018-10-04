# Author: Kai Tanaka

n = input()
s = set(map(int,input().split()))

for i in range(int(input())):
    cmd = input().split()
    func = cmd[0]
    set_tmp = set(map(int,input().split()))
    eval("s.{0}({1})".format(func,set_tmp))
print(sum(s))