import sys
input = sys.stdin.readline
mod = 998244353
N = 10**6+10
g = [0]*N
f = [0]*N
inv = [0]*N
fac = [0]*N
ifac = [0]*N
g[1] = 1
for i in range(2,N):
    g[i] = (mod-mod//i)*g[mod%i]%mod
f[0] = f[1] = inv[1] = fac[0] = fac[1] = ifac[0] = ifac[1] = 1
for i in range(2,N):
    f[i] = f[i-1]*g[i]%mod
    fac[i] = fac[i-1]*i%mod
    inv[i] = inv[mod%i]*(mod-mod//i)%mod
    ifac[i] = ifac[i-1]*inv[i]%mod
def C(n,m):
    if n<m:return 0
    return fac[n]*ifac[m]%mod*ifac[n-m]%mod
def S(n,m):
    if n<m:return 0
    return C(n+m,m)*f[n]%mod
n = int(input())
print((pow(3,n,mod)-2*S(n,1)+mod)%mod)