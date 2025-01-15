MOD = 10**9 + 7
MAX = 10**6 + 5
fact = [0]*MAX
invfact = [0]*MAX

def power(a, b):
    res = 1
    while b > 0:
        if b & 1:
            res = (res * a) % MOD
        a = (a * a) % MOD
        b >>= 1
    return res

def inv(n):
    return power(n, MOD - 2)

def C(n, k):
    if k < 0 or k > n:
        return 0
    return (fact[n] * ((invfact[k] * invfact[n - k]) % MOD)) % MOD

def add(a, b):
    a += b
    if a >= MOD:
        return a - MOD
    return a

def solve(n, k):
    if k < n:
        return 0
    ans = fact[k]
    ans = (ans * invfact[k - n]) % MOD
    ans = (ans * fact[n - 1]) % MOD
    ans = (ans * power(n, n - 2)) % MOD
    return ans

def main():
    fact[0] = 1
    invfact[0] = 1
    for i in range(1, MAX):
        fact[i] = (i * fact[i - 1]) % MOD
        invfact[i] = inv(fact[i])
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        print(solve(N, K))

if __name__ == "__main__":
    main()
