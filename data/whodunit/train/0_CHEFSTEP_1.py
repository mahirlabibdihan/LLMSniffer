def check_traversable(T, test_cases):
    for t in range(T):
        N, K, D = test_cases[t]
        result = ['1' if d % K == 0 else '0' for d in D]
        print(''.join(result))

T = int(input())
test_cases = []
for _ in range(T):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    test_cases.append((N, K, D))

check_traversable(T, test_cases)