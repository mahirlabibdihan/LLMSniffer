T = int(input())
for _ in range(T):
    N = int(input())
    players = []
    for i in range(N):
        R, Min, Max, Time, isRated, Color = input().split()
        R, Min, Max, Time = int(R), int(Min), int(Max), int(Time)
        players.append((R, Min, Max, Time, isRated, Color, i+1))
    waiting = []
    result = [0]*N
    for player in players:
        R, Min, Max, Time, isRated, Color, i = player
        for j, waiting_player in enumerate(waiting):
            R_w, Min_w, Max_w, Time_w, isRated_w, Color_w, i_w = waiting_player
            if Min <= R_w <= Max and Min_w <= R <= Max_w and Time == Time_w and isRated == isRated_w and (Color == "random" or Color_w == "random" or Color != Color_w):
                result[i-1] = i_w
                result[i_w-1] = i
                waiting.pop(j)
                break
        else:
            waiting.append(player)
    for i in range(N):
        if result[i] == 0:
            print("wait")
        else:
            print(result[i])