t=int(input())
for _ in range(t):
    li=list(map(int,input().split()))
    l=len(li)
    fl=0
    f=1<<l
    
    for i in range(1,f):
        s=0
        for j in range(0,l):
            k=1<<j
            if((i&k)!=0):
                s+=li[j]
        if(s==0):
            fl=1
            break
    if(fl==1):
        print('Yes')
    else:
        print('No')