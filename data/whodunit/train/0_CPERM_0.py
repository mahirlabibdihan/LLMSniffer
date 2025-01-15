MOD = 10**9 + 7
T = int(input().strip())
fact = [1, 1]
inv = [0, 1]
invfact = [1, 1]
for i in range(2, 1000001):
    fact.append((fact[-1]*i)%MOD)
    inv.append((MOD - (MOD//i) * inv[MOD%i] % MOD)%MOD)
    invfact.append((invfact[-1]*inv[i])%MOD)
for _ in range(T):
    N = int(input().strip())
    if N == 1:
        print(1)
    else:
        print((fact[N]*invfact[N-1] - fact[N-1] + MOD)%MOD)