for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=[]
    
    for i in range(len(l)):
        for j in range(len(l)):
            if(i!=j):
                p=str(l[i]*l[j])
                li=list(map(int,p))
                a.append(sum(li))
    print(max(a))                
        
    
    
