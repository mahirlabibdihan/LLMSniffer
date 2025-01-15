s=int(input())
for _ in range(s):
    r=int(input())
    u=list(map(int,input().split()))
    k=dict()
    p=0
    for c in u:
        if(c not in k):
            k[c]=1
            p=c
        else:
            if(c!=p):
                k[c]=k[c]+1
                p=c
            else:
                p=0
    z=sorted(k.items(),key=lambda s:(-s[1],s[0]))
    print(z[0][0])
    