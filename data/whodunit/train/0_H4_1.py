def power(x, y, p):
    res = 1
    x = x % p
    while (y > 0):
        if (y & 1):
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

t = int(input().strip())
for _ in range(t):
    n, m = map(int,input().strip().split())
    ans = 0
    for i in range(1, n+1):
        ans = (ans + power(i, i, m)) % m
    print(ans)