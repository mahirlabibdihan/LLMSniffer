MOD = 10**9+7
def goodness(n):
    if n == 0:
        return 0
    l = len(str(n))
    return ((n*(n+1))//2*l)%MOD

def solve(L, R):
    return (goodness(R) - goodness(L-1))%MOD

T = int(input())
for _ in range(T):
    L, R = [int(x) for x in input().split()]
    print(solve(L, R))