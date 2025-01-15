

t = int(input())

for i in range(t):
    x, w = input().split()
    d1 = d2 = 0
    for j in range(int(x)):
        y = input()
        if y[0] == '1' and y[-1] == '1':
            d1 += 1
        elif y[0] == '0' and y[-1] == '0':
            d2 += 1
    if d1 < d2:
        print("Dum")
    elif d2 < d1:
        print("Dee")
    else:
        print(w)