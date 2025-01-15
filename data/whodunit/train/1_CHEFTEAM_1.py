import functools
def ncr(n,r):
    r=min(r,n-r)
    a=functools.reduce(lambda x,y: x*y, range(n,n-r,-1),1)
    b=functools.reduce(lambda x,y: x*y, range(1,r+1),1)
    return a//b
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    if (k>n):
        print(0)
    else:
        print(ncr(n,k))
