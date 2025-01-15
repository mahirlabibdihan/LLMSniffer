def game_winner(T, test_cases):
    for i in range(T):
        S = test_cases[i]
        B_count = S.count('B')
        if B_count % 2 == 0:
            print("Chef")
        else:
            print("Aleksa")

T = int(input().strip())
test_cases = []
for _ in range(T):
    test_cases.append(input().strip())
game_winner(T, test_cases)