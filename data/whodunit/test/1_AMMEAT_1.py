for _ in range(int(input())):
    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    a=0
    count=0
    l.sort()
    for i in range(len(l)):
        a+=l[n-i-1]
        count+=1
        if a>=m:
            break 
    if a>=m:
        print(count)
    else:
        print(-1)
            
    
            