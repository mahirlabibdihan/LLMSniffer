MOD = 10**9 + 7
T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(pow(4, N-2, MOD) * 2 % MOD)