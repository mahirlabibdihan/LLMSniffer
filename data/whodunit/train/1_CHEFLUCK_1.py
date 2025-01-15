for _ in range(int(input())):
    n = int(input())
    flag = 0
    for x in range(7):
        if (n-x*4) < 0:
            break
        if (n-x*4) % 7 == 0:
            flag = 1
            print(n-x*4)
            break
    if flag == 0:
        print(-1)
