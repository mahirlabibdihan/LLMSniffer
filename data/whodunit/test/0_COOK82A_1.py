def la_liga_winner(T, matches):
    for match in matches:
        scores = {}
        for team, goals in match.items():
            scores[team] = goals
        if scores['RealMadrid'] < scores['Malaga'] and scores['Barcelona'] > scores['Eibar']:
            print('Barcelona')
        else:
            print('RealMadrid')

T = int(input())
matches = []
for _ in range(T):
    match = {}
    for _ in range(4):
        team, goals = input().split()
        match[team] = int(goals)
    matches.append(match)
la_liga_winner(T, matches)