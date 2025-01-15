def solve():
    T = int(input().strip())
    for _ in range(T):
        teams = {}
        for _ in range(12):
            home_team, home_goals, _, away_goals, away_team = input().strip().split()
            home_goals, away_goals = int(home_goals), int(away_goals)
            if home_team not in teams:
                teams[home_team] = [0, 0]
            if away_team not in teams:
                teams[away_team] = [0, 0]
            if home_goals > away_goals:
                teams[home_team][0] += 3
            elif home_goals < away_goals:
                teams[away_team][0] += 3
            else:
                teams[home_team][0] += 1
                teams[away_team][0] += 1
            teams[home_team][1] += home_goals - away_goals
            teams[away_team][1] += away_goals - home_goals
        teams = sorted(teams.items(), key=lambda x: (-x[1][0], -x[1][1]))
        print(teams[0][0], teams[1][0])

solve()