MOD = 10**9+7
T = int(input())
fact = [1]
for i in range(1, 10**6+1):
    fact.append((fact[-1]*i)%MOD)
for _ in range(T):
    N = int(input())
    print(fact[N])