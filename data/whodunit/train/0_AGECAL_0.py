def solve():
    N = int(input())
    a = list(map(int, input().split()))
    yb, mb, db = map(int, input().split())
    yc, mc, dc = map(int, input().split())
    leap = [0] * (N + 1)
    for i in range(1, N + 1):
        leap[i] = leap[i - 1] + a[i - 1]
    leap[N] += 1
    nonleap = leap[:-1]
    ans = 0
    if yb == yc:
        if yb % 4 == 0:
            ans = leap[mc - 1] + dc - (leap[mb - 1] + db) + 1
        else:
            ans = nonleap[mc - 1] + dc - (nonleap[mb - 1] + db) + 1
    else:
        if yb % 4 == 0:
            ans += leap[N] - (leap[mb - 1] + db) + 1
        else:
            ans += nonleap[N] - (nonleap[mb - 1] + db) + 1
        yb += 1
        while yb < yc:
            if yb % 4 == 0:
                ans += leap[N]
            else:
                ans += nonleap[N]
            yb += 1
        if yc % 4 == 0:
            ans += leap[mc - 1] + dc
        else:
            ans += nonleap[mc - 1] + dc
    print(ans)

T = int(input())
for _ in range(T):
    solve()