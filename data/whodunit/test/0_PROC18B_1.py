T = int(input())
for _ in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    result = a[0]
    for i in range(1, N):
        result = (result + a[i]) / 2
    print(result)