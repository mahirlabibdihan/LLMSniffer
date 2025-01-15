T= int(input())
for i in range(T):
    a=list(map(int,input().split()))
    l=[]
    for j in range(a[0]):
        b=input().split()
        t=int(b[0])
        if(t>a[2]+1):
         t=max(t-a[1],a[2])
        elif(t<a[2]-1):
         t=min(t+a[1],a[2])
        else:
         t=a[2]
        if(t >= a[3] and t <= a[4]):
         l += [int(b[1])]
    if(len(l)==0):
        print("-1")
    else:
        print(min(l))
                
