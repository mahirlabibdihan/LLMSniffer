from collections import Counter
MOD = 10**9+7

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    max_a = max(a)
    c = Counter(a)
    max_count = c[max_a]
    ans = pow(2, max_count, MOD) - 1
    print(ans)

T = int(input())
for _ in range(T):
    solve()