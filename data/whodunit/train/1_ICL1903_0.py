def gcd(a, b):
    if b > a:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a % b)
def snek(a, b):
    if b == 0:
        return 1, 0
    s = snek(b, a % b)
    x = s[1]
    y = s[0] - (a // b) * s[1]
    return x, y
def snak(a, b):
    ans = snek(a, b)
    return (ans[0] + b) % b
    
t = int(input())

for i in range(t):
    n, m, k = map(int, input().split())
    ans = 0
    if n < m or n % gcd(m, k) != 0:
        ans = -1
    else:
        g = gcd(m, k)
        n //= g
        m //= g
        k //= g
        c = ((n) * snak(k, m)) % m
        if n - k * c < m:
            ans = -1
        else:
            ans = c
    print(ans)