import math

for _ in range(eval(input())):
    n, a, k = [int(x) for x in input().split()]

    x = a*n*(n-1) + (k-1)*(360 * (n-2) - 2*a*n)
    y= n*(n-1)

    Gcd = math.gcd(x, y)
    print('{} {}'.format(int(x/Gcd), int(y/Gcd)))
