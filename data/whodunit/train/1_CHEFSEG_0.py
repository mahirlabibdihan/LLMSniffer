import math
T = int(input())
for _ in range(T):
    x,k = map(int,input().split())
    y = int(math.log2(k))
    z = 2**y
    m = k - z
    print((2*m+1)*(x)/(2**(y+1)))
    