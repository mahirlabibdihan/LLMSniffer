T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    result = ''
    for i in range(N):
        if D[i] % K == 0:
            result += '1'
        else:
            result += '0'
    print(result)