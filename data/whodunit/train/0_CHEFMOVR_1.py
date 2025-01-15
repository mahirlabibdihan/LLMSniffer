def min_moves(T, test_cases):
    for _ in range(T):
        N, D, A = test_cases[_]
        total = sum(A)
        if total % N != 0:
            print(-1)
            continue
        target = total // N
        moves = [0]*N
        for i in range(1, N):
            moves[i] = moves[i-D] + A[i-D] - target
            if moves[i] < 0:
                print(-1)
                break
        else:
            print(sum(map(abs, moves)))

T = int(input())
test_cases = []
for _ in range(T):
    N, D = map(int, input().split())
    A = list(map(int, input().split()))
    test_cases.append((N, D, A))
min_moves(T, test_cases)