t=int(input())
while(t):
    n=int(input())
    l=list(map(int,input().split()))
    b=[]
    l.sort()
    c=0
    for i in range(len(l)):
        c=0
        for j in range(i+1,len(l)):
            if l[j]>l[i]:
                b.append(n-j)
                c=1
                break
        if c==0:
            b.append(0)
    for i in range(n-1):
        print(b[i],end=" ")
    print(b[n-1])
    t-=1
