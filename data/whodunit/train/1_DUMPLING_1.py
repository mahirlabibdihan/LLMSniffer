import math
t = int(input())
for _ in range(t):
    a,b,c,d,k = map(int,input().split())
    x = math.gcd(a,b)
    y = math.gcd(c,d)
    z =(x*y)// math.gcd(x,y)
    ans = k//z
    print(2*ans+1)