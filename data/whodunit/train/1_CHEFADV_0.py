from collections import *
import sys
input=sys.stdin.readline
t=int(input())
while(t):
    t-=1
    n,m,x,y=map(int,input().split())
    n-=1
    m-=1
    if((n%x<=1 and m%y<=1 and n%x==m%y) or (n==m==0 or n==m==1) or((n-1)%x==(m-1)%y and (n-1)%x==0) and n-1>=0 and m-1>=0):
        print("Chefirnemo")
    else:
        print("Pofik")
    
    
