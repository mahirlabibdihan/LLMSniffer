def gcd(m, n):
    r = m%n
    while r!= 0:
        m = n
        n = r
        r = m%n
    return n


for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    x = gcd(s[0], s[1])
    for i in range(n-2):
        x = gcd(s[n-i-1], x)
    if x == 1:
        print(0)
    else:
        print(-1)