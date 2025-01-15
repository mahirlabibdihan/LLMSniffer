def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
        
t=int(input())

for i in range(t):
    x,y=map(int,input().split())
    while y!=1:
        z=gcd(x,y)
        if z==1:
            break
        else:
            y = y//z
    if y==1:
        print("Yes")
    else:
        print("No")
            
        
    
