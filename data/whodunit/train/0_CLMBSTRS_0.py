MOD = 1000000007
MAX = 1000000
fib = [0]*(MAX+1)
fib[1] = 1
fib[2] = 2
for i in range(3, MAX+1):
    fib[i] = (fib[i-1] + fib[i-2]) % MOD

T = int(input())
for _ in range(T):
    N, G = map(int, input().split())
    M = bin(fib[N]).count('1')
    if M == G:
        print("CORRECT")
    else:
        print("INCORRECT")