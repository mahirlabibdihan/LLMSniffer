from math import gcd
for _ in range(int(input().strip())):
    n, k = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    g = a[0]
    for i in range(1, n):
        g = gcd(g, a[i])
    g = g % k
    ans = 0
    for i in range(n):
        if a[i] % k >= g:
            ans += (k - a[i] % k)
        else:
            ans += ((k - a[i] % k) + g)
    print(ans)