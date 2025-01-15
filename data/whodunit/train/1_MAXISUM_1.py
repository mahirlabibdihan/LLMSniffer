t=int(input())
for i in range(t):
    a=[]
    b=[]
    n,k =map(int,input().split())
    a=list(map(int,input().strip().split()))[:n]
    b=list(map(int,input().strip().split()))[:n]
    max=abs(b[0])
    ind=0
    sum=0
    for j in range(n):
        if(abs(b[j])>max):
            max=abs(b[j])
            ind=j
    for j in range(n):
        sum=sum+(a[j]*b[j])
    print(sum+(k*abs(b[ind])))       
            