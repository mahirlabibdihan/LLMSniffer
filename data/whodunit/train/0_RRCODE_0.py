def solve(T, test_cases):
    for _ in range(T):
        N, K, Answer, A, Operator = test_cases[_]
        for _ in range(K):
            for j in range(N):
                if Operator == "AND":
                    Answer &= A[j]
                elif Operator == "OR":
                    Answer |= A[j]
                else:
                    Answer ^= A[j]
        print(Answer)

T = int(input())
test_cases = []
for _ in range(T):
    N, K, Answer = map(int, input().split())
    A = list(map(int, input().split()))
    Operator = input().strip()
    test_cases.append((N, K, Answer, A, Operator))
solve(T, test_cases)