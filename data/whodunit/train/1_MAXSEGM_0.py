t=int(input())
for i in range(t):
    n=int(input())
    c=list(map(int,input().split()))
    w=list(map(int,input().split()))
    s=set([])
    start=0
    s.add(c[0])
    maxi=w[0]
    sumi=w[0]
    for j in range(1,n):
        sumi+=w[j]
        if c[j] not in s:
            s.add(c[j])
        else:
            while start<j and c[j]!=c[start]:
                s.remove(c[start])
                start+=1
                sumi-=w[start-1]
            start+=1
            sumi-=w[start-1]
        if sumi>maxi:
            maxi=sumi
    print(maxi)            
            