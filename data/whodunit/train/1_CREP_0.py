t = int(input())
while t:
    t-=1 
    n,k = map(int,input().split())
    ls = list(map(int,input().split()))
    ls.sort()
    count,nsum=1,-1
    if n==1:
        print(ls[0])
    else:
        for i in range(n-1):
            if ls[i]==ls[i+1]:
                count+=1
                #print(count,ls[i])
            else:
                #print(count,ls[i])
                if count==k:
                    if nsum==-1:
                        nsum=0
                    nsum+=ls[i]
                count=1
        if count==k:
            if nsum==-1:
                nsum=0
            nsum+=ls[n-1]
        if nsum==-1:
            print(-1)
        else:
            print(nsum)
            