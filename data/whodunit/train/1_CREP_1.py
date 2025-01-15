from collections import Counter

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    c = Counter(a)
    ans = 0
    ok = False
    for i in c:
        if c[i] == k:
            ans += i
            ok = True
    if ok:
        print(ans)
    else:
        print(-1)
