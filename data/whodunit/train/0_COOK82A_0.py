T = int(input())
for _ in range(T):
    scores = {}
    for _ in range(4):
        team, goals = input().split()
        scores[team] = int(goals)
    if scores['RealMadrid'] < scores['Malaga'] and scores['Barcelona'] > scores['Eibar']:
        print('Barcelona')
    else:
        print('RealMadrid')