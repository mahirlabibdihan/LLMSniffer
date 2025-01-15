def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        A.sort()
        i = 0
        while i < N - 1:
            A[i], A[i+1] = A[i+1], A[i]
            i += 2
        print(' '.join(map(str, A)))

solve()