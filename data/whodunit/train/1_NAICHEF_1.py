t=int(input())
while t>0 :
    n,a,b=map(int,input().split())
    x=list(map(int,input().split()))
    print((x.count(a)*x.count(b))/(n*n))
    t-=1