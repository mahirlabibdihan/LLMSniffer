t = int(raw_input())
for test in range(t):
    n,k = map(int,raw_input().split())
    Map = dict()
    for i in range(n):
        tempset = map(int,raw_input().split())
        tempset.remove(tempset[0])
        
        key = frozenset(tempset)
        if key in Map:
            Map[key]+=1
        else :
            Map[key]=1
            
    ans1=0
    
    for seta in Map.keys():
        for setb in Map.keys():
            if seta!=setb:
                if len(seta|setb)==k:
                    ans1+=Map[seta]*Map[setb]
    ans1=ans1/2
 
    ans2=0
    fullset = frozenset([int(i) for i in range(1,k+1)])
    if fullset in Map :
        ans2 = Map[fullset]*(Map[fullset]-1)/2
    
    ans = ans1+ans2
    print(ans)