T = int(input())
for _ in range(T):
    N, K, S = map(int, input().split())
    if K > N:
        print(-1)
    elif K * S > N * ((S // 7) * 6 + min(S % 7, 6)):
        print(-1)
    else:
        print((K * S + N - 1) // N)