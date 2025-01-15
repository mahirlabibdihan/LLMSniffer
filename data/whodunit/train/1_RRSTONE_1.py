[n,k]=list(map(int,input().split()))
l=list(map(int,input().split()))
if k==0:
    for i in l:
        print(i,end=" ")
elif k%2==0:
    for i in range(0,2):
        m=max(l)
        for i in range(len(l)):
            l[i]=m-l[i] 
    for i in l:
        print(i,end=" ")
else:
     m=max(l)
     for i in range(len(l)):
            l[i]=m-l[i] 
     for i in l:
        print(i,end=" ")