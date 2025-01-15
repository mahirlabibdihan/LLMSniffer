from sys import stdin, stdout
from operator import itemgetter
mod = 10**9+7
fact = [1]
for i in range(1, 10**5+1):
    fact.append((fact[-1]*i)%mod)
inv = [0, 1]
for i in range(2, 10**5+1):
    inv.append((-(mod//i)*inv[mod%i])%mod)
for i in range(2, 10**5+1):
    inv[i] = (inv[i-1]*inv[i])%mod
def C(n, r):
    if r>n or r<0:
        return 0
    return (fact[n]*inv[r]*inv[n-r])%mod
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    a = sorted([(a[i], i) for i in range(n)], key=itemgetter(0))
    dp = [0]*n
    for i in range(n):
        dp[a[i][1]] = (C(i, 2)+C(i, 1)+1)%mod
    stdout.write(' '.join(map(str, dp))+'\n')