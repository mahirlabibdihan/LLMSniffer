T = int(input())

for tc in range (T):
    X,Y = map(int, input().split())
    if (X == Y):
        print(0)
    elif (X > Y):
        if ((X - Y) % 2 == 1):
            print(2)
        else:
            print(1)
    else:
        if ((Y - X) % 4 == 0):
            print(3)     
        elif ((Y - X) % 2 == 1):
            print(1)
        else:
            print(2)