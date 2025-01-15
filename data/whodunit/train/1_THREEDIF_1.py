t=int(input())
while t:
    a=[int (o) for o in input().split()]
    a.sort()
    res=1
    for i in range(3):
        res=res*(a[i]-i)
    print(res%1000000007)    
        
    t-=1
