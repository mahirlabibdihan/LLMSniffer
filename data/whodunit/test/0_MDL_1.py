def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        while len(A) > 2:
            A.pop(1)
        print(*A)

solve()