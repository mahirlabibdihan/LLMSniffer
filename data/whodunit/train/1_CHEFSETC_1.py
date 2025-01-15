n=16
def validate(l):
    for i in range(n):
        flag=False
        x=0
        for j in range(4):
            if(i&(1<<j) !=0):
                x+=l[j]
                flag=True
        if(flag and x==0):
            return("Yes")
    return ("No")
            
        
        
t=int(input())
while(t):
    l=list(map(int,input().split()))
    print(validate(l))
    
    t-=1
            
    
