from collections import Counter
from bisect import bisect_right

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    b = sorted(c.values())
    ans = 0
    for k, v in c.items():
        ans += bisect_right(b, k)
        if v >= k:
            ans -= 1
    print(ans)

t = int(input())
for _ in range(t):
    solve()