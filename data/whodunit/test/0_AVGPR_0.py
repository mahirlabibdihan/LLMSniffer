from collections import Counter

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    ans = 0
    for i in c:
        ans += c[i] * (c[i] - 1) // 2
    for i in c:
        if 2 * i in c:
            ans += c[i] * c[2 * i]
    print(ans)

t = int(input())
for _ in range(t):
    solve()