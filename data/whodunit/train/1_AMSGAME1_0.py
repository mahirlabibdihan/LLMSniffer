import math
for _ in range(int(input())):
    n=int(input())
    j=list(map(int,input().split(' ')))
    for i in range(1,n):
        j[i]=math.gcd(j[i],j[i-1])
    print(j[-1])