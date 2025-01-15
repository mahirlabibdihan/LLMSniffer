t=int(input())
for i in range(t):
    n,p=[int(j) for j in input().split() ]
    for j in range(1,n+1):
        q=p//(1<<j)
        r=p%(1<<j)
        if r<(1<<(j-1)):
            p=(1<<j)*q+2*r
        else:
            p=(1<<j)*(q-1)+2*r+1
    print(p)
            
        
    
