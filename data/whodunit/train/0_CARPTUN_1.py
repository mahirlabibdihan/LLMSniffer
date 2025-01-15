def time_delay(T, test_cases):
    results = []
    for _ in range(T):
        N = test_cases[_][0]
        A = test_cases[_][1]
        C, D, S = test_cases[_][2]
        results.append(max(A) * (C - 1))
    return results

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    C, D, S = map(int, input().split())
    test_cases.append((N, A, (C, D, S)))

print('\n'.join(map(str, time_delay(T, test_cases))))