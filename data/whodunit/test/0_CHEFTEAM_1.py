def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def number_of_ways(T, test_cases):
    for i in range(T):
        N, K = test_cases[i]
        print(factorial(N) // (factorial(K) * factorial(N - K)))

T = int(input())
test_cases = []
for _ in range(T):
    N, K = map(int, input().split())
    test_cases.append((N, K))

number_of_ways(T, test_cases)