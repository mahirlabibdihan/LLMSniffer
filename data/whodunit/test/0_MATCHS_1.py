def game_winner(T, test_cases):
    for i in range(T):
        N, M = test_cases[i]
        if N % 2 == 0 or M % 2 == 0:
            print("Ari")
        else:
            print("Rich")

T = int(input())
test_cases = []
for _ in range(T):
    test_cases.append(list(map(int, input().split())))
game_winner(T, test_cases)