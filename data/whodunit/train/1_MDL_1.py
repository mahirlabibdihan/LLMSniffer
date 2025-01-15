t=int(input())
while(t>0):
    n=int(input())
    lst=list(map(int,input().split()))
    while(len(lst)>=3):
        x=lst[:3]
        x=sorted(x)
        lst.remove(x[1])
    
    print(* lst)
    
    
    t-=1