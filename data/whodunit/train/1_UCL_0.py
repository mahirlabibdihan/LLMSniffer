for _ in range(int(input())):
    team={}
    for i in range(12):
        x=list(input().split(" "))
        team1=x[0]
        score1=int(x[1])
        team2=x[-1]
        score2=int(x[-2])

        if team1 not in team:
            team[team1]=[0,0]
        if team2 not in team:
            team[team2]=[0,0]
        if score1>score2:
            team[team1][0]+=3
        if score2>score1:
            team[team2][0]+=3
        if score1==score2:
            team[team1][0]+=1
            team[team2][0]+=1
        team[team1][1]+= score1-score2
        team[team2][1]+= score2-score1

    winner=sorted(team.values(),reverse=True)
    for key,values in team.items():
        if values==winner[0]:
            first=key
        if values==winner[1]:
            second=key
    print(first,second)