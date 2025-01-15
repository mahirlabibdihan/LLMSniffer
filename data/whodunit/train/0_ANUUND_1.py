def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        A.sort()
        result = [0]*N
        result[::2] = A[:N//2]
        result[1::2] = A[N//2:]
        print(' '.join(map(str, result)))

solve()