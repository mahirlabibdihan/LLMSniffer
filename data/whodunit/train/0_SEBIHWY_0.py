T = int(input())
for _ in range(T):
    S, SG, FG, D, T = map(int, input().split())
    other_car_speed = S + (D*50*18)/(5*T)
    if abs(SG - other_car_speed) < abs(FG - other_car_speed):
        print("SEBI")
    elif abs(SG - other_car_speed) > abs(FG - other_car_speed):
        print("FATHER")
    else:
        print("DRAW")