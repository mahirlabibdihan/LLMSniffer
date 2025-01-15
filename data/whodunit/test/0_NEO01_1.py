def max_happiness(T, test_cases):
    for _ in range(T):
        N = test_cases[_][0]
        A = test_cases[_][1]
        A.sort(reverse=True)
        ans = [0]*N
        ans[0] = A[0]
        for i in range(1, N):
            ans[i] = max(ans[i-1], A[i]*(i+1))
        print(ans[-1])

T = int(input().strip())
test_cases = []
for _ in range(T):
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    test_cases.append((N, A))
max_happiness(T, test_cases)