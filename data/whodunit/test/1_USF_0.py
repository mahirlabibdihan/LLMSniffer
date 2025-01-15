def func(i, counterArr):
    ans = 0
    for j in range(i,n,i):
        ans+=counterArr[j]
    return ans
n=int(1e5+1)
primes=[0]*n
for i in range(2,n):
    if primes[i]==0:
        for j in range(i,n,i):
            # distinct primes add
            primes[j]+=1
t = int(input())
from collections import Counter
for aaa in range(t):
    xxx = int(input())
    counterArr=Counter(map(int,input().split()))
    print(max(func(i, counterArr)*primes[i]for i in range(2,n)))