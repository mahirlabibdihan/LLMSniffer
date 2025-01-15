T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    i = 0
    while i < n:
        if cnt <= a[i]:
            cnt += 1
        i += 1
    print(n - cnt)