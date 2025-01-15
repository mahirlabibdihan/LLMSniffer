def game_winner(T, test_cases):
    for _ in range(T):
        N, K, A = test_cases[_]
        if sum(A) >= K or sum(A) % 2 == 1:
            print(1)
        else:
            print(2)

T = int(input())
test_cases = []
for _ in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    test_cases.append((N, K, A))
game_winner(T, test_cases)