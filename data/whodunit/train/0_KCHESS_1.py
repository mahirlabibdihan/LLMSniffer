def is_checkmate(T, test_cases):
    dx = [-2, -1, 1, 2, -2, -1, 1, 2]
    dy = [-1, -2, -2, -1, 1, 2, 2, 1]
    for _ in range(T):
        N, knights, king = test_cases[_]
        A, B = king
        check = [0]*8
        for i in range(N):
            X, Y = knights[i]
            if abs(X-A) == 2 and abs(Y-B) == 1:
                check[dx.index(X-A)] = 1
            if abs(X-A) == 1 and abs(Y-B) == 2:
                check[dx.index(X-A)] = 1
        print("YES" if sum(check) == 8 else "NO")

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    knights = [list(map(int, input().split())) for _ in range(N)]
    king = list(map(int, input().split()))
    test_cases.append((N, knights, king))
is_checkmate(T, test_cases)