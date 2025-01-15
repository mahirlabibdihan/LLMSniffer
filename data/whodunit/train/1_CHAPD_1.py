import math
def fgcd(a,b):
    if(b==0):
        return a
    return fgcd(b, a%b)


for _ in range(int(input())):
    a,b= map(int, input().split())
    a = math.gcd(a,b)
    while(a>1):
        b= b//a
        a= math.gcd(a,b)
    print("No") if b>1 else print("Yes")
    
    
        
    