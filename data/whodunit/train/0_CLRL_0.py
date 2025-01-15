def solve():
    n, r = map(int, input().split())
    a = list(map(int, input().split()))
    l = 1
    h = 10**9
    for i in range(n-1):
        if a[i] < r:
            if a[i] > l:
                l = a[i]
            else:
                return "NO"
        else:
            if a[i] < h:
                h = a[i]
            else:
                return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    print(solve())