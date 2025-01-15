T = int(input().strip())
for _ in range(T):
    N, K = map(int, input().strip().split())
    if K < N or K > 26*N:
        print(-1)
    else:
        result = ['a'] * N
        for i in range(N - 1, -1, -1):
            if K >= 25:
                result[i] = 'z'
                K -= 25
            else:
                result[i] = chr(ord('a') + K)
                K = 0
        print(''.join(result))