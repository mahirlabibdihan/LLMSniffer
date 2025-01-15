MOD = 10**9+7
T = int(input().strip())
for _ in range(T):
    K = int(input().strip())
    ans = pow(10, K, MOD)
    ans = (ans*2)%MOD
    ans = (ans-2)%MOD
    print(ans)