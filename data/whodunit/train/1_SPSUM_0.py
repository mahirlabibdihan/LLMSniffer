import math

t = int(input())
for _ in range(t):
    n , m = map(int, input().split())
    total = (n*(n+1))//2
    ans ='No'
    if total > m:
        remain = total-m
        half=remain//2
        if remain&1:
            ans='No'
        elif math.gcd(half+m,half)==1:
            ans='Yes'
    print(ans)         
