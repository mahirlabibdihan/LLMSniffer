import math

def is_fibonacci(n):
    x = 0
    y = 1
    while y < n:
        z = x + y
        x = y
        y = z
    return y == n or n == 0

T = int(input().strip())
for _ in range(T):
    A = int(input().strip())
    print("YES" if is_fibonacci(A) else "NO")