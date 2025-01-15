for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    maxdiff=0
    _min=arr[0]
    for i in range(1,n):
        if arr[i]-_min>maxdiff:
            maxdiff=arr[i]-_min
        if arr[i]<_min:
            _min=arr[i]
            
    if maxdiff==0:
        print("UNFIT")
    else:
        print(maxdiff)     
        
             
    
    
