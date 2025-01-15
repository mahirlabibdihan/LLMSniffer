T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 0
    for i in range(n):
        if cnt <= a[i]:
            cnt += 1
    print(n - cnt)