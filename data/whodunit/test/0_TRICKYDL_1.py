import math
T = int(input())
for _ in range(T):
    A = int(input())
    D1 = int(math.log2(A))
    D2 = max(D1, int(math.log2(A+1)) - 1)
    print(D1, D2)