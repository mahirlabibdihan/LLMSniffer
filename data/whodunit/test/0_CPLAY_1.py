def penalty_shootout(match):
    team_a = [int(match[i]) for i in range(0, 20, 2)]
    team_b = [int(match[i]) for i in range(1, 20, 2)]
    score_a = score_b = 0
    for i in range(10):
        score_a += team_a[i]
        if i < 5 or score_a != score_b:
            score_b += team_b[i]
        if score_a > score_b + (9 - i):
            return "TEAM-A", 2 * i + 1
        if score_b > score_a + (9 - i):
            return "TEAM-B", 2 * i + 2
    return ("TEAM-A" if score_a > score_b else "TEAM-B" if score_b > score_a else "TIE", 20)

matches = input().split()
for match in matches:
    winner, shots = penalty_shootout(match)
    print(winner, shots)