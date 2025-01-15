from math import *
from collections import *
from itertools import *
from bisect import *
from heapq import *
from operator import *
from sys import *
setrecursionlimit(1000000)
d=defaultdict(lambda:0,{})
def io():
    return map(int,input().split())
def op():
    return list(map(int,input().split()))
def o():
    return int(input())
def r(x):
    if type(x)==int:
        return range(x)
    else:return range(len(x))
def kl(con,x=0):
    if x==0:print('Yes') if con else print('No')
    elif x==1:print('yes') if con else print('no')
    elif x==2:print('YES') if con else print('NO')
MOD = 1000000007
MAX=float('inf')
MIN=-float('inf')
p=input
for _ in r(o()):
    n=o()
    x=x1=None
    for i in r(n):
        a,b,c=io()
        if a==1 or b==c:
            x=b
            x1=c
            print('YES')
        elif x==None:
            print('NO')
        else:
            z=sorted([b,c])
            if max(x1,x)<=min(b,c):
                print('NO')
                continue
            if x<z[0]:
                x=z[0]
                x1=z[1]
                print('YES')
            else:
                x=z[1]
                x1=z[0]
                print('YES')