MOD = 10**9 + 7

def solve(n1, n2, n3):
    n = min(n1, n2, n3)
    ans = pow(n, 3, MOD)
    ans = (ans + (n*(n+1)//2) % MOD * ((n1+n2+n3-n-n) % MOD) * 3) % MOD
    ans = (ans + ((n*(n+1)*(2*n+1)//6) % MOD) * 3) % MOD
    ans = (ans + ((n*(n+1)//2)**2) % MOD) % MOD
    return ans

T = int(input().strip())
for _ in range(T):
    n1, n2, n3 = map(int, input().strip().split())
    print(solve(n1, n2, n3))