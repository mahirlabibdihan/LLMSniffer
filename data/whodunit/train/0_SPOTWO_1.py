MOD = 10**9+7
T = int(input())
for _ in range(T):
    N = int(input())
    N_bin = int(format(N, 'b'))
    print(pow(pow(2, N_bin, MOD), 2, MOD))