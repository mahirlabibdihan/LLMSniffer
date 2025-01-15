t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=input()
    s=list(s)
    #prev=s[:k]
    c=0
    l=[]
    if(n%2==0):
        for i in range(1,n//2+1):
            d=min(n-k,k,i)
            l.append(d)
        for i in range(n//2-1,0,-1):
            d=min(n-k,k,i)
            l.append(d)
    else:
        for i in range(1,n//2+1):
            d=min(n-k,k,i)
            l.append(d)
        for i in range(n//2,0,-1):
            d=min(n-k,k,i)
            l.append(d)
    #print(l)
    for i in range(n-1):
        if(s[i]!=s[i+1]):
            c+=l[i]
    print(c)
    
       
        
        