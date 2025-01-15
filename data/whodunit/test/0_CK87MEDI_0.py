def max_median(T, test_cases):
    for _ in range(T):
        N, K, arr = test_cases[_]
        arr.sort()
        print(arr[(N+K)//2])

T = int(input())
test_cases = []
for _ in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    test_cases.append((N, K, arr))
max_median(T, test_cases)