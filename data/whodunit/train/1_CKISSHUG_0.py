import math
mod=10**9+7
t=int(input())
while t:
    n=int(input())
    p1=math.ceil((n+1)/2)
    p2=math.floor((n+1)/2)
    ans1=pow(2,p1,mod)
    ans2=pow(2,p2,mod)
    ans=(ans1+ans2-2)%mod
    print(ans)
    t-=1
