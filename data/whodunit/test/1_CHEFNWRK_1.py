for _ in range(int(input())):
    n, k = map(int,input().split())
    w = list(map(int,input().split()))
    l = 0
    trips = 0
    while len(w)>0:
        if w[0]<=k:
            l += w[0]
            if l <= k:
                w.pop(0)
                continue
            else:
               trips += 1
               l = 0
               continue
        else:
            print(-1)
            break
    else:
        trips +=1
        print(trips)    
        