from sys import stdout,stdin
from collections import defaultdict,deque
import math

m=115475
u=[0]*m
for i in range(m):
    u[i]=(i*((3*i)-1))//2

t=int(stdin.readline())
for _ in range(t):
    n,k=map(int,stdin.readline().split())
    temp=math.sqrt((1/36)+((2*k)/3))
    temp+=0.00000000000005
    #print(temp-(1/6),temp+(1/6))
    lower=math.floor(temp-(1/6))
    upper=math.floor(temp+(1/6))
    #print(lower,upper)
    a,b,c=0,0,0
    if (n+k-1)|(k)==(n+k-1):
        a=1
    for i in range(1,lower+1):
        x,y=n-1,k-u[i]-i
        x+=y
        if x|y==x:
            b=b^1
    for i in range(1,upper+1):
        x,y=n-1,k-u[i]
        x+=y
        if x|y==x:
            c=c^1
    print(a^b^c)
    
    
    
    
    
    
    
    
    
    
    
    



