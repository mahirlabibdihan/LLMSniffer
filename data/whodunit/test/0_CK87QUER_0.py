import math
T = int(input())
for _ in range(T):
    Y = int(input())
    limit = int(math.sqrt(Y))
    count = 0
    for A in range(1, limit+1):
        B = min(700, Y - A*A)
        count += B
    print(count)