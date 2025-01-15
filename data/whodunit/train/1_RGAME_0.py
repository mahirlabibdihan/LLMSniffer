t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    mod = 10**9+7
    n=n+1
    ans=0
    l = a[0]*2
    d = 1
    for i in range(1,n):
        ans =(2*ans +l*a[i])%mod
        d = (2*d)%mod
        l = (l+a[i]*d)%mod
    print(ans)