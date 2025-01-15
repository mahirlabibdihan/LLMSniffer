def p(b, e):
    t = 1
    while(e):
        if(e & 1):
            t = (t*b) % mod
        b = (b*b) % mod
        e >>= 1
    return t


def f(i, e):
    b = p(i, i)
    t = 0
    m = 1
    m2 = p(i, mod)
    while(e):
        if(e & 1):
            t = (t+m*b % mod) % mod
            m = (m*m2) % mod
        b = (b*(m2+1)) % mod
        m2 = (m2*m2) % mod
        e >>= 1
    return t


for _ in range(int(input())):
    n, mod = map(int, input().split())
    ans = 0
    for i in range(1, min(n+1, mod)):
        ans = (ans+f(i, (n+mod-i)//mod)) % mod
    print(ans)
