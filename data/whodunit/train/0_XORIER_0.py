from collections import Counter
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    ans = 0
    for x in c:
        ans += c[x]*(n-c[x])
    print(ans//2)

t = int(input())
for _ in range(t):
    solve()