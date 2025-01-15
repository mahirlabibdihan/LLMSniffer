from math import gcd
def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
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

t = int(input())
for _ in range(t):
    solve()