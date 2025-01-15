n, x = map(int, input().split())
a = list(map(int, input().split()))
prefix = [0]*(n+1)
for i in range(n):
    prefix[i+1] = prefix[i] + a[i]
min_prefix = [0]*(n+1)
for i in range(n):
    min_prefix[i+1] = min(min_prefix[i], prefix[i+1])
ans = float('inf')
for r in range(n):
    for l in range(r+1):
        total = prefix[n] - prefix[r+1] + (prefix[r+1] - prefix[l])/x
        ans = min(ans, total - min_prefix[l])
print("%.15f" % ans)