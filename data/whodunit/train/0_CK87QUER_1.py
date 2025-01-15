import math
T = int(input())
for _ in range(T):
    Y = int(input())
    limit = int(math.sqrt(Y))
    count = sum(min(700, Y - A*A) for A in range(1, limit+1))
    print(count)