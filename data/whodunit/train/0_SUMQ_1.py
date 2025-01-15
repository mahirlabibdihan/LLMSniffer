MOD = 10**9+7

def solve():
    p, q, r = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    C = sorted(list(map(int, input().split())))

    prefix_A = [0]*(p+1)
    prefix_C = [0]*(r+1)

    for i in range(1, p+1):
        prefix_A[i] = (prefix_A[i-1] + A[i-1]) % MOD

    for i in range(1, r+1):
        prefix_C[i] = (prefix_C[i-1] + C[i-1]) % MOD

    ans = 0
    j = k = 0

    for i in range(q):
        while j < p and A[j] <= B[i]:
            j += 1
        while k < r and C[k] <= B[i]:
            k += 1

        temp = (B[i]*B[i] % MOD * (j*k) % MOD) + (2*B[i] % MOD * (prefix_A[j] + prefix_C[k]) % MOD)
        temp %= MOD
        temp += ((prefix_A[j]*k % MOD + prefix_C[k]*j % MOD) % MOD)
        temp %= MOD
        ans = (ans + temp) % MOD

    print(ans)

T = int(input())
for _ in range(T):
    solve()
