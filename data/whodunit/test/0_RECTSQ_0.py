import math
def min_plots(T, test_cases):
    for i in range(T):
        N, M = test_cases[i]
        gcd = math.gcd(N, M)
        print((N * M) // (gcd * gcd))

T = int(input())
test_cases = []
for _ in range(T):
    N, M = map(int, input().split())
    test_cases.append((N, M))
min_plots(T, test_cases)