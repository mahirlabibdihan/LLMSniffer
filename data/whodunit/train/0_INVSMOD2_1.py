def solve():
    N, K = map(int, input().split())
    return (K % 2) ^ (N % 2)

T = int(input())
for _ in range(T):
    print(solve())