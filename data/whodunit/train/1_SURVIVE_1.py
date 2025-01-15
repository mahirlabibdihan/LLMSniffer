for i in range(int(input())):
    n,k,s = list(map(int,input().split()))
    total = k*s
    count = 0
    k = 0
    y = False
    for i in range(1,s+1):
        #print(i)
        if i%7!=0:
            count+=n
            k+=1
        else:
            continue
        if count>=total:
            y = True
            break
    #print(count,total)
    if y:
        print(k)
    else:
        print(-1)