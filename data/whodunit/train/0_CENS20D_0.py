def count_pairs(T, test_cases):
    for _ in range(T):
        N = test_cases[_][0]
        A = test_cases[_][1]
        count = 0
        for i in range(N):
            for j in range(i+1, N):
                if A[i] & A[j] == A[i]:
                    count += 1
        print(count)

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    test_cases.append((N, A))
count_pairs(T, test_cases)