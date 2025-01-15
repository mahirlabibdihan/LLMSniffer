import math

for _ in range(int(input())):
    angels = []
    dif = []
    gcd = 360
    nAngels = int(input())
    angels = list(map(int,input().split()))

    for i in range(1,len(angels)):
        dif.append(angels[i]-angels[i-1])
    
    dif.append(angels[0]+(360-angels[-1]))
    
    for d in dif:
        gcd = math.gcd(gcd,d)
    
    print(int(360/gcd)-nAngels)
