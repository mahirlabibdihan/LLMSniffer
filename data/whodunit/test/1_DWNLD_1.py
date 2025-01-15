tc=int(input())
for i in range(tc):
    (n,k)=map(int,input().split())
    tl=[]
    dl=[]
    for j in range(n):
        (t,d)=map(int,input().split())
        tl.append(t)
        dl.append(d)
    s=0
    h=0
    while(h!=len(tl) and k!=0):
        if(tl[h]==k):
            tl[h]=tl[h]-k
            k=0
        else:
            if(tl[h]>k):
                tl[h]=tl[h]-k
                k=0
            else:
                k=k-tl[h]
                tl[h]=0
        h+=1
    for x in range(len(tl)):
        s=s+(tl[x]*dl[x])
    print(s)
        