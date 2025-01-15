MOD = 10**9+7
def solve():
    p, q, r = map(int, input().split())
    A = sorted(map(int, input().split()))
    B = sorted(map(int, input().split()))
    C = sorted(map(int, input().split()))
    sumA = [0]*(p+1)
    sumC = [0]*(r+1)
    for i in range(p):
        sumA[i+1] = (sumA[i]+A[i])%MOD
    for i in range(r):
        sumC[i+1] = (sumC[i]+C[i])%MOD
    ans = 0
    for y in B:
        x = bisect.bisect(A, y)
        z = bisect.bisect(C, y)
        ans += (y*z+sumC[z])*x + (y*x+sumA[x])*z
        ans %= MOD
    print(ans)

T = int(input())
for _ in range(T):
    solve()