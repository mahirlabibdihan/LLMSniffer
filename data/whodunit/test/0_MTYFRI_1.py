def can_tomu_win(T, test_cases):
    for _ in range(T):
        N, K, A = test_cases[_]
        A.sort()
        motu = sum(A[i] for i in range(0, N, 2))
        tomu = sum(A[i] for i in range(1, N, 2))
        for i in range(N - 1, 0, -2):
            if K == 0:
                break
            if A[i] > A[i - 1]:
                tomu += A[i] - A[i - 1]
                K -= 1
        print("YES" if tomu > motu else "NO")

T = int(input())
test_cases = []
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    test_cases.append((N, K, A))
can_tomu_win(T, test_cases)