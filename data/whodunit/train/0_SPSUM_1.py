def solve(N, M):
    total_sum = N*(N+1)//2
    if total_sum < M or (total_sum - M) % 2 != 0:
        return "No"
    else:
        return "Yes"

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(solve(N, M))