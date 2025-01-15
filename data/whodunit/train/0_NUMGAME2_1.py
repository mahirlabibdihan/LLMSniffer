def game_winner():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print("BOB" if N == 1 or N % 2 == 0 else "ALICE")

game_winner()