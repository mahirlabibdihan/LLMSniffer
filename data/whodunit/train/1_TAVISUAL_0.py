t=int(input())
for x in range(t):
    n,c,q=map(int,input().split())
    for y in range(q):
        l,r=map(int,input().split())
        
        if c>=l and c<=r :
            c=c-r+1
            c=l-r+2-c
            c=c+r-1
            
    print(c)