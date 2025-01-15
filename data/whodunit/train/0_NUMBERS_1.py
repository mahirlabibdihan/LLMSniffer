def find_winner(T, test_cases):
    for _ in range(T):
        N, players = test_cases[_]
        players.sort(key=lambda x: x[1])
        winner = "Nobody wins."
        for i in range(N):
            if (i == 0 or players[i][1] != players[i-1][1]) and (i == N-1 or players[i][1] != players[i+1][1]):
                winner = players[i][0]
                break
        print(winner)

T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    players = []
    for _ in range(N):
        name, number = input().split()
        players.append((name, int(number)))
    test_cases.append((N, players))

find_winner(T, test_cases)