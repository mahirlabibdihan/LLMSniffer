T = int(input())
for _ in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(1, N):
        a[i] = (a[i] + a[i-1]) / 2
    print(a[-1])