for _ in range(int(input())):
    k,n = map(int,input().split())
    lst = list(map(int,input().split()))
    cnt = 0
    x = 0
    lst.sort()
    while len(lst) > 2:
        while lst[0] != 0:
            if len(lst) == 2:
                break
            lst[-2] += lst[-1]
            del lst[-1]
            cnt += 1
            lst[0] -= 1
            if lst[0] == 0:
                del lst[0]
                break
    if lst[0] == 0:
        del lst[0]
    if len(lst) == 2:
        print(cnt+1)
    else:
        print(cnt)
    