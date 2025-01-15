for _ in range(int(input())):
    x, y = list(map(int,input().split()))
    x, y = abs(x), abs(y)
    
    if x<=y:
        if(x+y)%2==0:
            p =2 *y
        else:
            p = 2*y-1
            
    else:
        if(x+y)%2==0:
            p = 2*x
        else:
            p = 2*x+1
            
    print(p)