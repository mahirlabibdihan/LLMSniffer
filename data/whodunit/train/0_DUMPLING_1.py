def solve(a, b, c, d, k):
    def gcd(x, y):
        while(y):
            x, y = y, x % y
        return x

    def lcm(x, y):
        lcm = (x*y)//gcd(x,y)
        return lcm

    lcm_ab = lcm(a, b)
    lcm_cd = lcm(c, d)
    lcm_abcd = lcm(lcm_ab, lcm_cd)

    return min(k//lcm_abcd*2+1, 2*k+1)

T = int(input().strip())
for _ in range(T):
    a, b, c, d, k = map(int, input().strip().split())
    print(solve(a, b, c, d, k))