from collections import Counter

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    ans = sum(v * (v - 1) // 2 for v in c.values())
    ans += sum(v * c[k * 2] for k, v in c.items() if k * 2 in c)
    print(ans)

t = int(input())
for _ in range(t):
    solve()