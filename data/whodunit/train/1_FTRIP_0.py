fact = [None]*1001
def nck(n,k):
    return fact[n]/(fact[n-k]*fact[k])

fact[0]=1;
for i in range(1,1001):
    fact[i]=fact[i-1]*i
t = int(input())
for z in range(t):
    s,n,m,k = map(int, input().split())
    P = 0
    for i in range(k, min(n,m)):
        P+=nck(m-1,i)*nck(s-m,n-i-1)
    Q = nck(s-1,n-1)
    ans = float(P/Q)
    print('%.6f' % ans)