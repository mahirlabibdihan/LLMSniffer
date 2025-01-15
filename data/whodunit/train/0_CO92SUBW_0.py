import math
T = int(input())
for _ in range(T):
    X = int(input())
    n = math.floor((-1 + math.sqrt(1 + 8*X)) / 2)
    if n * (n + 1) / 2 == X:
        print(n)
    elif n * (n + 1) / 2 + n + 1 >= X:
        print(n + 1)
    else:
        print(n + 2)