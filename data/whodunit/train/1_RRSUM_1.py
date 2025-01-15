
n,m = map(int,input().split())
a,b = 2+n, 3*n
t = (a+b) // 2
for _ in range(m):
    r = 0
    q = int(input())
    if q <= n:
        print(0)
    else:
        r = abs( t - q )
        print(n-r)
