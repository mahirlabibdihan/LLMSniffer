def hcf(a, b):
    if b < a:
        a, b = b, a
    if a % b == 0:
        return b
    h = 1
    for i in range(1, b + 1):
        if a % i == 0 and b % i == 0:
            h = i
    return h

def lcm(a, b, h):
    return a * b // h

for _ in range(int(input())):
    n, m = map(int, input().split())
    h = hcf(n, m)
    l = lcm(n, m, h)
    print(l // h)
