

for _ in range(int(input())):
    r,c = map(int, input().split())
    flag = 0

    for i in range(r):
        lst = list(map(int,input().split()))
        if flag == 1:
            continue
        else:
            for j in range(c):
                if i == 0 or i == r-1:
                    if j == 0 or j == c-1:
                        if lst[j] >= 2:
                            flag = 1
                    elif lst[j] >= 3:
                        flag = 1
                elif j == 0 or j == c-1:
                    if lst[j] >= 3:
                        flag = 1
                else:
                    if lst[j] >= 4:
                        flag = 1

    if flag == 1:
        print("Unstable")
    else:
        print("Stable")








