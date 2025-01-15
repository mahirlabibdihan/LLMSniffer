from sys import stdin, stdout
from bisect import bisect_left, bisect_right
from itertools import accumulate

MOD = 10**9+7
MAX = 10**5+10
fact = [1]*MAX
invfact = [1]*MAX

def add(x, y):
    return (x+y)%MOD

def mul(x, y):
    return (x*y)%MOD

def power(x, y):
    res = 1
    while y:
        if y&1:
            res = mul(res, x)
        x = mul(x, x)
        y >>= 1
    return res

def inv(x):
    return power(x, MOD-2)

def C(n, k):
    if n<k or k<0:
        return 0
    return mul(fact[n], mul(invfact[k], invfact[n-k]))

for i in range(1, MAX):
    fact[i] = mul(i, fact[i-1])
    invfact[i] = mul(inv(i), invfact[i-1])

T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    A = list(map(int, stdin.readline().split()))
    B = sorted([(A[i], i) for i in range(N)])
    ans = [0]*N
    pref = [0]*(N+1)
    for i in range(N):
        pref[i+1] = add(pref[i], B[i][0])
    for i in range(N):
        x, idx = B[i]
        pos = bisect_left(B, (x, -1))
        ans[idx] = add(ans[idx], mul(x, add(C(pos, 2), C(pos, 1))))
        if pos:
            ans[idx] = add(ans[idx], -mul(pref[pos], add(C(pos-1, 1), C(pos-1, 2))))
        pos = bisect_right(B, (x, N))
        ans[idx] = add(ans[idx], mul(x, add(C(N-pos, 2), C(N-pos, 1))))
        if N-pos:
            ans[idx] = add(ans[idx], -mul(pref[N]-pref[pos], add(C(N-pos-1, 1), C(N-pos-1, 2))))
    stdout.write(' '.join(map(str, ans))+'\n')
