def min_moves(T, test_cases):
    for _ in range(T):
        N, D, A = test_cases[_]
        total = sum(A)
        if total % N != 0:
            print(-1)
            continue
        target = total // N
        moves = 0
        for i in range(D):
            j = i
            temp = 0
            while j < N:
                temp += A[j] - target
                moves += abs(temp)
                j += D
            if temp != 0:
                print(-1)
                break
        else:
            print(moves)

T = int(input())
test_cases = []
for _ in range(T):
    N, D = map(int, input().split())
    A = list(map(int, input().split()))
    test_cases.append((N, D, A))
min_moves(T, test_cases)