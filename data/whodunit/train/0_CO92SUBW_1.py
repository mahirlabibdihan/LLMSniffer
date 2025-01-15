import math
T = int(input())
for _ in range(T):
    X = int(input())
    n = int(math.sqrt(2*X))
    if n*(n+1)//2 < X:
        n += 1
    if n*(n+1)//2 - X < 2:
        print(n)
    else:
        print(n+1)