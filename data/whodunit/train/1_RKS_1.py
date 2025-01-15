tc = int(input())
for _ in range(tc):
    n,k = list(map(int,input().split()))
    rows,cols = set(),set()
    cfull = rfull = set(i for i in range(1,n+1))
    for kk in range(k):
        x,y = list(map(int,input().split()))
        rows.add(x)
        cols.add(y)

    rfull = list(rfull - rows)
    cfull = list(cfull - cols)

    rfull.sort()
    cfull.sort()
    ans = []
    for i in range(len(rfull)):
        ans.append(rfull[i])
        ans.append(cfull[i])

    ans.insert(0,len(rfull))
    ans = list(map(str,ans))
    print(" ".join(ans))
