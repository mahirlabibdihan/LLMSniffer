def solve(T, test_cases):
    for _ in range(T):
        N = test_cases[_][0]
        A = test_cases[_][1]
        Q = test_cases[_][2]
        queries = test_cases[_][3]
        for q in range(Q):
            L, R = queries[q]
            result = A[L-1]
            for i in range(L, R):
                result &= A[i]
            if result % 2 == 0:
                print("EVEN")
            else:
                print("ODD")

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    queries = []
    for _ in range(Q):
        queries.append(list(map(int, input().split())))
    test_cases.append([N, A, Q, queries])

solve(T, test_cases)