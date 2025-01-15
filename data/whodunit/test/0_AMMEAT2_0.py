def solve(N, K):
    if K == 1:
        return [1]
    if K > N // 2:
        return [-1]
    plates = [1]
    for i in range(2, N + 1, 2):
        if len(plates) == K:
            break
        plates.append(i)
    return plates

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    result = solve(N, K)
    if result[0] == -1:
        print(-1)
    else:
        print(' '.join(map(str, result)))