MOD = 10**9+7
T = int(input())
fact = [1]
for i in range(1, 10**6+1):
    fact.append((fact[-1]*i)%MOD)
results = [fact[int(input())] for _ in range(T)]
for result in results:
    print(result)