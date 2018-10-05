# Author: Kai Tanaka

a = int(input())
b = int(input())
print("{0}\n{1}\n({0}, {1})".format(*divmod(a,b)))