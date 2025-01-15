T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        L, R = map(int, input().split())
        result = A[L-1]
        for i in range(L, R):
            result &= A[i]
        if result % 2 == 0:
            print("EVEN")
        else:
            print("ODD")