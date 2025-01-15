def main():
    n = int(input())
    if n < 0 or n > 50 :
        print("Invalid number of test case")
        exit()
    else:
        for i in range(n):
            get_winner()


def get_winner():
    team = {}
    for x in range(12):
        x = input().split(" ")
        hometeam = x[0]
        hometeamgoal = int(x[1])
        awayteamgoal = int(x[-2])
        awayteam = x[-1]

        if hometeam not in team:
            team[hometeam] = [0,0]
        if awayteam not in team:
            team[awayteam] = [0,0]
        if hometeamgoal > awayteamgoal:
            team[hometeam][0] +=3
        elif awayteamgoal > hometeamgoal:
            team[awayteam][0] += 3
        else:
            team[hometeam][0] += 1
            team[awayteam][0] += 1
        team[hometeam][1] += (hometeamgoal - awayteamgoal)
        team[awayteam][1] += (awayteamgoal - hometeamgoal)


    sorted_team = sorted(team.values(),reverse = True)
    for key, values in team.items():
        if values == sorted_team[0]:
            firstteam = key
        if values == sorted_team[1]:
            secondteam = key
    print(firstteam,secondteam)

main()
