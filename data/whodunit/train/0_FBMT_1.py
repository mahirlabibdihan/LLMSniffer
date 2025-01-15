T = int(input().strip())
for _ in range(T):
    n = int(input().strip())
    team1, team2 = None, None
    score1, score2 = 0, 0
    for _ in range(n):
        team = input().strip()
        if team1 is None:
            team1 = team
            score1 += 1
        elif team1 == team:
            score1 += 1
        elif team2 is None:
            team2 = team
            score2 += 1
        else:
            score2 += 1
    if score1 > score2:
        print(team1)
    elif score2 > score1:
        print(team2)
    else:
        print("Draw")