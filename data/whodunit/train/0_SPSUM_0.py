def solve(N, M):
    if N*(N+1)//2 < M or (N*(N+1)//2 - M) % 2 != 0:
        return "No"
    else:
        return "Yes"

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(solve(N, M))