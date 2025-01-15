from collections import Counter

for t in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    
    i=0
    
    while i<len(a)-1:
        
        if a[i]==a[i+1]:
            del a[i+1]
            
        i+=1
        
    cod=Counter(a)

    typ=-1
    val=-1
    
    for k,v in cod.items():
        if v>val:
            typ=k
            val=v
        elif v==val and k<typ:
            typ=k
            
    print(typ)
