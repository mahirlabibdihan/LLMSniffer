from math import factorial as f
def solve(n, k):
    return f(n-1)//(f(k-1)*f(n-k))

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    print(solve(n, k))