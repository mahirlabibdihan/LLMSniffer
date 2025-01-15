def solve():
    n = int(input())
    a = list(map(int, input().split()))
    c = [0]*1000005
    ans = 0
    for i in range(n):
        c[a[i]] += 1
    for i in range(1000005):
        if c[i] > 0:
            ans += c[i]*(n-c[i])
    print(ans//2)

t = int(input())
for _ in range(t):
    solve()