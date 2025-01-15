def game_winner(T, test_cases):
    for i in range(T):
        if test_cases[i] % 6 == 0:
            print("Misha")
        else:
            print("Chef")

T = int(input())
test_cases = []
for _ in range(T):
    test_cases.append(int(input()))
game_winner(T, test_cases)