import math

t = int(input())

while t:
    m, b = map(int, input().split())
    
    if m == b or (m == 0 or b == 0):
        print(m + b)
    else:
        print(2 * (math.gcd(m,b)))
    
    t -= 1