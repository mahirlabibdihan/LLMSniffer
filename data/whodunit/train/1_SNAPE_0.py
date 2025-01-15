from math import *
for j in range(int(input())):
    a,b=map(int,input().split())
    c=sqrt(abs(a**2-b**2))
    d=sqrt(a**2+b**2)
    print(c,d)