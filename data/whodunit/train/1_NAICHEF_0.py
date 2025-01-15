t=int(input())
for i in range(t):
    n,a,b=map(int,input().split())
    l=list(map(int,input().split()))
    w=(l.count(a)*l.count(b))/(n*n)
    print(w)