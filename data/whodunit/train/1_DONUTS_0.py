for _ in range(int(input())):
    N, M = input().split()
    N = int(N)
    M = int(M)
    a = []
    count = 0
    
    a = list(map(int,input().split()))
    lun = len(a)
    a.sort()
    
    while len(a)>1:
        
        a[0] -= 1
        if a[0] == 0:
            a.pop(0)
        
        a.pop(len(a)-1)
        
        count += 1 
     
       
            
    print(count)