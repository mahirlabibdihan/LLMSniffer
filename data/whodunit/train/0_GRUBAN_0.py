def max_gcd(T, testcases):
    for i in range(T):
        N, K = testcases[i]
        if K*(K+1)//2 > N:
            print(-1)
        else:
            print(K)

T = int(input())
testcases = []
for _ in range(T):
    N, K = map(int, input().split())
    testcases.append((N, K))
max_gcd(T, testcases)