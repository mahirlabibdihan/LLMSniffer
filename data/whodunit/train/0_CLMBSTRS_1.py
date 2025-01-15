MOD = 1000000007
MAX = 1000000
fib = [0]*(MAX+1)
fib[1] = 1
fib[2] = 2
for i in range(3, MAX+1):
    fib[i] = (fib[i-1] + fib[i-2]) % MOD

def solve(N, G):
    M = bin(fib[N]).count('1')
    return "CORRECT" if M == G else "INCORRECT"

T = int(input())
for _ in range(T):
    N, G = map(int, input().split())
    print(solve(N, G))