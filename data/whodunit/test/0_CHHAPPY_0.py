def chef_happiness(T, test_cases):
    for _ in range(T):
        N, A = test_cases[_]
        if len(set(A)) != len(A):
            print("Truly Happy")
        else:
            print("Poor Chef")

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    test_cases.append((N, A))

chef_happiness(T, test_cases)