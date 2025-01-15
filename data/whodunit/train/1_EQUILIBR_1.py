import math
try:
    n = int(input())
    k = int(input())
    if n==1 or n==2:
        print(0)
    else :
        num , denom = pow(2,n-1)-n , pow(2,n-1)
        MOD = 10**9 + 7
        print(((pow(denom,MOD-2,MOD))*num) % MOD)
except:
    pass