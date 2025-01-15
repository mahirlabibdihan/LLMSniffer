t=int(input())
while t:
    t=t-1
    k,n=map(int,input().split())
    a=[]
    while k!=0:
        x=k%10
        if x not in a:
            a.append(x)
            
        k=k//10
            
    print(len(a)**3)