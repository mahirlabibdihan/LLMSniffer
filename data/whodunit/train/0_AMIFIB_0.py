import math

def is_perfect_square(n):
    return n == math.isqrt(n) ** 2

def is_fibonacci(n):
    return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)

T = int(input().strip())
for _ in range(T):
    A = int(input().strip())
    print("YES" if is_fibonacci(A) else "NO")