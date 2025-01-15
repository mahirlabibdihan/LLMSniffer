from fractions import Fraction

def solve(n):
    return Fraction(10**n - 10**(n//2), 10**n)

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    p_q = solve(n)
    print(p_q.numerator, p_q.denominator)