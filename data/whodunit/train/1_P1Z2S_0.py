from math import *
n=int(input())
x=list(map(int,input().split()))
a=0
for j in x:
    a+=j/2
b=(ceil(a))
if(b<n):
    print(n)
else:
    print(b)
