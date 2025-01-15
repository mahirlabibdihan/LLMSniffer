import sys
input = sys.stdin.readline
mod = 998244353
N = 10**6+10
g = [0]*N
f = [0]*N
inv = [0]*N
inv[1] = 1
for i in range(2,N):
    inv[i] = mod - (mod//i)*inv[mod%i]%mod
g[0] = 1
g[1] = 1
for i in range(2,N):
    g[i] = g[i-1]*i%mod
f[N-1] = pow(g[N-1],mod-2,mod)
for i in range(N-2,-1,-1):
    f[i] = f[i+1]*(i+1)%mod
def C(n,k):
    if n<k or n<0 or k<0:
        return 0
    return g[n]*f[k]%mod*f[n-k]%mod
n = int(input())
ans = 0
for i in range(1,n+1):
    ans = (ans + C(n,i)*C(n-1,i-1)%mod*pow(2,n-i,mod)%mod)%mod
print(ans)
