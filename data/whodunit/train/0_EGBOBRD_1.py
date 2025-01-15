def min_packages(T, test_cases):
    for _ in range(T):
        N, K, A = test_cases[_]
        packages, remainder = divmod(A[0], K)
        for i in range(1, N):
            if A[i] > remainder:
                A[i] -= remainder
                q, remainder = divmod(A[i], K)
                packages += q
            else:
                remainder -= A[i]
        if remainder > 0:
            packages += 1
        print(packages)

T = int(input())
test_cases = []
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    test_cases.append((N, K, A))
min_packages(T, test_cases)