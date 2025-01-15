def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def min_plots(T, test_cases):
    for i in range(T):
        N, M = test_cases[i]
        gcd_val = gcd(N, M)
        print((N * M) // (gcd_val * gcd_val))

T = int(input())
test_cases = []
for _ in range(T):
    N, M = map(int, input().split())
    test_cases.append((N, M))
min_plots(T, test_cases)