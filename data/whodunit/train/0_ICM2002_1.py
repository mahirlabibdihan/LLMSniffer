def can_convert(T, test_cases):
    for i in range(T):
        N, K, B = test_cases[i]
        B.sort()
        if all(x % K == B[0] % K for x in B):
            print("YES")
        else:
            print("NO")

T = int(input())
test_cases = []
for _ in range(T):
    N, K = map(int, input().split())
    B = list(map(int, input().split()))
    test_cases.append((N, K, B))

can_convert(T, test_cases)