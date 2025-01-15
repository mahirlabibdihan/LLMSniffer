from collections import Counter

def find_winner(T, test_cases):
    for _ in range(T):
        N, players = test_cases[_]
        numbers = [player[1] for player in players]
        counter = Counter(numbers)
        unique_numbers = [number for number, count in counter.items() if count == 1]
        if unique_numbers:
            min_unique = min(unique_numbers)
            winner = [player[0] for player in players if player[1] == min_unique][0]
            print(winner)
        else:
            print("Nobody wins.")

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