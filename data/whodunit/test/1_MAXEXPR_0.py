from math import*
def listx():return [int(x) for x in input().split()]
def inpx():return int(input())
def mapx():return map(int,input().split())
def strx():return input()
def floatx():return float(input())

mod = 10 ** 9 + 7

for i in range(inpx()):
    n=inpx()
    k=list(map(float,input().split()))
    c=list(map(float,input().split()))
    SUMck,SUM_k=0.0,0.0
    for i in range(n):
        SUMck+=c[i]*k[i]
        SUM_k+=1/k[i]
    F2=SUMck*SUM_k
    if F2<0:
        print(-1)
    else:
        print(sqrt(F2),end=' ')
        t=SUMck/SUM_k
        for i in range(n):
            print(t/k[i]/k[i]-c[i],end=' ')
        print() 