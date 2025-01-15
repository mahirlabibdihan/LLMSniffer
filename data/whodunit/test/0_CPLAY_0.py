def penalty_shootout(match):
    team_a = 0
    team_b = 0
    remaining_a = 10
    remaining_b = 10
    for i in range(20):
        if i % 2 == 0:
            team_a += int(match[i])
            remaining_a -= 1
        else:
            team_b += int(match[i])
            remaining_b -= 1
        if team_a > team_b + remaining_b:
            return "TEAM-A", i + 1
        if team_b > team_a + remaining_a:
            return "TEAM-B", i + 1
    if team_a > team_b:
        return "TEAM-A", 20
    if team_b > team_a:
        return "TEAM-B", 20
    return "TIE", 20

matches = input().split()
for match in matches:
    winner, shots = penalty_shootout(match)
    print(winner, shots)