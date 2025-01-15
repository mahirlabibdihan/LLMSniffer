def greet_guests(n):
    MOD = 10**9 + 7
    a, b = 1, 1
    for _ in range(n-1):
        a, b = b, (a + b) % MOD
    return b

T = int(input())
for _ in range(T):
    N = int(input())
    print(greet_guests(N))