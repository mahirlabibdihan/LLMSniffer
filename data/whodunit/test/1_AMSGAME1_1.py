import math
for _ in range(int(input())):
    n=int(input())
    l=list(map(int, input().split()))
    for i in range(1,n):
        l[i]=math.gcd(l[i], l[i-1])
    print(l[-1])