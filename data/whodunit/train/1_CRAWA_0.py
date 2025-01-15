tsc = int(input())
for i in range(0,tsc):
    string = input()
    string = string.split()
    x = int(string[0])
    y = int(string[1])
    if x >= 0:
        if x % 2 == 1 and abs(y) % 2 == 0:
            print("YES")
        elif x % 2 == 1 and abs(y) % 2 == 1:
            print("YES") if y <= x+1 and y >= 1-x else print("NO")
        elif x % 2 == 0 and abs(y) % 2 == 0:
            print("YES") if y > x or y <= -x else print("NO")
        else:
            print("NO")
    elif x < 0:
        if abs(x) % 2 == 0 and abs(y) % 2 == 0:
            print("YES")
        elif abs(x) % 2 == 0 and abs(y) % 2 == 1:
            print("YES") if abs(y) <= abs(x) else print("NO")
        elif abs(x) % 2 == 1 and abs(y) % 2 == 0:
            print("YES") if abs(y) > abs(x) else print("NO")
        else:
            print("NO")