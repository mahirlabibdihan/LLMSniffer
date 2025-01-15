def chef_happiness(T, test_cases):
    for _ in range(T):
        N, A = test_cases[_]
        A.insert(0, 0)
        for i in range(1, N+1):
            if A[A[i]] == A[i] and A[i] != i:
                print("Truly Happy")
                break
        else:
            print("Poor Chef")

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    test_cases.append((N, A))

chef_happiness(T, test_cases)