def solve():
    T = int(input())
    for _ in range(T):
        N, A, B = map(int, input().split())
        a = bin(A)[2:].count('1')
        b = bin(B)[2:].count('1')
        a = min(a+b, N)
        print((1<<a)-1<<(N-a))

solve()