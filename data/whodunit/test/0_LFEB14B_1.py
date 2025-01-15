MOD = 10**9+7

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    max_a = max(a)
    max_count = a.count(max_a)
    ans = pow(2, max_count, MOD) - 1
    print(ans)

T = int(input())
for _ in range(T):
    solve()