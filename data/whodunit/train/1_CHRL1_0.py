def rec(k, w=0, i=0):
    global ans
    ans = max(ans, w)
    if i == n: return
    if o[i][0] <= k:
        rec(k - o[i][0], w + o[i][1], i + 1)
    rec(k, w, i + 1)

for test in range(int(input())):
    n, k = map(int, input().split())
    o = [tuple(map(int, input().split())) for i in range(n)]
    ans = 0
    rec(k)
    print(ans)
