MOD = 10**9 + 7
def solve():
    H = int(input())
    if H == 0:
        return False
    V = list(map(int, input().split()))
    P = [0] * (2**H)
    for i in range(2**H - 1, -1, -1):
        if i >= 2**(H - 1):
            P[i] = V[i]
        else:
            P[i] = max(V[i] * P[2 * i], V[i] * P[2 * i + 1]) % MOD
    print(P[1])
    return True

while solve():
    pass