from math import gcd

def solve(a, b, c, d, k):
    lcm = a*b // gcd(a, b)
    lcm2 = c*d // gcd(c, d)
    lcm3 = lcm*lcm2 // gcd(lcm, lcm2)
    return min(k//lcm3*2+1, 2*k+1)

T = int(input().strip())
for _ in range(T):
    a, b, c, d, k = map(int, input().strip().split())
    print(solve(a, b, c, d, k))