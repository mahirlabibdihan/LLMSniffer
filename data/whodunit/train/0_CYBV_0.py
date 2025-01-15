T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    if K % N == 0:
        print(K // N)
    else:
        print(K // N)