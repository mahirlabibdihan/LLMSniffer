MOD = 10**9 + 7
def power(x, y):
    res = 1
    while y > 0:
        if y & 1:
            res = (res * x) % MOD
        y = y >> 1
        x = (x * x) % MOD
    return res

T = int(input())
for _ in range(T):
    N = int(input())
    if N % 2 == 0:
        print((26 * power(26, N // 2 - 1) % MOD * 26) % MOD)
    else:
        print((26 * power(26, N // 2) % MOD) % MOD)