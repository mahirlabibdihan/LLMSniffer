for _ in range(int(input())):
    x1,y1,x2,y2=map(int,input().split())
    x3,y3,x4,y4=(map(int,input().split()))
    p=0
    x5=max(x1,x3)
    y5=max(y1,y3)
    x6=min(x2,x4)
    y6=min(y2,y4)
    p=((x2-x1)*(y2-y1)+(x4-x3)*(y4-y3))
    if x5<x6 and y5 < y6:
        p -= ((x6-x5) * (y6-y5))
   
    print(p)
    
