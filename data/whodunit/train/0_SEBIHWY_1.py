def guess_winner(S, SG, FG, D, T):
    other_car_speed = S + (D*50*18)/(5*T)
    if abs(SG - other_car_speed) < abs(FG - other_car_speed):
        return "SEBI"
    elif abs(SG - other_car_speed) > abs(FG - other_car_speed):
        return "FATHER"
    else:
        return "DRAW"

T = int(input())
for _ in range(T):
    S, SG, FG, D, T = map(int, input().split())
    print(guess_winner(S, SG, FG, D, T))