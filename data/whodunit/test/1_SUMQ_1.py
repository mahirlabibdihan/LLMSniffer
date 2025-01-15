def R():     return list(map(int,input().split()))

m=1000000007
for i in range(int(input())):
    a,b,c=R()
    a1=sorted(R()); b1=sorted(R()); c1=sorted(R())
    ass=css=asum=csum=s=0

    for i in b1:
        while ass<a and a1[ass]<=i:
            asum+=a1[ass]
            ass+=1
        while css<c and c1[css]<=i:
            csum+=c1[css]
            css+=1

        s+=(i*ass+asum)*(i*css+csum)
        s=s%m

    print(s)