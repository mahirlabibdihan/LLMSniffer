T = int(input().strip())
for _ in range(T):
    N, K = map(int, input().strip().split())
    print((K % 2) ^ (N % 2))