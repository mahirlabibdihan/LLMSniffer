def solve():
    N = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    avg = total // N
    return [avg - ai for ai in a]

T = int(input())
for _ in range(T):
    print(*solve())