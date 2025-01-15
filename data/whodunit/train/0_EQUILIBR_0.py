import sys
from math import factorial as f
mod = 10**9+7
n = int(input())
k = int(input())
fact = [1]*(3*(10**5)+1)
for i in range(1,3*(10**5)+1):
    fact[i] = (fact[i-1]*i)%mod
def power(x,y):
    res = 1
    while y > 0:
        if y%2:
            res = (res*x)%mod
        y = y//2
        x = (x*x)%mod
    return res
def nCr(n,r):
    return (fact[n]*((power(fact[r],mod-2)*power(fact[n-r],mod-2))%mod))%mod
print((nCr(n+k-1,n-1)*power(2,n-1))%mod)