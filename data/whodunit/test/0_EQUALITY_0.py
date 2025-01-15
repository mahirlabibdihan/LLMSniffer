T = int(input())
for _ in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    avg = total // N
    for i in range(N):
        print(avg - a[i], end=' ')
    print()