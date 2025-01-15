def game_winner(T, test_cases):
    for i in range(T):
        A, B = test_cases[i]
        if min(A, B) % 2 == 0:
            print("Vanka")
        else:
            print("Tuzik")

T = int(input())
test_cases = []
for _ in range(T):
    test_cases.append(list(map(int, input().split())))

game_winner(T, test_cases)