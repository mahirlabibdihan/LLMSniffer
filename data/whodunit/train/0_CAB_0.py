T = int(input().strip())
for _ in range(T):
    N, K = map(int, input().strip().split())
    if K < N or K > 26*N:
        print(-1)
    else:
        result = ['a'] * N
        K -= N
        i = N - 1
        while K > 0:
            if K >= 25:
                result[i] = 'z'
                K -= 25
            else:
                result[i] = chr(ord('a') + K)
                K = 0
            i -= 1
        print(''.join(result))