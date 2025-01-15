def power(x, y, p) :
    res = 1
    x = x % p
    while (y > 0) :
        if ((y & 1) == 1) :
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

def countPalindromes(t, test_cases):
    p = 1000000007
    for _ in range(t):
        n = test_cases[_]
        if (n & 1) :
            print ((power(26, n // 2 + 1, p) + p - 1) % p)
        else :
            print ((power(26, n // 2, p) + 26 * power(26, n // 2 - 1, p)) % p)

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    test_cases.append(n)
countPalindromes(t, test_cases)